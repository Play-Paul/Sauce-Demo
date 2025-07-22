import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
time.sleep(3)
driver.maximize_window()

#Call provided url
driver.get("https://www.saucedemo.com/v1/index.html")
time.sleep(3)

#Proceed to login to sauce demo site
driver.find_element(By.XPATH, "(//input[@id='user-name'])[1]").send_keys("standard_user")
driver.find_element(By.XPATH, "(//input[@id='password'])[1]").send_keys("secret_sauce")
driver.find_element(By.XPATH, "(//input[@id='login-button'])[1]").click()

#Select products from list
driver.find_element(By.XPATH, "//div[@class='inventory_list']//div[1]//div[3]//button[1]").click()
driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(3) > button:nth-child(2)").click()
driver.find_element(By.XPATH, "//div[6]//div[3]//button[1]").click()
driver.find_element(By.CLASS_NAME, "btn_primary btn_inventory").click()
driver.find_element(By.XPATH, "(//*[name()='path'][@fill='currentColor'])[1]").click()