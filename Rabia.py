#!/usr/bin/python2
#coding=utf-8
try:
    import os
    import sys
    import time
    import datetime
    import re
    import threading
    import json
    import random
    import requests
    import hashlib
    import cookielib
    import uuid
    import getpass
    import mechanize
    from multiprocessing.pool import ThreadPool
    from requests.exceptions import ConnectionError
except ImportError:
    os.system('pip2 install requests')
    os.system('pip2 install mechanize')
    os.system("pip2 install lolcat")
    os.system('python2 ztst.py')
    __author__ = 'Bilal-Khan'
    __copyright = 'All rights reserved . Copyright  Bilal-Khan'
os.system('termux-setup-storage')

try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass

bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)
header = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
os.system('git pull')
os.system('clear')

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.1)
##### INTRO #####
logo ="""
\033[1;94m ########  #### ##        #########  ##
 \033[1;94m##     ##  ##  ##       ##       ## ##
 \033[1;92m##     ##  ##  ##       ##       ## ##
 \033[1;92m########   ##  ##       ########### ##
 \033[1;92m##     ##  ##  ##       ##       ## ##
 \033[1;94m##     ##  ##  ##       ##       ## ##
 \033[1;94m########  #### ######## ##       ## ########
\033[1;95m::::::::::::::::::::::::::::::::::::::::::::::::::
\033[1;92m[✓]\033[1;93m MAKER       :   TIPU SULTAN
\033[1;92m[✓]\033[1;93m FACEBOOK    :   Tipu Sultan
\033[1;92m[✓[\033[1;93m WHATSAPP    :   +92333******
\033[1;92m[✓]\033[1;93m CITY        :   Punjab
\033[1;92m[✓]\033[1;96m Change Is The Unchangeable Law Of Nature
\033[1;95m::::::::::::::::::::::::::::::::::::::::::::::::::"""
CorrectUsername = "bilo@#223344"
CorrectPassword = "bilo@#234567"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m\x1b[1;91mKEY-NO-1 🔐 \x1b[1;97m»» \x1b[1;92m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m \x1b[1;91mKEY-NO-2 🔐  \x1b[1;97m»» \x1b[1;92m")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username #BilalKhan
	    time.sleep(2)
            loop = 'false'
        else:
            print "\033[1;94mWrong Password"
            os.system('xdg-open https://wa.me/+923485664243')
    else:
        print "\033[1;94mWrong Username"
        os.system('xdg-open https://wa.me/+923485664243')



##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


def reg():
    os.system('clear')
    print logo
    print ''
    print '\033[1;31;1mTake The Approval For Login'
    print ''
    time.sleep(1)

    try:
        to = open('/sdcard/.JaNaN404.txt', 'r').read()
    except (KeyError, IOError):
        reg2()
