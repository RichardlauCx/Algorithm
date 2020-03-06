# -*- coding: utf-8 -*-
#  @ Date   : 2019/5/20 13:14
#  @ Author : RichardLauCx
#  @ file   : Richard.py
#  @ IDE    : PyCharm


def func_sort_two():
    """
    排序两个数大小（升序）
    :param x:
    :param y:
    :return: x, y (x < y)
    """
    if x > y:
        temp = x
        x = y
        y = temp

    return x, y


def func_sort_three(x, y, z):
    """
    排序三个数的大小（升序）
    :param x:
    :param y:
    :param z:
    :return: x, y, z (x < y < y)
    """
    x, y = func_sort_two(x, y)
    y, z = func_sort_two(y, z)
    x, y = func_sort_two(x, y)

    return x, y, z


def func_sort_four(w, x, y, z):
    """
    排序四个数的大小（升序）
    :param w:
    :param x:
    :param y:
    :param z:
    :return: w, x, y, z (w < x < y < z)
    """
    w, x, y = func_sort_three(w, x, y)
    x, y, z = func_sort_three(x, y, z)
    w, x, y = func_sort_three(w, x, y)

    return w, x, y, z


def minority_sort(n, lists):
    if n == 2:
        print(func_sort_two(lists[0], lists[1]))  # 输出两个数排序

    elif n == 3:
        print(func_sort_three(lists[0], lists[1], lists[2]))  # 输出三个数排序

    elif n == 4:
        print(func_sort_four(lists[0], lists[1], lists[2], lists[3]))  # 输出四个数排序


def minority_sort_1(amount, tuples):
    n = amount
    function_name = "def func_sort_" + str(n) + "(n, tuple_s)" + ":"

    function_initialization = "tuples = tuple(tuple_s)"
    function_body_1 = "tuples[: n-1] = func_sort_" + str(n - 1) + "(tuples[: n-1])"
    function_body_2 = "tuples[n-1:] = func_sort_" + str(n - 1) + "(tuples[n-1:])"
    function_body_3 = "tuples[: n-1] = func_sort_" + str(n - 1) + "(tuples[: n-1])"

    function_return = "return tuples"

    with open("sort_minority.py", "a") as f:
        # Notice: 此自动生成方法需要建立在前一个方法（n-1）存在的基础上才能实现
        f.write(function_name + "\n")
        f.write("\t" + function_initialization + "\n")
        f.write("\t" + function_body_1 + "\n")
        f.write("\t" + function_body_2 + "\n")
        f.write("\t" + function_body_3 + "\n")
        f.write("\n\t" + function_return + "\n"*3)


def how_many():
    """
    此方法适合三个及以上使用，否则可以直接调用基础方法
    :return:
    """
    print("请问您要排序几个数字？")
    amount = int(input())
    print("请分别输入这些数字（以换行为Enter）：")
    lists = []  # 数字集合
    n = amount

    while amount:
        lists.append(int(input()))
        amount -= 1

    tuple_s = tuple(lists)
    for num in range(3, n+1):
        minority_sort_1(num, tuple_s)


if __name__ == '__main__':
    how_many()



