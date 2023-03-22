def calculate(expression):
    if isinstance(expression, int):
        return expression
    elif type(expression) is tuple or type(expression) is list:
        operator = expression[0]
        operands = expression[1:]
        if operator == 'add':
            return sum(calculate(operand) for operand in operands)
        elif operator == 'deduct':
            return calculate(operands[0]) - sum(calculate(operand) for operand in operands[1:])
        elif operator == 'multiply':
            result = 1
            for operand in operands:
                result *= calculate(operand)
            return result
        elif operator == 'divide':
            result = calculate(operands[0])
            for operand in operands[1:]:
                try:
                    result /= calculate(operand)
                except ZeroDivisionError:
                    return 0
            return result
        else:
            raise ValueError('Invalid operator: {}'.format(operator))


def main():
    msg = """
        Author: Alex Ledoskih
        ---------------------
        Enter your calculation based on operators available below:
        * and - add numbers.
        * deduct - subtract numbers.
        * multiply - multiply numbers.
        * divide - divide numbers.

        FORMAT: ['ACTION', #, #]

        Example: "['add',21,25]"
        Example: "['multiply',21,25]"
        Example: "['deduct',25,21]"
        Example: "['divide',20,10]"
        Example: "['multiply',2,3,['add',2,8]]"
    """

    print(msg)
    user_input = input("Enter a variable: ")

    # we want to check the type of user input, as we need only integer, tuple or list
    try:
        # Check if the user input is an integer
        integer_input = int(user_input)
        print(calculate(integer_input))
    except ValueError:
        # Check if the user input is a tuple
        try:
            tuple_input = tuple(eval(user_input))
            print(calculate(tuple_input))
        except:
            # Check if the user input is a list
            try:
                list_input = list(eval(user_input))
                print(calculate(list_input))
            except:
                # The input could not be converted to any of the expected types
                print("The user input is of unknown type.")


if __name__ == '__main__':
    main()
