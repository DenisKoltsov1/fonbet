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

kcal = driver.find_elements(By.XPATH,'//div[@class="event__participant event__participant--home"]')
time.sleep (5)

element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler'))).click()
live = driver.find_element(By.XPATH,'//div[@class="filters__group"]/div[@class="filters__tab"]/div[contains(text(),"LIVE")]') 
live.click()  
#teamHome=driver.find_element(By.XPATH,'//span[@class="event__expanderBlock"]')                                                                                                                     #нажатие на элемент Live
#teamHome.click()
HomeMatch= driver.find_element(By.XPATH,'//div[@title="Подробности матча!"]')                                                               #нажатие на игру для открытия игры
newPage=HomeMatch.click()
#newPages= driver.find_element(By.XPATH,'//body') 
#print(newPages.text)

handles = driver.window_handles
driver.switch_to.window(handles[-1])
time.sleep (5)
sostavLink = driver.find_element(By.XPATH, '//a[.="Составы"]').click()
time.sleep(3)
sostavPage = driver.find_elements(By.XPATH, "//div[contains(text(), 'Стартовые составы')]/following-sibling::div[@class='lf__sidesBox']//a[@class='lf__participantName']/child::div")
 
for player in sostavPage:
    print(player.text)
 
#driver.quit()
 
#print(sostavPage.text)

