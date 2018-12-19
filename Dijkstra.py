#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Author : TIXhjq
# @Time   : 2018/12/19 11:48


#******************************------------------------*******************************

'''
tiltle:
    User Dijkstra find min path.
Abstract:
    find point to point min len in graph.
version:
    alpha 1.0.
'''

class Dijkstra(object):
    def __init__(self,graph,init_point):
        '''
        param
            graph:
                need judge min len(init point to point) graph.
            init_pint:
                start point.
        '''

        self.graph=graph
        self.init_point=init_point


        self.init_table={}
        self.find_out_point=[]

        self.max_len=0
        self.point_num=0
        self.now_point_values=0
        self.now_point=init_point

#--------------------------------------------------------------------------------------
    #protected
    def Point_num(self):
        self.point_num=len(self.init_table[self.init_point])

    def graph_to_table(self):
        V_point = []
        for point in self.graph:
            V_point.append([point, 0])
        self.init_table={self.init_point:V_point}

    def get_now_point_len(self):
        for point,len in self.init_table[self.init_point]:
            if(point==self.now_point):
                self.now_point_values=len

    def max_graph_len(self):
        max=0
        for point in self.graph:
            for point,len in self.graph:
                if(len>max):
                    max=len
        self.max_len=max

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>----------------------------------------

    def judege_point(self,flag_point):
        '''
        param
            flag_point:
                need judge userd(y/n) point.
        return:
            Flag:
                1:n
                0:y
        '''
        Flag=1
        for point in self.find_out_point:
            if(flag_point==point):
                Flag=0
                return Flag
        return Flag

    def find_flag_point(self,flag_len):
        '''
        param
            flag_len:
                len of need find point.
        return:
            need point.
        #same
        '''
        for flag_point,len in self.graph[self.now_point]:
            if(len==flag_len):
                return flag_point

    def table_update(self,flag_point,flag_len):
        '''
        param
            flag_point:
                need update point.
            flag_len:
                need update len.
        '''
        seg=self.init_table[self.init_point]
        self.get_now_point_len()
        loc=0
        i=0
        for point,len in seg:
            if(point==flag_point):
                loc=self.now_point_values+flag_len
                if(seg[i][1]!=0):
                    if(loc<len):
                        seg[i]=[flag_point,loc]
                else:
                    seg[i]=[flag_point,loc]
            i+=1

    def get_next_point(self):
        min = 6
        for next_point,next_len in self.graph[self.now_point]:
            if(self.judege_point(next_point)):
                if(next_len<min):
                    min=next_len
                self.table_update(next_point,next_len)

        #update user point
        self.find_out_point.append(self.now_point)

        #update next point
        self.now_point=self.find_flag_point(min)

    def find_min_len(self):
        while (len(self.find_out_point) < self.point_num):
            self.get_next_point()


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#public
    def transform(self):

        self.graph_to_table()
        self.Point_num()
        self.find_min_len()
        return self.init_table

#******************************------------------------*******************************
