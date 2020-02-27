from selenium import webdriver
from selenium.webdriver.chrome.options import Options
option=Options()
option.add_argument("--headless")
option.add_argument("--no-sandbox")
option.add_argument("start-maximized")
option.add_argument("disable-infobars")
option.add_argument('--disable-extensions')
option.add_argument('--disable-dev-shm-usage')
driver=webdriver.Chrome('',chrome_options=option)
driver.implicitly_wait(5)
driver.get('http://localhost:8080/')
driver.maximize_window()
print(driver.title)
assert driver.title=='PetClinic :: a Spring Framework demonstration','Title not matched'
print("Login Test successfull")
driver.close()
driver.quit()
