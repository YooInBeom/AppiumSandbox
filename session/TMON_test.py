import time

from appium import webdriver
from selenium.webdriver.common.by import By

desired_cap = {
    "appium:deviceName": "Android Emulator",
    "platformName": "Android",
    "appium:app": "D:/util/ticketmonster_v5.7.5.apk",
    "appPackage": "com.tmon",
    "appWaitActivity": "com.tmon.main.MainActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

"""Permission Deny"""
driver.find_element(By.ID, "com.tmon:id/btn_do_not_receive").click()
driver.find_element(By.ID, "com.tmon:id/slimNavibarClose").click()
driver.find_element(By.ID, "com.tmon:id/btn_confirm").click()
driver.find_element(By.ID, "com.android.permissioncontroller:id/permission_deny_button").click()
driver.find_element(By.ID, "com.tmon:id/btn_cancel").click()

"""search"""
driver.find_element(By.ID, "com.tmon:id/keyword").click()
driver.find_element(By.XPATH, "//android.widget.EditText[@resource-id='search_input']").click()
driver.find_element(By.XPATH, "//android.widget.EditText[@resource-id='search_input']").set_value("iphone")
driver.find_element(By.XPATH, "//android.widget.Button[@text='검색']").click()

ts = time.strftime("%Y_%m_%d_%H%M%S")
activityname = driver.current_activity
filename = activityname+ts
time.sleep(3)
driver.save_screenshot("C:/Users/inbeom/PycharmProjects/AppiumSandbox/Screenshots/"+filename+".png")
