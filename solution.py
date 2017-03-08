# python 2.7

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