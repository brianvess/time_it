# timeit_function.py
import time
import resource
import functools
import logging
from contextlib import ContextDecorator

class time_it(ContextDecorator):
    """
    A decorator and context manager for measuring execution time, 
    memory usage, and CPU time of a function.
    """
    def __init__(self, measure_time=True, log_file=None, logger=None):
        self.measure_time = measure_time
        self.log_file = log_file
        self.logger = logger

    def __enter__(self):
        if self.measure_time:
            self.start_time = time.perf_counter_ns()  # Nanosecond precision
            self.start_resources = resource.getrusage(resource.RUSAGE_SELF)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self.measure_time:
            self._report()

    def __call__(self, func):
        """ Allows use as a decorator """
        if not self.measure_time:
            return func  # If disabled, return the original function

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with self:  # Use context manager functionality
                return func(*args, **kwargs)
        return wrapper

    def _report(self):
        """ Internal method to calculate and display results """
        end_time = time.perf_counter_ns()
        end_resources = resource.getrusage(resource.RUSAGE_SELF)

        execution_time = (end_time - self.start_time) / 1e9  # Convert ns to seconds
        memory_usage = (end_resources.ru_maxrss - self.start_resources.ru_maxrss) / 1024  # MB
        user_time = end_resources.ru_utime - self.start_resources.ru_utime
        system_time = end_resources.ru_stime - self.start_resources.ru_stime

        report = (
            f"Execution Time: {execution_time:.6f} sec\n"
            f"Memory Usage: {memory_usage:.2f} MB\n"
            f"User CPU Time: {user_time:.6f} sec\n"
            f"System CPU Time: {system_time:.6f} sec"
        )

        # Print to console
        print(report)

        # Write to a log file if specified
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(report + "\n")

        # Log using the Python logging module if specified
        if self.logger:
            self.logger.info(report)