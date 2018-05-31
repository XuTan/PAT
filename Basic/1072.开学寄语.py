"""
1072. 开学寄语(20)
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
下图是上海某校的新学期开学寄语：天将降大任于斯人也，必先删其微博，卸其QQ，封其电脑，夺其手机，收其ipad，
断其wifi，使其百无聊赖，然后，净面、理发、整衣，然后思过、读书、锻炼、明智、开悟、精进。而后必成大器也！

本题要求你写个程序帮助这所学校的老师检查所有学生的物品，以助其成大器。
输入格式：
输入第一行给出两个正整数N（<= 1000）和M（<= 6），分别是学生人数和需要被查缴的物品种类数。
第二行给出M个需要被查缴的物品编号，其中编号为4位数字。随后N行，每行给出一位学生的姓名缩写（由1-4个大写英文字母组成）、
个人物品数量K（0 <= K <= 10）、以及K个物品的编号。
输出格式：
顺次检查每个学生携带的物品，如果有需要被查缴的物品存在，则按以下格式输出该生的信息和其需要被查缴的物品的信息
（注意行末不得有多余空格）：
姓名缩写: 物品编号1 物品编号2 ……
最后一行输出存在问题的学生的总人数和被查缴物品的总数。
输入样例：
4 2
2333 6666
CYLL 3 1234 2345 3456
U 4 9966 6666 8888 6666
GG 2 2333 7777
JJ 3 0012 6666 2333
输出样例：
U: 6666 6666
GG: 2333
JJ: 6666 2333
3 5
"""
# -*-encoding:utf-8-*-
if __name__ == "__main__":
    N, M = [int(i) for i in input().split()]
    Ms = input().split()
    print_l = []
    for i in range(N):
        ips = input().split()
        ll = [ips[0] + ":"]
        for item in ips[1:]:
            if item in Ms:
                ll.append(item)
        print_l.append(ll)
    stu_count, good_count = 0, 0
    for i in range(N):
        if len(print_l[i]) > 1:
            stu_count += 1
            good_count += len(print_l[i]) - 1
            for j in range(len(print_l[i]) - 1):
                print(print_l[i][j], end=" ")
            print(print_l[i][-1])
    print(stu_count, good_count)
