from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from selenium.common.exceptions import NoSuchElementException
# NoSuchElementException:
# selenium.common.exceptions.NoSuchElementException

desired_cap = {
  "platformName": "Android",
  "deviceName": "52039bba5aecc343",
  "appPackage": "com.cuvora.carinfo",
  "appWaitActivity": "com.cuvora.carinfo.activity.HomePageActivity",
  "app": "C:\\Android\\com.cuvora.carinfo-5.5.4-free-www.apksum.com.apk"
}
def rem_dup(li):
    updated = []
    for i in li:
        if i in updated:
            continue
        updated.append(i)
    return updated


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
driver.implicitly_wait(10)
driver.back()
sleep(1)
driver.back()
driver.find_element_by_id('com.cuvora.carinfo:id/feature1_layout').click()
search = driver.find_element_by_id('com.cuvora.carinfo:id/et_vehicle_number')
search.send_keys('MH12HN6793')
driver.find_element_by_id('com.cuvora.carinfo:id/tv_search').click()
# sleep(2)
try:
    driver.find_element_by_accessibility_id('Report Ad')
    driver.back()
except NoSuchElementException:
    pass

try:
    no = driver.find_element_by_id('com.cuvora.carinfo:id/tv_no')
    if no.is_displayed():
        no.click()
except NoSuchElementException:
    pass

all_props = []
touch = TouchAction(driver)
touch.press(x=5, y=1400).move_to(x=5, y=100).release().perform()
touch.press(x=10,y=1800).move_to(x=15,y=611).release().perform()
li = driver.find_elements_by_id('com.cuvora.carinfo:id/value')
contents = [item.get_attribute('text') for item in li]
all_props.extend(contents)
touch.press(x=10,y=1800).move_to(x=15,y=611).release().perform()
li = driver.find_elements_by_id('com.cuvora.carinfo:id/value')
contents = [item.get_attribute('text') for item in li]
all_props.extend(contents)
print("dup all_props", all_props)
all_props = rem_dup(all_props)
print("non-dup all_props", all_props)


'''
dup all_props ['MH12HN6793', 'MARUTI SUZUKI INDIA LTD, MARUTI SWIFT DZIRE VXI BSIV', 'Motor Car(LMV)', 'K12MN11XXXXX', 'MA3EJKD1S001XXXXX', 'PETROL', 'MH12HN6793', 'MARUTI SUZUKI INDIA LTD, MARUTI SWIFT DZIRE VXI BSIV', 'Motor Car(LMV)', 'K12MN11XXXXX', 'MA3EJKD1S001XXXXX', 'PETROL']

non-dup all_props ['MH12HN6793', 'MARUTI SUZUKI INDIA LTD, MARUTI SWIFT DZIRE VXI BSIV', 'Motor Car(LMV)', 'K12MN11XXXXX', 'MA3EJKD1S001XXXXX', 'PETROL']
'''
