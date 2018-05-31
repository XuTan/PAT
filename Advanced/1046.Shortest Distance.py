"""
1046. Shortest Distance (20)
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
The task is really simple: given N exits on a highway which forms a simple cycle, you are supposed to tell the shortest distance between any pair of exits.
Input Specification:
Each input file contains one test case. For each case, the first line contains an integer N (in [3, 105]), followed by N integer distances D1 D2 ... DN, where Di is the distance between the i-th and the (i+1)-st exits, and DN is between the N-th and the 1st exits. All the numbers in a line are separated by a space. The second line gives a positive integer M (<=104), with M lines follow, each contains a pair of exit numbers, provided that the exits are numbered from 1 to N. It is guaranteed that the total round trip distance is no more than 107.
Output Specification:
For each test case, print your results in M lines, each contains the shortest distance between the corresponding given pair of exits.
Sample Input:
5 1 2 4 14 9
3
1 3
2 5
4 1
Sample Output:
3
10
7
"""
# TIMEOUT
# -*-encoding:utf-8-*-
# if __name__ == "__main__":
#     Ns = input().split(" ")
#     M = int(input())
#     pwd = [int(i) for i in Ns[1:]]
#     case = []
#     for i in range(M):
#         ii = [int(num) for num in input().split(" ")]
#         case.append(ii)
#     for c in case:
#         low = min(c[0], c[1]) - 1
#         high = max(c[0], c[1]) - 1
#         p1 = sum(pwd[low:high])
#         p2 = sum(pwd[:low]) + sum(pwd[high:])
#         print(min(p1, p2))

# -*-encoding:utf-8-*-
if __name__ == "__main__":
    inputNL = [int(_) for _ in input().split(" ")]
    N = inputNL[0]
    NL = inputNL[1:]
    SUM = sum(NL)
    M = int(input())
    for i in range(M):
        C1, C2 = [int(_) for _ in input().split(" ")]
        if C2 < C1:
            tmp = C1
            C1 = C2
            C2 = tmp
        dis1 = sum(NL[C1 - 1:C2 - 1])
        dis2 = SUM - dis1
        print(min(dis1, dis2))
