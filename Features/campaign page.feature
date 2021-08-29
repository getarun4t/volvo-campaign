# Created by kannan at 29/08/21
Feature: Campaign page
  - The Safety Campaign page of Volvo lists the different safety features of Volvo Cars
  - The page also has weblinks for viewing and purchasing the different Volvo cars

  Background: User is opening Volvo Safety Campaign page
    Given user is opening the Volvo Safety Campaign page

  Scenario: User is verifying the list of safety features
    Then the below options should be available in the Safety Section:
      Safety header
      Safety video
      Speed section header
      Speed cap
      Highway pilot
      Driver monitoring cameras
      Care key
      Learn more URL
      Conditions message

  Scenario: User is verifying the list of testimonials
    Then the below options should be available in the Testimonial Section:
      Testimonial header
      Testimonial description
      Amy Video
      Amy
      Amy Description
      Summer Video
      Summer
      Summer Description
      Linda & Molly Video
      Linda & Molly
      Linda & Molly Description
      Alex Video
      Alex
      Alex Description

  Scenario: User is verifying the Innovation
    Then the below options should be available in the Innovation Section:
      Innovation header
      Innovation description
      Learn more URL
      Innovation image

  Scenario: User is verifying the list of Models
    Then the below options should be available in the Models Section:
      Models Header
      XC90 SUV Header
      XC90
      XC90 Learn
      XC90 Shop
      XC60 SUV Header
      XC60
      XC60 Learn
      XC60 Shop
      XC40 SUV Header
      XC40
      XC40 Learn
      XC40 Shop
      XC40 Pure Electric SUV Header
      XC40 Pure Electric
      XC40 Pure Electric Learn
      XC40 Pure Electric Shop
    When user clicks on Next in Models Section
    Then the below options should be available in the Models Section:
      V90 Estate Header
      V90
      V90 Learn
      V90 Shop
    When user clicks on Next in Models Section
    Then the below options should be available in the Models Section:
      V60 Estate Header
      V60
      V60 Learn
      V60 Shop
    When user clicks on Next in Models Section
    Then the below options should be available in the Models Section:
      S90 Sedan Header
      S90
      S90 Learn
      S90 Shop
    When user clicks on Previous in Models Section
    Then the below options should be available in the Models Section:
      XC40 Pure Electric SUV Header
      XC40 Pure Electric
      XC40 Pure Electric Learn
      XC40 Pure Electric Shop
    And the below options should be available in the Models Section:
      Learn More
      Mild Hybrid Cars

  Scenario: User is verifying the Footer
    Then the below options should be available in the Footer Section:
      Disclaimer 1
      Disclaimer 2
      Cookies
      Legal
      Privacy
      Socail Media
      Copyright

  Scenario: User is verifying the Top Panel
    Then the below options should be available in the Top Panel Section:
      Volvo logo
      Our Cars URL
      Options

  Scenario: User is verifying the options in Top Panel
    Then the below options should be available in the Top Panel options Section:
      Volvo logo
      Buy
      Own
      Why Volvo
      Explore
      More
      International
      Facebook
      Instagram
      Twitter
      Youtube
    When user clicks on Buy in Top Panel options Section
    Then the below options should be available in the Buy Section:
      Purchase Header
      Fleet sales
      Used cars
      Diplomatic sales
      Child seats
      Explore
      Experience Volvo Cars

