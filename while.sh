while :
do
cat <<-EAF
     +---------------------------------+
     |     系统管理工具                |
     +---------------------------------+
     |                                 |
     |    1.显示用户数量               |
     |    2.显示进程数量               |
     |    3.退出                       |
     +---------------------------------+
EAF

read -p "please input you choose: "  choose
case ${choose} in
  1)
     number=$(wc -l /etc/passwd)
     echo "user number: ${number:0:3}"
     ;;
  2)
     number=$(ps aux | wc -l)
     echo "procsee number: ${number}"
     ;;
  3)
     exit
     ;;
  *)
     echo "输入错误，请重新输入"
esac
done
