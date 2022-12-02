# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 14:13:14 2022

@author: Gökhan Akay
"""

import selenium
import requests
from selenium import webdriver

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get("https://www.isyatirim.com.tr/tr-tr/analiz/hisse/Sayfalar/sirket-karti.aspx?hisse=KCHOL")    
