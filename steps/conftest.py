import time

import pytest
from pytest_bdd import given, parsers
from steps.common_actions import PageActions
from steps.drivers import Chromedriver

driver = Chromedriver.driver
actions = PageActions()


@pytest.fixture(scope="session", autouse=True)
def setup_teardown():
    driver.get("https://www.volvocars.com/intl/v/car-safety/a-million-more")
    actions.navigation_prompt()
    yield driver
    driver.close()