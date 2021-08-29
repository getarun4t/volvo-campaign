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

