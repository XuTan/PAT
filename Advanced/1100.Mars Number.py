"""
1100. Mars Numbers (20)
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
People on Mars count their numbers with base 13:
Zero on Earth is called "tret" on Mars.
The numbers 1 to 12 on Earch is called "jan, feb, mar, apr, may, jun, jly, aug, sep, oct, nov, dec" on Mars, respectively.
For the next higher digit, Mars people name the 12 numbers as "tam, hel, maa, huh, tou, kes, hei, elo, syy, lok, mer, jou", respectively.
For examples, the number 29 on Earth is called "hel mar" on Mars; and "elo nov" on Mars corresponds to 115 on Earth. In order to help communication between people from these two planets, you are supposed to write a program for mutual translation between Earth and Mars number systems.
Input Specification:
Each input file contains one test case. For each case, the first line contains a positive integer N (< 100). Then N lines follow, each contains a number in [0, 169), given either in the form of an Earth number, or that of Mars.
Output Specification:
For each number, print in a line the corresponding number in the other language.
Sample Input:
4
29
5
elo nov
tam
Sample Output:
hel mar
may
115
13
"""
low = ['tret', 'jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jly', 'aug', 'sep', 'oct', 'nov', 'dec']
high = ['tam', 'hel', 'maa', 'huh', 'tou', 'kes', 'hei', 'elo', 'syy', 'lok', 'mer', 'jou']


def convert2Mars(s):
    n = int(s)
    returnL = []
    hi = int(n / 13)
    lo = n % 13
    if hi:
        returnL.append(high[hi - 1])
    if n == 0 or lo != 0:
        returnL.append(low[lo])
    return returnL


def convert2Earch(s):
    sL = s.split(" ")
    num = 0
    if len(sL) == 1:
        if sL[0] in low:
            num = low.index(sL[0])
        elif sL[0] in high:
            num = 13 * (high.index(sL[0]) + 1)
    elif len(sL) == 2:
        num += low.index(sL[-1])
        num += 13 * (high.index(sL[0]) + 1)
    return num


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        s = input()
        if s.isdigit():
            print(" ".join(item for item in convert2Mars(s)))
        else:
            print(convert2Earch(s))
