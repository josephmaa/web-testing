from selenium import webdriver
import unittest
import configparser

class TestWebsite(unittest.TestCase):
    def setUp():
        parser = configparser.ConfigParser()
        parser.read("web.ini")
        driver = webdriver.Chrome(executable_path="./chromedriver")
        driver.get(parser["DEFAULT"]["url"])