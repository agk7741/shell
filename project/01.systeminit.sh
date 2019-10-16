#!/usr/bin/env bash
#
# filepath: shell/project/01.systeminit.sh
# email: hlions@163.com
# author: hlions
# date: 2019/10/12/16:36
# modify_time: @times
# usage: system init of website.


# 关闭防火墙和selinux
systemctl stop firewalld && systemctl disable firewalld
sed -i s/SELINUX=enfrocing/SELINUX=disabled/g /etc/selinux/config
setenforce 0

# 在系统中安装常用的运维工具
yum -y install vim unzip wget lsof net-tools epel-release ntpdate
yum -y groupinstall "Development Tools"

# 

