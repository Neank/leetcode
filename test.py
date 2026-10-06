# class Solution(object):
#     def evalRPN(self, tokens):
#         stack = []
#         for token in tokens:
#             if token == '+':
#                 b = stack.pop(); a = stack.pop()
#                 stack.append(a + b)
#             elif token == '-':
#                 b = stack.pop(); a = stack.pop()
#                 stack.append(a - b)
#             elif token == '*':
#                 b = stack.pop(); a = stack.pop()
#                 stack.append(a * b)
#             elif token == '/':
#                 b = stack.pop(); a = stack.pop()
#                 stack.append(int(a / b))
#             else:
#                 stack.append(int(token))
#         return stack[0]

# s = Solution()
# print(s.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
var1 = -7
var2 = 2

print(int(var1 / var2))
print(var1 // var2)