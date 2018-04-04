# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。
# 我们以自定义一个求绝对值的my_abs函数为例：
def my_abs(x):
    if x >= 0:
        return x;
        ec
    else:
        return -x;


print(my_abs(-99))


# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句，用来还没想好写什么代码，姑且放着留着以后去做。
def nop():
    pass;


# 当参数类型不对时，python不会报错，只会在执行的时候报错。。数据类型检查可以用内置函数isinstance()实现,数据类型检查如下：
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x;
    else:
        return -x;


# 返回多个值
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)


# 原来返回值是一个tuple！
# 但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，
# 按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。

# 练习
#
# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#
# ax2 + bx + c = 0
#
# 的两个解。
#
# 提示：计算平方根可以调用math.sqrt()函数：
# ax2 + bx + c = 0
def quadratic(a, b, c):
    delta = b * b - 4 * a * c;
    temp2 = -b / (2 * a)
    if delta > 0:
        temp1 = math.sqrt(delta) / (2 * a)
        return temp2 + temp1, temp2 - temp1;
    elif delta == 0:
        temp1 = math.sqrt(delta) / (2 * a)
        return temp2
    elif delta < 0:
        return "无解呀。"


print(quadratic(1, 8, 3))
