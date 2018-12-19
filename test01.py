#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author : TIXhjq
# @Time   : 2018/12/19 14:51

import Dijkstra

#example

graph={
    'A':[['B',6],['C',3]],
    'B':[['C',2],['D',5]],
    'C':[['B',2],['D',3],['E',4]],
    'D':[['B',5],['C',3],['E',2],['F',3]],
    'E':[['C',4],['D',2],['F',5]],
    'F':[['D',3],['E',5]]
}

dsa=Dijkstra.Dijkstra(graph,'A')
table=dsa.transform()
print("point'A' to other point min path:\n{}".format(table))


