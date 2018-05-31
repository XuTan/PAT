"""
1064. 朋友数(20)
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
如果两个整数各位数字的和是一样的，则被称为是“朋友数”，而那个公共的和就是它们的“朋友证号”。
例如123和51就是朋友数，因为1+2+3 = 5+1 = 6，而6就是它们的朋友证号。给定一些整数，
要求你统计一下它们中有多少个不同的朋友证号。注意：我们默认一个整数自己是自己的朋友。
输入格式：
输入第一行给出正整数N。随后一行给出N个正整数，数字间以空格分隔。题目保证所有数字小于104。
输出格式：
首先第一行输出给定数字中不同的朋友证号的个数；随后一行按递增顺序输出这些朋友证号，数字间隔一个空格，
且行末不得有多余空格。
输入样例：
8
123 899 51 998 27 33 36 12
输出样例：
4
3 6 9 26
"""
# -*-encoding:utf-8-*-
if __name__ == "__main__":
    n = int(input())
    ips = input().split()
    friends_num = []
    for i in range(n):
        num = sum([int(_) for _ in ips[i]])
        if num not in friends_num:
            friends_num.append(num)
        friends_num.sort()
    print(len(friends_num))
    for i in range(len(friends_num) - 1):
        print(friends_num[i], end=" ")
    print(friends_num[-1])
