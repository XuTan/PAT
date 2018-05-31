"""
1002. A+B for Polynomials (25)
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
This time, you are supposed to find A+B where A and B are two polynomials.
Input
Each input file contains one test case. Each case occupies 2 lines, and each line contains the information of a polynomial: K N1 aN1 N2 aN2 ... NK aNK, where K is the number of nonzero terms in the polynomial, Ni and aNi (i=1, 2, ..., K) are the exponents and coefficients, respectively. It is given that 1 <= K <= 10，0 <= NK < ... < N2 < N1 <=1000.

Output
For each test case you should output the sum of A and B in one line, with the same format as the input. Notice that there must be NO extra space at the end of each line. Please be accurate to 1 decimal place.
Sample Input
2 1 2.4 0 3.2
2 2 1.5 1 0.5
Sample Output
3 2 1.5 1 2.9 0 3.2
"""
if __name__ == "__main__":
    a = [0 for i in range(1001)]
    s1 = input().split(" ")
    s2 = input().split(" ")
    for i in range(int(s1[0])):
        a[int(s1[i * 2 + 1])] += float(s1[i * 2 + 2])
    for i in range(int(s2[0])):
        a[int(s2[i * 2 + 1])] += float(s2[i * 2 + 2])
    countNo = 0
    for i in range(1001):
        if a[i]:
            countNo += 1
    if countNo:
        print(countNo, end=" ")
    else:
        print(countNo)
    for i in range(1000, -1, -1):
        if a[i]:
            countNo -= 1
            if countNo > 0:
                print(i, round(a[i], 1), end=" ")
            else:
                print(i, round(a[i], 1))
