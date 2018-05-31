"""
1116. Come on! Let's C (20)
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
"Let's C" is a popular and fun programming contest hosted by the College of Computer Science and Technology, Zhejiang University. Since the idea of the contest is for fun, the award rules are funny as the following:
0. The Champion will receive a "Mystery Award" (such as a BIG collection of students' research papers...).
1. Those who ranked as a prime number will receive the best award -- the Minions (小黄人)!
2. Everyone else will receive chocolates.
Given the final ranklist and a sequence of contestant ID's, you are supposed to tell the corresponding awards.
Input Specification:
Each input file contains one test case. For each case, the first line gives a positive integer N (<=10000), the total number of contestants. Then N lines of the ranklist follow, each in order gives a contestant's ID (a 4-digit number). After the ranklist, there is a positive integer K followed by K query ID's.
Output Specification:
For each query, print in a line "ID: award" where the award is "Mystery Award", or "Minion", or "Chocolate". If the ID is not in the ranklist, print "Are you kidding?" instead. If the ID has been checked before, print "ID: Checked".
Sample Input:
6
1111
6666
8888
1234
5555
0001
6
8888
0001
1111
2222
8888
2222
Sample Output:
8888: Minion
0001: Chocolate
1111: Mystery Award
2222: Are you kidding?
8888: Checked
2222: Are you kidding?
"""

# -*-encoding:utf-8-*-

import math


def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def main():
    N = int(input())
    NL = []
    for i in range(N):
        NL.append(input())
    K = int(input())
    KL = []
    for i in range(K):
        KL.append(input())
    CHECKED = []
    for i in range(K):
        if KL[i] in NL:
            if KL[i] not in CHECKED:
                rank = NL.index(KL[i]) + 1
                if rank == 1:
                    print("%s: Mystery Award" % KL[i])
                elif isPrime(rank):
                    print("%s: Minion" % KL[i])
                else:
                    print("%s: Chocolate" % KL[i])
                CHECKED.append(KL[i])
            else:
                print("%s: Checked" % KL[i])
        else:
            print("%s: Are you kidding?" % KL[i])


if __name__ == "__main__":
    main()
