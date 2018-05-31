"""
1001. A+B Format (20)
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
Calculate a + b and output the sum in standard format -- that is, the digits must be separated into groups of three by commas (unless there are less than four digits).
Input
Each input file contains one test case. Each case contains a pair of integers a and b where -1000000 <= a, b <= 1000000. The numbers are separated by a space.

Output
For each test case, you should output the sum of a and b in one line. The sum must be written in the standard format.
Sample Input
-1000000 9
Sample Output
-999,991
"""
if __name__ == "__main__":
    s = input().split(" ")
    a = int(s[0])
    b = int(s[1])
    c = str(a + b)
    countIndex = 0
    for i in range(len(c)):
        print(c[i], end="")
        if c[i] == '-':
            continue
        if (i + 1) % 3 == len(c) % 3 and i < len(c) - 1:
            print(",", end="")
