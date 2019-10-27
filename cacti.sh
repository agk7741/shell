#!/bin/bash
passwd=123
ip=192.168.240.20
install(){
yum -y install httpd mariadb mariadb-server mariadb-devel net-snmp net-snmp-utils net-snmp-libs net-snmp-agent-libs net-snmp-devel php php-snmp php-ldap php-pdo php-mysql php-devel php-pear php-common php-gd php-mbstring php-xml php-process rrdtool rrdtool-php rrdtool-perl rrdtool-devel gcc openssl-devel dos2unix autoconf automake binutils libtool cpp postfix glibc-headers kernel-headers glibc-devel gd gd-devel help2man ntpdate wget patch
}
#安装所需软件包
cat > /etc/yum.repos.d/mariadb.repo <<EOF
[mariadb]
name=MariaDB
baseurl=http://mirrors.aliyun.com/mariadb/yum/10.3/centos7-amd64
gpgkey= http://mirrors.aliyun.com/mariadb/yum/RPM-GPG-KEY-MariaDB
gpgcheck = 1
EOF
yum -y install epel-release
install
if [ $? -ne 0  ]
then
echo -e "\e[7;31m 下载所需软件包失败。重新下载！ \e[0m"
install
if [ $? -ne 0  ]
then
echo -e "\e[7;31m 下载所需软件包失败。请手动下载! \e[0m"
exit 1
fi
fi

echo -e "\e[7;32m 下载软件包成功。。。 \e[0m"

#修改PHP配置文件
sed -i 's/sql.safe_mode = On/sql.safe_mode = Off/' /etc/php.ini
grep 'date.timezone = Asia/Shanghai' /etc/php.ini
if [ $? -ne 0 ]
then
sed -i '/\[Date\]/a\date.timezone = Asia/Shanghai' /etc/php.ini
fi
#配置web服务器(此处以Apache为例)
grep -n 'LoadModule php5_module modules/libphp5.so' /etc/httpd/conf.d/php.conf
if [ $? -ne 0 ]
then
cat >> /etc/httpd/conf.d/php.conf <<EOF
# PHP is an HTML-embedded scripting language which attempts to make it

# easy for developers to write dynamically generated webpages.

LoadModule php5_module modules/libphp5.so
EOF
fi
grep -n 'AddHandler php5-script .php' /etc/httpd/conf.d/php.conf
if [ $? -ne 0 ]
then
cat >> /etc/httpd/conf.d/php.conf <<EOF
# Cause the PHP interpreter to handle files with a .php extension.

AddHandler php5-script .php
EOF
fi
#配置数据库mariadb
systemctl start mariadb
mysqladmin -uroot password $passwd
#导入时区数据到数据库
mysql_tzinfo_to_sql /usr/share/zoneinfo | mysql -uroot mysql -p$passwd
if [ $? -ne 0 ]
then
echo -e "\e[7;31m 导入时区数据到数据库失败，请手动导入。。\e[0m"
exit 2
fi
echo -e "\e[7;32m 导入时区数据到数据库成功\e[0m"
sed -i '/\[mysqld\]/d' /etc/my.cnf.d/server.cnf
cat >>  /etc/my.cnf.d/server.cnf <<EOF
[mysqld]

character_set_server = utf8mb4
collation_server = utf8mb4_unicode_ci
character_set_client = utf8mb4
max_connections = 100
max_heap_table_size = 48M
max_allowed_packet = 16777216
join_buffer_size = 64M
tmp_table_size = 64M
innodb_file_per_table = ON
innodb_buffer_pool_size = 240M
innodb_doublewrite = OFF
innodb_lock_wait_timeout = 50
innodb_flush_log_at_timeout = 3
innodb_read_io_threads = 32
innodb_write_io_threads = 16
EOF
systemctl restart mariadb
if [ $? -ne 0 ]
then
echo -e "\e[1;32m 数据库重启失败，请检查配置文件。。\e[0m"
exit 3
fi
sed -i 's/^com2sec notConfigUser  default       public/com2sec notConfigUser  127.0.0.1     public/' /etc/snmp/snmpd.conf
sed -i '/^access  notConfigGroup/c\access  notConfigGroup ""      any       noauth    exact  all    none   none' snmpd.conf 
sed -i '85s/#/ /' /etc/snmp/snmpd.conf
echo -e "\e[7;32m 配置文件修改成功。。。\e[0m"
#安装配置cacti
cd /var/www/html
wget http://www.cacti.net/downloads/cacti-1.1.23.tar.gz
if [ $? -ne 0 ]
then
echo -e "\e[1;31m 源码包地址失效，请手动下载。。。(或者更改脚本里面的地址)\e[0m"
exit 1
fi
tar zxvf cacti-1.1.23.tar.gz
#创建cacti数据库，创建cactiuser用户，并设置相关授权
mysql -uroot -p$passwd -e "CREATE database cacti default character set utf8"
mysql -uroot -p$passwd -e "create user 'cactiuser'@'localhost' identified by 'cactiuser'"
mysql -uroot -p$passwd -e "grant all privileges on cacti.* to cactiuser@localhost"
mysql -uroot -p$passwd -e "grant select on mysql.time_zone_name to 'cactiuser'@'localhost' identified by 'cactiuser'"
mysql -uroot -p$passwd -e "flush privileges"
#导入cacti默认数据库
mysql -uroot -p$passwd cacti < /var/www/html/cacti-1.1.23/cacti.sql
if [ $? -ne 0 ]
then
echo -e "\e[1;31m 导入sql错误，请手动导入。。。\e[0m"
exit 4
fi
cat >> /var/www/html/cacti-1.1.23/include/config.php <<EOF
\$database_type = "mysql";

\$database_default = "cacti";

\$database_hostname = "localhost";

\$database_username = "cactiuser";

\$database_password = "cactiuser";

/* load up old style plugins here */

\$plugins = array();

//\$plugins[] = 'thold'
EOF
#创建 cacti 系统用户，设置 graph/log 目录权限
useradd -r -M cacti
ln -s /var/www/html/cacti-1.1.23 /var/www/html/cacti
chown -R apache.apache /var/www/html/cacti/
chown -R cacti /var/www/html/cacti-1.1.23/{rra,log}/
echo "*/5 * * * * /usr/bin/php /var/www/html/cacti/poller.php > /dev/null 2>&1" > /var/spool/cron/root
systemctl enable httpd
systemctl enable mariadb
systemctl enable crond
systemctl enable snmpd
systemctl restart httpd
systemctl restart mariadb
systemctl restart crond
systemctl restart snmpd
echo -e "\e[1;33m 部署成功。。请打开浏览器访问\e[0m"
echo -e "\e[1;33m http://$ip/cacti \e[0m"
echo -e "\e[1;33m 一定要完成浏览器页面的配置，在往下执行！！ \e[0m"
while :
do
read -p "是否完成浏览器页面配置。（请输入y/n）" char
if ! test "$char" == "y" -o "$char" == "n"
then
echo "请重新输入！！y or n  ......"
continue
else
break 
fi
done
if [ "$char" == "n"  ]
then
echo -e "\e[1;33m 请先完成浏览器页面的配置!!!!! \e[0m"
echo "退出。。"
exit 7
else 
echo -e "\e[1;33m 按任意键继续部署 \e[0m"
read -n1
fi

#下载解压与 Cacti 相同版本号 Spine 源码安装包 编译 安装 修改配置文件
cd /usr/local/src
wget http://www.cacti.net/downloads/spine/cacti-spine-1.1.23.tar.gz
if [ $? -ne 0 ]
then
echo -e "\e[1;31m 源码包地址失效，请手动下载。。。(或者更改脚本里面的地址)\e[0m"
exit 1
fi 
tar xf cacti-spine-1.1.23.tar.gz 
ln -s /usr/lib64/libmysqlclient.so.18.0.0 /usr/lib64/libmysqlclient.so
cd cacti-spine-1.1.23
./configure && make && make install
if [ $? -ne 0 ]
then
echo -e "\e[7;31m 编译失败，请手动编译....\e[0m"
fi
echo -e "\e[7;32m 编译成功。。。\e[0m"
cp /usr/local/spine/etc/spine.conf.dist /usr/local/spine/etc/spine.conf



echo -e "\e[1;33m 部署完成，请浏览器访问操作! \e[0m"
echo -e "\e[1;33m http://$ip/cacti \e[0m"




