from selenium import webdriver
import unittest
import configparser
from typing import Optional


class test_website(unittest.TestCase):
    def __init__(self):
        self.driver: Optional["webdriver"] = None

    def setUp(self):
        parser = configparser.ConfigParser()
        parser.read("web.ini")
        self.driver = webdriver.Chrome(executable_path="./chromedriver")
        self.driver.get(parser["DEFAULT"]["url"])

    def tearDown(self):
        self.driver.close()

    def test_


if __name__ == "__main__":
    unittest.main()
