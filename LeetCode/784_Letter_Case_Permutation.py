# -*- coding: utf-8 -*-
"""
784. 字母大小写全排列

给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。


示例:
输入: S = "a1b2"
输出: ["a1b2", "a1B2", "A1b2", "A1B2"]

输入: S = "3z4"
输出: ["3z4", "3Z4"]

输入: S = "12345"
输出: ["12345"]


注意：

S 的长度不超过12。
S 仅由数字和字母组成。


"""


# my answer
class Solution:

    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if len(S) == 0:
            return [""]
        res = self.get_res(S, '')
        return res

    def get_res(self, S, s):
        """
        递归查找字符串，找出所有可能

        :param S: 原始字符串
        :param s: 链接字符串
        :return: 字符串集
        """
        index = len(s)
        if index == len(S) - 1:  # 判断是否是最后一个
            if S[index].isalpha():
                return [s + S[index].upper(), s + S[index].lower()]
            else:
                return [s + S[index]]
        else:
            if S[index].isalpha():
                return self.get_res(S, s + S[index].upper()) + self.get_res(S, s + S[index].lower())
            else:
                return self.get_res(S, s + S[index])


# better answer by other
class Solution2:
    def letterCasePermutation(self, S):
        """
        列表生成器精妙的使用，一个一个字符判断加入ans数组，字母就在ans列表中的每个字符串加上大小写两种情况
        （字符串数量翻倍），数字就在列表中每个字符串加上数字字符

        :type S: str
        :rtype: List[str]
        """
        ans = ['']
        for ch in S:
            if ch.isalpha():
                ans = [i + j for i in ans for j in [ch.upper(), ch.lower()]]
            else:
                ans = [i + ch for i in ans]
        return ans


# better answer by other
import itertools

class Solution3:
    def letterCasePermutation(self, S):
        """
        依旧是使用列表生成器，但先遍历S，把每个位置的可能列出，生成string列表，空间和时间花费稍微高一点

        :type S: str
        :rtype: List[str]
        """

        string = []
        for s in S:
            if s.isalpha():
                string.append([s.upper(), s.lower()])
            else:
                string.append(s)

        return [''.join(i) for i in itertools.product(*string)]
