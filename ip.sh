#!/usr/bin/env bash

a=$(egrep "*com|cn" url.txt)
for o in ${a};do
  stau=$(curl -I --connect-timeout 3 -m 10 -s ${o} | grep "HTTP")
  if [[ ${stau:9:3} -eq 200 ]] || [[ ${stau:9:3} -eq 302 ]];then
     echo "$(date +'%Y-%m-%d %H:%M:%S') - run monitor program ${o}  is ok" >>/var/log/urlMonitor.log
  else
     echo "$(date +'%Y-%m-%d %H:%M:%S') - run monitor program ${o} is failed" >>/var/log/urlMonitor.log
     echo "[ERROR] ${o} Downtime! Please repair." | mail -s "warnning website" x997870394@163.com
  fi
done
