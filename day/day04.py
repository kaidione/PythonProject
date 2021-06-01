"""i = 1
while i <= 9:
    j = 1
    while j <= i:
        print(j, "X", i, "=", (j * i), "        ", end="")
        j = j + 1
    print()
    i = i + 1
"""

'''
    数据类型：
        str : 字符串:'' ,“jason”
        int : 整型， 6 9 8  -5
        bool: True,False
        float:浮点，小数点 3.15，  1.76

        容器类型：
            元组：()  ,缺点：不能做任何修改
            列表：[] , 好处：可以进行修改
            集合：
            字典

'''



# # 添加
# a.append("旺财")
#
# # 修改：将第一个人改成，张三
# a[0] = "张三"
#
# # 删除
# a.remove("张三")
# print(a)

a = ["刘家名","复议","宫浩凯","谢飞机","李老虎"]
'''
     随机点名程序和处罚程序：
        1.会随机抽一个人名。
            random.randint(0,5)  当成角标
        2.随机处罚0~200遍之内，并这个人移除名单
            index = random.randint(0,201)  
            a.remove()
'''
import random
print("--------------欢迎来到教务管理系统--------------------")

while True:  # 一直运行
    if a.__len__() == 0:
        break
    print("1：随机点名，2:随机处罚")
    num = input("请输入您的业务编号：")  # 输入业务编号
    if num == "1":  # 判断是1号业务
        index = random.randint(0, a.__len__()-1)  # 获取人的角标，  randint()
        print("恭喜你，",a[index],"!")  # 打印
    elif num == "2":  # 判断是否2号业务
        if a.__len__() >= 1:
            index1 = random.randint(0, a.__len__()-1)
#            print(a.__len__())
#            print(index1)
#            print(a)
            print(a[index1])
            a.remove(a[index1])
#            print(a)
            chose = random.randint(0, 201)  # 获取随机处罚遍数
            print("恭喜，您被处罚",chose,"遍！") # 打印处罚遍数
        else:
            print("此次随机处罚到此结束")
            break
    elif num == "q" or num == "Q":   # 退出
        print("下次欢迎光临！")
        break
    else:
        print("对不起，没有该业务，请重新输入！")

# print(a.__len__())
# print(a)



"""i = int(input("请输入打印星号的行数:"))
m = 0
while m <= i:
    j = 1
    while j <= m:
        print("*", end="")
        j = j + 1
    print()
    m = m + 1"""
