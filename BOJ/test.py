import math

n = 10
print(math.ceil(math.log2(n)))
b = math.ceil(math.log2(n)) + 1
node_n = 1 << b
print(node_n)