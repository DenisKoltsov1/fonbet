from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Initialize Chrome WebDriver
driver = webdriver.Chrome(executable_path="C:\\fonbet\\chromedriver.exe" )
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=chrome_options)
html=driver.get("https://www.flashscorekz.com/");
stroka=str("g_1_8QmkYkDb")
kcal = driver.find_elements(By.XPATH,'//div[@class="event__participant event__participant--home"]')
for x in  kcal:
    print(x.text)
time.sleep(1)



