from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
import tkinter as tk
import secrets
import random
import string
import os
import random
import time
###TEMP-NAMES###
w = random.randint(65,105)
t = random.randint(10,25)
t1 = random.randint(100,220)
t2 = random.randint(5,40)
url_list= ['https://shortznewz.blogspot.com/2022/04/some-best-places-in-dubai.html?m=1', 'https://shortznewz.blogspot.com/2022/04/best-places-to-visit.html', 'https://shortznewz.blogspot.com/2022/04/facts-about-humans.html', 'https://shortznewz.blogspot.com/2022/04/random-facts.html', 'https://shortznewz.blogspot.com/2022/04/interesting-facts.html']
url = random.choice(url_list)

'''option = Options()

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", { 
    "profile.default_content_setting_values.notifications": 1 
})

driver = webdriver.Chrome(chrome_options=option)'''
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 1}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(t)
driver.get(url)
driver.maximize_window()
time.sleep(10)

actionChains = ActionChains(driver)
button_xpath  = '//*[@id="HTML5"]/div[1]/button' 
button = driver.find_element_by_xpath(button_xpath)
driver.execute_script("arguments[0].click();", button)
time.sleep(w)
driver.switch_to.window(driver.window_handles[0])
time.sleep(t1)
