#__author__:"jcm"
import paramiko
import configparser

class SSH_link(object):
    def __init__(self,host_config):
        self.title = host_config.name
        self.hostname = host_config.get('ipaddr')
        self.username = host_config.get('username')
        self.password = host_config.get('password')
        self.port = host_config.get('port')
        self.ssh = paramiko.SSHClient()
        self.SSH_Connect()
    def SSH_Connect(self):
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=self.hostname,port=self.port,username=self.username,password=self.password)
    def SSH_Execute(self,commond):
        stdin,stdout,stderr = self.ssh.exec_command(commond)
        res,err = stdout.read(),stderr.read()
        result = res if res else err

        print('--------------------- %s(%s) -------------'%(self.title,self.hostname))
        print(result.decode('utf8'))


