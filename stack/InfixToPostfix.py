# Function to define operator precedence
def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    else:
        return 0
# Function to check if a character is an operator
def is_operator(c):
    return c in '+-*/^'

# Function to convert infix to postfix
def infix_to_postfix(expression):
    stack = []       # Stack for operators
    result = []      # Output list (postfix)

    for char in expression:
        # If the character is an operand (A-Z, a-z, 0-9)
        # case 1
        if char.isalnum():
            result.append(char)
         # case 2
        # If left parenthesis -> push to stack
        elif char == '(':
            stack.append(char)
        # case 3
        # If right parenthesis -> pop until '(' found
        elif char == ')':
            while stack and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()  # remove '('
 
        # case 4
        # If an operator
        elif is_operator(char):
            while stack and precedence(char) <= precedence(stack[-1]):
                result.append(stack.pop())
            stack.append(char)


    # Pop all remaining operators
    while stack:
        result.append(stack.pop())  

    return ''.join(result) # join use for array of each char is combined as a string


# Input from user
user_input = input("Enter an infix expression: ")

# Convert & display result
postfix_result = infix_to_postfix(user_input)
print("Postfix expression:", postfix_result)






# # infix to postfix conversion code
# def precedence(opr):
#     if opr=='+' or opr=='-':
#         return 1;
#     elif opr=='*' or opr == '/':
#         return 2;
#     elif opr=='^':
#         return 3;
#     else:
#         return 0;
        
# def isoprator(opr):
#     return opr in '+-*/^'

# # functiion for infix_postfix
# def infix_to_postfix(expression):
#     stack = []
#     result = []
#     for ch in expression:
#         # ch  is a isalnum() then add resultPostfix
#         if ch.isalnum():
#             result.append(ch)
#         elif ch == '(':
#             stack.append(ch)
#         elif ch == ')':
#             # pop until matching '('
#             while stack and stack[-1] != '(':
#                 result.append(stack.pop())
#             if stack and stack[-1] == '(':
#                 stack.pop()  # pop '('
#         elif isoprator(ch):
#             while stack and precedence(ch) <= precedence(stack[-1]):
#                 result.append(stack.pop())
#             stack.append(ch)
        
#     # remaining pop all and append
#     while stack:
#         result.append(stack.pop())
#     return ''.join(result)
    
    
# user_input = input("enter infix expression : ");
# postfix_express = infix_to_postfix(user_input);
# print("postfix expression is : ",postfix_express);


    
            
            
            










