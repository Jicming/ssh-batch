#__author__:"jcm"
import paramiko
import configparser
#ssh paramiko 连接
class SSH_link(object):
    def __init__(self,host_config):
        self.title = host_config.name
        self.hostname = host_config.get('ipaddr')
        self.username = host_config.get('username')
        self.password = host_config.get('password')
        self.port = host_config.get('port')
        self.ssh = paramiko.SSHClient()

    def SSH_Connect(self):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.hostname,port=self.port,username=self.username,password=self.password)

    def SSH_Execute(self,commond):
        try:
            self.SSH_Connect()
            stdin, stdout, stderr = self.ssh.exec_command(commond)
            res, err = stdout.read(), stderr.read()
            result = res if res else err
            print('--------------------- %s(%s) -------------' % (self.title, self.hostname))
            print(result.decode('utf8'))
        except TimeoutError as f:
            print('--------------------- %s(%s) -------------' % (self.title, self.hostname))
            print('%s:%s 连接尝试失败'%(self.title,self.hostname))





