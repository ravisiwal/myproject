import selenium.webdriver.support.ui as ui
import time
from selenium.webdriver.support import expected_conditions as EC
import re
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from pago.webelement import WebElement
from pago.elements.element import BaseElement
from typing import Union, Optional, Dict, List


class DropDownList(BaseElement):
    """
    ex:
    Dropdown List element used two different style on copilot frontend,
    1: select member, select strategy, select advertiser on strategies list as ObjectMultiDropdown component on frontend
    2: select member, advertiser on strategy wizard as ObjectDropdown component on frontend
    """

    def __init__(self, driver, locator: str, model: Optional[Dict[str, str]] = None):
        super().__init__(driver, locator, _injector=lambda s, x: x.format(s.locator))
        model = model or dict()
        self.model = {**model, **dict(inputbox='{}//input[@type="text"]', listbox='{}//div[@role="listbox"]',
                                      option='{}//div[@role="option"]',
                                      selected_option='{}//*[self::a or self::div[@class="text"]]',
                                      dropdownicon='{}//i[@class="dropdown icon"]')}
        self.wait = ui.WebDriverWait(self.driver, timeout=20)

    def input(self, value: str, options: Optional[Union[str, int, List[str]]] = None):
        """
        :param value: the string to type into inputbox for dropdown list
        :param options: the list to select from dropdown list
            if options is empty, only provide value to inputbox without clicking ony option
            if options is n=integrat, click nth option from option list
            if options is list, click option from option list one by one
            if options is string, click option from option list
        :return:
        """
        el = self.driver.find_element_by_locator(getattr(self, 'inputbox'))
        time.sleep(0.5)
        if isinstance(value, str) and re.match(r'clear()', value):
            selected_options = self.get_selected_options()
            self.unclick(options=selected_options)
        else:
            el.send_keys(value)
            self.wait.until(EC.element_to_be_clickable(self.driver.match_by_locator(getattr(self, "option"))))
            if options:
                self.click(options)

    def click(self, options: Optional[Union[str, int, List[str]]] = None, position: Optional[int] = None):
        """
        :param options: the list to select from dropdown list
            if options is empty, click first option from option list
            if options is n=integrat, click nth option from option list
            if options is list, click option from option list one by one
            if options is string, click option from option list
        :param position: index of option if there is duplicated option text
        :return:
        """
        options = [options] if not isinstance(options, list) else options
        opt_loc = getattr(self, 'option')
        for option in options:
            if isinstance(option, str):
                loc = f'{opt_loc}//*[.="{option}"][position()={position or 1}]'
            elif isinstance(option, int):
                loc = f'{opt_loc}[position()={option}]'
            else:
                loc = f'{opt_loc}[position()=1]'

            self.wait.until(EC.presence_of_element_located(self.driver.match_by_locator(loc)))
            el = self.driver.find_element_by_locator(loc)
            if not self.is_element_present(el):
                self.driver.find_element_by_locator(f'{self.locator}//i[@class="dropdown icon"]').click()
            el = self.wait.until(EC.element_to_be_clickable(self.driver.match_by_locator(loc)))
            el.click()

    def unclick(self, options: Optional[Union[str, List[str]]] = None):
        """
        :param options: the list to deselect from dropdown list, if options is empty, unclick all option from option list
        :return: None
        """
        options = [options] if not isinstance(options, list) else options
        opt_loc = getattr(self, 'selected_option')
        for option in options:
            if not option:
                loc = f'{opt_loc}/i'
            else:
                loc = f'{opt_loc}[.="{option}"]/i'
            els = self.driver.find_elements_by_locator(loc)
            for i in els:
                i.click()

    def options_size(self) -> int:
        return len(self.get_options())

    def get_options(self) -> List[str]:
        options = []
        try:
            els = self.driver.find_elements_by_locator(getattr(self, 'option'))
            options += [WebElement(e).get_attribute('innerText') for e in els]
        except NoSuchElementException:
            pass
        return options

    def get_selected_options(self) -> List[str]:
        els = self.driver.find_elements_by_locator(getattr(self, 'selected_option'))
        return list(filter(None, [e.get_attribute('innerText') for e in els]))

    def wait_for_inputbox(self) -> bool:
        """
        wait for dropdown input box ready to type
        :return:
        """
        try:
            self.wait.until(lambda x: self.driver.check_attribute(self.locator, 'aria-disabled', 'false'))
        except TimeoutException:
            return False

    def extend_inputbox(self, value: bool = True):
        el = self.driver.find_element_by_locator(self.locator)
        extended = el.get_attribute('aria-expanded') == 'true' or False
        if value != extended:
            self.driver.find_element_by_locator(getattr(self, 'dropdownicon')).click()

    def is_element_present(self, loc: Optional[Union[WebElement, str]] = None) -> bool:
        if isinstance(loc, WebElement):
            el = loc
        elif isinstance(loc, str):
            el = self.driver.find_element_by_locator(loc)
        else:
            el = getattr(self, loc) if loc else self.locator
            return self.driver.is_element_present(el)
        return el.is_displayed()

    def is_element_enabled(self, loc: Union[WebElement, str] = None) -> bool:
        if isinstance(loc, WebElement):
            el = loc
        elif isinstance(loc, str):
            el = self.driver.find_element_by_locator(loc)
        else:
            return self.driver.is_enabled(getattr(self, loc) if loc else self.locator)
        return el.is_enabled()
