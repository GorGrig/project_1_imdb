import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys


class SeleniumBase:
    
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 45, 0.3)
        
    def __selenium_find_by(self, find_by):
        find_by = find_by.lower()
        locating = {'css' : By.CSS_SELECTOR, 'xpath' : By.XPATH, 
                    'partial_link_text' : By.PARTIAL_LINK_TEXT, 'id' : By.ID,
                    'link_text' : By.LINK_TEXT, 'class_name' : By.CLASS_NAME,
                    'name' : By.NAME, 'tag_name' : By.TAG_NAME }
        return locating[find_by]
    
    def is_visible_element(self, find_by : str, locator : str, locator_name =None) -> WebElement:
        return self.wait.until(ec.visibility_of_element_located((self.__selenium_find_by(find_by), locator)), locator_name)
    
    def is_visible_element_click(self, find_by : str, locator : str) -> None:
        self.is_visible_element(find_by, locator).click()
        
    def send_text_to_field(self, find_by : str, locator : str, text : str) -> WebElement:
        element_1 = self.is_visible_element(find_by, locator)
        element_1.clear()
        element_1.send_keys(text)
        
    def get_text(self, find_by : str, locator : str) -> str:
        return self.is_visible_element(find_by, locator).text
    
    def scoll(self) -> None:
        html = self.is_visible_element("tag_name", 'html')
        html.send_keys(Keys.END)
        
    def switching_between_tabs(self, index_page) -> None:
        driver = self.driver
        driver.switch_to.window(driver.window_handles[index_page])
        
    def wait_time(self, wait_second) -> None:
        time.sleep(wait_second)
    
    def get_current_url(self) -> str:
        driver = self.driver
        return driver.current_url
    
    