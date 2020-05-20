from selenium import webdriver
from selenium.webdriver.chrome.options import Options
option=Options()
option.add_argument("--headless")
option.add_argument("--no-sandbox")
option.add_argument("start-maximized")
option.add_argument("disable-infobars")
option.add_argument('--disable-extensions')
option.add_argument('--disable-dev-shm-usage')

def initial_check():
    global driver
    driver=webdriver.Chrome("./testing/chromedriver", options=option)
    #driver=webdriver.Chrome("/home/devops/Capstone/testing/chromedriver.exe", options=option)
    #driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver.exe")
    driver.implicitly_wait(15)                         
    driver.get('http://192.168.56.120:8083')
    #driver.implicitly_wait(10) 
    driver.maximize_window()
    print(driver.title)
    
def title_check():
    #assert (driver.title=='PetClinic :: a Spring Framework demonstration'), 'Title not matched'
    #driver.implicitly_wait(10)
    assert (driver.title == 'PetClinic :: a Spring Framework demonstration'), 'title not matched'
    driver.close()
    #print("Login Test successfull")
    #driver.close()
    #driver.quit()
