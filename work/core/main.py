#__author__:"jcm"
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
from config import setting
from core import ssh_client
import configparser
import optparse
import queue
import threading

class ArvgHandler(object):
    def __init__(self,filename=os.path.basename(__file__)):
        self.filename = filename
        self.parser = optparse.OptionParser()
        (options, args) = self.parser.parse_args()
        self.verify_args(options, args)
    def verify_args(self,options,args):
        if args:
            if hasattr(self,args[0]):
                func = getattr(self,args[0])
                func()
            else:
                exit("usage:python %s start/stop"%self.filename)
        else:
            exit("usage:python %s start/stop"%self.filename)
    def start(self):
        print('---\033[32;1m批量程序已启动 \033[0m----')
        while True:
            groups = self.group_list()
            num=1
            groups_dict={}
            for key in  groups:
                print('%s host group %s [%s]'%(num,num,len(groups[key])))
                groups_dict[str(num)] = key
                num+=1


            while True:
                flog_1 = input('#>')
                if flog_1 in groups_dict.keys():
                    hosts = []
                    config_obj = self.config_read(groups_dict[flog_1])
                    for i in config_obj.sections():
                        hosts.append(config_obj[i])
                    flogs ='''
                         %s1.exec df\n2.send file
                    '''%''.join(['%s : %s\n'%(i.name,i.get('IPADDR')) for i in hosts])
                    print(flogs.lstrip())
                    q = queue.Queue()


                while True:
                    [q.put(i, block=False,timeout=0.1) for i in hosts]
                    flog_2 = input('#>')
                    global ssh_client
                    if flog_2 == '1':
                        count = q.qsize()
                        t_objs = []

                        for i in range(count):
                            ssh = ssh_client.SSH_link(q.get)
                            threads = threading.Thread(target=ssh.SSH_Execute,args=('df',))
                            threads.start()
                            t_objs.append(threads)
                        for t in t_objs:
                            t.join()
                    if flog_2 == '2':
                        count = q.qsize()
                        t_objs =[]
                        for i in range(count):
                            ssh = ssh_client.SSH_link(q.get())
                            threads = threading.Thread(target=ssh.SSH_Execute,args=('cp /tmp/test.py /opt/',))
                            threads.start()
                            t_objs.append(threads)
                        for  t in t_objs:
                            t.join()
    def group_list(self):
        config_file_dirs = setting.collect_cfg()  #获取存放服务器信息的地址列表
        host_list =[]
        group_dir={}
        for i in config_file_dirs:
            config_obj = self.config_read(i)
            for j in config_obj.sections():
                host_list.append(config_obj[j].get('IPADDR'))
            group_dir[i]=host_list
            host_list = []

        return group_dir
    def config_read(self,read_obj):
        config_obj = configparser.ConfigParser()
        config_obj.read(read_obj)
        return config_obj
    def queue_put(self):
        queues = queue.Queue()
        queues.put()
ArvgHandler().group_list()

