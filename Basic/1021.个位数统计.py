"""
1021. 个位数统计 (15)
时间限制
100 ms
内存限制
65536 kB
代码长度限制
8000 B
判题程序
Standard
作者
CHEN, Yue
给定一个k位整数N = dk-1*10k-1 + ... + d1*101 + d0 (0<=di<=9, i=0,...,k-1, dk-1>0)，
请编写程序统计每种不同的个位数字出现的次数。例如：给定N = 100311，则有2个0，3个1，和1个3。
输入格式：
每个输入包含1个测试用例，即一个不超过1000位的正整数N。
输出格式：
对N中每一种不同的个位数字，以D:M的格式在一行中输出该位数字D及其在N中出现的次数M。要求按D的升序输出。
输入样例：
100311
输出样例：
0:2
1:3
3:1
"""
# -*-encoding:utf-8-*-
if __name__ == "__main__":
    ns = input()
    nums_count = [0 for i in range(10)]
    for s in ns:
        nums_count[int(s)] += 1
    for i in range(10):
        if nums_count[i]:
            print("%d:%d" % (i, nums_count[i]))
