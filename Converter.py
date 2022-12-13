from  infix import infixToPostfix
from  infix import InfixToPrefix
from  prefix import prefixToInfix
from  prefix import prefixTopostfix
from  postfix import PostfixToPrefix
from  postfix import PostfixToInfix

def isInfix(e):
    operator=["+","-","/","^","*"]
    if(e[0] not in operator )and(e[-1] not in operator):
        return  True
    return False
def isPrefix(e):
    operator=["+","-","/","^","*"]
    if (e[0]  in operator ):
        return True
    return False
def isPostfix(e):
    operator=["+","-","/","^","*"]
    if e[-1]  in operator :
        return True
    return False

def Convert(e):
    result=["","",""]
    if isInfix(e):
        result[0]=InfixToPrefix(e)
        result[1] =e
        result[2] =infixToPostfix(e)
    elif isPostfix(e):
        result[0]=PostfixToPrefix(e)
        result[1] =PostfixToInfix(e)
        result[2] =e
    elif isPrefix(e):
        result[0]=e
        result[1]=prefixToInfix(e)
        result[2]=prefixTopostfix(e)
    return result





