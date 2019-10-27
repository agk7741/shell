#!/bin/bash
echo -e "\e[7;35m 准备环境！时间会有点长，请耐心等待。。。。。。\e[0m"
echo -e "\e[7;32m 请确保关闭防火墙！！！文件请提前上传到root目录下 \e[0m"
groupadd haclient
useradd -g haclient hacluster
yum -y install epel-release &> /dev/null
yum -y install gcc gcc-c++ autoconf automake libtool glib2-devel libxml2-devel bzip2 bzip2-devel e2fsprogs-devel libxslt-devel libtool-ltdl-devel asciidoc &>/dev/null
echo -e "\e[1;32m 环境准备完毕！准备解压！\e[0m"
cd /root
#安装glue
tar xf 0a7add1d9996.tar.bz2
if [ $? -ne 0 ]
then 
echo -e "\e[1;31m 请上传文件到指定目录！\e[0m"
fi
cd /root/Reusable-Cluster-Components-glue--0a7add1d9996/
./autogen.sh
./configure --prefix=/usr/local/heartbeat --with-daemon-user=hacluster --with-daemon-group=haclient --enable-fatal-warnings=no LIBS='/lib64/libuuid.so.1'
make && make install
if [ $? -eq 0 ]
then
echo -e "\e[7;32m 安装glue成功！\e[0m"
else
echo -e "\e[7;31m 安装glue失败！\e[0m"
exit 1
fi
cd /root

#安装Resource Agents
tar xf resource-agents-3.9.6.tar.gz
cd /root/resource-agents-3.9.6/
./autogen.sh 
./configure --prefix=/usr/local/heartbeat --with-daemon-user=hacluster --with-daemon-group=haclient --enable-fatal-warnings=no LIBS='/lib64/libuuid.so.1'
make && make install
if [ $? -eq 0 ]
then
echo -e "\e[7;32m 安装Resource Agents成功！\e[0m"
else
echo -e "\e[7;31m 安装Resource Agents失败！\e[0m"
exit 2
fi
cd /root


#安装HeartBeat
tar xf 958e11be8686.tar.bz2
cd /root/Heartbeat-3-0-958e11be8686/
./bootstrap
export CFLAGS="$CFLAGS -I/usr/local/heartbeat/include -L/usr/local/heartbeat/lib"
./configure --prefix=/usr/local/heartbeat --with-daemon-user=hacluster --with-daemon-group=haclient --enable-fatal-warnings=no LIBS='/lib64/libuuid.so.1'
make && make install
if [ $? -eq 0 ]
then
echo -e "\e[7;32m 安装HeartBeat成功！\e[0m"
else
echo -e "\e[7;31m 安装HeartBeat失败！\e[0m"
exit 3
fi
cp doc/{ha.cf,haresources,authkeys} /usr/local/heartbeat/etc/ha.d/
if [ $? -ne 0 ]
then
echo "复制文件错误，请手动复制。。。"
fi
cd ..


#配置网卡支持插件文件
mkdir -pv /usr/local/heartbeat/usr/lib/ocf/lib/heartbeat/
cp /usr/lib/ocf/lib/heartbeat/ocf-* /usr/local/heartbeat/usr/lib/ocf/lib/heartbeat/
#注意：一般启动时会报错因为 ping和ucast这些配置都需要插件支持 需要将lib64下面的插件软连接到lib目录 才不会抛出异常

ln -svf /usr/local/heartbeat/lib64/heartbeat/plugins/RAExec/* /usr/local/heartbeat/lib/heartbeat/plugins/RAExec/
ln -svf /usr/local/heartbeat/lib64/heartbeat/plugins/* /usr/local/heartbeat/lib/heartbeat/plugins/
echo -e "\e[7;32m 成功完成配置，请继续手动操作！\e[0m"
