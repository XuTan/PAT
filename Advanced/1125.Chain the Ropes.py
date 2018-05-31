"""
1125. Chain the Ropes (25)
时间限制
200 ms
内存限制
65536 kB
代码长度限制
16000 B
判题程序
Standard
作者
CHEN, Yue
Given some segments of rope, you are supposed to chain them into one rope. Each time you may only fold two segments into loops and chain them into one piece, as shown by the figure. The resulting chain will be treated as another segment of rope and can be folded again. After each chaining, the lengths of the original two segments will be halved.

Your job is to make the longest possible rope out of N given segments.
Input Specification:
Each input file contains one test case. For each case, the first line gives a positive integer N (2 <= N <= 104). Then N positive integer lengths of the segments are given in the next line, separated by spaces. All the integers are no more than 104.
Output Specification:
For each case, print in a line the length of the longest possible rope that can be made by the given segments. The result must be rounded to the nearest integer that is no greater than the maximum length.
Sample Input:
8
10 15 12 3 4 13 1 15
Sample Output:
14
"""
# -*-encoding:utf-8-*-
if __name__ == "__main__":
    N = int(input())
    L = [int(i) for i in input().split(" ")]
    L.sort()
    ropeLength = L[0]
    for i in range(1, N):
        ropeLength = (ropeLength + L[i]) / 2
    print(int(ropeLength))
