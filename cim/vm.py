from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import tkinter as tk
import secrets
import random
import string
import os

###TEMP-NAMES###

t = random.randint(30,31)
t1 = random.randint(200,320)
t2 = random.randint(5,60)
url_list= ['https://shortznewz.blogspot.com/2022/04/some-best-places-in-dubai.html?m=1', 'https://shortznewz.blogspot.com/2022/04/best-places-to-visit.html', 'https://shortznewz.blogspot.com/2022/04/facts-about-humans.html', 'https://shortznewz.blogspot.com/2022/04/random-facts.html', 'https://shortznewz.blogspot.com/2022/04/interesting-facts.html']
url = random.choice(url_list)
driver = webdriver.Chrome()
driver.get(url)
time.sleep(4)
languages = 8
for i in range(languages):
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[i+1])
    driver.get(url)
    time.sleep(10)
    driver.find_element_by_xpath('/html/body/div/div[2]/aside/div/div[1]/div[1]/div[1]/button').click()
    time.sleep(5)
time.sleep(300)
