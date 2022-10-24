from selenium import webdriver
import unittest
import configparser


class test_website(unittest.TestCase):
    parser = configparser.ConfigParser()
    parser.read("web.ini")
    print(parser["DEFAULT"]["url"])
    driver = webdriver.Chrome(executable_path="./chromedriver")
    driver.get(parser["DEFAULT"]["url"])


if __name__ == "__main__":
    unittest.main()
