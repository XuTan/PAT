"""
1083. List Grades (25)
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
Given a list of N student records with name, ID and grade. You are supposed to sort the records with respect to the grade in non-increasing order, and output those student records of which the grades are in a given interval.
Input Specification:
Each input file contains one test case. Each case is given in the following format:
N
name[1] ID[1] grade[1]
name[2] ID[2] grade[2]
... ...
name[N] ID[N] grade[N]
grade1 grade2
where name[i] and ID[i] are strings of no more than 10 characters with no space, grade[i] is an integer in [0, 100], grade1 and grade2 are the boundaries of the grade's interval. It is guaranteed that all the grades are distinct.
Output Specification:
For each test case you should output the student records of which the grades are in the given interval [grade1, grade2] and are in non-increasing order. Each student record occupies a line with the student's name and ID, separated by one space. If there is no student's grade in that interval, output "NONE" instead.
Sample Input 1:
4
Tom CS000001 59
Joe Math990112 89
Mike CS991301 100
Mary EE990830 95
60 100
Sample Output 1:
Mike CS991301
Mary EE990830
Joe Math990112
Sample Input 2:
2
Jean AA980920 60
Ann CS01 80
90 95
Sample Output 2:
NONE
"""
#-*-coding:utf-8-*-
if __name__ == "__main__":
    N = int(input())
    d = {}
    for i in range(N):
        inputL = input().split(" ")
        d[inputL[0] + " " + inputL[1]] = int(inputL[2])
    i = input().split(" ")
    low = int(i[0])
    high = int(i[1])
    sorted_l = sorted(d.items(), key=lambda x: x[1], reverse=True)
    countNum = 0
    for i in range(N):
        if low <= sorted_l[i][1] <= high:
            print(sorted_l[i][0])
            countNum += 1
    if countNum == 0:
        print("NONE")
