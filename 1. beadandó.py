# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 12:55:52 2022

@author: bpank
"""

#Csomagok
import re #regex kódolás -> szöveg összehasonlítás

#Változók
ip = [] #lista az ip címeknek
e = 0 #hibás adatok száma (nem ipv6 típusú ip címek)
elist = [] #hibás adatok listája
a = 0 #2001:0db8 kezdetű ip címek
b = 0 #2001:0e kezdetű ip címek
c = 0 #fc vagy fd kezdetű ip címek
d = 0 #további ip címek

#Fájl megnyítása és beolvasása
with open('ip.txt') as f:
    ip = f.readlines()
    
#Adatsorok száma
n = len(ip)
        
#Ip címek kategorizálása
for i in ip:
    s = re.search("....:....:....:....:....:....:....:....", i)
    
    #a nem ipv6 típusú adatok megszámolása és elmentése egy külön listába
    if s is None: 
        e = e+1
        elist.append(i)
    #az ipv6 típúsú ip címek kategorizálása
    else:
        if re.search("2001:0db8.*", i) is not None:
            a = a + 1
        elif re.search("2001:0e.*", i) is not None:
            b = b + 1
        elif re.search("fc.*", i) is not None:
            c = c + 1
        elif re.search("fd.*", i) is not None:
            c = c + 1
        else:
            d = d + 1
    
#Eredmények kiírása
print("Adatsorok száma: ", n)
print("Dokumentációs ip-címek: ", a)
print("Globális ip-címek: ", b)
print("Eszközöknek kiosztott helyi ip-címek: ", c)

#Hibás adatok kiírása a felhasználó számára
if d != 0:
    print("Egyéb típusú ip-címek száma: ", d)
if e != 0:
    print("Nem ipv6 típusú adatok száma: ", e)    
