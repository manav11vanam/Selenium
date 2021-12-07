from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import csv
# NoSuchElementException:
# selenium.common.exceptions.NoSuchElementException
f = open('data.csv', 'a', newline='')
writer = csv.writer(f)
# MH12AA0001 ['IMRAN AHMED', 'Fourth Owner', 'MH12AA0001', 'MARUTI SUZUKI INDIA LTD, MARUTI 800', 'Motor Car(LMV)', '4XXXXX', '3XXXXX', 'PETROL']
# writer.writerow(['Owner', 'Owner Level', 'Reg No', 'Model', 'LMV etc', 'Eng No', 'Chs No', 'Fuel Type'])
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

def click_no():
    global click_flag
    try:
        no = driver.find_element_by_id('com.cuvora.carinfo:id/tv_no')
        if no.is_displayed():
            no.click()
            click_flag = 0
    except NoSuchElementException:
        pass

click_flag = 1
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
driver.implicitly_wait(12)
# driver.back()
# sleep(2)
# driver.back()
data_dict = {}
reg_nos = []
for i in range(51,151):
    reg_nos.append('MH12AA'+str(i).zfill(4))

driver.find_element_by_id('com.cuvora.carinfo:id/feature1_layout').click()
# reg_nos = ['MH12HN6793', 'MH12SU6483', 'MH12KE9005', 'MH12AA1111']
touch = TouchAction(driver)

for reg_no in reg_nos:
    search = driver.find_element_by_id('com.cuvora.carinfo:id/et_vehicle_number')
    search.send_keys(reg_no)
    driver.find_element_by_id('com.cuvora.carinfo:id/tv_search').click()
    # sleep(2)
    # try:
    #     driver.find_element_by_accessibility_id('Report Ad')
    #     driver.back()
    # except NoSuchElementException:
    #     pass
    if click_flag:
        click_no()
    all_props = []
    li = driver.find_elements_by_id('com.cuvora.carinfo:id/value')
    if li == []: # Just for a wait
        print(reg_no, 'Does Not Exist')
        driver.back()
        continue
    touch.press(x=468,y=1355).move_to(x=468,y=407).release().perform()
    if click_flag:
        click_no()
    li = driver.find_elements_by_id('com.cuvora.carinfo:id/value')
    contents = [item.get_attribute('text') for item in li]
    all_props.extend(contents)
    try:
        touch.press(x=424,y=1430).move_to(x=424,y=450).release().perform()
    except StaleElementReferenceException:
        click_no()
        touch.press(x=424,y=1430).move_to(x=424,y=450).release().perform()
    li = driver.find_elements_by_id('com.cuvora.carinfo:id/value')
    contents = [item.get_attribute('text') for item in li]
    all_props.extend(contents)
    touch.press(x=424,y=1430).move_to(x=424,y=450).release().perform()
    li = driver.find_elements_by_id('com.cuvora.carinfo:id/value')
    contents = [item.get_attribute('text') for item in li]
    all_props.extend(contents)
    # print("dup all_props", all_props)
    all_props = rem_dup(all_props)
    print(reg_no, all_props)
    # all_props.insert(0, reg_no)
    writer.writerow(all_props)
    driver.back()
f.close()
'''
dup all_props ['MH12HN6793', 'MARUTI SUZUKI INDIA LTD, MARUTI SWIFT DZIRE VXI BSIV', 'Motor Car(LMV)', 'K12MN11XXXXX', 'MA3EJKD1S001XXXXX', 'PETROL', 'MH12HN6793', 'MARUTI SUZUKI INDIA LTD, MARUTI SWIFT DZIRE VXI BSIV', 'Motor Car(LMV)', 'K12MN11XXXXX', 'MA3EJKD1S001XXXXX', 'PETROL']

non-dup all_props ['MH12HN6793', 'MARUTI SUZUKI INDIA LTD, MARUTI SWIFT DZIRE VXI BSIV', 'Motor Car(LMV)', 'K12MN11XXXXX', 'MA3EJKD1S001XXXXX', 'PETROL']
'''
