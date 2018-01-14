splunk_code=raw_input("Please Enter Splunk Code: ")
mid_code=splunk_code.split("|")
trans_code='\n|'.join(mid_code)
print trans_code


print"########################"

a = "{0} is {1}".format("Who","Eric")
print a


from functools import wraps
import time
def validate_param_as_int(fn):
    @wraps(fn)
    def test(*args, **kwargs):
        for x in range args:
            if not isinstance(x, int):
                raise ValueError()
        for k,v in range kwargs.iteritems():
            if not isinstance(v, int):
                raise ValueError()
        ret = fn(*args, **kwargs)
        return ret


def validate_param(int,str,float)




    from functools import wraps
    import time
    def log_time(prefix="**"):
        def log_time(fn):
            @wraps(fn)
            def test(*args, **kwargs):
                start = time.time()
                ret = fn(*args, **kwargs)
                end = time.time()
                print prefix + "{} used {}s".format(fn.func_name, end - start)
                return ret

            return test

    @log_time(prefix="##")
    def test():
        print "xxx"
        import time
        time.sleep(2)

    test()