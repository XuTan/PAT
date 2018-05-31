"""
1036. Boys vs Girls (25)
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
This time you are asked to tell the difference between the lowest grade of all the male students and the highest grade of all the female students.
Input Specification:
Each input file contains one test case. Each case contains a positive integer N, followed by N lines of student information. Each line contains a student's name, gender, ID and grade, separated by a space, where name and ID are strings of no more than 10 characters with no space, gender is either F (female) or M (male), and grade is an integer between 0 and 100. It is guaranteed that all the grades are distinct.

Output Specification:
For each test case, output in 3 lines. The first line gives the name and ID of the female student with the highest grade, and the second line gives that of the male student with the lowest grade. The third line gives the difference gradeF-gradeM. If one such kind of student is missing, output "Absent" in the corresponding line, and output "NA" in the third line instead.
Sample Input 1:
3
Joe M Math990112 89
Mike M CS991301 100
Mary F EE990830 95
Sample Output 1:
Mary EE990830
Joe Math990112
6
Sample Input 2:
1
Jean M AA980920 60
Sample Output 2:
Absent
Jean AA980920
NA
"""
if __name__ == "__main__":
    FName = ""
    FID = ""
    FGrade = -1
    MName = ""
    MID = ""
    MGrade = 101
    n = int(input())
    for i in range(n):
        i = input().split(" ")
        if i[1] == "F":
            if int(i[3]) > FGrade:
                FName = i[0]
                FID = i[2]
                FGrade = int(i[3])
        elif i[1] == "M":
            if int(i[3]) < MGrade:
                MName = i[0]
                MID = i[2]
                MGrade = int(i[3])
    printcount = 0
    if FGrade!=-1:
        print(FName, FID)
        printcount += 1
    else:
        print("Absent")
    if MGrade!=101:
        print(MName, MID)
        printcount += 1
    else:
        print("Absent")
    if printcount == 2:
        print(FGrade - MGrade)
    else:
        print("NA")
