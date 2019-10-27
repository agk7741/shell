#!/bin/bash
#kvm batch create vm tool
#version: 0.1
#author: wing
red='\e[1;31m'
green='\e[1;32m'
yellow='\e[1;33m'
blue='\e[1;34m'
pink='\e[1;35m'
clean='\e[0m'
install_kvm(){
 :
}
manage_kvm(){
cat <<-EOF
`echo -e "\e[1;33m========================================="`
            查看虚拟机——1
            启动虚拟机——2
            关闭虚拟机——3
            重启虚拟机——4
            重置虚拟机——5
            暂停虚拟机——6
            恢复虚拟机——7
            删除虚拟机——8
            虚拟机开机自动启动——9
            查看虚拟机配置文件——l
            返回上一层——c
            退出——q
`echo -e "=========================================\e[0m"`
EOF
read -p " 请输入选项：" num
echo -e "\e[1;32m"
case "$num" in
1)
sleep 1
virsh list --all
;;
2)
read -p "请输入你要启动的虚拟机：" vm
virsh list --all | grep $vm &>/dev/null
if [ ! $? -eq 0 ];then
echo "请输入正确的虚拟机。"
sleep 1
continue
fi
virsh start $vm
;;
3)
read -p "请输入你要关闭的虚拟机：" vm
virsh list --all | grep $vm &>/dev/null
if [ ! $? -eq 0 ];then
echo "请输入正确的虚拟机。"
sleep 1
continue

fi
virsh shutdown $vm
;;
4)
read -p "请输入你要重启的虚拟机：" vm
virsh list --all | grep $vm &>/dev/null
if [ ! $? -eq 0 ];then
echo "请输入正确的虚拟机。"
sleep 1
continue

fi
virsh reboot $vm
;;
5)
read -p "请输入你要重置的虚拟机：" vm
virsh list --all | grep $vm &>/dev/null
if [ ! $? -eq 0 ];then
echo "请输入正确的虚拟机。"
sleep 1
continue

fi
virsh reset $vm
;;
6)
read -p "请输入你要暂停的虚拟机：" vm
virsh list --all | grep $vm &>/dev/null
if [ ! $? -eq 0 ];then
echo "请输入正确的虚拟机。"
sleep 1
continue

fi
virsh suspend $vm
;;
7)
read -p "请输入你要恢复的虚拟机：" vm
virsh list --all | grep $vm &>/dev/null
if [ ! $? -eq 0 ];then
echo "请输入正确的虚拟机。"
sleep 1
continue

fi
virsh resume $vm
;;
8)
read -p "请输入你要删除的虚拟机：" vm
virsh list --all | grep $vm &>/dev/null
if [ ! $? -eq 0 ];then
echo "请输入正确的虚拟机。"
sleep 1
continue

fi
virsh undefine $vm
;;
9)
read -p "请输入你要开机启动的虚拟机：" vm
virsh list --all | grep $vm &>/dev/null
if [ ! $? -eq 0 ];then
echo "请输入正确的虚拟机。"
sleep 1
continue

fi
virsh autostart $vm
;;
l)
read -p "请输入你要查看的虚拟机：" vm
virsh list --all | grep $vm &>/dev/null
if [ ! $? -eq 0 ];then
echo "请输入正确的虚拟机。"
sleep 1
continue

fi
virsh dumpxml $vm
;;
c)
sleep 1
break
;;
q)
echo -e "\e[0m"
exit 2
;;
*)
echo -e "请重新输入正切选项"
sleep 1
continue

esac
echo -e "\e[0m"
}
create_vm(){
#需要事先准备模板镜像和配置文件模板
model1=/var/lib/libvirt/images/model.qcow2
model2=/etc/libvirt/qemu/model.xml
p_model1=/var/lib/libvirt/images/
p_model2=/etc/libvirt/qemu/
#echo -e "\e[1;5;32m需要事先准备模板镜像和配置文件模板!\e[0m"
ls -l /var/lib/libvirt/images | grep model.qcow2 &>/dev/null
if [ ! $? -eq 0 ];then
echo -e "${red} 没有查询到文件模板！${clean}"
exit 1
fi
ls -l /etc/libvirt/qemu/ | grep model.xml &>/dev/null
if [ ! $? -eq 0 ];then
echo  -e "${red}没有查询到配置文件！${clen}"
exit 1
fi
echo -e "${yellow}请输入需要的内存：${clean}"
read -n1 new_memory
echo
if [[ ! $new_memory =~ [1-9] ]];then
echo -e "${red}请输入1-9的数字${clean}"
sleep 1
continue
fi
echo -e "${yellow}请输入cup个数：${clean}" 
read -n1 new_cpu
echo
if [[ ! $new_cpu =~ [1-9] ]];then
echo -e "${red}请输入1-9的数字${clean}"
sleep 1
continue
fi
echo -e "${yellow}请输入创建个数：${clean}"
read -n1 new_vmnum
echo
if [[ ! $new_vmnum =~ [1-9] ]];then
echo -e "${red}请输入1-9的数字${clean}"
sleep 1
continue 
fi
for i in `seq $new_vmnum`
do
new_name="vm${RANDOM}"
new_uuid=`uuidgen`
echo "$new_name"
echo "$new_uuid"
#new_memory=
#new_cpu=
#new_vmnum=
n_new_memory=${new_memory}000000
new_mac=`openssl rand -hex 3 | sed -r 's/(..)\B/\1:/g'`
cp $model1  ${p_model1}${new_name}.qcow2 
if [ ! $? -eq 0 ];then
echo "复制出错${new_name}.qcow2"
exit 2
fi
cp $model2  ${p_model2}${new_name}.xml
if [ ! $? -eq 0 ];then
echo "复制出错${new_name}.xml"
exit 2
fi
sed -i "s/vm_name/$new_name/;s/vm_uuid/$new_uuid/;s/vm_memory/$n_new_memory/;s/vm_cpu/$new_cpu/;s/vm_mac/$new_mac/" ${p_model2}${new_name}.xml
virsh define ${p_model2}${new_name}.xml
done
virsh list --all
}
memu(){
cat <<-EOF
`echo -e "\e[4;7;1;5;33m=================== 一键部署,管理KVM ===================\e[0m ${green}"`
`printf "%-0s%10s%35s%15s\n" "||" "选 项" "功能实现" "||"`
`echo "========================================================"`
`printf "%-6s%-25s%-28s\n"  "||" "1-c" "*创建虚拟机*"``echo "||"`
`printf "%-6s%-25s%-28s\n"  "||" "2-k" "*克隆虚拟机*"``echo "||"`
`printf "%-6s%-25s%-28s\n"  "||" "3-p" "*创建存储池*"``echo "||"`
`printf "%-6s%-25s%-28s\n"  "||" "4-s"  "*快照虚拟机*"``echo "||"`
`printf "%-6s%-25s%-28s\n"  "||" "5-m" "*管理虚拟机*"``echo "||"`
`printf "%-6s%-25s%-28s\n"  "||" "6-d" "*删除虚拟机*"``echo "||"`
`printf "%-6s%-25s%-27s\n"  "||" "7-q" "*退出管理-*"``echo "||"`
`printf "%-6s%-25s%-27s\n"  "||" "8-n" "*网络管理*-"``echo "||"`
`printf "%-6s%-25s%-27s\n"  "||" "9-g" "*磁盘挂载-*"``echo "||"`
`echo "========================================================"`
`echo -en "${clean}"`
EOF
echo -en "${pink}请输入选项：${clean}"
read -n1 opt
echo 
}
memu 
while :
do
case $opt in 
c)
echo -e "${pink}--* 创建虚拟机 *--${clean}"
create_vm
;;
q)
echo -e "${red}退出。。${clean}"
exit 1
;;
m)
manage_kvm
;;
*)
echo "hello"
exit 1
esac
done















