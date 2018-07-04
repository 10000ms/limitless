# -*- coding: utf-8 -*-
"""
设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。


示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.
"""


# my answer
class MinStack:
    """
    多维护一个栈，记录对应位置的最小值。
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
        self.enum = 0

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.enum or self.min_stack[-1] > x:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])
        self.stack.append(x)
        self.enum += 1

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        self.min_stack.pop()
        self.enum -= 1

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# better answer by other
class MinStack2:
    """
    只维护一个栈，stack = [[x,min]],两个list合一，x是栈元素值，min是该栈位的最小值
    """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        min = self.getMin()
        if min is not None:
            curMin = min if x > min else x
        else:
            curMin = x
        return self.stack.append((x, curMin))

    def pop(self):
        """
        :rtype: void
        """
        return self.stack.pop()[0]

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1][0]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
            return self.stack[-1][1]
        return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
