# -*- coding: utf-8 -*-
"""
860. 柠檬水找零

在柠檬水摊上，每一杯柠檬水的售价为 5 美元。

顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。

每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。

注意，一开始你手头没有任何零钱。

如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

示例 1：

输入：[5,5,5,10,20]
输出：true
解释：
前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。

示例 2：

输入：[5,5,10]
输出：true
示例 3：

输入：[10,10]
输出：false
示例 4：

输入：[5,5,10,10,20]
输出：false
解释：
前 2 位顾客那里，我们按顺序收取 2 张 5 美元的钞票。
对于接下来的 2 位顾客，我们收取一张 10 美元的钞票，然后返还 5 美元。
对于最后一位顾客，我们无法退回 15 美元，因为我们现在只有两张 10 美元的钞票。
由于不是每位顾客都得到了正确的找零，所以答案是 false。


提示：

0 <= bills.length <= 10000
bills[i] 不是 5 就是 10 或是 20
"""


# my answer
class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # 获取长度
        length = len(bills)
        # 长度0直接返回
        if length == 0:
            return True
        need_return = {5: 0, 10: 0}
        # 倒序递推bills
        for x in range(length - 1, -1, -1):
            # 第一种情况，20元的时候
            if bills[x] == 20:
                need_return[10] += 1
                need_return[5] += 1
            # 第二种情况，10元的时候
            elif bills[x] == 10:
                if need_return[10] > 0:
                    need_return[10] -= 1
                need_return[5] += 1
            # 第三种情况，5元的时候
            elif bills[x] == 5:
                if need_return[5] > 0:
                    need_return[5] -= 1
                elif need_return[10] > 0:
                    need_return[5] += 1
                    need_return[10] -= 1
        # 列表生成器直接算出需要退回的钱
        if sum([x * y for x in need_return.keys() for y in need_return.values()]) == 0:
            return True
        else:
            return False


# better answer by other
class Solution2:
    """
    这个是正序递推版，本身速度更快，并且可以在中途就判断出某些False的情况直接返回，并且最后也不需要做额外
    的运算进行判断
    """
    def lemonadeChange(self, bills):
        wallet = dict({5: 0, 10: 0})
        for i in bills:
            # 第一种情况，5元的时候
            if i == 5:
                wallet[5] += 1
            # 第二种情况，10元的时候
            elif i == 10:
                if wallet[5] < 1:
                    return False
                else:
                    wallet[5] -= 1
                    wallet[10] += 1
            else:
                if wallet[10] > 0 and wallet[5] > 0:
                    wallet[5] -= 1
                    wallet[10] -= 1
                elif wallet[5] > 2:
                    wallet[5] -= 3
                else:
                    return False
        return True


# better answer by other
class Solution3:
    """
    这个是速度最快的版本，原理基本和上面的版本一样，只是储存钱值的dict：wallet变成a、b两个变量表示状态，速度更快
    """
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        a = b = 0
        for i in bills:
            if i == 5:
                a += 1
            elif i == 10:
                if a > 0:
                    a -= 1
                    b += 1
                else:
                    return False
            elif i == 20:
                if b > 0 and a > 0:
                    b -= 1
                    a -= 1
                elif b <= 0 and a > 2:
                    a -= 3
                else:
                    return False
        return True
