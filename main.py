from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


driver = webdriver.Chrome(service=Service(executable_path="c:/Users/User/Downloads/chromedriver-win64/chromedriver.exe"))
print("TC2: Вход с валидными учетными данными")

try:
    driver.get("https://idemo.bspb.ru/")
    username = driver.find_element(By.XPATH, "//input[@name='username']")
    username.clear()
    username.send_keys("demo")
    password = driver.find_element(By.XPATH, "//input[@name='password']")
    password.clear()
    password.send_keys("demo")
    driver.find_element(By.ID, "login-button").click()
    driver.find_element(By.ID, "login-otp-button").click()

    if driver.find_element(By.ID, "bank-overview"): print("\033[92m{}\033[0m".format("Test PASS"))
    driver.save_screenshot("srcshot_TC1.png")
except:
    driver.save_screenshot("eror_tc1.png")
    print("\033[31m{}\033[0m".format("Test FAIL"))


driver.quit()