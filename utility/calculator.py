class Calculator:

    @staticmethod
    def select_function(op, num1, num2):

        if op == "addition":
            return num1 + num2

        elif op == "subtraction":
            if num1 > num2:
                return num1 - num2
            else:
                return num2 - num1

        elif op == 'multiplication':
            return num1 * num2

        elif op == 'division':
            if num1 > num2:
                return num1 / num2
            else:
                return num2 / num1
