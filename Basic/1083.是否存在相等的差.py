"""
1083. 是否存在相等的差 (20)
时间限制
400 ms
内存限制
65536 kB
代码长度限制
8000 B
判题程序
Standard
作者
CHEN, Yue
给定 N 张卡片，正面分别写上 1、2、……、N，然后全部翻面，洗牌，在背面分别写上 1、2、……、N。
将每张牌的正反两面数字相减（大减小），得到 N 个非负差值，其中是否存在相等的差？
输入格式：
输入第一行给出一个正整数 N（2 <= N <= 10000），随后一行给出 1 到 N 的一个洗牌后的排列，
第 i 个数表示正面写了 i 的那张卡片背面的数字。
输出格式：
按照“差值 重复次数”的格式从大到小输出重复的差值及其重复的次数，每行输出一个结果。
输入样例：
8
3 5 8 6 2 1 4 7
输出样例：
5 2
3 3
2 2
"""
# -*-encoding:utf-8-*-
if __name__ == "__main__":
    n = int(input())
    nums = [int(i) for i in input().split()]
    counts = [0 for i in range(10010)]
    for i in range(len(nums)):
        counts[abs((i + 1) - nums[i])] += 1
    for i in range(10001, -1, -1):
        if counts[i] >= 2:
            print(i, counts[i])
