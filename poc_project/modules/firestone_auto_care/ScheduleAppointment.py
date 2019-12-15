from env_setup.page import Page
from page_elements.locators.FirestoneAutoCareNameTuple import ScheduleAppointmentConst, HomePageConst
from typing import List


class ScheduleAppointmentPage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def open_schedule_appointment_page(self):
        self.find_element_by_locator(HomePageConst.top_nav_links.format('Schedule an Appointment')).click()
        self.wait_for_page_ready()

    def select_store(self, zip_code: str = '60605'):
        """
        Method to find store based on zip code.
        :param zip_code: Zip code in string format.
        """
        self.input_text(ScheduleAppointmentConst.find_a_store_textbox, zip_code)
        self.find_element_by_locator(ScheduleAppointmentConst.find_a_store_button).click()
        self.wait_for_element_to_present(ScheduleAppointmentConst.searched_store_list)
        self.find_element_by_locator(ScheduleAppointmentConst.select_store_button.format(1)).click()
        self.wait_for_page_ready()

    def select_service(self, services: List = 'Tire Replacement'):
        """
        Method to select services based on available options.
        :param services:
        :return:
        """
        for service in services:
            self.find_element_by_locator(ScheduleAppointmentConst.select_service_checkbox.format(service)).click()

