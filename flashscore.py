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
#email_form = driver.find_element_by_class_name("event__title--type")
stroka=str("g_1_8QmkYkDb")
divelem=driver.find_elements(By.TAG_NAME,'div')
individual_element = divelem[0000]
#individual_element_one=individual_element.find_elements(By.CLASS_NAME,'event__participant event__participant--home')
kcal = individual_element.find_element(By.CLASS_NAME,'event__participant event__participant--home')
print(kcal)
time.sleep(1)
#t=driver.getTitle("Премьер-лига")


