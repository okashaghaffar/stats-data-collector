from commanSteps import Initialize,NavigateToUrl,click,getTblTxt,UrlExtenstion
from selenium.webdriver.common.by import By
import time

def ExtractFormat(driver,format):
    
    try:
        print(f"------Printing for the format {format}----------")
        text=driver.find_elements(By.CLASS_NAME,"ds-grow")
        for i in text:
            if i.text==format:
                i.click()
        time.sleep(2)
        getTblTxt(driver,"/html/body/div[1]/section/section/div[5]/div[1]/div[2]/div[2]/div[2]/div/div[2]")
        getTblTxt(driver,"/html/body/div[1]/section/section/div[5]/div[1]/div[2]/div[2]/div[2]/div/div[3]")
        getTblTxt(driver,"/html/body/div[1]/section/section/div[5]/div[1]/div[2]/div[2]/div[2]/div/div[4]")
        getTblTxt(driver,"/html/body/div[1]/section/section/div[5]/div[1]/div[2]/div[2]/div[2]/div/div[5]")
        getTblTxt(driver,"/html/body/div[1]/section/section/div[5]/div[1]/div[2]/div[2]/div[2]/div/div[6]")
        getTblTxt(driver,"/html/body/div[1]/section/section/div[5]/div[1]/div[2]/div[2]/div[2]/div/div[7]")
        time.sleep(1)
    except Exception as e:
        print(e)
def dropdownclick(driver,xpath):
    click(driver,xpath)


def CallFormat(driver,path,format):
    dropdownclick(driver,path)
    ExtractFormat(driver,format)

    



if __name__=="__main__":
    
    
    count = 1
    driver=Initialize()
    NavigateToUrl(driver,"Chris Gayle")
    click(driver,"//*[@id='viewport']/div[5]/div[2]/main/div/div[4]/ul/li/h3/a")
    UrlExtenstion(driver)
    click(driver,"/html/body/div[2]/div[2]/div[3]/button[1]")
    #TESTS
    CallFormat(driver,"/html/body/div[1]/section/section/div[5]/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/i","Tests")
    #ODIs
    CallFormat(driver,"/html/body/div[1]/section/section/div[5]/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/i","ODIs")
    #T20IS
    CallFormat(driver,"/html/body/div[1]/section/section/div[5]/div[1]/div[2]/div[2]/div[2]/div/div[1]/div[2]/div[1]/div/div/i","T20Is")
   
   
  


