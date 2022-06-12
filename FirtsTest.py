from appium import webdriver
from selenium.webdriver.common.by import By

desired_cap = {
  "appium:deviceName": "R3CM906NL0V",
  "platformName": "Android",
  "appium:app": "D:\\util\\AirMirror Remote control_v1.1.2.2.apk"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.implicitly_wait(30)

driver.find_element(By.ID, 'com.sand.airmirror:id/tvLogin').click()

search_element = driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.widget.LinearLayout/android.widget.RelativeLayout/androidx.viewpager.widget.ViewPager/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]/android.widget.LinearLayout/android.widget.AutoCompleteTextView')
search_element.set_text('yib95us@gmail.com')