#!/usr/bin/env bash
#
#
usage: ping
email: x997870394@163.com
path: shell/ping.sh
author: akg7741
date: 2019/10/14

read -p "请输入你要查询的ip地址段: " netip
for ip in $(seq 254);do
  {
    ping -c1 -s0.1 ${netip}.${ip} &>/dev/null
    if [ $? -eq 0 ];then
       echo ${netip}.${ip} >>/tmp/iplist.txt
    fi
   }&
done
echo "finish"
