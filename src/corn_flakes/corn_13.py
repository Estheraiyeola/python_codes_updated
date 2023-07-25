# def calculator_app(num1, operator, num2):
#     total = 0
#     if operator == chr(43):
#         total = num1 + num2
#         return total
#     elif operator == chr(45):
#         total = num1 - num2
#         return total
#     elif operator == chr(42):
#         total = num1 * num2
#         return total
#     elif operator == chr(47):
#         total = num1 / num2
#         return total
#     else:
#         print('Logic error')
#     return total
#
#
# def calculate():
#     user_input1 = int(input(""))
#     operators = input("")
#     user_input2 = int(input(""))
#     return calculator_app(user_input1, operators, user_input2)
#
#
# print(calculate())
import parser

expression = "5 + 4"

parsing = parser.expr(expression)

res = eval(parsing)