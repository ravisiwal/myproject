from datetime import datetime
from dateutil import relativedelta
#from pago.elements.element import BaseElement
#from elements.button import Button
from typing import Union
import re


class DateTimePicker(BaseElement):
    def __init__(self, driver, locator, index=1):
        super().__init__(driver, locator)
        self.model = dict(
            date_locator=f'{{}}[{index}]//div[@class="react-datepicker-wrapper"]',
            time_locator=f'{{}}/..//following-sibling::div[1]/div[{index}]//input[@class="rc-time-picker-input"]',
            time_options='xpath==//div[@class="rc-time-picker-panel-combobox"]/div[{{}}]/ul/li[.="{{}}"]',
            picker_next_button='{}//button[@class="react-datepicker__navigation react-datepicker__navigation--next"]',
            picker_previous_button='{}//button[@class="react-datepicker__navigation react-datepicker__navigation--previous"]',
            picker_day='{}//div[@class="react-datepicker__week"]/div[@role="option" and not(contains(@class, "outside-month"))][.="{{}}"]',
            picker_today='{}//div[@class="react-datepicker__week"]/div[@role="option" and (contains(@class, "today"))]',
            picker_current_month='{}//div[@class="react-datepicker__current-month"]',
            picker_button='{}//div[@class="react-datepicker"]//button'
        )
        self.date_button = Button(driver, getattr(self, "date_locator"))
        self.time_input = Button(driver, getattr(self, "time_locator"))
        self.picker_button = Button(driver, getattr(self, "picker_button"))

    @property
    def date_picker(self) -> str:
        loc = f'{getattr(self, "date_locator")}//*[@value]'
        if self.driver.is_element_present(loc):
            return self.driver.find_element_by_locator(loc).get_attribute('value')
        else:
            return self.textgetter('date_locator')

    @date_picker.setter
    def date_picker(self, value: Union[str, datetime]):
        """
        Method to select start date and end dates.
        :param value: Input date object to select
        :return:
        """
        self.date_button.click()
        try:
            if isinstance(value, str):
                self.picker_button.click(value)
            else:
                input_date = value if value.strftime('%d') else datetime.now()
                formatted_input_date = datetime.strptime(datetime.strftime(input_date, '%B %Y'), '%B %Y')

                date_picker_current_month = self.driver.find_element_by_locator(
                    getattr(self, "picker_current_month")).text
                ui_date = datetime.strptime(date_picker_current_month, '%B %Y')

                d = relativedelta.relativedelta(formatted_input_date, ui_date)
                difference = d.months + d.years * 12
                if difference >= 1:
                    for i in range(0, difference):
                        self.driver.find_element_by_locator(getattr(self, "picker_next_button")).click()
                elif difference < 0:
                    for i in range(0, difference, -1):
                        self.driver.find_element_by_locator(getattr(self, "picker_previous_button")).click()
                self.driver.find_element_by_locator(
                    getattr(self, "picker_day").format(int(input_date.strftime('%d')))).click()

                self.driver.find_element_by_locator(f'{self.locator}/../ancestor::body').click()
        except Exception:
            raise Exception(f'Getting error while selecting date on {self.__class__.__name__}.')

    @property
    def time_picker(self) -> str:
        return self.driver.find_element_by_locator(getattr(self, "time_locator")).get_attribute('value')

    @time_picker.setter
    def time_picker(self, value: datetime):
        """
        Method to select time for start and end dates.
        :param value: Input time object to select time from combobox.
        :return:
        """
        self.time_input.click()
        try:
            select_time = re.split('[- :]', value.strftime('%I:%M %p').lower())
            count = 1
            for time in select_time:
                time = time.zfill(2)
                if count == 2:
                    time = '00' if int(time) < 15 else '15' if int(time) < 30 else '30' if int(time) < 45 else '45'
                loc = getattr(self, "time_options").format(count, time)
                self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                           self.driver.find_element_by_locator(loc))
                self.driver.find_element_by_locator(loc).click()
                count = count + 1

            self.driver.find_element_by_locator(f'{self.locator}/../ancestor::body').click()
        except Exception as e:
            raise Exception(f'Getting error while selecting date on {self.__class__.__name__}.')
