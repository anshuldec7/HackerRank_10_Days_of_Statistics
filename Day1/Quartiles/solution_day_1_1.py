# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = input()
line = input()
elements = line.split()
data = [int(i) for i in elements]

def cal_median(data):
    data_length = len(data)
    median = 0
    if data_length%2 == 0:
        med1=data[int(data_length/2) -1]
        med2=data[int(data_length/2)]
        median = (med1 + med2) //2
    else:
        median = data[int(data_length/2)]
    return median
data.sort()
if len(data)%2 == 0:
    data1 = data[0:len(data)//2]
    data2 = data[len(data)//2:]
else:
    data1 = data[0:len(data)//2]
    data2 = data[len(data)//2+1:]
    
q1 = cal_median(data1)
q2 = cal_median(data)
q3 = cal_median(data2)

print(q1)
print(q2)
print(q3)
