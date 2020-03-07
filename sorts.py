# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLauCx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def func_sort_2(tuples):
    """
    排序两个数大小（升序）
    :param x:
    :param y:
    :return: x, y (x < y)
    """
    x = tuples[0]
    y = tuples[1]

    if x > y:
        temp = x
        x = y
        y = temp

    return x, y


def minority_sort_1(n):
    function_name = "\tdef func_sort_" + str(n) + "(self)" + ":"
    function_initialization = "\tn = self.n\n" + "\t\ttuples = self.tuples"
    function_body_1 = "\ttuples[: n-1] = self.func_sort_" + str(n - 1) + "(self.tuples[: n-1])"
    function_body_2 = "\ttuples[n-1:] = self.func_sort_" + str(n - 1) + "(self.tuples[n-1:])"
    function_body_3 = "\ttuples[: n-1] = self.func_sort_" + str(n - 1) + "(self.tuples[: n-1])"

    function_return = "\treturn tuples"

    with open("sort_minority.py", "a") as f:
        # Notice: 此自动生成方法需要建立在前一个方法（n-1）存在的基础上才能实现
        f.write(function_name + "\n")
        f.write("\t" + function_initialization + "\n")
        f.write("\t" + function_body_1 + "\n")
        f.write("\t" + function_body_2 + "\n")
        f.write("\t" + function_body_3 + "\n")
        f.write("\n\t" + function_return + "\n"*2)


def how_many():
    """
    此方法适合三个及以上使用，否则可以直接调用基础方法（自动生成排序函数）
    :return:
    """
    while True:
        print("请问您要排序几个数字？")
        amount = int(input())
        if amount < 2:
            print("您此次输入的数量没有可比性，请您重新输入：")
            continue

        else:
            break

    print("请分别输入这些数字（以换行为Enter）：")
    lists = []  # 数字集合
    n = amount

    while amount:
        lists.append(int(input()))
        amount -= 1

    tuple_s = tuple(lists)

    if n == 2:
        func_sort_2(tuple_s)

    else:
        func_class = "class Sort_Minority:\n" \
                     + "\tdef __init__(self, n, tuples):\n" \
                     + "\t\tself.n = n\n" \
                     + "\t\tself.tuples = tuples\n\n"

        func_sort_two = "\tdef func_sort_2(self):\n" \
                        + "\t\tx = self.tuples[0]\n" \
                        + "\t\ty = self.tuples[1]\n" \
                        + "\t\tif x > y:\n" \
                        + "\t\t\ttemp = x\n" \
                        + "\t\t\tx = y\n" \
                        + "\t\t\ty = temp\n" \
                        + "\t\treturn x, y" + "\n"*2

        with open("sort_minority.py", "a") as f:
            f.write(func_class)
            f.write(func_sort_two)

        for num in range(3, n+1):
            minority_sort_1(num)

        instantiation_object = "\tn = 0\n" + "\ttuple_s = tuple()\n" \
                               + "\topt = Sort_Minority(n, tuple_s)\n"
        func_start = "if __name__ == '__main__':\n" + instantiation_object + "\topt.func_sort_" + str(n) + "()\n"
        with open("sort_minority.py", "a") as f:
            f.write(func_start)


if __name__ == '__main__':
    how_many()




