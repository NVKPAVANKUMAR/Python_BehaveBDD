Feature: Calculator

  Scenario Outline: perform any arithmetic operation on  two numbers
    Given I have entered <number1> into the calculator
    And I have also entered <number2> into the calculator
    When I press <operation>
    Then then result should be <result>
    Examples:
      | number1 | number2 | operation      | result |
      | 5       | 2       | addition       | 7      |
      | 4       | 8       | multiplication | 32     |
      | 100     | 200     | division       | 2      |
      | 300     | 100     | subtraction    | 200    |