# -*- coding: utf-8 -*-
import re
import collections


# 题 1
# 检查密码规则合法性
# 考察基本编码能力和字符串处理
# 参考 python 文档的字符串库

# 给定一个字符串，用以下规则检查合法性
# 完全符合返回 True，否则返回 False
# 1，第一位是字母
# 2，只能包含字母、数字、下划线
# 3，只能字母或数字结尾
# 4，最小长度2
# 5，最大长度10


def valid_password(pwd):
    pwd_re = re.compile(r'^\w{1,9}[A-Za-z0-9]$')
    res = re.match(pwd_re, pwd)
    if res:
        return True
    else:
        return False


# 题 2
# 返回 100 内的素数列表
# 考察基本的循环和选择概念、列表的使用


def prime_numbers():

    res = []
    for x in range(2, 101):
        signal = True
        for y in res:
            if x % y == 0:
                signal = False
                break
        if signal:
            res.append(x)
    return res


# 题 3
# 给定一个只包含字母的字符串，返回单个字母出现的次数
# 考察字典的概念和使用
# 返回值为包含元组的列表，格式如下（对列表中元组的顺序不做要求）
# 参数 "hello"
# 返回值 [('h', 1), ('e', 1), ('l', 2), ('o', 1)]


def letter_count(str):
    temp_dict = {}
    for s in str:
        if temp_dict.get(s):
            temp_dict[s] += 1
        else:
            temp_dict[s] = 1
    return [(key, value) for key, value in temp_dict.items()]


# 题 4
# 给定一个英文句子（一个只有字母的字符串），将句中所有单词变为有且只有首字母大写的形式


def cap_string(str):
    first_capital = str[0]
    other_capital = str[1:]
    return first_capital.upper() + other_capital.lower()


# 题 5
# 写一个 Queue 类，它有两个方法，用法如下


class Queue:

    def __init__(self):
        self.queue = collections.deque()

    def enqueue(self, num):
        self.queue.append(num)

    def dequeue(self):
        res_num = self.queue.popleft()
        return res_num


if __name__ == '__main__':
    # 第一道题测试
    print(valid_password('sdf$'))                # False
    print(valid_password('sd'))                  # True
    print(valid_password('s'))                   # False
    print(valid_password('_1s1S1'))              # True
    print(valid_password('_1s1s1_'))             # False
    print(valid_password('_1s1s1asdasdsadads'))  # False

    # 第二道题测试
    print(prime_numbers())

    # 第三道题测试
    print(letter_count('sdnklasdjaslkjdklajd'))

    # 第四道题测试
    print(cap_string('sHIasdJKhioHIOasdHOH'))

    # 第五道题测试
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print(q.dequeue())  # 1
    print(q.dequeue())  # 2
    print(q.dequeue())  # 3
