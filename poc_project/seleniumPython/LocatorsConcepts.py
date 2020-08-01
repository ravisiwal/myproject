from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver_path = '/home/ravindra/poc_project/configs/browsers/chromedriver.exe'

driver = webdriver.Chrome(executable_path=driver_path)

driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
print(driver.title)

firstname =  driver.find_element_by_name('FirstName')
firstname.send_keys('testtduser')

feature_link = driver.find_element(By.LINK_TEXT, "Features")
feature_link.click()
driver.implicitly_wait(3)
time.sleep(4)
driver.quit()

#======================================
#RightClick Action chain