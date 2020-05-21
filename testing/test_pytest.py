#!/usr/bin/env python3

from selenium.webdriver import Chrome
import time
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.headless = True

driver = Chrome(options=opts, executable_path='./testing/chromedriver')

try:
    print("Attempt")
    time.sleep(5)
    driver.get('http://localhost:8083')
    print("PetClinic Successfully Launched")
    
finally:
    driver.quit()
