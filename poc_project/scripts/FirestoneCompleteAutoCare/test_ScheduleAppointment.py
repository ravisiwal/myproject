from env_setup.browser_setup import TestBaseCase
from modules.firestone_auto_care.ScheduleAppointment import ScheduleAppointmentPage
from page_elements.locators.FirestoneAutoCareNameTuple import ScheduleAppointmentConst


class TestScheduleAppointment(TestBaseCase):
    @classmethod
    def setup_class(cls):
        super(TestScheduleAppointment, cls).setup_class()
        cls.schedule_appointment_page = ScheduleAppointmentPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        super(TestScheduleAppointment, cls).teardown_class()

    def test_open_schedule_appointment_page(self):
        self.schedule_appointment_page.open_schedule_appointment_page()
        assert self.schedule_appointment_page.is_element_present(ScheduleAppointmentConst.find_a_store_textbox)
        assert self.schedule_appointment_page.is_element_present(ScheduleAppointmentConst.find_a_store_button)
        self.schedule_appointment_page.select_store(zip_code='10101')
        assert self.schedule_appointment_page.get_element_text(
            ScheduleAppointmentConst.select_service_page_header) == 'SELECT A SERVICE AND APPOINTMENT TIME'



