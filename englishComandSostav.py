from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sostavPage= []
Age=[]
TotalGameMatch=[]
driver = webdriver.Chrome(executable_path="C:\\fonbet\\chromedriver.exe")

def parser(sostavPages,Age,TotalGameMatch,driver):
    

    chrome_options = Options()
    chrome_options.headless = True
    chrome_options.add_argument("--disable-extensions")

    html=driver.get("https://www.flashscorekz.com")
    time.sleep(5)
    kcal = driver.find_element(By.XPATH,'//a[@class="leftMenu__href"]')
    time.sleep (5)
    kcal.click()
    time.sleep (5)
   
    element = WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.ID, 'onetrust-accept-btn-handler'))).click()
    time.sleep (5)
    comand = driver.find_element(By.XPATH,'//a[@class="tableCellParticipant__name"]')
    comand.click()
    sostavLink = driver.find_element(By.XPATH, '//a[.="Состав"]').click()
    time.sleep(3)
    '''
    #Amplua = driver.find_elements(By.XPATH, '//div[@class="lineup__title"]')
    sostavPage = driver.find_elements(By.XPATH, '//a[@class="lineup__cell lineup__cell--name"]')
    #for amp in Amplua:
    #    print(amp.text)
    for player in sostavPage:
            
        print(player.text)

    
    Age = driver.find_elements(By.XPATH, '//div[@class="lineup__cell lineup__cell--age"]')
    for age in Age:
        #if  age.isdigit():
        print(age.text)

    TotalGameMatch = driver.find_elements(By.XPATH, '//div[@class="lineup__cell lineup__cell--matchesPlayed"]')
    for total in TotalGameMatch:
        #if  age.isdigit():
        print(total.text)   
    '''
    Amplua = driver.find_elements(By.XPATH, '//div[@class="lineup__title"]')
    i=0
  
    while len(Amplua) <5:
        print(len(Amplua))
        for amp in Amplua:
            print(amp.text)
            while    amp.text !='Защитники' :
                print(amp.text)
                sostavPage = driver.find_elements(By.XPATH, '//div[.="Вратари"]//a[@class="lineup__row"]')
                i=i+1
                
                print(len(sostavPage))
    '''
    sostavPage = driver.find_element(By.XPATH, '//div[@class="lineup__rows"]//a[@class="lineup__cell lineup__cell--name"]')
    print(sostavPage.text)
    return [sostavPage,Age,TotalGameMatch]
    '''

parser(sostavPage,Age,TotalGameMatch,driver)
#print(sostavPage.count())
#for player in sostavPages:
#    print(player.text)
returnSostavPage=sostavPage
returnAge=Age
returnTotal=TotalGameMatch
#driver.close()
#driver.quit()