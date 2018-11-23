Feature: Calculator

  Scenario Outline: Add any two numbers
      Given I have entered <number1> into the calculator
      And I have also entered <number2> into the calculator
      When I press add
      Then the sum should be <result>
    Examples:
      |  number1|  number2|   result|
      |        5|        2|        7|
      |        4|        8|       12|
      |      100|      200|      300|