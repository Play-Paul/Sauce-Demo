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
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[2]/div/div[2]/div/div[3]/div[3]/button").click()

#Go to CART
driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link fa-layers fa-fw'] svg path").click()
time.sleep(3)

#CHECKOUT and LOGOUT
driver.find_element(By.XPATH, "/html/body/div/div[2]/div[3]/div/div[2]/a[2]")
driver.find_element(By.XPATH, "//*[@id='menu_button_container']/div/div[3]/div/button").click()
time.sleep(2)
driver.find_element(By.XPATH, "//*[@id='logout_sidebar_link']").click()