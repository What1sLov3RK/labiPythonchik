import operator
import sys
ds = {'add': operator.add, 'sub': operator.sub, 'div': operator.truediv, "mul": operator.mul}
first_num = int(sys.argv[2])
operation = str(sys.argv[1])
second_num = int(sys.argv[3])
print(ds[operation](first_num, second_num))