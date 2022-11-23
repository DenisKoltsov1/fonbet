from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Initialize Chrome WebDriver
driver = webdriver.Chrome(executable_path="C:\\fonbet\\chromedriver.exe")

chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument("--disable-extensions")

html=driver.get("https://www.flashscorekz.com")
time.sleep(50)
kcal = driver.find_elements(By.XPATH,'//div[@class="event__participant event__participant--home"]')
time.sleep (5)

element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler'))).click()
#live = driver.find_element(By.XPATH,'//div[@class="filters__group"]/div[@class="filters__tab"]/div[contains(text(),"LIVE")]') 
#live.click() 
HomeTeame= driver.find_element(By.XPATH,'//div[@class="event__participant event__participant--home"]')
print(HomeTeame.text)
AwayTeame= driver.find_element(By.XPATH,'//div[@class="event__participant event__participant--away"]')
print(AwayTeame.text)
#HomeMatch= driver.find_element(By.XPATH,'//div[@title="Подробности матча!"]')  
HomeMatch= driver.find_element(By.XPATH,'//*[@id="g_1_ARmio3Rl"]')                                                             #нажатие на игру для открытия игры
newPage=HomeMatch.click()

handles = driver.window_handles
driver.switch_to.window(handles[-1])
time.sleep (5)
#sostavLink = driver.find_element(By.XPATH, '//a[.="Составы"]').click()
time.sleep(3)
#sostavPage = driver.find_elements(By.XPATH, "//div[contains(text(), 'Стартовые составы')]/following-sibling::div[@class='lf__sidesBox']//a[@class='lf__participantName']/child::div")
 
#for player in sostavPage:
    #print(player.text)
 
HistoryGame = driver.find_element(By.XPATH, '//div[@class="tabs__group"]/a[3]')
time.sleep(5)
HistoryGame.click()


time.sleep(5)
ListStitistic = driver.find_element(By.XPATH, '//div[@class="rows"]')

print(ListStitistic.text)
driver.close()
driver.quit()