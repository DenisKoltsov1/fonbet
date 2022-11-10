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
live = driver.find_element(By.XPATH,'//*[@id="live-table"]/div[1]/div/div[2]')                                                     #нахождение элемента Live
live.click()                                                                                                                       #нажатие на элемент Live
teamHome = driver.find_element(By.XPATH,'//*[@id="g_1_C4mFUMeR"]')                                                                 #нажатие на игру для открытия игры
newPage=teamHome.click()

handles = driver.window_handles                                                                                                    #открытие нового окна браузера с игрой
size = len(handles)

for x in range(size):                                                                                                              #переход на новое окно
  driver.switch_to.window(handles[x])
  print(driver.title)

sostavLink=driver.find_element(By.XPATH,'//*[@id="detail"]/div[7]/div/a[3]')                                                        #безуспешная попытка нажать на вкладку "Составы"
#sostavLink=sostavLink.get_attribute('textContent')
#driver.find_element(By.LINK_TEXT,sostavLink).click()
sostavLink.click()
print(sostavLink.text)
'''
size1 = len(sostavLink)
for b in  range(size1):
    print(sostavLink[b].text)
'''   
#sostavTeam=driver.find_elements(By.XPATH,'//*[@id="detail"]/div[8]/div[1]/div[2]/div/div[1]/div[1]/a') 
sostavPage = driver.find_element(By.TAG_NAME,'body') 
#for x in sostavTeam:
#    print(x.text) 
print(sostavPage.text)



