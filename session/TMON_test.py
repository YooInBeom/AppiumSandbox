from appium import webdriver
from selenium.webdriver.common.by import By

desired_cap = {
    "appium:deviceName": "Android Emulator",
    "platformName": "Android",
    "appium:app": "/Users/yooinbeom/Downloads/apk/ticketmonster_v5.7.5.apk",
    "appPackage": "com.tmon",
    "appWaitActivity": "com.tmon.main.MainActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

driver.find_element(By.ID, 'com.tmon:id/keyword').click()
driver.find_element(By.ID, 'com.tmon:id/keyword').send_keys('iphone')



