# timeit_function.py
import time
import resource
from functools import wraps

def time_it(measure_time=True):
    def decorator(func):
        if not measure_time:
            # No measurement; return the original function immediately
            return func

        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            start_resources = resource.getrusage(resource.RUSAGE_SELF)
            
            result = func(*args, **kwargs)
            
            end_time = time.perf_counter()
            end_resources = resource.getrusage(resource.RUSAGE_SELF)

            memory = (end_resources.ru_maxrss - start_resources.ru_maxrss) / 1024  # MB
            user_time = end_resources.ru_utime - start_resources.ru_utime
            system_time = end_resources.ru_stime - start_resources.ru_stime

            print(
                f"Execution Time: {end_time - start_time:.6f} seconds\n"
                f"Memory Usage: {memory:.2f} MB\n"
                f"User CPU Time: {user_time:.6f} seconds\n"
                f"System CPU Time: {system_time:.6f} seconds"
            )

            return result
        return wrapper
    return decorator