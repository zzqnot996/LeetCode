'''
一群孩子站成一排，每一个孩子有自己的评分。现在需要给这些孩子发糖果，规则是如果一
个孩子的评分比自己身旁的一个孩子要高，那么这个孩子就必须得到比身旁孩子更多的糖果；所
有孩子至少要有一个糖果。求解最少需要多少个糖果。

输入输出样例
输入是一个数组，表示孩子的评分。输出是最少糖果的数量。
Input: [1,0,2]
'''


def candy(ratings):
    size = len(ratings)
    if size < 2:
        return size
    num = [1] * size
    
    for i in range(1, size):
        if ratings[i] > ratings[i-1]:
            num[i] = num[i-1] + 1
            
    for i in range(size - 1, 0, -1):
        if ratings[i] < ratings[i-1]:
            num[i-1] = max(num[i-1], num[i] + 1)
            
    return sum(num)  # 使用 sum 函数求和




if __name__== "__main__":
    # 示例用法
    ratings = [1, 0, 2]
    print(candy(ratings))  # 输出：5