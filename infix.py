from Stack import Stack



Operators = set(['+', '-', '*', '/', '(', ')', '^'])  # collection of Operators

Priority = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # dictionary having priorities of Operators

def isOperator(c):
    return (not (c >= 'a' and c <= 'z') and not(c >= '0' and c <= '9') and not(c >= 'A' and c <= 'Z'))
def infixToPostfix(expression):
    stack = []  # initialization of empty stack

    output = ''

    for character in expression:

        if character not in Operators:  # if an operand append in postfix expression

            output += character

        elif character == '(':  # else Operators push onto stack

            stack.append('(')

        elif character == ')':

            while stack and stack[-1] != '(':
                output += stack.pop()

            stack.pop()

        else:

            while stack and stack[-1] != '(' and Priority[character] <= Priority[stack[-1]]:
                output += stack.pop()

            stack.append(character)

    while stack:
        output += stack.pop()

    return output

def getPriority(x):
    if x in "+-":
        return 1
    elif x in "*/":
        return 2
    elif x in "^":
        return 3
    return 0

def InfixToPrefix(infix):
    # stack for operators.
    operators = []

    # stack for operands.
    operands = []

    for i in range(len(infix)):
        # If current character is an
        # opening bracket, then
        # push into the operators stack.
        if (infix[i] == '('):
            operators.append(infix[i])

        # If current character is a
        # closing bracket, then pop from
        # both stacks and push result
        # in operands stack until
        # matching opening bracket is
        # not found.
        elif (infix[i] == ')'):
            while (len(operators) != 0 and operators[-1] != '('):
                # operand 1
                op1 = operands[-1]
                operands.pop()

                # operand 2
                op2 = operands[-1]
                operands.pop()

                # operator
                op = operators[-1]
                operators.pop()

                # Add operands and operator
                # in form operator +
                # operand1 + operand2.
                tmp = op + op2 + op1
                operands.append(tmp)

            # Pop opening bracket
            # from stack.
            operators.pop()

        # If current character is an
        # operand then push it into
        # operands stack.
        elif (not isOperator(infix[i])):
            operands.append(infix[i] + "")

        # If current character is an
        # operator, then push it into
        # operators stack after popping
        # high priority operators from
        # operators stack and pushing
        # result in operands stack.
        else:
            while (len(operators) != 0 and getPriority(infix[i]) <= getPriority(operators[-1])):
                op1 = operands[-1]
                operands.pop()

                op2 = operands[-1]
                operands.pop()

                op = operators[-1]
                operators.pop()

                tmp = op + op2 + op1
                operands.append(tmp)
            operators.append(infix[i])

    # Pop operators from operators
    # stack until it is empty and
    # operation in add result of
    # each pop operands stack.
    while (len(operators) != 0):
        op1 = operands[-1]
        operands.pop()

        op2 = operands[-1]
        operands.pop()

        op = operators[-1]
        operators.pop()

        tmp = op + op2 + op1
        operands.append(tmp)

    # Final prefix expression is
    # present in operands stack.
    return operands[-1]



