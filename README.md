# ssh-batch
简单主机批量管理工具

已实现：

    1.实现主机分组
    
    2.登录后显示主机分组，选择分组后查看主机列表
    
    3.可批量执行命令，发送文件，结果实时返回
    
    4.主机用户名密码可以不同
    
  ssh-batch启动方式

在 work/bin 目录下 执行 python ssh_client.py  start

主要代码存储在core目录下，data/accounts目录下存放主机用户名密码等信息
