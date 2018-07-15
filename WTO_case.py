#scraping wto cases

#WARNING: under development!

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import csv
import numpy as np
import chardet
import re


#Phantom JS is no longer availabe. Use headless Chrome. 
options = Options()
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
options.add_argument('--headless')

#access to case list page
driver = webdriver.Chrome(executable_path = "/Users/sakikuzushima/Documents/programming/python/chromedriver", chrome_options = options)
driver.get("https://www.wto.org/english/tratop_e/dispu_e/dispu_status_e.htm")

#get case links
case_links = []
for a in driver.find_elements_by_xpath("//a"):
    temp = a.get_attribute('href')
    if temp != None:
        if '/english/tratop_e/dispu_e/cases_e' in temp:
            case_links.append(temp)


for case_link in case_links:
    driver.get(case_link)
    
    #get current status
    status_we = driver.find_element_by_xpath("//span[@class='paraboldcolourtext']")
    status = status.text
    print(status)
    
    time.sleep(3)

