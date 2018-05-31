"""
1144. The Missing Number (20)
时间限制
150 ms
内存限制
65536 kB
代码长度限制
16000 B
判题程序
Standard
作者
CHEN, Yue
Given N integers, you are supposed to find the smallest positive integer that is NOT in the given list.
Input Specification:
Each input file contains one test case. For each case, the first line gives a positive integer N (<= 105). Then N integers are given in the next line, separated by spaces. All the numbers are in the range of int.
Output Specification:
Print in a line the smallest positive integer that is missing from the input list.
Sample Input:
10
5 -25 9 6 1 3 4 2 5 17
Sample Output:
7
"""


# -*-encoding:utf-8-*-
def getResult(nums):
    L = [0 for i in range(100009)]
    L[0] = 1
    for item in nums:
        if int(item) > 0:
            L[int(item)] = 1
    for i in range(100009):
        if L[i] == 0:
            return i
    return 0


if __name__ == '__main__':
    N = int(input())
    nums = input().split()
    print(getResult(nums))
