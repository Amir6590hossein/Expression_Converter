# Python3 program to find infix for
# a given postfix.
import Stack
from infix import InfixToPrefix
import Stack as stk
def isOperand(x):
    return ((x >= 'a' and x <= 'z') or
            (x >= 'A' and x <= 'Z'))

def PostfixToInfix(exp):
    stack=stk.Stack()

    for i in exp:
        if (isOperand(i)):
           stack.push(i)

        else:

            op1=stack.pop()
            op2 =stack.pop()
            stack.push(f"({op2}{i}{op1})")

    return stack.pop()


def PostfixToPrefix (e):
 infix=PostfixToInfix(e)
 prefix=InfixToPrefix(infix)
 return prefix


