import sys

user_input = sys.argv[1]
if user_input:
    try:
        print(eval(user_input))
    except SyntaxError:
        print("Input error (Syntax error)")