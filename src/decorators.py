from time import time

def log(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                start_time = time()
                result = func(*args, **kwargs)
                end_time = time()
                if filename is None:
                    print(f'{func.__name__} ok, start func: {start_time}, end func: {end_time}')
                else:
                    with open(filename, 'w') as file:
                        file.write(f'{func.__name__} ok, start func: {start_time}, end func: {end_time}')
            except type(error).__name__:
                if filename is None:
                    print(f'{func.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}')
                else:
                    with open('mylog.txt', 'w') as file:
                        file.write(f'{func.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}')

        return wrapper
    return decorator
