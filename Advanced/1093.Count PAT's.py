"""
1093. Count PAT's (25)
时间限制
120 ms
内存限制
65536 kB
代码长度限制
16000 B
判题程序
Standard
作者
CAO, Peng
The string APPAPT contains two PAT's as substrings. The first one is formed by the 2nd, the 4th, and the 6th characters, and the second one is formed by the 3rd, the 4th, and the 6th characters.
Now given any string, you are supposed to tell the number of PAT's contained in the string.
Input Specification:
Each input file contains one test case. For each case, there is only one line giving a string of no more than 105 characters containing only P, A, or T.
Output Specification:
For each test case, print in one line the number of PAT's contained in the string. Since the result may be a huge number, you only have to output the result moded by 1000000007.
Sample Input:
APPAPT
Sample Output:
2
"""
# -*-encoding:utf-8-*-
if __name__ == "__main__":
    s = input().strip()
    p, pa, pat = 0, 0, 0
    for sitem in s:
        if sitem == 'P':
            p += 1
        elif sitem == 'A':
            pa += p
        else:
            pat += pa
    print(pat % 1000000007)