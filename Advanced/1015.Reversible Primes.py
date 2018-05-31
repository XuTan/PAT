"""
1015. Reversible Primes (20)
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
A reversible prime in any number system is a prime whose "reverse" in that number system is also a prime. For example in the decimal system 73 is a reversible prime because its reverse 37 is also a prime.
Now given any two positive integers N (< 105) and D (1 < D <= 10), you are supposed to tell if N is a reversible prime with radix D.
Input Specification:
The input file consists of several test cases. Each case occupies a line which contains two integers N and D. The input is finished by a negative N.
Output Specification:
For each test case, print in one line "Yes" if N is a reversible prime with radix D, or "No" if not.
Sample Input:
73 10
23 2
23 10
-2
Sample Output:
Yes
Yes
No
"""
#-*-coding:utf-8-*-
import math


def isPrime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def getReverse(number, radix):
    a = []
    while number:
        a.append(number % radix)
        number = int(number / radix)
    newNum = 0
    a.reverse()
    for i in range(len(a)):
        newNum += a[i] * radix**i
    return newNum


if __name__ == "__main__":
    while True:
        i = input().split(" ")
        if len(i) < 2:
            break
        else:
            n = int(i[0])
            radix = int(i[-1])
            if isPrime(n):
                if isPrime(getReverse(n, radix)):
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
            continue
