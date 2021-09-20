import operator
import sys
ds={'+': operator.add, '-': operator.sub, '/': operator.truediv, '*': operator.mul}
first_num = int(sys.argv[1])
operation = str(sys.argv[2])
second_num = int(sys.argv[3])
print(ds[operation](first_num, second_num))