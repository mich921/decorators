import inspect
import re
import functools
import time


def print_params(func):
    @funct11ools.wraps(func)
    def other_func(*args, **kwargs):
        val = inspect.signature(func)
        str_val = re.sub("[ )(]", '', str(val)).split(',')
        print(func.__name__)
        for param, arg in zip(str_val, args):
            print("Параметр функции", param, "=", arg, "(", type(arg), ")")
            for key, el in kwargs.items():
                print("Параметр функции", key, "=", el, "(", type(el), ")")
        return func(*args, **kwargs)
    return other_func


def time_check(func):
    @functools.wraps(func)
    def other_func(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        runtime = time.perf_counter() - start_time
        print(f'{func.__name__} выполнялась {runtime:4f} secs')
    return other_func


def query_debugger(func):
    """
        Декоратор печатает количество обращений к БД и общее время работы программы
    """
    settings.DEBUG = True

    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()

        start_queries = len(connection.queries)

        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        end_queries = len(connection.queries)

        print(f"Функция: {func.__name__}")
        print(f"Количество обращений к БД: {end_queries - start_queries}")
        print(f"завершено за: {(end - start):.6f}сек.")
        return result

    return inner_func
