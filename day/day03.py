import random
num = int(random.randint(1, 1000))
print(num)
"""
num = int(input("输入一个输入一个数据"))
"""


if 90 <= num <= 100:
    print("优秀")
elif 80 <= num < 90:
    print("good")
elif 70 <= num < 80:
    print("一般")
elif 60 <= num < 70:
    print("及格")
elif 0 <= num < 60:
    print("不及格")
else:
    print("非法")

num1 = 1
while num1 <= 10:
    print(num1)
    num1 = num1 + 1
