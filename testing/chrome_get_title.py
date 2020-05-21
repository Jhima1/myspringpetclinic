#!/usr/bin/env python3

from selenium.webdriver import Chrome import urllib3
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.headless = True

driver = Chrome(options=opts, executable_path='./testing/chromedriver')

try:
    driver.get('http://localhost:8083')

    assert 'PetClinic :: a Spring Framework demonstration' == driver.title

finally:

    driver.quit()
