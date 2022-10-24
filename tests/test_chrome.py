from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import unittest
import configparser
from typing import Optional


class test_website_chrome(unittest.TestCase):
    def setUp(self):
        parser = configparser.ConfigParser()
        parser.read("web.ini")
        self.driver: Optional["webdriver"] = None
        chrome_executable = Service(
            executable_path="./drivers/chromedriver", log_path="NUL"
        )
        self.driver = webdriver.Chrome(service=chrome_executable)
        self.driver.get(parser["DEFAULT"]["url"])

    def tearDown(self):
        self.driver.quit()

    def test_ajax_block_element_0(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, "li.ajax_block_product")
        self.driver.implicitly_wait(1)
        if elements[0].is_displayed():
            self.driver.implicitly_wait(1)
            elements[0].click()
            self.driver.implicitly_wait(1)
            self.driver.back()

    def test_ajax_block_element_5(self):
        elements = self.driver.find_elements(By.CSS_SELECTOR, "li.ajax_block_product")
        self.driver.implicitly_wait(1)
        if elements[5].is_displayed():
            self.driver.implicitly_wait(1)
            elements[5].click()
            self.driver.implicitly_wait(1)
            self.driver.back()

    def test_input_box_enter(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input.search_query")
        element.send_keys("Testing")
        element.send_keys(Keys.ENTER)

    def test_input_box_submit(self):
        element = self.driver.find_element(By.CSS_SELECTOR, "input.search_query")
        element.send_keys("Testing")
        element.submit()


if __name__ == "__main__":
    unittest.main()
