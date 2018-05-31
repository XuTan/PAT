"""
1077. Kuchiguse (20)
时间限制
100 ms
内存限制
65536 kB
代码长度限制
16000 B
判题程序
Standard
作者
HOU, Qiming
The Japanese language is notorious for its sentence ending particles. Personal preference of such particles can be considered as a reflection of the speaker's personality. Such a preference is called "Kuchiguse" and is often exaggerated artistically in Anime and Manga. For example, the artificial sentence ending particle "nyan~" is often used as a stereotype for characters with a cat-like personality:
Itai nyan~ (It hurts, nyan~)
Ninjin wa iyada nyan~ (I hate carrots, nyan~)
Now given a few lines spoken by the same character, can you find her Kuchiguse?
Input Specification:
Each input file contains one test case. For each case, the first line is an integer N (2<=N<=100). Following are N file lines of 0~256 (inclusive) characters in length, each representing a character's spoken line. The spoken lines are case sensitive.
Output Specification:
For each test case, print in one line the kuchiguse of the character, i.e., the longest common suffix of all N lines. If there is no such suffix, write "nai".
Sample Input 1:
3
Itai nyan~
Ninjin wa iyadanyan~
uhhh nyan~
Sample Output 1:
nyan~
Sample Input 2:
3
Itai!
Ninjinnwaiyada T_T
T_T
Sample Output 2:
nai
"""
# -*-encoding:utf-8-*-
if __name__ == "__main__":
    N = int(input())
    L = []
    min = 333
    minIndex = -1
    for i in range(N):
        line = input()
        L.append(line[::-1])
        if len(line) <= min:
            min = len(line)
            minIndex = i
    failIndex = -1
    for i in range(min):
        chr = L[minIndex][i]
        for j in range(N):
            if L[j][i] != chr:
                failIndex = i
                break
        if failIndex >= 0:
            break
    if failIndex > 0:
        print(L[minIndex][:failIndex][::-1])
    elif failIndex == -1:
        print(L[minIndex][::-1])
    else:
        print("nai")
