from collections import namedtuple

HomeNamedTuple = namedtuple('HomeNamedTuple',
                            ['top_nav_links',
                             'firestone_logo'])
HomePageConst = HomeNamedTuple(
    top_nav_links='xpath==//*[@id="top-nav"]//div[@class="links"]/a[.="{}"]',
    firestone_logo='xpath==//*[@id="top-nav"]//div[@class="logo-wrapper"]')

ScheduleAppointmentNamedTuple = namedtuple('ScheduleAppointmentNamedTuple',
                                           ['input_name',
                                            'find_a_store_textbox',
                                            'find_a_store_button',
                                            'searched_store_list',
                                            'select_store_button',
                                            'select_service_page_header',
                                            'select_service_checkbox'])
ScheduleAppointmentConst = ScheduleAppointmentNamedTuple(
    input_name='xpath==//input[@name="{}"]',
    find_a_store_textbox='xpath==//*[@id="appt-step-1"]//input[@name="zip"]',
    find_a_store_button='xpath==//*[@id="appt-step-1"]//form/button',
    searched_store_list='xpath==//div[@class="appt-step-1-results"]//div[@class="result"]',
    select_store_button='xpath==//div[@class="appt-step-1-results"]//div[@class="result"][{}]'
                        '//div[@class="cta"]//button',
    select_service_page_header='xpath==//*[@id="appt-step-2"]//h2[@class="heading "]',
    select_service_checkbox='xpath==//*[@id="appt-step-2"]//div[@class="custom-checkbox"]/input[@value="{}"]')
