# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
elements = input()
array_values = elements.split()
numbers = [int(elem) for elem in array_values]

# Get the mean
mean = sum(numbers)/len(numbers)

# Get the Median
numbers.sort()
length = len(numbers)

if length%2 == 0:
    med1 = numbers[int(length/2) -1]
    med2 = numbers[int(length/2)]
    median = (med1 + med2) /2
else:
    median = numbers[int(length/2)]

# Get the Mode
count_dict = {}
mode = None
for number in numbers:
    if number in count_dict:
        count_dict[number] += count_dict[number]
    else:
        count_dict[number] = 1
    if mode is None:
        mode = (number, 1)
    else:
        if count_dict[number] > mode[1]:
            mode = (number, count_dict[number])
print(round(mean, 1))
print(round(median, 1))
print(mode[0])
