#!/bin/bash
node1ip=192.168.240.111
node2ip=192.168.240.30
name=llhq
nodename=elk-node2
testip=$node2ip
rpm --import https://packages.elastic.co/GPG-KEY-elasticsearch
cat > /etc/yum.repos.d/elasticsearch.repo <<EOF
[elasticsearch-2.x]
name=Elasticsearch repository for 2.x packages
baseurl=http://packages.elastic.co/elasticsearch/2.x/centos
gpgcheck=0
gpgkey=http://packages.elastic.co/GPG-KEY-elasticsearch
enabled=1
EOF
yum -y install -y epel-release &> /dev/null
yum install -y elasticsearch  redis nginx  java
#elasticsearch 配置
mkdir -p /data/es-data &> /dev/null
chown  -R elasticsearch.elasticsearch /data/
cat >>  /etc/elasticsearch/elasticsearch.yml  <<EOF
cluster.name: $name
node.name: $nodename  
path.data: /data/es-data 
path.logs: /var/log/elasticsearch/   
bootstrap.mlockall: true  
network.host: 0.0.0.0         
http.port: 9200       
discovery.zen.ping.multicast.enabled: false
discovery.zen.ping.unicast.hosts: ["$node1ip","$node2ip"]
EOF
systemctl  start elasticsearch 
if [ $? -eq 0 ]
then
systemctl enable elasticsearch &>/dev/null
echo -e "\e[7;32m elasticsearch 配置成功，请打开网页检查！\e[0m"
echo -e "\e[7;32m http://$testip:9200/ \e[0m"
else
echo -e "\e[7;31m elasticsearch 配置失败，请手动检查问题！\e[0m"
exit 1
fi
echo -e "\e[1;33m 按任意键继续部署logstash \e[0m"
read -n1

#安装插件
 /usr/share/elasticsearch/bin/plugin install mobz/elasticsearch-head
if [ $? -ne 0 ]
then
echo -e "\e[1;31m 安装插件1失败请检查日志或手动下载！\e[0m"
exit 6
fi
 chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/plugins
systemctl  restart  elasticsearch
if [ $? -ne 0 ]
then
echo -e "\e[1;31m elasticsearch重启失败请检查日志！\e[0m"
exit 4
fi
/usr/share/elasticsearch/bin/plugin install lmenezes/elasticsearch-kopf
if [ $? -ne 0 ]
then
echo -e "\e[1;31m 安装插件2失败请检查日志或手动下载！\e[0m"
exit 6
fi
 chown -R elasticsearch:elasticsearch /usr/share/elasticsearch/plugins
systemctl  restart  elasticsearch
if [ $? -ne 0 ]
then
echo -e "\e[1;31m elasticsearch重启失败请检查日志！\e[0m"
exit 5
fi
echo -e "\e[1;32m 请访问网址进行测试！\e[0m"
echo -e "\e[1;33m http://$testip:9200/_plugin/head/ \e[0m"
echo -e "\e[1;33m http://$testip:9200/_plugin/kopf \e[0m"
echo -e "\e[1;33m 按任意键继续部署logstash \e[0m"
read -n1


#部署logstash
rpm --import https://packages.elastic.co/GPG-KEY-elasticsearch
if [ $? -ne 0 ]
then
echo -e "\e[7;31m rpm包安装失败，请手动安装！\e[0m"
exit 2
fi
cat >/etc/yum.repos.d/logstash.repo<<EOF
[logstash-2.1]
name=Logstash repository for 2.1.x packages
baseurl=http://packages.elastic.co/logstash/2.1/centos
gpgcheck=0
gpgkey=http://packages.elastic.co/GPG-KEY-elasticsearch
enabled=1
EOF
 yum install -y logstash
if [ $? -ne 0 ] 
then 
echo -e "\e[7;31m Yum 安装logstash失败，请手动安装！\e[0m"
exit 3
fi
echo -e "\e[7;32m 部署logstash 成功！\e[0m"
while :
do
read -p "是否退出，进行测试。（请输入y/n）" char
if ! test "$char" == "y" -o "$char" == "n"
then
echo "请重新输入！！y or n  ......"
continue
else
break 
fi
done
if [ "$char" == "y"  ]
then
echo "退出。。"
exit 7
else 
echo -e "\e[1;33m 按任意键继续部署kibana \e[0m"
read -n1
fi


##部署kibana
#cd /usr/local/src
# wget https://download.elastic.co/kibana/kibana/kibana-4.3.1-linux-x64.tar.gz
#if [ $? -ne 0 ]
#then
#echo -e "\e[1;31m 源码包地址失效，请手动下载源码包！\e[0m"
#fi
#tar zxf kibana-4.3.1-linux-x64.tar.gz
#mv kibana-4.3.1-linux-x64 /usr/local/
#ln -s /usr/local/kibana-4.3.1-linux-x64/ /usr/local/kibana
#cd /usr/local/kibana/config
#cp kibana.yml kibana.yml.bak
#cat >>/usr/local/kibana/config/kibana.yml <<EOF
#server.port: 5601
#server.host: "0.0.0.0"
#elasticsearch.url: "http://$testip:9200"
#kibana.index: ".kibana"
#EOF
#yum -y install screen 
#echo -e "\e[1;35m 请手动启动kibana \e[0m" 
#echo -e "\e[1;33m  /usr/local/kibana/bin/kibana \e[0m"
#echo -e "\e[1;33m  http://$testip:5601 \e[0m"
