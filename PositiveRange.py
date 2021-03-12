list1 = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input())

    list1.append(ele)

print(f"list1={list1}")
i=0
while i<n:
    if list1[i]>0:
        print(list1[i],end=" ")
    i+=1
