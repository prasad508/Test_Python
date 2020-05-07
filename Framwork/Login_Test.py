import time
import unittest
from Framwork.Login_Page import LoginPage
from Framwork.Home import HomePage
from selenium import webdriver
from pyunitreport import HTMLTestRunner
import sys
import os
import pytest_html
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

class LoginUnit(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.dr = webdriver.Firefox(
            executable_path='C:/Users/prasad.keluskar/AppData/Local/Programs/Python/Python39/geckodriver.exe')

        cls.dr.implicitly_wait(15)
        cls.dr.maximize_window()

    def test_login_valid(self):
        dr = self.dr
        self.dr.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(dr)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        logout = HomePage(dr)
        #logout.click_welcome()
        #logout.click_logout()
        time.sleep(15)

    def tearDown(self):
        self.dr.quit()

    if __name__ == '__main__':
        unittest.main(testRunner=HTMLTestRunner(output='C:/Users/prasad.keluskar/Downloads/Test'))
