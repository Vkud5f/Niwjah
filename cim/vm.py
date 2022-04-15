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
ov1 = random.randint(1,15)
t = random.randint(8,15)
t1 = random.randint(5,10)
t2 = random.randint(5,20)
ov = random.randint(270,300)
url_list= ['https://shortznewz.blogspot.com/2022/04/some-best-places-in-dubai.html?m=1', 'https://shortznewz.blogspot.com/2022/04/best-places-to-visit.html', 'https://shortznewz.blogspot.com/2022/04/facts-about-humans.html', 'https://shortznewz.blogspot.com/2022/04/random-facts.html', 'https://shortznewz.blogspot.com/2022/04/interesting-facts.html']
url = random.choice(url_list)
driver = webdriver.Chrome()
time.sleep(ov1)
driver.get(url)
languages = 8
for i in range(languages):
    driver.execute_script("window.open()")
    driver.switch_to.window(driver.window_handles[i+1])
    time.sleep(t1)
    driver.get(url)
    time.sleep(15)
    driver.find_element_by_xpath('//*[@id="HTML7"]/div[1]/button').click()
    time.sleep(t2)
time.sleep(ov)
