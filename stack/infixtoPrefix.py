

# # infix to prefix code

# # precedency return 

# def precedence(op):
#     if op=='+' or op=='-':
#         return 1
#     elif op=='*' or op=='/':
#         return 2
#     elif op=='^':
#         return 3
#     else:
#         return 0
    
# # function for infix to postfix

# def infix_to_postfix(expre):
#     stack = []
#     output = ""
#     for ch in expre:
#         if ch.isalnum():
#             output+=ch
#         elif ch=='(':
#             stack.append(ch)
#         elif ch==')':
#             while stack and stack[-1]!=')':
#                output+=stack.pop()         
#             stack.pop()
#         else:
#             while stack and precedence(stack[-1]) > precedence(ch):
#                 output+=stack.pop()
#             stack.append(ch)
#     # pop remaining and push
#     while stack:
#         output+=stack.pop()
#     return output         
           
# # function for infix to prefix

# def infix_to_prefix(expr):
#     expr = expr[::-1] # reverse expression 

#     expr = list(expr)  # convert str expression to list

#     for i in range(len(expr)): # traverse each char of list
#         if expr[i]=='(':
#             expr[i]==')'
#         elif expr[i]==')':
#             expr[i] = '('
#         expr="".join(expr)
#     postfix = infix_to_postfix(expr)  # call here and return postfix expression
#     prefix = postfix[::-1] # reveresed postfix i.e prefix expression as result
#     return prefix

# expr = input("enter infix expression:")
# print("prefix expression is :",infix_to_prefix(expr))                      





#  following code is simple and short code for infix to prefix




def prec(op):
    return 1 if op in '+-' else 2 if op in '*/' else 3 if op == '^' else 0

def isop(c):
    return c in '+-*/^'

def infix_to_postfix(s):
    out, st = [], []
    for c in s:
        if c == ' ': 
            continue
        if c.isalnum():
            out.append(c)
        elif c == '(':
            st.append(c)
        elif c == ')':
            while st and st[-1] != '(':
                out.append(st.pop())
            st.pop()
        elif isop(c):
            if c == '^':
                while st and isop(st[-1]) and prec(st[-1]) > prec(c):
                    out.append(st.pop())
            else:
                while st and isop(st[-1]) and prec(st[-1]) >= prec(c):
                    out.append(st.pop())
            st.append(c)

    while st:
        out.append(st.pop())
    return ''.join(out)


def infix_to_prefix(expr):
    rev = expr[::-1].translate(str.maketrans('()', ')('))
    return infix_to_postfix(rev)[::-1]

if __name__ == "__main__":
    s = input("Enter infix expression: ")
    print("Prefix:", infix_to_prefix(s))





