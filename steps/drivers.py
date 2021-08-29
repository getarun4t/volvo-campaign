from selenium import webdriver


class Chromedriver:
    '''This can be used for saving driver settings'''

    driver = webdriver.Remote(
        command_executor='http://selenium:4444/wd/hub',
        desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
