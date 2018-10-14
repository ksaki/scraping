##################################################
## Project: WTO ICSID scraping
## Script purpose: scraping ICSID pending cases
## Date: 2018/02/27
## Author: Saki Kuzushima
## Version: 1
##################################################

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import csv
import numpy as np
import chardet


# Use headless Chrome. 
options = Options()
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
options.add_argument('--headless')

# access to case list page
driver = webdriver.Chrome(executable_path = "/Users/sakikuzushima/Documents/programming/python/chromedriver", chrome_options = options)
driver.set_window_size(1440, 900)
driver.get("http://investmentpolicyhub.unctad.org/IIA/IiasByCountry#iiaInnerMenu")

print("waiting for 5 seconds...")
time.sleep(5)

# get country url
base_url = "http://investmentpolicyhub.unctad.org/IIA/"

country_urls = []
for i in range(1,235):
	country_urls.append(base_url+"CountryBits/%s#iiaInnerMenu" %(i))

for country_url in country_urls[1:5]:

	print(country_url)

	# extract information
	driver.get(country_url)

	# country A
	ca = driver.find_element_by_tag_name('h2').text

	# country B
	cb_ls = []
	cbs_we = driver.find_elements_by_css_selector("td[data-position='1']")
	for cb_we in cbs_we:
		cb_ls.append(cb_we.text)

	# status
	st_ls = []
	sts_we = driver.find_elements_by_css_selector("td[data-position='2']")
	for st_we in sts_we:
		st_ls.append(st_we.text)

	# sign
	sg_ls = []
	sgs_we = driver.find_elements_by_css_selector("td[data-position='3']")
	for sg_we in sgs_we:
		sg_ls.append(sg_we.text)

	# force
	fo_ls = []
	fos_we = driver.find_elements_by_css_selector("td[data-position='4']")
	for fo_we in fos_we:
		fo_ls.append(fo_we.text)

	# put data into a dictionary
	data = {'country_a': ca, 
			'country_b': cb_ls,
			'status':st_ls,
			'sign':sg_ls,
			'force':fo_ls,
			}
	df = pd.DataFrame.from_dict(data) 

	if country_urls.index(country_url) == 1:
		df.to_csv("BIT.csv")
	else:
		df.to_csv("BIT.csv", mode = "a", header=False)


