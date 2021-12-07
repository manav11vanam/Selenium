from selenium import webdriver
from time import sleep

url = 'http://coreyms.com/'
driver = webdriver.Chrome()
driver.get(url)

last_height = driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
print('Last Height:', last_height)

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    sleep(0.5)
    new_height = driver.execute_script('return document.body.scrollHeight;')
    print('New Height:', new_height)
    if new_height==last_height:
        break
    last_height = new_height

driver.quit()
