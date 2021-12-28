import os
import sys
import time
import json
import urllib2
import base64
from datetime import datetime, timedelta
from termcolor import cprint, colored
from base64 import *

r = "\33[31;1m"
y = "\33[33;1m"
g = "\33[32;1m"
w = "\33[37;1m"

def ins():
        time.sleep(1)
        os.system("clear")
        try:
                file_data = open("data/credits.txt")
                os.system("python2 run.py")
        except:
                print( (datetime.now() + timedelta()).strftime(g+'['+w+'%H:%M:%S'+g+']')+" Installing Tools ...")
                time.sleep(1)
                os.system("mkdir data")
                os.system("touch data/credits.data")
                file_credits = open("data/credits.data", "w")
                code_credits = 'Author : ItzHex08\nVersion : 1.0.1\nGitHub : https://github.com/ItzHex08\n'
                file_credits.write(code_credits)
                file_credits.close()
ins()
