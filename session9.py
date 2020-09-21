# Import all Libraries
from datetime import datetime
from functools import wraps
from functools import singledispatch
from collections import abc
import numbers
import html
#Question1

def odd_sec_func(sec):
    '''
    This function runs only during the odd time
    Here we are building a small function which only prints and returns the mathematical calculation
    as the output
    '''
    from functools import wraps
    def outer(fn):
        if not ( sec % 2):
            @wraps(fn)
            def inner(*args, **kwargs):
                print(f'{fn.__name__} was called at {sec+1} th second ')
                return fn(*args, **kwargs)
            return inner
        else:
            print('This function only runs on odd seconds - Run it again and see if it works')
    return outer

@odd_sec_func(datetime.now().second)
def add(*args):
    '''
    implements the decorator
    '''
    return sum(args)
#Question-2

def log_func(fn):
    '''
    function to demonstrate logging feature
    it logs
    1. The id of the function object called
    2. The doc string of the function
    3. All the local variables used in the function
    '''
    from functools import wraps
    from datetime import datetime, timezone
    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        print(f'{fn.__name__} was called at {run_dt}')
        print(f'the id of function object called is {hex(id(fn))}')
        print(f'the docstring of the function {fn.__name__} is {fn.__doc__}')
        print(f'the parameter and local varaibles used are {fn.__code__.co_varnames}')
        return fn(*args, **kwargs)
    return inner
@log_func
def add_func(*args):
    ''' returns the sum of the given sequence'''
    return sum(args)

#Question-3
def authenticate_func():
    '''
    This function is created to authenticate the users based on the provided password
    '''
    password = ''
    def inner():
        nonlocal password
        if password == '':
            password = 'niharkanungotsai'
        return password
    return inner
auth_password = authenticate_func()

def auth_factory_func(fn1,user_password):
    '''
    This function takes the password that has been set with the user defined password and
    checks if the user is authorized to perform the operation
    '''
    def authenticate_func(fn):
        from functools import wraps
        cnt = 0
        if user_password == fn1():
            @wraps(fn)
            def inner(*args, **kwargs):
                nonlocal cnt
                cnt += 1
                print(f'{fn.__name__} was called {cnt} times')
                return fn(*args, **kwargs)
            return inner
        else:
            print('You seems to be a scamster!!')
    return authenticate_func

@auth_factory_func(auth_password,'nihark')
def add_not_work(a, b):
    return a + b
@auth_factory_func(auth_password,'nihark')
def mult_not_work(a, b):
    return a * b
@auth_factory_func(auth_password,'niharkanungotsai')
def add_work(a, b):
    return a + b
@auth_factory_func(auth_password,'niharkanungotsai')
def mult_work(a, b):
    return a * b


#Question-4
def timed_func(reps):
    '''
    This function shows the time elapsed in performing the function
    '''
    def timed(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0

            for i in range(reps):
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)
            avg_run_time = total_elapsed / reps
            print('Avg Run time: {0:.6f}s ({1} reps)'.format(avg_run_time, reps))
            return result
        return inner
    return timed

@timed_func(10)
def add_times(*args):
    return sum(args)

#Question-5

def prev_access_func(privilege):
    '''
    This function Provides privilege access has 4 parameters, based on privileges
    high, medium, low, no gives access to all 4, 3, 2 or 1 params
    '''

    a,b,c,d = 'high','medium','low','no'
    def dec(fn):
        registry = {1: lambda x=a:fn(x),2:lambda x=a,y=b:fn(x,y),3: lambda x=a,y=b,z=c:fn(x,y,z),4:lambda x=a,y=b,w=c,z=d:fn(x,y,w,z)}
        def inner():
            nonlocal privilege
            if privilege not in set(range(1,5)):
                raise ValueError("Priority should be provided in the range of 1-4")
            fn =  registry.get(privilege,None)
            return fn()
        return inner
    return dec
@prev_access_func(1)
def fn1(*args):
    print(f'can access only {len(args)} parameters and they are {args}')

@prev_access_func(2)
def fn2(*args):
    print(f'can access only {len(args)} parameters and they are {args}')

@prev_access_func(3)
def fn3(*args):
    print(f'can access only {len(args)} parameters and they are {args}')
@prev_access_func(4)
def fn4(*args):
    print(f'can access only {len(args)} parameters and they are {args}')

@prev_access_func(5)
def fn5(*args):
    print(f'can access only {len(args)} parameters and they are {args}')
@prev_access_func(15)
def fn15(*args):
    print(f'can access only {len(args)} parameters and they are {args}')

#Question 6

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)

@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<p>{0}</p>'.format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0x{0:x})</pre>'.format(n)

@htmlize.register(tuple)
@htmlize.register(abc.MutableSequence)
def _(seq):
    inner = '</li>\n<li>'.join(htmlize(item) for item in seq)
    return '<ul>\n<li>' + inner + '</li>\n</ul>'
