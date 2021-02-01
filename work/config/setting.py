#__author__:"jcm"
import os,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
opts_dir=os.path.join(BASE_DIR,r'data\accounts')
def collect_cfg():
    cfg_dir_list = [os.path.join(opts_dir,i)  for i in [file for a,b,file in os.walk(opts_dir)][0]]
    return cfg_dir_list

