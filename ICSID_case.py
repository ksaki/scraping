##################################################
## Project:WTO ICISD scraping
## Script purpose: scrape ICSID case lists
## Date:2018/02/27
## Author: Saki Kuzushima
## Version:1
##################################################
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import pandas as pd
import csv
import numpy as np
import chardet


#Phantom JS is no longer availabe. Use headless Chrome. 
options = Options()
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
options.add_argument('--headless')

#access to case list page
driver = webdriver.Chrome(executable_path = "/Users/sakikuzushima/Documents/programming/python/chromedriver", chrome_options = options)
driver.set_window_size(1440, 900)
driver.get("https://icsid.worldbank.org/en/Pages/cases/AdvancedSearch.aspx")

time.sleep(5)

#choose all from dropdown
s1 = webdriver.support.select.Select(driver.find_element_by_class_name("CVpagecount"))
s1.select_by_value("All")

casenos = driver.find_elements_by_class_name("casecol1")
url_base = "https://icsid.worldbank.org/en/Pages/cases/casedetail.aspx?CaseNo="


case_keys = ["Subject of Dispute:",
			 'Economic Sector:',
			 'Instrument(s) Invoked: i',
			 'Claimant(s)/Nationality(ies): i',
			 'Respondent(s):',
			 'Date Registered:',
			 'Status of Proceeding:',
			 'Latest Development:', 
			 'Outcome of Proceeding:']

url_ls = []
case_dict_ls = []
for caseno in casenos[1:]:
	caseno_tx = caseno.text

	url_ls.append(url_base+caseno_tx)


loop = 1

for url in url_ls:

	print(loop)
	
	#access each case page 
	driver.get(url)
	time.sleep(5)

	case1_we = driver.find_element_by_class_name("proceedingcaselist1")
	case2_we = driver.find_element_by_class_name("proceedingcaselist2")

	case1 = case1_we.text
	case2 = case2_we.text
	cases = case1 + case2
	case_ls = cases.split("\n")
	# print(case_ls)

	#get key and value
	case_pairs =[]
	for case_key in case_keys:

		try:
			case_index = case_ls.index(str(case_key)) + 1 #value is normally  next element to its key
			case_val = case_ls[int(case_index)]
			case_pairs.append((case_key, case_val))

		except ValueError:
			case_pairs.append((case_key, ""))

	case_dict = dict(case_pairs)
	case_dict_ls.append(case_dict)

	loop = loop + 1


	case_df = pd.DataFrame(case_dict_ls) #index = list(range(0,685))

	case_df.to_csv("ICSID_case.csv")



	


