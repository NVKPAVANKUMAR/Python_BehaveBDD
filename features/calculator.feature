Feature: Calculator


  Scenario: Login Validation
    Given user is on loginpage
    When user enters valid username and password
    And clicks on signin button
    Then user navigates to Demodashboardpage



