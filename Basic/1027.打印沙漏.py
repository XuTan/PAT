"""
1027. 打印沙漏(20)
时间限制
200 ms
内存限制
65536 kB
代码长度限制
8000 B
判题程序
Standard
作者
CHEN, Yue
本题要求你写个程序把给定的符号打印成沙漏的形状。例如给定17个“*”，要求按下列格式打印

*****
 ***
  *
 ***
*****
所谓“沙漏形状”，是指每行输出奇数个符号；各行符号中心对齐；相邻两行符号数差2；符号数先从大到小顺序递减到1，
再从小到大顺序递增；首尾符号数相等。

给定任意N个符号，不一定能正好组成一个沙漏。要求打印出的沙漏能用掉尽可能多的符号。

输入格式：

输入在一行给出1个正整数N（<=1000）和一个符号，中间以空格分隔。

输出格式：

首先打印出由给定符号组成的最大的沙漏形状，最后在一行中输出剩下没用掉的符号数。

输入样例：
19 *
输出样例：
*****
 ***
  *
 ***
*****
2
"""

if __name__ == "__main__":
    n, pattern = input().split()
    cnt_l = [1]
    i = 3
    n = int(n)
    n -= 1
    while n - 2 * i >= 0:
        cnt_l.append(i)
        n -= i * 2
        i += 2
    length = len(cnt_l)
    for i in range(length - 1, -1, -1):
        for j in range((cnt_l[length - 1] - cnt_l[i]) // 2):
            print(" ", end="")
        for k in range(cnt_l[i]):
            print(pattern, end="")
        print("", end="\n")
    for i2 in range(1, length):
        for j2 in range((cnt_l[length - 1] - cnt_l[i2]) // 2):
            print(" ", end="")
        for k2 in range(cnt_l[i2]):
            print(pattern, end="")
        print("", end="\n")
    if n >= 0:
        print(n)
