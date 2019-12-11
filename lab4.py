def wraps(str_func):
    def wrapper(wrapper_func):
        wrapper_func.__name__ = str_func.__name__
        wrapper_func.__doc__ = str_func.__doc__
        return wrapper_func
    return wrapper

def decorator(func):
    @wraps(func)
    def wrapper(wrapper_func):
        value = func(wrapper_func)
        return value
    return wrapper

@decorator
def get_string(string):
    """text"""
    return string

if __name__ == '__main__':
    print(get_string.__name__)
    print(get_string.__doc__)