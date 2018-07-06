# -*- coding: utf-8 -*-
"""
349. 两个数组的交集

给定两个数组，写一个函数来计算它们的交集。

例子:

 给定 num1= [1, 2, 2, 1], nums2 = [2, 2], 返回 [2].

提示:

每个在结果中的元素必定是唯一的。
我们可以不考虑输出结果的顺序。

"""


# my answer
class Solution(object):

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 先判断是否有传入
        if len(nums1) == 0 or len(nums2) == 0:
            return []
        # 利用Python的set交集可以直接获得结果
        return list(set(nums1) & set(nums2))
