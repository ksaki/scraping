#ICSID_url
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


#Phantom JS is no longer availabe. Use headless Chrome. 
options = Options()
options.binary_location = '/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary'
options.add_argument('--headless')

#access to case list page
driver = webdriver.Chrome(executable_path = "/Users/sakikuzushima/Documents/python/chromedriver", chrome_options = options)
driver.get("https://icsid.worldbank.org/en/Pages/cases/AdvancedSearch.aspx")

time.sleep(1)

casenos = driver.find_elements_by_class_name("casecol1")
for caseno in casenos[1:]:
	caseno_tx = caseno.text
	print(caseno_tx)

