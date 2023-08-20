factors = []
num = int(input())
for i in range(1,num+1):
    if num % i == 0:
        factors.append(i)

if(len(factors)==2):
    print("it is a prime number")
else:
    print("it is a not a prime number")

