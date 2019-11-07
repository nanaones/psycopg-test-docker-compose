import time

def time_print(function):
    def func(*args, **kwargs):
        
        _start_time = time.time()
        print(f"[start]{function.__name__}")
        function(*args, **kwargs)
        _end_time = time.time()
        print(f"[result][{function.__name__}] {_end_time - _start_time} (sec)")
        print(f"[end]{function.__name__}")

    return func