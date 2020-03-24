_ = input()
line1 = input()
line2 = input()
elements = line1.split()
frequency = line2.split()
data = []
for x in range(len(elements)):
  for i in range(int(frequency[x])):
    data.append(int(elements[x]))

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
q3 = cal_median(data2)
iqr = float(q3-q1)
print(round(iqr, 1))
