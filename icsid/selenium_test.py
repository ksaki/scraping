#selenium practice

from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path = "/Users/sakikuzushima/Documents/python/chromedriver")
driver.get("https://icsid.worldbank.org/en/Pages/cases/AdvancedSearch.aspx")
time.sleep(5)

casecol1_ls = driver.find_elements_by_class_name("casecol1")
print(len(casecol1_ls))

for casecol1 in casecol1_ls:
	print(casecol1)
	j = 0

	if j == 0:
		pass
	else:
		time.sleep(3)
		casecol1.click()
		j = j + 1
		print("looping")

print("end")


#class casecol1 でcase noを検索をかける
