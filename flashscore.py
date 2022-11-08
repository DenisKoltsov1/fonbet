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
from selenium.webdriver.common.action_chains import ActionChains

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

element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler'))).click()
live = driver.find_element(By.XPATH,'//*[@id="live-table"]/div[1]/div/div[2]')
live.click()
teamHome = driver.find_element(By.XPATH,'//*[@id="g_1_niwjpG14"]') 
newPage=teamHome.click()
action=ActionChains(driver)
action.key_down(Keys.ALT).send_keys(Keys.TAB).send_keys(Keys.TAB)
sostavPage = driver.find_element(By.TAG_NAME,'body')  
print(sostavPage.text)



