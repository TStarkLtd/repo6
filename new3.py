# python 2.7

def gcd_Stein(a, b):    
    if a < b:
        a, b = b, a
    if (0 == b):
        return a
    if a % 2 == 0 and b % 2 == 0:
        return 2 * gcd_Stein(a/2, b/2)
    if a % 2 == 0:
        return gcd_Stein(a / 2, b)
    if b % 2 == 0:
        return gcd_Stein(a, b / 2)
    
    return gcd_Stein((a + b) / 2, (a - b) / 2) 

def gcd(a, b):
    if a < b:
        a, b = b, a
    r = a % b
    if r:
        return gcd(b, r)
    else:
        return b
#print gcd(13, 6)

def lcm(a, b):
    return a * b / gcd(a, b)
#print lcm(12, 6)

def lcmAll(seq):
    return reduce(lcm, seq)

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
            return min( [ y for y in [arr[mid],binary_search(arr[:mid+1],d_arr,tx)] if y!=-1] )
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


def x_range(start,stop):
    i = start
    while i < stop:
        yield i
        i += 1

def process_input(input_str):
    try:
        input_arr = [int(i) for i in input_str.split()]
        X = input_arr[0]
        d = input_arr[1:]
        d_min = min(d)
        sum_all = sum( float(1)/k for k in d)
        z = X / sum_all
        if z == int(z):
            print('time taken %s' % int(z))
            return z
        p = int(z)
        #print(p)
        X -= sum( p//k for k in d )
		
        step = 1
        while X > 0:
            for y in x_range(p*step, p*(step+1)):
                print('.'),
                for di in d:
                    X -= (1 if y % di == 0 else 0)
                    if X == 0:
                        print('time taken %s' % y)
                        return y
            step += 1
    except ValueError as err:
        print(err.args)
        raise


print('please input config')

_input = raw_input()

print('-'*20)

#print(_input)

_inputArr = _input.split(r'\n')

#print(_inputArr)

for x in _inputArr:
    process_input(x)