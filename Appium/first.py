from appium import webdriver

desired_cap = {
  "platformName": "Android",
  "deviceName": "Android Emulator",
  "appPackage": "com.cuvora.carinfo",
  "appWaitActivity": "com.cuvora.carinfo.activity.HomePageActivity",
  "app": "C:\\Android\\com.cuvora.carinfo-5.5.4-free-www.apksum.com.apk"
}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap, )
