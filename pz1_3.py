# Write a Python-script that determines whether the input string is the correct entry for the 'formula' according EBNF syntax (without
# using regular expressions).
# Formula = Number | (Formula Sign Formula)
# Sign = '+' | '-'
# Number = '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
# Input: string
# Result: (True / False, The result value / None)
# Example,
# user_input = '1+2+4-2+5-1' result = (True, 9)
# user_input = '123' result = (True, 123)
# user_input = 'hello+12' result = (False, None)
# user_input = '2++12--3' result = (False, None)
# user_input = '' result = (False, None)
import sys


def check(string, curr_pos):
    if not string[curr_pos].isdigit() and (string[curr_pos] not in oper_list or string[curr_pos - 1] in oper_list):
        return False
    elif not curr_pos:
        if string[len(string) - 1] not in oper_list:
            return True
    else:
        return check(string, curr_pos - 1)


user_input = sys.argv[1:]
# parameter list
oper_list = ['+', '-']
# list of operation signs

if not user_input:
    # check if there is an input
    print("No parameters")
else:
    user_input_str = "".join(user_input)
    # converting a list of parameters into string
    if check(user_input_str, len(user_input_str) - 1):
        # if string is correct, printing the answer
        # else, printing the "False" message
        print("True", eval(user_input_str), sep=", ")
    else:
        print("False, None")