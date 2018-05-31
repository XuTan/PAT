"""
1002. 写出这个数 (20)
时间限制
400 ms
内存限制
65536 kB
代码长度限制
8000 B
判题程序
Standard
作者
CHEN, Yue
读入一个自然数n，计算其各位数字之和，用汉语拼音写出和的每一位数字。
输入格式：每个测试输入包含1个测试用例，即给出自然数n的值。这里保证n小于10100。
输出格式：在一行内输出n的各位数字之和的每一位，拼音数字间有1 空格，但一行中最后一个拼音数字后没有空格。
输入样例：
1234567890987654321123456789
输出样例：
yi san wu
"""
# -*-encoding:utf-8-*-
if __name__ == "__main__":
    s = input()
    s_sum = sum([int(item) for item in list(s)])
    nums = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
    s_sum = list(str(s_sum))
    for i in range(len(s_sum) - 1):
        print(nums[int(s_sum[i])], end=" ")
    print(nums[int(s_sum[-1])])
