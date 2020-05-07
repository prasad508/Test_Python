import time
from selenium import webdriver

browser = webdriver.Chrome(executable_path = 'Framwork/chromedriver.exe')

browser.get('https://www.google.com') 
time.sleep(10)
browser.quit()