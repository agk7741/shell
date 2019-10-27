#!/bin/bash
#kvm batch create vm tool
#version: 1.0
#author:YYQ
#需要实现准备模板镜像和配置文件模板

cat <<-EOF
`echo -e "\e[1;34mCommand action(选项)\e[0m"`
`echo -e "\e[1;32m
		1.创建自定义配置单个虚拟机
		2.批量创建自定义配置虚拟机
		3.批量创建默认配置虚拟机
		4.删除虚拟机
		5.退出\e[0m"`
EOF

echo -en "\e[1;34minput number(请输入选项): \e[0m"
read num

case $num in
1)
#-----------------------------
images_pwd="/var/lib/libvirt/images/"
model_qcow2="centos7.0.qcow2"

xml_pwd="/etc/libvirt/qemu/"
model_xml="centos7.0.xml"

new_vmname=`date +%Y-%m-%d-%H:%M:%S`

cp $images_pwd$model_qcow2  $images_pwd$new_vmname.qcow2
cp $xml_pwd$model_xml $xml_pwd$new_vmname

read -p "请输入你创建主机的内存大小(G)：" vm_mem
read -p "请输入你创建主机的cpu个数：" vm_cpu
read -p "请输入你创建主机的磁盘个数：" vm_disk

new_mac=`openssl rand -hex 3 | sed -r 's/(..)\B/\1:/g'`
new_uuid=`uuidgen`
new_mem="$vm_mem0000"

sed -ri "s/model_name/$new_vmname/g;s/model_uuid/new_uuid/g;s/model_mem/$new_mem/g;s/model_cpu/vm_cpu/g;s/model_mac/new_mac/g" /etc/libvirt/qemu/$new_vmname.xml

virsh define $new_vmname.xml
virsh list --all
#-----------------------------
;;
2)
222
;;
3)
333
;;
4)
444
;;
5)
exit
;;
"")
;;
*)
echo "错误选项，请重新输入"
;;
esac
sleep 3

done


