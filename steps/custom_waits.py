from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from steps.drivers import Chromedriver

driver = Chromedriver.driver
timeout = 3
wait = WebDriverWait(driver, timeout)


def wait_action_scroll_into_view(locator_type, element, n=0):
    if locator_type == "xpath":
        wait_till_element_appears(locator_type, element)
        driver.find_elements_by_xpath(element)[n].location_once_scrolled_into_view


def wait_and_click(locator_type, element):
    if locator_type == "xpath":
        wait.until(EC.visibility_of_element_located((By.XPATH, element)))
        driver.find_element_by_xpath(element).click()


def wait_till_element_appears(locator_type, element):
    if locator_type == "xpath":
        wait.until(EC.visibility_of_element_located((By.XPATH, element)))
