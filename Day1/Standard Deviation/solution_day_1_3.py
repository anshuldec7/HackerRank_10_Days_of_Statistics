# Enter your code here. Read input from STDIN. Print output to STDOUT
import math 
_ = input()
line = input()
values = line.split()
data = [int(i) for i in values]

sqrd_sum = 0
mean = sum(data)/len(data)
for x in data:
    sqrd_sum = sqrd_sum + (x-mean)**2
variance = sqrd_sum/len(data)
s_d = math.sqrt(variance)
print(round(s_d,1))
