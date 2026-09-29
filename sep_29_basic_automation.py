import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import select
#//div[@id='Alh6id']//ul//li
class SearchUtility:
    def __init__(self):
        self.driver = webdriver.Chrome()


    def send_keys(self, locator,text):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
        element.send_keys(text)

    def click_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, locator)))
        element.click()

    def select_by_index(self,locator,index):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, locator)))
        elements=self.driver.find_elements(By.XPATH, locator)
        for element in elements:
            print(element.text)
        if len(elements)>=index:
            target_index=elements[index-1]
            target_index.click()

class Locators:
    search_box=("//textarea[@id='ti6dpd']")
    search_items=("//div[@id='Alh6id']//ul//li")

def test_google_search():
    search = SearchUtility()
    search.driver.get("https://google.com")
    time.sleep(3)
    search.click_element(Locators.search_box)
    search.send_keys(Locators.search_box,'prince')
    time.sleep(5)
    search.select_by_index(Locators.search_items,3)
    time.sleep(10)

