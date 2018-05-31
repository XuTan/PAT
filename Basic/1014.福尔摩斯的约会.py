"""
1014. 福尔摩斯的约会 (20)
时间限制
100 ms
内存限制
65536 kB
代码长度限制
8000 B
判题程序
Standard
作者
CHEN, Yue
大侦探福尔摩斯接到一张奇怪的字条：“我们约会吧！
3485djDkxh4hhGE 2984akDfkkkkggEdsb s&hgsfdk d&Hyscvnm”。大侦探很快就明白了，
字条上奇怪的乱码实际上就是约会的时间“星期四 14:04”，因为前面两字符串中第1对相同的大写英文字母（大小写有区分）
是第4个字母'D'，代表星期四；第2对相同的字符是'E'，那是第5个英文字母，代表一天里的第14个钟头
（于是一天的0点到23点由数字0到9、以及大写字母A到N表示）；后面两字符串第1对相同的英文字母's'出现在第4个位置（
从0开始计数）上，代表第4分钟。现给定两对字符串，请帮助福尔摩斯解码得到约会的时间。
输入格式：
输入在4行中分别给出4个非空、不包含空格、且长度不超过60的字符串。
输出格式：
在一行中输出约会的时间，格式为“DAY HH:MM”，其中“DAY”是某星期的3字符缩写，
即MON表示星期一，TUE表示星期二，WED表示星期三，THU表示星期四，FRI表示星期五，SAT表示星期六，SUN表示星期日。
题目输入保证每个测试存在唯一解。
输入样例：
3485djDkxh4hhGE
2984akDfkkkkggEdsb
s&hgsfdk
d&Hyscvnm
输出样例：
THU 14:04
"""
# -*-encoding:utf-8-*-
import string

if __name__ == "__main__":
    ips1 = input()
    ips2 = input()
    ips3 = input()
    ips4 = input()
    week, hour = -1, ""
    weeks = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    hours = "0123456789ABCDEFGHIJKLMN"
    for i in range(min(len(ips1), len(ips2))):
        if ips1[i] == ips2[i]:
            if week == -1 and hour == "" and ips1[i] in "ABCDEFG":
                week = "ABCDEFG".index(ips1[i])
            elif week != -1 and hour == "":
                if ips1[i] in '0123456789':
                    hour = ips1[i]
                elif ips1[i] in 'ABCDEFGHIJKLMN':
                    hour = ips1[i].upper()
    minute = 0
    for j in range(min(len(ips3), len(ips4))):
        if ips3[j] == ips4[j] and (ips3[j] in string.ascii_lowercase or ips3[j] in string.ascii_uppercase):
            minute = j
            break
    print(weeks[week], "%02d:%02d" % (hours.index(hour), minute))
