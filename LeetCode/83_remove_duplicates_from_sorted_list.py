# -*- coding: utf-8 -*-
"""
83. 删除排序链表中的重复元素

给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# my answer
class Solution:

    # 储存链表元素值
    val_set = set()

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 判断链表是否存在和长度是否为1,为真则直接返回head
        if head and head.next:
            # 创建链表下一个元素指针
            next_node = head.next
            # 创建链表当前元素指针
            this_node = head
            # 遍历检测链表
            while next_node:
                # 链表元素是否被出现过，真则跳过该节点
                if this_node.val in self.val_set:
                    last_node.next = next_node
                else:
                    self.val_set.add(this_node.val)
                    # 创建或移动链表上一个元素指针
                    last_node = this_node
                # 移动当前元素指针和下一个元素指针
                this_node = next_node
                next_node = this_node.next
            # 检测链表最后一个元素，真则跳过该节点
            if this_node.val in self.val_set:
                last_node.next = None
        return head
