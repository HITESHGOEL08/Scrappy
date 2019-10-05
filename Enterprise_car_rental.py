from selenium import webdriver
# import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from bs4 import BeautifulSoup
# import pandas as pd
from selenium.webdriver.support import ui

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait


import datetime
from datetime import date

browser = webdriver.Chrome('/usr/bin/chromedriver')
browser.set_window_size(1200,1400)
browser.set_window_position(0,0)
browser.get('https://www.enterprise.com/en/home.html')
sleep(10)