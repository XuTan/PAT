"""
1009. Product of Polynomials (25)
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
This time, you are supposed to find A*B where A and B are two polynomials.
Input Specification:
Each input file contains one test case. Each case occupies 2 lines, and each line contains the information of a polynomial: K N1 aN1 N2 aN2 ... NK aNK, where K is the number of nonzero terms in the polynomial, Ni and aNi (i=1, 2, ..., K) are the exponents and coefficients, respectively. It is given that 1 <= K <= 10, 0 <= NK < ... < N2 < N1 <=1000.

Output Specification:
For each test case you should output the product of A and B in one line, with the same format as the input. Notice that there must be NO extra space at the end of each line. Please be accurate up to 1 decimal place.
Sample Input
2 1 2.4 0 3.2
2 2 1.5 1 0.5
Sample Output
3 3 3.6 2 6.0 1 1.6
"""
#-*-coding:utf-8-*-
if __name__ == "__main__":
    a = [0 for i in range(2001)]
    s1 = input().split(" ")
    s2 = input().split(" ")
    for i in range(int(s1[0])):
        for j in range(int(s2[0])):
            index= int(s1[i*2+1])+int(s2[j*2+1])
            value = float(s1[i*2+2])*float(s2[j*2+2])
            a[index] += value
    countNo=0
    for i in range(2001):
        if a[i]:
            countNo+= 1
    if countNo:
        print(countNo, end=" ")
    else:
        print(countNo)
    for i in range(2000, -1, -1):
        if a[i]:
            countNo -= 1
            if countNo:
                print(i, round(a[i], 1), end=" ")
            else:
                print(i, round(a[i], 1))