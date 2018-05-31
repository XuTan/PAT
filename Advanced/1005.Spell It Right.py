"""
1005. Spell It Right (20)
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
Given a non-negative integer N, your task is to compute the sum of all the digits of N, and output every digit of the sum in English.
Input Specification:
Each input file contains one test case. Each case occupies one line which contains an N (<= 10100).
Output Specification:
For each test case, output in one line the digits of the sum in English words. There must be one space between two consecutive words, but no extra space at the end of a line.
Sample Input:
12345
Sample Output:
one five
"""
#-*-coding:utf-8-*-
if __name__ == "__main__":
    num = str(sum(int(i) for i in list(input())))
    str = [
        'zero',
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine',
        'ten']
    for i in range(len(num)):
        if i < len(num) - 1:
            print(str[int(num[i])], end=" ")
        else:
            print(str[int(num[i])])
