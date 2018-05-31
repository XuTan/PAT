"""
1023. Have Fun with Numbers (20)
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
Notice that the number 123456789 is a 9-digit number consisting exactly the numbers from 1 to 9, with no duplication. Double it we will obtain 246913578, which happens to be another 9-digit number consisting exactly the numbers from 1 to 9, only in a different permutation. Check to see the result if we double it again!
Now you are suppose to check if there are more numbers with this property. That is, double a given number with k digits, you are to tell if the resulting number consists of only a permutation of the digits in the original number.
Input Specification:
Each input file contains one test case. Each case contains one positive integer with no more than 20 digits.
Output Specification:
For each test case, first print in a line "Yes" if doubling the input number gives a number that consists of only a permutation of the digits in the original number, or "No" if not. Then in the next line, print the doubled number.
Sample Input:
1234567899
Sample Output:
Yes
2469135798
"""
#-*-coding:utf-8-*-
if __name__ == "__main__":
    i = input()
    l1 = list(i)
    l2 = list(str(int(i) * 2))
    flag = True
    for item in l2:
        if item in l1:
            l1.remove(item)
        else:
            flag = False
            break
    if flag and l1 == []: #Note the second condition
        print("Yes")
    else:
        print("No")
    print(int(i) * 2)
