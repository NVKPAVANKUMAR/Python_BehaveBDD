Feature: static login

  @browser
  Scenario: Login Validation
    Given user is on loginpage
    When user inputs valid username and password
    And clicks on signin button
    Then user navigates to Demodashboardpage



