"""
1027. Colors in Mars (20)
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
People in Mars represent the colors in their computers in a similar way as the Earth people. That is, a color is represented by a 6-digit number, where the first 2 digits are for Red, the middle 2 digits for Green, and the last 2 digits for Blue. The only difference is that they use radix 13 (0-9 and A-C) instead of 16. Now given a color in three decimal numbers (each between 0 and 168), you are supposed to output their Mars RGB values.
Input
Each input file contains one test case which occupies a line containing the three decimal color values.

Output
For each test case you should output the Mars RGB value in the following format: first output "#", then followed by a 6-digit number where all the English characters must be upper-cased. If a single color is only 1-digit long, you must print a "0" to the left.
Sample Input
15 43 71
Sample Output
#123456
"""
#-*-coding:utf-8-*-
if __name__ == "__main__":
    l = [int(i) for i in input().split(" ")]
    print("#", end="")
    s = "0123456789ABC"
    for i in range(len(l)):
        print(s[int(l[i] / 13)], end="")
        print(s[int(l[i] % 13)], end="")
