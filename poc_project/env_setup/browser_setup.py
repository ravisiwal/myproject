from selenium import webdriver
from env_setup.page import Page

__author__ = 'Abhijit Yadav'

driver_path = '/home/ravindra/poc_project/configs/browsers/chromedriver.exe'
url_path = 'https://cwh-uat.firestonecompleteautocare.com/'


class TestBaseCase(object):
    @classmethod
    def setup_class(cls):
        if hasattr(super(TestBaseCase, cls), 'setup_class'):
            super(TestBaseCase, cls).setup_class()
        cls.driver = webdriver.Chrome(executable_path=driver_path)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(7)
        cls.page = Page(cls.driver).open_default_page(url_path)

    @classmethod
    def teardown_class(cls):
        cls.driver.close()
        cls.driver.quit()

    def back_page(self):
        self.driver.back()

    def forward_page(self):
        self.driver.forward()
