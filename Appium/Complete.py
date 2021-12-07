from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
import json
# NoSuchElementException:
# selenium.common.exceptions.NoSuchElementException
# f = open('data.csv', 'a', newline='')
# writer = csv.writer(f)
# MH12AA0001 ['IMRAN AHMED', 'Fourth Owner', 'MH12AA0001', 'MARUTI SUZUKI INDIA LTD, MARUTI 800', 'Motor Car(LMV)', '4XXXXX', '3XXXXX', 'PETROL']
# writer.writerow(['Owner', 'Owner Level', 'Reg No', 'Model', 'LMV etc', 'Eng No', 'Chs No', 'Fuel Type'])
def rem_dup(li):
    updated = []
    for i in li:
        if i in updated:
            continue
        updated.append(i)
    return updated

def click_no(driver):
    global click_flag
    try:
        no = driver.find_element_by_id('com.cuvora.carinfo:id/tv_no')
        if no.is_displayed():
            no.click()
            click_flag = 0
    except NoSuchElementException:
        pass

def scroll(driver, start_x, start_y, end_x, end_y):
    TouchAction(driver).press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()

def main(alphabets = 'HN', start = 1, stop = 10):
    # keys_to_remove = ['Financer\'s Name (HP)', 'Vehicle Age', 'Fitness Upto', 'Insurance Expiry (Tentative)', 'Insurance expiring in', 'Pollution Upto', 'Pollution expiring in', 'Color', 'RC Status', 'Name', 'Code', 'Engine Capacity (cc)', 'RTO Address', 'RTO Phone']

    requirements = ['Owner Name', 'Ownership (Serial No)', 'Registration No', 'Maker Model', 'Vehicle Class', 'Engine  No.', 'Chassis No.', 'Fuel Type', 'Fuel Norms', 'Registration Date', 'Unloaded Weight (Kg)']

    desired_cap = {
      "platformName": "Android",
      # "deviceName": "52039bba5aecc343",
      "deviceName": "33002f5cd112c4a9",
      "appPackage": "com.cuvora.carinfo",
      "appWaitActivity": "com.cuvora.carinfo.activity.HomePageActivity",
      "app": "C:\\Android\\com.cuvora.carinfo-5.5.4-free-www.apksum.com.apk"
    }
    global click_flag
    click_flag = 1
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    # NO THANKS AND CROSS
    driver.implicitly_wait(14)
    driver.find_element_by_xpath('//android.widget.Button[@text="NO THANKS"]')
    try:
        # driver.find_element_by_id('com.cuvora.carinfo:id/collapse_button').click() # Stupid Pop up ad
        driver.find_element_by_id('com.cuvora.carinfo:id/iv_cancel').click() # True caller login
    except NoSuchElementException:
        pass
    # reg_nos = []
    # for i in range(start, stop + 1):
    #     reg_nos.append('MH12' + alphabets + str(i).zfill(4))

    driver.find_element_by_id('com.cuvora.carinfo:id/feature1_layout').click() #Search by RC
    # reg_nos = ['MH12HN6793', 'MH12JU7137', 'MH12RF5509', 'MH12ML2037', 'MH12KE9005', 'MH12NU3148', 'MH12HZ3776', 'MH12HN6131', 'MH12KN9982', 'MH12JU9930', 'MH12JM956', 'MH14GN2807', 'MH12SY9791', 'MH12ML7110', 'MH12PH3827', 'MH12MR8328', 'MH12NP5113', 'MH12MB2412', 'MH12DY4148', 'MH14FX6330', 'MH12MB2684', 'MH12KY1124', 'MH12ML3876', 'MH12MW3058', 'MH12PC4051', 'MH12QF3979', 'MH12DM8923', 'MH12JC0989', 'MH12RT1183', 'MH12NE9308', 'MH12JZ8033', 'MH12KE2164', 'MH12MF1114', 'MH12PH3702', 'MH12CQ3000', 'MH12RT8443', 'JH01BF3108', 'MH12FU4493', 'MH12MF5401', 'MH20AG1684', 'MH04CD8195', 'MH12SE5991', 'MH12GV3505', 'MH12SU6483', 'MH12RF5509']
    # with open ('list1.txt') as f:
    #     reg_nos = f.readlines()[46:]
    # reg_nos = list(map(str.strip, reg_nos))
    reg_nos = ['RJ20CD3333', 'MH02CL7473', 'DL2FBL0400', 'DL3CBP8003', 'RJ27CC4351', 'DL10CD6116', 'GJ27AP3331', 'HR26CP6209', 'GJ18BE3161', 'MH14EY6587', 'DL12CK8604', 'GJ01RS7345', 'MH46AU8208', 'TN21BY0159', 'TN876403', 'DL3CAL4242', 'DL3CAQ9353', 'GJ01KL6432', 'UP16AF7175', 'DL2CAM5957', 'GJ02AP6689', 'AP31CA4899', 'DL10CD1533', 'DL10CK0294', 'MH48AW2749', 'RJ14WC1763', 'GJ01HU6464', 'MH12SS0070', 'TN87B6881', 'TN87B1015', 'TN87B1026', 'TN87B1039', 'TN87B7309', 'MH12SU1116', 'MH01AR4824', 'GJ05CN5717', 'TN06B2396', 'DL8CX8036', 'DL10CD4278', 'DL1CP2171', 'GJ01RG3071', 'GJ05JK1920', 'MH02DZ6636', 'PB03AM8899', 'DL8CAT1804', 'TS08FJ0639', 'DL7CR8542', 'DL3CBR3500', 'UP16AU3317', 'MH02DJ1966', 'WB02AF9899', 'DL7CL6816', 'DL12CE1617', 'DL8CAE4718', 'MH02DS3934', 'DL8CAF9703', 'MH03CP0979', 'MH47W1533', 'TN870911', 'MH10CA9695', 'DL7CM3464', 'DL12CG9696', 'DL12CG8376', 'WB02AH7752', 'KA03ND2290', 'DL8CAR4685', 'KA02MN2705', 'TN87A0119', 'MH02EU3341', 'MH12SU1198', 'MH12SU1137', 'MH12SS0021', 'MH12SU1100', 'KA04MW6334', 'MH12SU1140', 'UP16CQ4573', 'TN87B7747', 'MH12SU1123', 'MH12SU1152', 'DL10CN8636', 'TN87B4561', 'TN87B4578', 'TN87B4575', 'MH12SU1153']

    for reg_no in reg_nos:
        search = driver.find_element_by_id('com.cuvora.carinfo:id/et_vehicle_number')
        search.send_keys(reg_no)
        sleep(1)
        driver.find_element_by_id('com.cuvora.carinfo:id/tv_search').click()
        previous = []
        current = driver.find_elements_by_id('com.cuvora.carinfo:id/value')
        if current == []: # If number does not exist exit and return asap
            print(reg_no, 'Does Not Exist')
            driver.back()
            continue

        all_props = []
        all_keys = []

        for _ in range(7):
            if click_flag:
                click_no(driver)
                driver.implicitly_wait(8)

            # if click_flag:
            #     click_no(driver)

            keys = driver.find_elements_by_id('com.cuvora.carinfo:id/key')
            key_contents = [item.get_attribute('text') for item in keys]
            current = driver.find_elements_by_id('com.cuvora.carinfo:id/value')
            contents = [item.get_attribute('text') for item in current]
            if previous == contents:
                scroll(driver, 468, 1695, 477, 695)
                print("Value Repeat hori")
            previous = contents[:]
            if 'M-Cycle/Scooter(2WN)' in contents:
                break
            all_keys.extend(key_contents)
            all_props.extend(contents)
            scroll(driver, 468, 1595, 477, 560)

            # print('key_contents', key_contents)
            # print('contents', contents)
        all_keys = rem_dup(all_keys)
        all_props = rem_dup(all_props)
        if 'M-Cycle/Scooter(2WN)' in contents:
            driver.back()
            continue
        tmp_dict = dict(zip(all_keys, all_props))
        # final_dict['Registration No'] = reg_no
        final_dict = {}

        ''' '''
        for requirement in requirements:
            final_dict[requirement] = tmp_dict.get(requirement, 'Not Found')
        ''' '''

        print(reg_no, final_dict)
        print('\n*****************************************************************\n')
    # all_props.insert(0, reg_no)
    # writer.writerow(all_props)
        with open('data_for_emissions.txt', 'a') as f:
            f.write(json.dumps(final_dict) + '\n')
        driver.back()
# f.close()
    driver.quit()

if __name__ == '__main__':
    main(alphabets = 'SA', start = 600, stop = 625)
    # sleep(10)
    # main(alphabets = 'SU', start = 1164, stop = 1200)
