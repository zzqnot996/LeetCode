
"""
有一群孩子和一堆饼干，每个孩子有一个饥饿度，每个饼干都有一个大小。每个孩子只能吃
一个饼干，且只有饼干的大小不小于孩子的饥饿度时，这个孩子才能吃饱。求解最多有多少孩子
可以吃饱。

输入输出样例
输入两个数组，分别代表孩子的饥饿度和饼干的大小。输出最多有多少孩子可以吃饱的数
量。
Input: [1,2], [1,2,3]
"""

def findContentChildren(children, cookies):
    children.sort()
    cookies.sort()
    child = 0
    cookie = 0
    while child < len(children) and cookie < len(cookies):
        if children[child] <= cookies[cookie]:
            child += 1
        cookie += 1
    return child



if __name__== "__main__":

    children = [1, 2]
    cookies = [1, 2, 3]
    result = findContentChildren(children, cookies)
    print(result)  # 输出满足的孩子数量

