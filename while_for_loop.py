#while loop
n=0
sum=0
# while n<=10:
#     sum=sum+n
#     n+=1
# print(sum)

# for loop
for x in range(0,6):
    sum = sum + x
print(sum)

n=0
for x in [0,1,2,3,4,5]:
    if x%2 == 0:
        continue
    print(x)
    n += 1
print(n)

n1 = int(input("enter a number : "))
for i in range(n1):
    if i*i == n1:
        print(i)
        break
else:
    print("no find")

