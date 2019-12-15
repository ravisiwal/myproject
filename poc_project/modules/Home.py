from env_setup.page import Page


class HomePage(Page):
    def __init__(self, driver):
        super().__init__(driver)

    def open_default_page(self, url: str = None):
        self.driver.get(url)
        self.driver.implicitly_wait(20)
        return self
