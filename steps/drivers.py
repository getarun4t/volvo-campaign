from selenium import webdriver


class Chromedriver:
    '''This can be used for saving driver settings'''

    chromedriver = 'chromedriver'
    driver = webdriver.Chrome()

    # driver = webdriver.Remote(
    #     command_executor='http://selenium:4444/wd/hub',
    #     desired_capabilities={'browserName': 'chrome', 'javascriptEnabled': True})
    driver.maximize_window()