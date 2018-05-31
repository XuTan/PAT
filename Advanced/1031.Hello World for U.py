"""
1031. Hello World for U (20)
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
Given any string of N (>=5) characters, you are asked to form the characters into the shape of U. For example, "helloworld" can be printed as:
h  d
e  l
l  r
lowo
That is, the characters must be printed in the original order, starting top-down from the left vertical line with n1 characters, then left to right along the bottom line with n2 characters, and finally bottom-up along the vertical line with n3 characters. And more, we would like U to be as squared as possible -- that is, it must be satisfied that n1 = n3 = max { k| k <= n2 for all 3 <= n2 <= N } with n1 + n2 + n3 - 2 = N.

Input Specification:
Each input file contains one test case. Each case contains one string with no less than 5 and no more than 80 characters in a line. The string contains no white space.
Output Specification:
For each test case, print the input string in the shape of U as specified in the description.
Sample Input:
helloworld!
Sample Output:
h   !
e   d
l   l
lowor
"""

# -*-encoding:utf-8-*-
if __name__ == "__main__":
    s = input()
    sl = len(s)
    n = int((sl - 1) / 3)  # note this line (sl-1)
    space = ""
    for j in range(sl - 2 * n - 2):
        space += " "
    for i in range(n):
        print(s[i] + space + s[sl - i - 1])
    print(s[n:sl - n])
