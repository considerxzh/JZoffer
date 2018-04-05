'''
输入两个整数序列，第一个序列表示栈的压入顺序，
请判断第二个序列是否为该栈的弹出顺序。假设压
入栈的所有数字均不相等。例如序列1,2,3,4,5是
某栈的压入顺序，序列4，5,3,2,1是该压栈序列对
应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）

#out of time

def IsPopOrder(pushV, popV):
# write code here
    if not pushV:
        return False
    stack = []
    stack.append(pushV[0])
    pushV.pop(0)
    for i in range(len(popV)):
        while stack[-1] != popV[i]:
            if pushV:
                stack.append(pushV[0])
                pushV.pop(0)
        if stack[-1]==popV[i]:
            stack.pop(-1)
        else:
            return False
    if stack:
        return True
    else:
        return False
'''
#others
def IsPopOrder( pushV, popV):
    # write code here
    if not pushV or len(pushV) != len(popV):
        return False
    stack = []
    for i in pushV:
        stack.append(i)
        while len(stack) and stack[-1] == popV[0]:
            stack.pop()
            popV.pop(0)
    if len(stack):
        return False
    return True

def main():
    pushV = [1, 2, 3, 4, 5]
    popV = [4, 5, 3, 2, 1]
    IsPopOrder(pushV, popV)
main()