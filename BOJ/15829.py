l = int(input())
string = input()
exponent = 0
result = 0
for i in string:
    num = ord(i) - 96
    result += num * (31 ** exponent)
    exponent += 1
print(result % 1234567891)
