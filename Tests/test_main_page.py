from Pages.MainPage import MainPage


class TestMainPage():

    def test_main_page(self):
        page = MainPage(self.driver)
        page.open_page()
