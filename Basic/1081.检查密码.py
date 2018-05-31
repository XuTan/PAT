"""
1081. 检查密码 (15)
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
本题要求你帮助某网站的用户注册模块写一个密码合法性检查的小功能。
该网站要求用户设置的密码必须由不少于6个字符组成，并且只能有英文字母、数字和小数点"."，还必须既有字母也有数字。
输入格式：
输入第一行给出一个正整数 N（<=100），随后 N 行，每行给出一个用户设置的密码，为不超过80个字符的非空字符串，
以回车结束。
输出格式：
对每个用户的密码，在一行中输出系统反馈信息，分以下5种：
如果密码合法，输出“Your password is wan mei.”；
如果密码太短，不论合法与否，都输出“Your password is tai duan le.”；
如果密码长度合法，但存在不合法字符，则输出“Your password is tai luan le.”；
如果密码长度合法，但只有字母没有数字，则输出“Your password needs shu zi.”；
如果密码长度合法，但只有数字没有字母，则输出“Your password needs zi mu.”。
输入样例：
5
123s
zheshi.wodepw
1234.5678
WanMei23333
pass*word.6
输出样例：
Your password is tai duan le.
Your password needs shu zi.
Your password needs zi mu.
Your password is wan mei.
Your password is tai luan le.
"""
# -*-encoding:utf-8-*-
if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        ips = input()
        if len(ips) < 6:
            print("Your password is tai duan le.")
        else:
            invalid, hasnum, hasstr = False, False, False
            for s in ips:
                if s != '.' and s.isalpha() is not True and s.isalnum() is not True:
                    invalid = True
                elif s.isalpha():
                    hasstr = True
                elif s.isdigit():
                    hasnum = True
            if invalid:
                print("Your password is tai luan le.")
            elif hasnum is not True:
                print("Your password needs shu zi.")
            elif hasstr is not True:
                print("Your password needs zi mu.")
            else:
                print("Your password is wan mei.")
