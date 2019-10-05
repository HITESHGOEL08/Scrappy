
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.support import ui

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


import datetime
from datetime import date

import urllib.request
from collections import Counter

browser = webdriver.Chrome('/usr/bin/chromedriver')
browser.set_window_size(1200,1400)
browser.set_window_position(0,0)
browser.get('https://www.budget.com/en/home')
sleep(10)
browser.find_element_by_xpath('//*[@id="PicLoc_value"]').clear()
browser.find_element_by_xpath('//*[@id="PicLoc_value"]').send_keys('HNL')
sleep(2)
# browser.find_element_by_xpath('//*[@id="DropLoc_value"]').clear()
# browser.find_element_by_xpath('//*[@id="DropLoc_value"]').send_keys('HNL')
sleep(2)
# browser.findElement(By.id("res-home-select-car")).submit()#.click()
browser.find_element_by_xpath('//*[@id="res-home-select-car"]').click()
# sleep(6)
sleep(6)
print("hello")



# today = date.today()
# today = today.strftime("%m/%d/%Y")
# date_1 = datetime.datetime.strptime(today, "%m/%d/%Y")
# print(date_1)
# end_date = date_1 + datetime.timedelta(days=1)
# end_date1 = end_date.strftime("%m/%d/%Y")
# print(today,end_date1)
