"""
1003. Emergency (25)
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
As an emergency rescue team leader of a city, you are given a special map of your country. The map shows several scattered cities connected by some roads. Amount of rescue teams in each city and the length of each road between any pair of cities are marked on the map. When there is an emergency call to you from some other city, your job is to lead your men to the place as quickly as possible, and at the mean time, call up as many hands on the way as possible.

Input
Each input file contains one test case. For each test case, the first line contains 4 positive integers: N (<= 500) - the number of cities (and the cities are numbered from 0 to N-1), M - the number of roads, C1 and C2 - the cities that you are currently in and that you must save, respectively. The next line contains N integers, where the i-th integer is the number of rescue teams in the i-th city. Then M lines follow, each describes a road with three integers c1, c2 and L, which are the pair of cities connected by a road and the length of that road, respectively. It is guaranteed that there exists at least one path from C1 to C2.
Output
For each test case, print in one line two numbers: the number of different shortest paths between C1 and C2, and the maximum amount of rescue teams you can possibly gather.
All the numbers in a line must be separated by exactly one space, and there is no extra space allowed at the end of a line.
Sample Input
5 6 0 2
1 2 1 5 3
0 1 1
0 2 2
0 3 1
1 2 1
2 4 1
3 4 1
Sample Output
2 4
"""
import sys
import queue


class City(object):

    def __init__(self, index, rescue, distance=sys.maxsize):
        self.index = index
        self.rescue = rescue
        self.distance = distance
        self.prev = []

    def __lt__(self, other):
        return self.distance < other.distance


def main():
    city_num, roads, src, des = [int(_) for _ in input().split()]
    city_rescue = [int(_) for _ in input().split()]

    cities = [City(i, city_rescue[i]) for i in range(city_num)]
    cities[src].distance = 0

    city_map = list()
    for i in range(city_num):
        city_map.append([sys.maxsize if i != j else 0 for j in range(city_num)])

    for i in range(roads):
        c1, c2, weight = [int(_) for _ in input().split()]
        city_map[c1][c2] = weight
        city_map[c2][c1] = weight

    mark = [False for _ in range(city_num)]
    pq = queue.PriorityQueue()
    pq.put(cities[src])
    for i in range(city_num):
        if not pq.empty():
            city = pq.get()
            mark[city.index] = True

            for c2, weight in enumerate(city_map[city.index]):
                if weight != sys.maxsize and not mark[c2]:
                    new_weight = city.distance + weight

                    if new_weight == cities[c2].distance:
                        cities[c2].prev.append(city.index)
                        continue

                    if new_weight < cities[c2].distance:
                        cities[c2].distance = new_weight
                        cities[c2].prev = [city.index]
                        if cities[c2].index not in [q.index for q in pq.queue]:
                            pq.put(cities[c2])
        else:
            for i in range(city_num):
                if not mark[i]:
                    pq.put(cities[i])
                    break

    road_num = 0
    rescue_num = 0

    def recurisive(city_obj, res_num):
        nonlocal road_num, rescue_num

        if city_obj.index == src:
            road_num += 1
            if res_num + city_obj.rescue > rescue_num:
                rescue_num = res_num + city_obj.rescue
        elif city_obj.prev:
            for c_index in city_obj.prev:
                recurisive(cities[c_index], res_num + city_obj.rescue)

    recurisive(cities[des], 0)
    print('{} {}'.format(road_num, rescue_num), end='')


if __name__ == '__main__':
    main()
