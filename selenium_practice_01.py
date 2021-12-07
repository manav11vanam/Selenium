from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
PATH = 'C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)
# driver.get('https://techwithtim.net')
driver.get('https://coreyms.com/')

print(driver.title)
try:
    search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 's')))

    search.send_keys('django')
    search.send_keys(Keys.RETURN)
except Exception:
    print('Problem')
sleep(15)
driver.quit()
