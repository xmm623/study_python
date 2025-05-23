from appium import webdriver
caps = {
    "platformName": "Android",
    "automationName": "uiautomator2",
    "deviceName": "emulator-5554",
    "app": "/path/to/app.apk"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.quit()
