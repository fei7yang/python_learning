from functools import wraps
def log_enter_and_exit(fn):
    @wraps(fn)
    def test(*args, **kwargs):
        print "-"*66
        ret = fn(*args, **kwargs)
        print "="*66
        return ret
    return test


@log_enter_and_exit
def test1():
    """xxxxxxxxxxxx"""
    print"hello"

print test1()

print"-"*200

from functools import wraps
import time
def log_time(fn):
    @wraps(fn)
    def test(*args, **kwargs):
        start=time.time()
        ret = fn(*args, **kwargs)
        end = time.time()
        print"** {} used {}s".format(fn.func_name,end-start)
        return ret
    return test


@log_time
def test():
    print "xxx"
    import time
    time.sleep(2)
test()

print"-"*200








from functools import wraps
def call(n=1):
    def real_call(fn):
        @wraps(fn)
        def test(*args, **kwargs):
            return[fn(*args,**kwargs) for x in range(n)]
        return test
    return real_call

@call(n=1)
def hi(name):
    print "xxx", name


hi("x")