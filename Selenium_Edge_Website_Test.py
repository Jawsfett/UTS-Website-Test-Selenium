
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.wait import WebDriverWait
import os
from selenium import webdriver



s = Service('/usr/local/bin/msedgedriver')
options = webdriver.EdgeOptions()
options = Options()
options.add_argument("--headless")
options.add_argument("--private")
options.add_argument("--window-size=1920,1080")



driver = webdriver.Edge(service=s, options=options)

driver.get('https://www.uts.edu.au/')

try:
    driver.find_element(By.XPATH, "/html/body/div[1]/header/div[4]/nav/ul/li[1]/span").click()
    driver.find_element(By.XPATH, '//*[@id="edit-search"]').click()
    driver.find_element(By.XPATH, '//*[@id="edit-search"]').send_keys('Bachelor of Information Technology')
    driver.find_element(By.XPATH, '//*[@id="edit-submit-course-search"]').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[1]/a').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div[2]/section[1]/div/div/div/div/div/main/div[3]/div/div/div/section[1]/div/section[1]/h4').click()
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div[2]/section[1]/div/div/div/div/div/main/div[3]/div/div/div/section[1]/div/section[1]/div/table[1]/tbody/tr[4]/td[1]/a').click()
    driver.find_element(By.XPATH, '//*[@id="input-text"]').click()
    driver.find_element(By.XPATH, '//*[@id="input-text"]').send_keys('I hate NetFund')
    driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/form/div/input[4]').click()
    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/a/img').click()

finally:
    driver.quit()