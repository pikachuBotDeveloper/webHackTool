# !/usr/bin/env python
# -*- coding: utf-8 -*-
# turkhackteam.org/net
# Coded By Connec - Safak-Bey
#  .::Green Team::.

import os
import time

print("\033[1;31m[\033[1;33m*\033[1;31m]\033[1;32m turkhackteam.org/net")
time.sleep(1)
print("\033[1;31m[\033[1;33m*\033[1;31m]\033[1;32m Green Team Araç Kiti")
time.sleep(2)
print("\033[1;31m[\033[1;33m*\033[1;31m]\033[1;32m Ek paketler hazırlanıyor")
time.sleep(2)
print("\033[1;31m[\033[1;33m*\033[1;31m]\033[1;32m Paketler indiriliyor\033[0m")
time.sleep(1)

# Araçlar
os.system("apt-get install python3 -y")
os.system("apt-get install python3-pip -y")
os.system("apt-get install nmap -y")
os.system("apt-get install wpscan -y")
os.system("apt-get install sqlmap -y")
os.system("apt-get install assetfinder -y")
os.system("apt-get install subjack -y")
os.system("apt-get install dmitry -y")

# Modüller
os.system("pip3 install colored")
os.system("pip3 install requests")
os.system("pip3 install proxybroker")
os.system("pip3 install cookiejar")
os.system("pip3 install termcolor")
os.system("pip3 install http")
os.system("pip install googlesearch-python")

time.sleep(1)
print("\033[1;31m[\033[1;33m*\033[1;31m]\033[1;32m Paketler indirildi.")
time.sleep(2)
print("\033[1;31m[\033[1;33m*\033[1;31m]\033[1;32m Kurulum başarıyla tamamlandı.\033[0m")
