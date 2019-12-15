import time
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.ui as ui
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from typing import Optional, List
from selenium.webdriver.remote.webelement import WebElement as SeleniumWebElement
from selenium.common.exceptions import NoSuchElementException

__author__ = 'Abhijit Yadav'


class WebElement(SeleniumWebElement):
    def __init__(self, element):
        super(WebElement, self).__init__(element.parent, element.id)


class Page(object):
    timeout_seconds = 180
    sleep_interval = .75

    def __init__(self, driver: webdriver):
        """
        :param driver: selenium webdriver
        """
        self.driver = driver
        self.wait = ui.WebDriverWait(self.driver, timeout=self.timeout_seconds)
        self.EC = expected_conditions

    def open_default_page(self, url: str = None):
        self.driver.get(url)
        self.wait_for_page_ready()
        return self

    def sleep(self, seconds: Optional[float] = None):
        if seconds:
            time.sleep(seconds)
        else:
            time.sleep(self.sleep_interval)

    def find_element_by_locator(self, locator: str) -> WebElement:
        locator_type, locator_value = locator.split('==')
        if locator_type == 'class':
            return WebElement(self.driver.find_element_by_class_name(locator_value))
        elif locator_type == 'css':
            return WebElement(self.driver.find_element_by_css_selector(locator_value))
        elif locator_type == 'id':
            return WebElement(self.driver.find_element_by_id(locator_value))
        elif locator_type == 'link':
            return WebElement(self.driver.find_element_by_link_text(locator_value))
        elif locator_type == 'name':
            return WebElement(self.driver.find_element_by_name(locator_value))
        elif locator_type == 'plink':
            return WebElement(self.driver.find_element_by_partial_link_text(locator_value))
        elif locator_type == 'tag':
            return WebElement(self.driver.find_element_by_tag_name(locator_value))
        elif locator_type == 'xpath':
            return WebElement(self.driver.find_element_by_xpath(locator_value))
        else:
            raise Exception('Invalid locator')

    def find_elements_by_locator(self, locator: str) -> List[WebElement]:
        locator_type, locator_value = locator.split('==')
        if locator_type == 'class':
            elements = self.driver.find_elements_by_class_name(locator_value)
        elif locator_type == 'css':
            elements = self.driver.find_elements_by_css_selector(locator_value)
        elif locator_type == 'id':
            elements = self.driver.find_elements_by_id(locator_value)
        elif locator_type == 'link':
            elements = self.driver.find_elements_by_link_text(locator_value)
        elif locator_type == 'name':
            elements = self.driver.find_elements_by_name(locator_value)
        elif locator_type == 'plink':
            elements = self.driver.find_elements_by_partial_link_text(locator_value)
        elif locator_type == 'tag':
            elements = self.driver.find_elements_by_tag_name(locator_value)
        elif locator_type == 'xpath':
            elements = self.driver.find_elements_by_xpath(locator_value)
        else:
            raise Exception('Invalid locator')
        return [WebElement(e) for e in elements]

    def wait_for_enabled(self, locator: str):
        for i in range(self.timeout_seconds):
            if not self.driver.is_enabled(locator):
                self.sleep()
            else:
                break
        else:
            raise Exception('Wait for enabled timed out')

    def wait_for_element_to_present(self, locator: str):
        for i in range(self.timeout_seconds):
            if not self.is_element_present(locator):
                self.sleep()
            else:
                break
        else:
            raise Exception('Wait for enabled timed out')

    def wait_for_page_ready(self):
        try:
            self.sleep(self.sleep_interval * 4)
            self.wait.until(lambda x: self.driver.execute_script('return document.readyState;') == 'complete')
            return True
        except Exception:
            raise TimeoutException(msg='Wait for page to load timed out')

    def is_element_present(self, locator: str) -> bool:
        try:
            self.find_element_by_locator(locator)
            return True
        except NoSuchElementException:
            return False

    def is_visible(self, locator: str) -> bool:
        if self.is_element_present(locator):
            if self.find_element_by_locator(locator).is_displayed():
                return True
            else:
                return False
        else:
            return False

    def is_active(self, locator: str) -> bool:
        if self.is_element_present(locator):
            if 'active' in self.find_element_by_locator(locator).get_attribute('class'):
                return True
            else:
                return False
        else:
            return False

    def is_enabled(self, locator: str) -> bool:
        if self.is_element_present(locator):
            if self.find_element_by_locator(locator).get_attribute('disabled'):
                return False
            elif 'disabled' in self.find_element_by_locator(locator).get_attribute('class'):
                return False
            else:
                return True
        else:
            return False

    def input_text(self, locator: str, value: str):
        el = WebElement(self.find_element_by_locator(locator))
        el.clear()
        el.send_keys(value)

    def get_element_text(self, locator: str) -> str:
        return self.find_element_by_locator(locator).text
