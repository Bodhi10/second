
n = int(input("Enter the number of terms till which you want to find the Fibonnaci series: "))

a = 0
b = 1
c = 0
for f in range(n):
    print(c,end=",")
    c = a + b
    a=b
    b=c