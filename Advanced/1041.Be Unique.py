"""
1041. Be Unique (20)
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
Being unique is so important to people on Mars that even their lottery is designed in a unique way. The rule of winning is simple: one bets on a number chosen from [1, 104]. The first one who bets on a unique number wins. For example, if there are 7 people betting on 5 31 5 88 67 88 17, then the second one who bets on 31 wins.
Input Specification:
Each input file contains one test case. Each case contains a line which begins with a positive integer N (<=105) and then followed by N bets. The numbers are separated by a space.
Output Specification:
For each test case, print the winning number in a line. If there is no winner, print "None" instead.
Sample Input 1:
7 5 31 5 88 67 88 17
Sample Output 1:
31
Sample Input 2:
5 888 666 666 888 888
Sample Output 2:
None
"""

# TIMEOUT
# def getResult(L):
#     countL = []
#     indexL = []
#     for item in L:
#         if item in countL:
#             indexL[countL.index(item)] += 1
#         else:
#             indexL.append(1)
#             countL.append(item)
#     flag = True
#     key = -1
#     for i in range(len(indexL)):
#         if indexL[i] == 1:
#             flag = False
#             key = countL[i]
#             break
#     if flag:
#         return None
#     else:
#         return key
#
#
# if __name__ == "__main__":
#     inputL = [int(i) for i in input().strip().split(" ")]
#     print(getResult(inputL[1:]))

# -*-encoding:utf-8-*-
if __name__ == "__main__":
    inputL = input().split(" ")
    countD = {}
    countL = []
    for item in inputL[1:]:
        if item in countD:
            countD[item] += 1
        else:
            countL.append(item)
            countD[item] = 1
    flag = True
    for v in countL:
        if countD[v] == 1:
            print(v)
            flag = False
            break
    if flag:
        print("None")
