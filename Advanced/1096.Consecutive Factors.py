"""
1096. Consecutive Factors (20)
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
Among all the factors of a positive integer N, there may exist several consecutive numbers. For example, 630 can be factored as 3*5*6*7, where 5, 6, and 7 are the three consecutive numbers. Now given any positive N, you are supposed to find the maximum number of consecutive factors, and list the smallest sequence of the consecutive factors.
Input Specification:
Each input file contains one test case, which gives the integer N (1<N<231).
Output Specification:
For each test case, print in the first line the maximum number of consecutive factors. Then in the second line, print the smallest sequence of the consecutive factors in the format "factor[1]*factor[2]*...*factor[k]", where the factors are listed in increasing order, and 1 is NOT included.
Sample Input:
630
Sample Output:
3
5*6*7
"""
# -*-encoding:utf-8-*-
import math

if __name__ == "__main__":
    N = int(input())
    MAX = int(math.sqrt(N))
    range = 0
    first, end = -1, -1
    i, j = 2, 2
    while i <= MAX:
        tmp = 1
        j = i
        while j <= MAX:
            tmp *= j
            if tmp > N:
                break
            if N % tmp == 0 and j - i + 1 > range:
                range = j - i + 1
                first, end = i, j
            j += 1
        i += 1
    if range:
        print(range)
        print(first, end="")
        k = first + 1
        while k <= end:
            print("*%d" % k, end="")
            k += 1
    else:
        print(1)
        print(N)
