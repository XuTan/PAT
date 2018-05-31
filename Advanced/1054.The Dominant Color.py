"""
1054. The Dominant Color (20)
时间限制
100 ms
内存限制
65536 kB
代码长度限制
16000 B
判题程序
Standard
作者
CHEN, Yue
Behind the scenes in the computer's memory, color is always talked about as a series of 24 bits of information for each pixel. In an image, the color with the largest proportional area is called the dominant color. A strictly dominant color takes more than half of the total area. Now given an image of resolution M by N (for example, 800x600), you are supposed to point out the strictly dominant color.
Input Specification:
Each input file contains one test case. For each case, the first line contains 2 positive numbers: M (<=800) and N (<=600) which are the resolutions of the image. Then N lines follow, each contains M digital colors in the range [0, 224). It is guaranteed that the strictly dominant color exists for each input image. All the numbers in a line are separated by a space.
Output Specification:
For each test case, simply print the dominant color in a line.
Sample Input:
5 3
0 0 255 16777215 24
24 24 0 0 24
24 0 24 24 24
Sample Output:
24
"""
# -*-encoding:utf-8-*-
if __name__ == "__main__":
    MN = input().split(" ")
    M = int(MN[0])
    N = int(MN[-1])
    d = {}
    for i in range(N):
        nums = input().split(" ")
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
    print(sorted(d.items(), key=lambda x: x[1])[-1][0])
