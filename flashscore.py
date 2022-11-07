from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# Initialize Chrome WebDriver
driver = webdriver.Chrome(executable_path="C:\\fonbet\\chromedriver.exe" )
chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=chrome_options)
html=driver.get("https://www.flashscorekz.com/");
stroka=str("g_1_8QmkYkDb")
kcal = driver.find_elements(By.XPATH,'//div[@class="event__participant event__participant--home"]')
time.sleep (5)
#teamHome = driver.find_element(By.XPATH,'//*[@id="g_1_KAOyH3RR"]/div[2]').click()
element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler'))).click()
teamHome = driver.find_element(By.XPATH,'//*[@id="g_1_KAOyH3RR"]/div[3]') 
newPage=teamHome.click()
#//*[@id="detail"]/div[9]/div[1]/div[3]/div
name = driver.find_element(By.XPATH,'///*[@id="detail"]/div[9]/div[1]/div[3]/div')
for elem in range(0,3):
    driver.find_element(By.TAG_NAME,'body').send_keys(
    Keys.CONTROL + "Tab")

#//*[@id="detail"]/div[7]/div/a[3]  
sostavPage = driver.find_element(By.XPATH,'//*[@id="g_1_KAOyH3RR"]/div[2]').click()   
#//*[@id="detail"]/div[9]/div[1]/div[2]/div/div[1]/div[1]/a
for elem in range(0,3):
    driver.find_element(By.TAG_NAME,'body').send_keys(
    Keys.CONTROL + "Tab")
sostav = driver.find_elements(By.CLASS_NAME,'lf__participantName')
for i in sostav:
    print(i.text)

print(teamHome.text)
print(name.text)


