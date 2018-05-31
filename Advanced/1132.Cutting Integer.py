"""
1132. Cut Integer (20)
时间限制
400 ms
内存限制
65536 kB
代码长度限制
16000 B
判题程序
Standard
作者
CHEN, Yue
Cutting an integer means to cut a K digits long integer Z into two integers of (K/2) digits long integers A and B. For example, after cutting Z = 167334, we have A = 167 and B = 334. It is interesting to see that Z can be devided by the product of A and B, as 167334 / (167 x 334) = 3. Given an integer Z, you are supposed to test if it is such an integer.
Input Specification:
Each input file contains one test case. For each case, the first line gives a positive integer N (<= 20). Then N lines follow, each gives an integer Z (10<=Z<=231). It is guaranteed that the number of digits of Z is an even number.
Output Specification:
For each case, print a single line "Yes" if it is such a number, or "No" if not.
Sample Input:
3
167334
2333
12345678
Sample Output:
Yes
No
No
"""


# -*-coding:utf-8-*-
def isYes(n):
    A = int(n[:int(len(n) / 2)])
    B = int(n[int(len(n) / 2):])
    if B == 0:  # note this condition
        return False
    else:
        nn = int(n)
        tmp = int(nn / (A * B))
        return nn == tmp * A * B


if __name__ == "__main__":
    N = int(input())
    for i in range(N):
        n = input()
        if isYes(n):
            print("Yes")
        else:
            print("No")
