import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# driver = webdriver.Chrome(executable_path = "/Users/naruaponsuwanwijit/Desktop/chromedriver")
# driver = webdriver.Edge('C:\driver\msedgedriver.exe')
s = Service('C:\driver\msedgedriver.exe')
driver = webdriver.Edge(service=s)
driver.get("http://www.google.com/")
time.sleep(2)
driver.close()