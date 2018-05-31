"""
1022. D进制的A+B (20)
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
输入两个非负10进制整数A和B(<=230-1)，输出A+B的D (1 < D <= 10)进制数。
输入格式：
输入在一行中依次给出3个整数A、B和D。
输出格式：
输出A+B的D进制数。
输入样例：
123 456 8
输出样例：
1103
"""
# -*-encoding:utf-8-*-
if __name__ == "__main__":
    A, B, D = [int(i) for i in input().split()]
    C = A + B
    if C == 0:
        print(0)
    else:
        numsl = []
        while C:
            numsl.append(str(C % D))
            C = C // D
        print("".join(i for i in numsl[::-1]))
