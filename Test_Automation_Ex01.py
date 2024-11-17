from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert 

import time

class Exercicio01:
    def __init__(self):        
        self.SITE_LINK = "C:/GIT/TestAutomation/sample-exercise.html"
        self.SITE_MAP = {}

        service = Service(executable_path='C:\\driver\\chromedriver.exe')
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=service, options=options)
        ##self.driver.maximize_window()
        

    def open_page(self):   
        time.sleep(5)
        self.driver.get(self.SITE_LINK)
        time.sleep(5)

    def click_on_generate(self):
        self.open_page()
        button = self.driver.find_element(By.NAME, "generate")        
        button.click()
        time.sleep(5)
        generatedText = self.driver.find_element(By.ID, "my-value")
        time.sleep(5)
        generatedText.is_displayed()
        return generatedText.text
    
            
    def generate_text_test(self):
        text = self.click_on_generate()  
        input = self.driver.find_element(By.ID, 'input')
        input.clear()
        input.send_keys(text)
        button = self.driver.find_element(By.NAME, "button")
        button.click()
        time.sleep(5)
        Alert(self.driver).accept()  
        time.sleep(5)
        testText = "It workls! " + text + "!"    
        resultText = self.driver.find_element(By.ID, "result")
        resultText.is_displayed()
        
        assert testText in resultText.text, "Texto não confere"    
        


testes = Exercicio01()
testes.generate_text_test()
testes.generate_text_test()
testes.generate_text_test()


