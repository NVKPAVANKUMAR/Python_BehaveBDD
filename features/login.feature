Feature: Login


  Scenario Outline: Do Login
    Given user is on Demologinpage
    When user enters valid <username> and <password>
    And clicks on login button
    Then user navigates to dashboardpage

    Examples:
      | username | password |
      | ADMIN    | password |
      | admin    | sandbox  |


