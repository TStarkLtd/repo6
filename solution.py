#!/usr/bin/python
# -*- coding: utf-8 -*-
# python 2.7

import sys


def binary_search(arr,d_arr,tx):
    low = 0
    high = len(arr)-1
    t = mid = 0
    while low < high:
        mid = (low+high)/2
        t = tx - sum( arr[mid]//k for k in d_arr)
        #print(low,high,arr[mid],t)
        if t > 0:
            low = mid + 1

        elif t < 0:
            high = mid - 1

        else:
            #print(arr[mid])
            return min( [ y for y in [arr[mid],binary_search(arr[:mid+1],d_arr,tx)] ] )
    i = 1 
    if t > 0:
        z = arr[mid] + i
        tz = tx - sum( z//k for k in d_arr)
        if tz == 0:
            return z
        t = tz
        i +=1
        #print(t,z)
    if t < 0:
        z = arr[mid] - i
        tz = tx - sum( z//k for k in d_arr)
        if tz == 0:
            return z
        t = tz
        i -=1
        #print(t,z)
    return arr[mid]


def process_input(input_str):
    try:
        input_arr = [int(i) for i in input_str.split()]
        X = X0 = input_arr[0]
        d = input_arr[1:]
        d_len = len(d)
        C = sum( float(1)/k for k in d)
        z = X / C
        range_low = int(z)
        if z == range_low:
            print('> %s' % range_low)
            return range_low
        
        X -= sum( range_low//k for k in d )
        range_high = range_low + int(d_len/C) + 1
        #print(range_low,range_high,X0)
        res = binary_search(range(range_low,range_high),d,X0)
        print('> %s' % res)
    except ValueError as err:
        print(err.args)
        raise

#print(sys.argv)
arg_len = len(sys.argv)
if arg_len != 2:
    #print('usage: python solution.py <data file name e.g. proc_disk_usage.data>')
    raise ValueError('usage: python solution.py <data file name e.g. proc_disk_usage.data>')

#_input = raw_input()
#print(_input)
#_inputArr = _input.split(r'\n')
#print(_inputArr)

with open(sys.argv[1], "r") as ins:
    for x in ins:
        process_input(x)