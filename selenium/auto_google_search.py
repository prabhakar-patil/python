from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time # to provide delay if required


driver = webdriver.Chrome()	# open Chrome browser 
driver.get('https://www.google.com')	# provide url: google 

# time.sleep(1)	# hang around 1 sec to load page, if required. Not elegant way to do this

# search this by pressing 'ctrl + shift + i' or 'rt-click + inspect'
# there are many find methods. read appropriate documents
h_search_box = driver.find_element_by_name('q')	# get search field handle for 'name' element,
h_search_box.send_keys('selenium python package') # send search text 
h_search_box.send_keys(Keys.RETURN)	# just like hitting enter on editbox

# driver.quit()	# close chrome driver(browser)
