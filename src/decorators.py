from time import time


def log(filename=None):
    "Декоратор, который логирует начало и конец выполнения функции, а также ее результаты или возникшие ошибки"

    def decorator(func):
        def wrapper(*args, **kwargs):
            if filename is None:
                try:
                    start_time = time()
                    result = func(*args, **kwargs)
                    end_time = time()
                    print(f"{func.__name__} ok, start func: {start_time}, end func: {end_time}")
                    return result
                except Exception as error:
                    print(f"{func.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}")
            else:
                try:
                    start_time = time()
                    result = func(*args, **kwargs)
                    end_time = time()
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} ok, start func: {start_time}, end func: {end_time}\n")
                        return result
                except Exception as error:
                    with open(filename, "a") as file:
                        file.write(f"{func.__name__} error: {type(error).__name__}. Inputs: {args}, {kwargs}\n")

        return wrapper

    return decorator
