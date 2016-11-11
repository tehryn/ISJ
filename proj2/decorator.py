#!/usr/bin/env python3
except TypeError as e:
   import inspect
   got_args = int(re.search("\d+.*(\d+)",str(e)).groups()[0])
   print "missing args:",inspect.getargspec(f).args[got_args:]

def arg_decorator(fn):
   def func(*args,**kwargs):
       try: 
           return fn(*args,**kwargs)
       except TypeError:
           arg_spec = inspect.getargspec(fn)
           missing_named = [a for a in arg_spec.args if a not in kwargs]
           if arg_spec.defaults:
                    missing_args = missing_named[len(args): -len(arg_spec.defaults) ]
           else:
                    missing_args = missing_named[len(args):]
           print ("Missing:",missing_args)
   return func

@arg_decorator
def fn1(x,y,z):                      
      pass

def fn2(x,y):
    pass

arged_fn2 = arg_decorator(fn2)

fn1(5,y=2)
arged_fn2(x=1)
