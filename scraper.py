import os

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time 


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Scrapper:

    def __init__(self,exchange: str, ticker: str, page: str):
        
        self.__driver = None
        self.__ticker = ticker
        self.__page = page
        self.__exchange = exchange
        self.__path = f"https://www.morningstar.com/stocks/{exchange}/{ticker}/{page}"
        self.__data_export_path = f"{os.path.dirname(os.path.realpath(__file__))}/data/{self.exchange}-{self.ticker}"
        self.__create__driver()


    @property 
    def driver_is_set(self):
        return False if (self.__driver == None) else True

    @property
    def path(self):
        return self.__path

    @property
    def driver(self):
        return self.__driver
    
    @property
    def page(self):
        return self.__page

    @property
    def ticker(self):
        return self.__ticker

    @property
    def exchange(self):
        return self.__exchange

    @property
    def report_index(self):
        return self.__report_index

    @property
    def data_export_path(self):
        return self.__data_export_path

    def __str__(self) -> str:
        return self.path


    def __create__driver(self) -> bool:
        
        chrome_options = Options()                                   # setting of the driver
        chrome_options.add_experimental_option("detach", True)       # "True" to be keep browser 
              
        prefs = { "download.default_directory" : self.data_export_path } # Setting path to store the rdata
        chrome_options.add_experimental_option("prefs",prefs)

        service = Service(executable_path="chromedriver")                  # set chrome driver path
        driver = webdriver.Chrome(service=service, options=chrome_options) # Instantiation of Chrome driver
        driver.get(self.__path)
   
        try:
            assert "Page Not Found | Morningstar" not in driver.title
            self.__driver = driver
            return True
        
        except:
            return False
    


    def get_financial_reports(self) -> str:

        '''                                             
        /financials :
        Reports: 'balanceSheet', 'incomeStatement', 'cashFlow' 
        '''
        # Key ID:
        # balanceSheet
        # incomeStatement
        # cashFlow

        if self.driver_is_set :
            try:
                self.driver.find_element(By.ID, 'balanceSheet').click()       # Tricky Point here! pre-click some btn making sure the whole DOM is ready
                self.driver.find_element(By.CLASS_NAME, 'sal-component-footer-expand').click() 

                time.sleep(5)
                self.driver.find_element(By.XPATH,"//span[contains(text(), 'Export Data')]").click()
                time.sleep(5)

                self.driver.find_element(By.ID, 'incomeStatement').click()   

                time.sleep(5)
                self.driver.find_element(By.XPATH,"//span[contains(text(), 'Export Data')]").click()
                time.sleep(5)   

                self.driver.find_element(By.ID, 'cashFlow').click()   

                time.sleep(5)    
                self.driver.find_element(By.XPATH,"//span[contains(text(), 'Export Data')]").click()
          

                return f"Balance Sheet Report', 'Income Statement Report' and 'Cash Flow Report' were succefully downloaded"
            except:
                return f"Error:  Reports cannot be downloaded."

        else :

            return f'Error: Driver is not set'
            


  

    def get_valuation_reports(self):

        '''                                             
        /valuation :
        Reports: 'Growth', 'Operating', 'Financial Health', 'Cash Flow' 
        '''

        # ID :
        # keyStatsoverview
        # keyStatsgrowthTable
        # keyStatsOperatingAndEfficiency
        # keyStatsfinancialHealth
        # keyStatscashFlow


        if self.driver_is_set :
            try:
                self.driver.find_element(By.ID, 'keyStatsoverview').click() 
       
                self.driver.find_element(By.ID, 'keyStatsgrowthTable').click() 
                time.sleep(5)

                self.driver.find_element(By.XPATH,"//span[contains(text(), 'Export Data')]").click()
                time.sleep(5)

                self.driver.find_element(By.ID, 'keyStatsOperatingAndEfficiency').click()   
                time.sleep(5)
                
                self.driver.find_element(By.XPATH,"//span[contains(text(), 'Export Data')]").click()
                time.sleep(5)   

                self.driver.find_element(By.ID, 'keyStatsfinancialHealth').click()   
                time.sleep(5)    

                self.driver.find_element(By.XPATH,"//span[contains(text(), 'Export Data')]").click()
                time.sleep(5)  

                self.driver.find_element(By.ID, 'keyStatscashFlow').click()   
                time.sleep(5)    

                self.driver.find_element(By.XPATH,"//span[contains(text(), 'Export Data')]").click()

                return f"Balance Sheet Report', 'Income Statement Report' and 'Cash Flow Report' were succefully downloaded"
            except:

                return f"Error:  Reports cannot be downloaded."

        else :

            return f'Error: Driver is not set'
         

        

