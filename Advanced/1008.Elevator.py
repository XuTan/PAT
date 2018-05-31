"""
1008. Elevator (20)
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
The highest building in our city has only one elevator. A request list is made up with N positive numbers. The numbers denote at which floors the elevator will stop, in specified order. It costs 6 seconds to move the elevator up one floor, and 4 seconds to move down one floor. The elevator will stay for 5 seconds at each stop.
For a given request list, you are to compute the total time spent to fulfill the requests on the list. The elevator is on the 0th floor at the beginning and does not have to return to the ground floor when the requests are fulfilled.
Input Specification:
Each input file contains one test case. Each case contains a positive integer N, followed by N positive numbers. All the numbers in the input are less than 100.
Output Specification:
For each test case, print the total time on a single line.
Sample Input:
3 2 3 1
Sample Output:
41
"""
if __name__ == "__main__":
    i = [int(i) for i in input().split(" ")]
    sum = 0
    l = i[1::]
    l.insert(0, 0)
    for i in range(i[0]):
        length = l[i + 1] - l[i]
        if length > 0:
            sum += length * 6
        elif length < 0:
            sum += abs(length) * 4
        sum += 5
    print(sum)
