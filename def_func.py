# def multyply(n1,n2):
#     x = n1/n2
#     return x
# y = multyply(n2=4,n1=16)+multyply(2,1)
# print(y)

# # def calculate():
# #     sum = 0
# #     x1 = int(input("munber1: "))
# #     x2 = int(input("number2: "))
# #     for i in range(x1,x2):
# #         sum = sum+i
# #     print(sum)

# # calculate()

# def say(msg="Hello"):
#     print(msg)
# say()

# # unlimited *
# def say1(*msgs):
#     for i in msgs:
#         print(i)

# say1("a","b","c")

# def power(base, exp): #base^exp
#     x = base**exp
#     return x

# print(power(2,3))

def avg(*n):
    sum = 0
    for i in n:
        sum = sum+i
    x = (sum/len(n))
    return x

print(avg(3,9))
print(avg(3,6,9))
print(avg(1,-3,-6,12))


