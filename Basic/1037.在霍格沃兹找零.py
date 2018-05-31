"""
1037. 在霍格沃茨找零钱（20）
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
如果你是哈利·波特迷，你会知道魔法世界有它自己的货币系统 —— 就如海格告诉哈利的：
“十七个银西可(Sickle)兑一个加隆(Galleon)，二十九个纳特(Knut)兑一个西可，很容易。
”现在，给定哈利应付的价钱P和他实付的钱A，你的任务是写一个程序来计算他应该被找的零钱。
输入格式：
输入在1行中分别给出P和A，格式为“Galleon.Sickle.Knut”，其间用1个空格分隔。
这里Galleon是[0, 107]区间内的整数，Sickle是[0, 17)区间内的整数，Knut是[0, 29)区间内的整数。
输出格式：
在一行中用与输入同样的格式输出哈利应该被找的零钱。如果他没带够钱，那么输出的应该是负数。
输入样例1：
10.16.27 14.1.28
输出样例1：
3.2.1
输入样例2：
14.1.28 10.16.27
输出样例2：
-3.2.1
"""
# -*-encoding:utf-8-*-
if __name__ == "__main__":
    ips = input().split()
    p = [int(i) for i in ips[0].split(".")]
    a = [int(i) for i in ips[1].split(".")]
    result = a[0] * 17 * 29 + a[1] * 29 + a[2] - p[0] * 17 * 29 - p[1] * 29 - p[2]
    if result < 0:
        print('-', end="")
        result = -result
    galleon = result // (17 * 29)
    sickle = (result - galleon * 17 * 29) // 29
    knut = result - galleon * 17 * 29 - sickle * 29
    print("%d.%d.%d" % (galleon, sickle, knut))
