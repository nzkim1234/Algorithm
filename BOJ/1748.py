from sys import stdin 

n = int(stdin.readline()) 
len_n = len(str(n)) 
count = 0 

for i in range(len_n -1): 
    count += 9 * 10 ** i * (i + 1) 

print(count + (n - 10 ** (len_n - 1) + 1) * len_n)
