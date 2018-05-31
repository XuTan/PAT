""""
1043. 输出PATest(20)
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
给定一个长度不超过10000的、仅由英文字母构成的字符串。请将字符重新调整顺序，按“PATestPATest....”
这样的顺序输出，并忽略其它字符。当然，六种字符的个数不一定是一样多的，若某种字符已经输出完，
则余下的字符仍按PATest的顺序打印，直到所有字符都被输出。

输入格式：

输入在一行中给出一个长度不超过10000的、仅由英文字母构成的非空字符串。

输出格式：

在一行中按题目要求输出排序后的字符串。题目保证输出非空。

输入样例：
redlesPayBestPATTopTeePHPereatitAPPT
输出样例：
PATestPATestPTetPTePePee
"""
# -*-encoding:utf-8-*-
if __name__ == "__main__":
    ips = input()
    P, A, T, e, s, t = 0, 0, 0, 0, 0, 0
    for item in ips:
        if item == "P":
            P += 1
        elif item == "A":
            A += 1
        elif item == "T":
            T += 1
        elif item == "e":
            e += 1
        elif item == "s":
            s += 1
        elif item == "t":
            t += 1
    for i in range(len(ips)):
        if P > 0:
            print("P", end="")
            P -= 1
        if A > 0:
            print("A", end="")
            A -= 1
        if T > 0:
            print("T", end="")
            T -= 1
        if e > 0:
            print("e", end="")
            e -= 1
        if s > 0:
            print("s", end="")
            s -= 1
        if t > 0:
            print("t", end="")
            t -= 1
