"""
1010. Radix (25)
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
Given a pair of positive integers, for example, 6 and 110, can this equation 6 = 110 be true? The answer is "yes", if 6 is a decimal number and 110 is a binary number.
Now for any pair of positive integers N1 and N2, your task is to find the radix of one number while that of the other is given.
Input Specification:
Each input file contains one test case. Each case occupies a line which contains 4 positive integers:
N1 N2 tag radix
Here N1 and N2 each has no more than 10 digits. A digit is less than its radix and is chosen from the set {0-9, a-z} where 0-9 represent the decimal numbers 0-9, and a-z represent the decimal numbers 10-35. The last number "radix" is the radix of N1 if "tag" is 1, or of N2 if "tag" is 2.
Output Specification:
For each test case, print in one line the radix of the other number so that the equation N1 = N2 is true. If the equation is impossible, print "Impossible". If the solution is not unique, output the smallest possible radix.
Sample Input 1:
6 110 1 10
Sample Output 1:
2
Sample Input 2:
1 ab 1 2
Sample Output 2:
Impossible
"""
# -*-encoding:utf-8-*-
import string

s = "0123456789" + string.ascii_lowercase


def getRadixV(n, radix):
    radix = int(radix)
    nl = list(str(n))[::-1]
    SUM = 0
    for i in range(len(nl)):
        SUM += s.index(nl[i]) * (radix ** i)
    return SUM


def main():
    N1, N2, tag, radix = input().split(" ")
    if N1 == N2 == '1':
        return 2
    if N1 == N2 and N1 != '1':
        return radix
    v1, v2 = 0, 0
    if tag == '1':
        v1 = getRadixV(N1, radix)
    else:
        v1 = getRadixV(N2, radix)
        N2 = N1
    # TIMEOUT
    # RADIX = 0
    # minRadix = s.index(max(list(str(N2)))) + 1
    # for i in range(minRadix, v1 + 2):
    #     v2 = getRadixV(N2, i)
    #     if v2 > v1:
    #         break
    #     elif v2 == v1:
    #         RADIX = i
    #         break
    # if RADIX:
    #     return RADIX
    # else:
    #     return "Impossible"
    RADIX = 0
    minRadix = s.index(max(list(str(N2)))) + 1
    maxRadix = v1 + 2  # note this line +2
    while minRadix < maxRadix:
        tmpRadix = int((minRadix + maxRadix) / 2)
        v2 = getRadixV(N2, tmpRadix)
        if v2 > v1:
            maxRadix = tmpRadix
        elif v2 < v1:
            minRadix = tmpRadix
        else:
            RADIX = tmpRadix
            break
    if RADIX:
        return RADIX
    else:
        return "Impossible"


if __name__ == "__main__":
    rs = main()
    print(rs)
