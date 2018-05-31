"""
1065. A+B and C (64bit) (20)
时间限制
100 ms
内存限制
65536 kB
代码长度限制
16000 B
判题程序
Standard
作者
HOU, Qiming
Given three integers A, B and C in [-263, 263], you are supposed to tell whether A+B > C.
Input Specification:
The first line of the input gives the positive number of test cases, T (<=10). Then T test cases follow, each consists of a single line containing three integers A, B and C, separated by single spaces.
Output Specification:
For each test case, output in one line "Case #X: true" if A+B>C, or "Case #X: false" otherwise, where X is the case number (starting from 1).
Sample Input:
3
1 2 3
2 3 4
9223372036854775807 -9223372036854775808 0
Sample Output:
Case #1: false
Case #2: true
Case #3: false
"""
# -*-encoding:utf-8-*-
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        ABC = [int(num) for num in input().split(" ")]
        flag = ""
        if ABC[0] + ABC[1] > ABC[2]:
            flag = "true"
        else:
            flag = "false"
        print("Case #%d:" % (i + 1), flag)
