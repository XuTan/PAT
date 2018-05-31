"""
1050. String Subtraction (20)
时间限制
100 ms
内存限制
65536 kB
代码长度限制
16000 B
判题程序
Standard
作者
CHEN, Yue
Given two strings S1 and S2, S = S1 - S2 is defined to be the remaining string after taking all the characters in S2 from S1. Your task is simply to calculate S1 - S2 for any given strings. However, it might not be that simple to do it fast.
Input Specification:
Each input file contains one test case. Each case consists of two lines which gives S1 and S2, respectively. The string lengths of both strings are no more than 104. It is guaranteed that all the characters are visible ASCII codes and white space, and a new line character signals the end of a string.
Output Specification:
For each test case, print S1 - S2 in one line.
Sample Input:
They are students.
aeiou
Sample Output:
Thy r stdnts.
"""
#-*-coding:utf-8-*-
if __name__=="__main__":
    s1=input()
    s2=input()
    for s in s1:
        if s not in s2:
            print(s, end="")

