import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from LogicBuilding import Transformation

def Initialize():
    try:
        # Create ChromeOptions instance
        options = webdriver.ChromeOptions()

        # Adding argument to disable the AutomationControlled flag
        options.add_argument("--disable-blink-features=AutomationControlled")

        # Exclude the collection of enable-automation switches
        options.add_experimental_option("excludeSwitches", ["enable-automation"])

        # Specify the path to the ChromeDriver executable
        chrome_driver_path = "D:\Cricket-Analysis\chromedriver-win64\chromedriver.exe"

        # Create a Service instance using the executable_path

        service = Service(executable_path=chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=options)
            # Changing the property of the navigator value for webdriver to undefined
        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        return driver
    except Exception as e:
        print(e)

def NavigateToUrl(driver,player):
    try:
        driver.get(f"https://search.espncricinfo.com/ci/content/site/search.html?search={player};type=player")
    except Exception as e:
        print(e)

def click(driver,path):
    try:
        name = driver.find_element(By.XPATH,path)
        name.click()
        print("Clicked")
    except Exception as e:
        print(e)
    

def UrlExtenstion(driver):
    print("Extending URL")
    curUrl=driver.current_url
    driver.get(curUrl+"/bowling-batting-stats")
    time.sleep(17)
    print("Executed...")
    
    

def getTblTxt(driver,path):
    print("----------------------Getting  table text---------------------------------------------")
    try:
        table=driver.find_element(By.XPATH,path)
        print(Transformation(table.text))
    except Exception as e:
        print(e)