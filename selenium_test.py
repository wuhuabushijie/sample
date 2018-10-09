from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(executable_path="chromedriver.exe")
browser.get("http://www.taobao.com/")
time.sleep(1)
kw = browser.find_element_by_id("q")
kw.send_keys("python")
time.sleep(1)
kw.send_keys(Keys.RETURN)