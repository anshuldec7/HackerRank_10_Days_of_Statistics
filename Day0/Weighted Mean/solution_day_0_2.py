# Enter your code here. Read input from STDIN. Print output to STDOUT
_ = input()
line1 = input()
line2 = input()

array = line1.split()
weigths = line2.split()

X = [int(x) for x in array]
W = [int(y) for y in weigths]
num = 0
for i in range(len(X)):
    num = num + (X[i]*W[i])
w_m = num/sum(W)
print(round(w_m, 1))
