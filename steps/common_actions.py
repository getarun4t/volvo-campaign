import time

from selenium.common.exceptions import NoSuchElementException

from steps.custom_waits import wait_action_scroll_into_view, wait_and_click, wait_till_element_appears
from steps.drivers import Chromedriver
from steps.page_map import PageMap

driver = Chromedriver.driver

class PageActions(PageMap):
    ''' Actions class

    - The class is used to illustrate the different actions that can be performed.
    '''

    app = 'Campaign page'

    def page_check(self, page, app):
        wait_till_element_appears(self.action_map[self.app][page]['Heading']['type'],
                                  self.action_map[self.app][page]['Heading']['locator'])

    def check_list(self, page, options):
        options_list = options.splitlines()
        self.page_check(page, self.app)
        for option in options_list:
            try:
                wait_action_scroll_into_view(self.action_map[self.app][page][option]['type'],
                                             self.action_map[self.app][page][option]['locator'])
            except IndexError:
                raise AssertionError(f"{option} is not present in {page} in {self.app}")

    def click_button(self, button, page):
        '''Click button mimics click action on the UI. If-else logic is used to differentiate between different buttons
        types and locators
        '''
        self.page_check(page, self.app)
        try:
            wait_and_click(self.action_map[self.app][page][button]['type'],
                           self.action_map[self.app][page][button]['locator'])
        except:
            raise NoSuchElementException(f"{button} is not present on the {page} in {self.app}")

    def navigation_prompt(self):
        wait_till_element_appears(self.action_map[self.app]['Cookies alert']['Accept']['type'],
                           self.action_map[self.app]['Cookies alert']['Accept']['locator'])
        self.click_button('Accept', 'Cookies alert')
