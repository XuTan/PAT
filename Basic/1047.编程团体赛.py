"""
1047. 编程团体赛(20)
时间限制
400 ms
内存限制
65536 kB
代码长度限制
8000 B
判题程序
Standard
作者
CHEN, Yue
编程团体赛的规则为：每个参赛队由若干队员组成；所有队员独立比赛；参赛队的成绩为所有队员的成绩和；成绩最高的队获胜。
现给定所有队员的比赛成绩，请你编写程序找出冠军队。
输入格式：
输入第一行给出一个正整数N（<=10000），即所有参赛队员总数。随后N行，每行给出一位队员的成绩，
格式为：“队伍编号-队员编号 成绩”，其中“队伍编号”为1到1000的正整数，“队员编号”为1到10的正整数，
“成绩”为0到100的整数。
输出格式：
在一行中输出冠军队的编号和总成绩，其间以一个空格分隔。注意：题目保证冠军队是唯一的。
输入样例：
6
3-10 99
11-5 87
102-1 0
102-3 100
11-9 89
3-2 61
输出样例：
11 176
"""
# -*-encoding:utf-8-*-
if __name__ == "__main__":
    n = int(input())
    count_d = {}
    for i in range(n):
        ips = input().split()
        dui = ips[0].split('-')[0]
        if dui in count_d:
            count_d[dui] += int(ips[1])
        else:
            count_d[dui] = int(ips[1])
    sorted_count_d = sorted(count_d.items(), key=lambda x: x[1])
    print(sorted_count_d[-1][0],sorted_count_d[-1][1])
