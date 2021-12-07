from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
# driver.get('https://coreyms.com/')
driver.get('https://techwithtim.net')
print(driver.title)
try:
    link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Python Programming')))
    link.click()

    link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, 'Tic Tac Toe Tutorial')))

    link.click()

    sleep(4)
    driver.back()
except Exception:
    print('Problem')

sleep(10)
driver.quit()
