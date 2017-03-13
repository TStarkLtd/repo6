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
        #print('t>0',arr[mid])
        z = arr[mid] + i
        tz = tx - sum( z//k for k in d_arr)
        tz_1 = tx - sum( (z-1)//k for k in d_arr)
        tz1 = tx - sum( (z+1)//k for k in d_arr)
        if tz == 0 or (tz > 0 and tz1 < 0):
            return z
        elif tz_1 > 0 and tz < 0:
            return z-1
        t = tz
        i +=1
        #print(t,z)
    if t < 0:
        #print('t<0',arr[mid])
        z = arr[mid] - i
        tz = tx - sum( z//k for k in d_arr)
        tz_1 = tx - sum( (z-1)//k for k in d_arr)
        tz1 = tx - sum( (z+1)//k for k in d_arr)
        if tz == 0 or (tz > 0 and tz1 < 0):
            return z
        elif tz < 0 and tz_1 > 0:
            return z-1
        t = tz
        i -=1
        #print(t,z)


def process_input(input_str):
    try:
        input_arr = [int(i) for i in input_str.split()]
        X = input_arr[0]
        d = input_arr[1:]
        d_len = len(d)
        d_span = max(d) - min(d)
        C = sum( float(1)/k for k in d)
        range_low = int(X / C)
        X_range_low = sum( range_low//k for k in d)
        #print( X, X_range_low, X_range_low - X, d_len )
        if X == X_range_low:
            print('> %s' % range_low)
            return range_low
        elif X_range_low > X:
            X_temp = X_range_low - X
            range_low -= int(X_temp/C)
        range_high = range_low + int(d_len/C) + 1 
        #print(range_low - d_span,range_high,X,sum( (range_low - d_span)//k for k in d)) 
        res = binary_search(range(range_low - d_span,range_high),d,X)
        print('> %s' % res)
    except ValueError as err:
        print(err.args)
        raise

#print(sys.argv)
arg_len = len(sys.argv)
if arg_len != 2:
    #print('usage: python solution.py <data file name e.g. proc_disk_usage.data>')
    raise ValueError('usage: python solution.py <data file name e.g. proc_disk_usage.data>')


with open(sys.argv[1], "r") as ins:
    for x in ins:
        process_input(x)