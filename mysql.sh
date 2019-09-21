#!/usr/bin/env bash
#
#
#
#author:mc wang
#usage:源码编译数据库

systemctl stop firewalld && systemctl disable firewalld
sed -i s/SELINUX=enfrocing/SELINUX=disabled/g  /etc/selinux/config
setenforce 0
cd /usr/local
yum -y install unzip wget lsof net-tools ntpdate vim epel-release
yum -y install ncurses ncurses-devel openssl-devel bison gcc gcc-c++ make cmake
wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.28.tar.gz
wget http://sourceforge.net/projects/boost/files/boost/1.59.0/boost_1_59_0.tar.gz
groupadd mysql

useradd -r -g mysql -s /bin/false mysql

tar xf mysql-5.7.28.tar.gz

tar xf boost_1_59_0.tar.gz -C /usr/local/mysql-5.7.28 
cd mysql-5.7.28


if  [  $? -eq 0];then
  echo"完成，正在下一步"
else
   echo"出现错误。请排查"
fi

cmake . \
-DWITH_BOOST=boost_1_59_0/ \
-DCMAKE_INSTALL_PREFIX=/usr/local/mysql \
-DSYSCONFDIR=/etc \
-DMYSQL_DATADIR=/usr/local/mysql/data \
-DINSTALL_MANDIR=/usr/share/man \
-DMYSQL_TCP_PORT=3306 \
-DMYSQL_UNIX_ADDR=/tmp/mysql.sock \
-DDEFAULT_CHARSET=utf8 \
-DEXTRA_CHARSETS=all \
-DDEFAULT_COLLATION=utf8_general_ci \
-DWITH_READLINE=1 \
-DWITH_SSL=system \
-DWITH_EMBEDDED_SERVER=1 \
-DENABLED_LOCAL_INFILE=1 \
-DWITH_INNOBASE_STORAGE_ENGINE=1

make && make install
if  [  $? -eq 0];then
   echo"make完成，正在下一步"
else
    echo"出现错误。请排查"
fi

cd /usr/local/mysql
mkdir mysql-files
chown -R mysql.mysql /usr/local/mysql
 /usr/local/mysql/bin/mysqld --initialize --user=mysql --basedir=/usr/local/mysql --datadir=/usr/local/mysql/data
/usr/local/mysql/bin/mysql_ssl_rsa_setup --datadir=/usr/local/mysql/data
#mv /etc/my.cnf my.cnf.bak

echo "[mysqld]
skip-grant-tables 
basedir=/usr/local/mysql

datadir=/usr/local/mysql/data" >> /etc/my.cnf
cd /usr/local/mysql
cp support-files/mysql.server /etc/init.d/mysqld
chkconfig --add mysqld
chkconfig mysqld on
echo "export PATH=$PATH:/usr/local/mysql/bin" >> /etc/profile
source /etc/profile
echo $?
service mysqld start

if [ $? -eq 0];then
   echo"成功"
else
   echo"失败"
fi

