'''Page Objects Folder

This document is used for storing the locators for the page/sections'''


class SafetyFeatures:
    safety_header = "//h2[contains(.,'Ideas that change the world are often the most controversial.')]"
    safety_video = "//video[contains(@poster,'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HA')]"
    safety_section_header = "//span[contains(.,'With new and existing safety features, we are determined to save a million more lives.')]"
    speed_cap = "//em[contains(.,'Speed cap')]"
    highway_pilot = "//em[contains(.,'Highway pilot')]"
    driver_monitor = "//em[contains(.,'Driver monitoring cameras')]"
    care_key = "//em[contains(.,'Care Key')]"
    learn_more = "/intl/v/car-safety"
    conditions = "//p[contains(.,'Features depicted may not be standard or available for all styles, engine options, model years and regions.')]"

class Testimonials:
    tesimonial_header = "//h2[contains(.,'One of a million')]"
    testomonial_description = "//p[contains(.,'Hear the stories from real car crash survivors and see how they've managed to turn an accident into a positive change in their lives.')]"
    amy = "//em[contains(.,'Amy')]"
    amy_description = "//p[contains(.,'Meet Amy Ma, who survived a multi-vehicle collision thanks to the safety belt.')]"
    amy_video = "//video[contains(@poster,'amy')]"

class Innovation:
    innovation_header = "//h2[contains(.,'Decades of innovation')]"
    innovation_description = "//p[contains(.,'Ever since our founding in 1927, we've been designing cars that put people first. Discover our most important safety innovations over the years.')]"
    learn_more = "/intl/v/car-safety/safety-heritage"
    innovation_image = '''//img[@alt='A safety belt in grey with the text "Since 1959" engraved on the buckle.']'''

class Models:
    models_header = "//h2[contains(.,'Explore our models')]"
    xc_90_header = "(//em[contains(.,'SUV')])[1]"
    xc_90 = "//span[contains(.,'XC90 Recharge')]"
    xc_90_image = "//img[contains(., 'A birch light Volvo SUV XC90 Recharge plugin hybrid standing')]"
    xc_90_learn = "(//a[contains(.,'Learn')])[3]"
    xc_90_shop = "//a[@href='https://www.volvocars.com/intl/build/xc90-hybrid']"
    next = "//button[contains(., 'springCarouselNextButton')]"
    previous = "//button[contains(., 'springCarouselPreviousButton')]"
    v_90_header = "(//em[contains(.,'ESTATE')])[1]"
    v_90 = "//span[contains(.,'V90 Recharge')]"
    v_90_image= "//img[contains(., 'A grey Volvo estate V90 Recharge plugin hybrid standing still on grey floor in a studio')]"
    v_90_learn = "(//a[contains(.,'Learn')])[7]"
    v_90_shop = "//a[@href='https://www.volvocars.com/intl/build/v90-hybrid']"
    learn_more = "//a[@aria-label='Learn more about Recharge']"
    mild_hybrid = "//a[contains(.,'Mild hybrid cars')]"

class TopPanel:
    volvo_logo = '''//a[@data-track-onclick='{"eventAction":"click","eventLabel":"volvo logo"}']'''
    our_cars = "//span[contains(.,'Our Cars')]"
    options = "//div[contains(., 'SiteNav-a')]"

class Options:
    volvo_logo = '''//img[contains(., 'https://www.volvocars.com/static/shared/images/volvo-wordmark-black.svg')]'''
    buy = "//em[contains(.,'Buy')]"
    own = "//em[contains(.,'Own')]"
    why_volvo = "//em[contains(.,'Why Volvo')]"
    explore = "//em[contains(.,'Explore')]"
    more = "//em[contains(.,'More')]"
    international = "//p[contains(.,'International')]"
    facebook = "//h2[contains(.,'facebook')]"
    purchase = "//h3[contains(.,'Purchase')]"
    fleet_sales = "//em[contains(.,'Fleet sales')]"
    used_sales = "//em[contains(.,'Used cars')]"