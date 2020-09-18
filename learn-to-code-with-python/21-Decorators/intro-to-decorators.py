# import functools



def uppercase(fn):

#     @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        fn(*args, **kwargs).upper()
    return wrapper
@uppercase

def concatenate(a, b):

    """Combines two strings together"""

    return a + b



print(concatenate("pyt", "hon"))