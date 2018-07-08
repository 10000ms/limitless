# -*- coding: utf-8 -*-
"""
119. 杨辉三角 II

给定一个非负索引 k，其中 k ≤ 33，返回杨辉三角的第 k 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。


示例:

输入: 3
输出: [1,3,3,1]


进阶：

你可以优化你的算法到 O(k) 空间复杂度吗？
"""


# my answer
class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 建立顶点层情况
        res = [1]
        # 循环生成，获得指定层数的情况
        for x in range(rowIndex):
            # 这里使用列表生成器获得该层情况
            # 实际就是获得res+[0]和[0]+res对应位置的和
            res = ([sum(y) for y in zip(res+[0], [0]+res)])
        return res


# better answer by other
class Solution2:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 先建立该层数对应长度的list，里面全部都是1
        ans=[1 for i in range(rowIndex+1)]
        # 循环递推得到该层情况
        for i in range(1,rowIndex+1):
            for j in range(i-1,0,-1):
                ans[j]=ans[j-1]+ans[j]
        return ans
