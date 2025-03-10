
# 🚀 `time-it-profiler` – Python Execution & Memory Profiler

`time-it-profiler` is a lightweight Python decorator and context manager for measuring **execution time, memory usage, and CPU time** of any function. This updated version adds **nanosecond precision, logging support, and a context manager feature!**

---

## 📌 Features

✅ **High-Precision Execution Time** (Uses `time.perf_counter_ns()`)  
✅ **Memory Usage Tracking** (Peak memory in MB)  
✅ **CPU Time Monitoring** (User & System CPU time)  
✅ **Context Manager Support** (`with time_it():`)  
✅ **File & Logging Integration** (`@time_it(log_file="log.txt")` or `@time_it(logger=my_logger)`)  
✅ **Zero Overhead When Disabled** (`measure_time=False` skips profiling)  
✅ **Lightweight & No External Dependencies**  

---

## 📥 Installation

Install directly from PyPI using:
```bash
pip install time-it-profiler
```

📂 **GitHub Repository:** [https://github.com/brianvess/time_it.git](https://github.com/brianvess/time_it.git)  

---

## 📖 Usage

### ✅ **1. As a Decorator**
```python
from time_it import time_it

@time_it(measure_time=True)
def sample_function():
    total = sum(range(1, 1000000))
    return total

sample_function()
```

🔹 **Example Output:**
```
Execution Time: 0.012345 sec
Memory Usage: 1.23 MB
User CPU Time: 0.002345 sec
System CPU Time: 0.000678 sec
```

### ✅ **2. As a Context Manager**
```python
with time_it():
    result = sum(range(1, 1000000))
```

### ✅ **3. With Logging to a File**
```python
@time_it(log_file="profile.log")
def test_logging():
    time.sleep(1)

test_logging()
```

### ✅ **4. Using Python’s `logging` Module**
```python
import logging

logger = logging.getLogger("Profiler")
logging.basicConfig(level=logging.INFO)

@time_it(logger=logger)
def test_logger():
    time.sleep(2)

test_logger()
```

---

## 🔍 How It Works

### **`time_it` Class**
```python
import time
import resource
import functools
import logging
from contextlib import ContextDecorator

class time_it(ContextDecorator):
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
        if not self.measure_time:
            return func  # Return original function if profiling is disabled

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with self:
                return func(*args, **kwargs)
        return wrapper

    def _report(self):
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

        print(report)

        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(report + "\n")

        if self.logger:
            self.logger.info(report)
```

---

## 🛠️ Contributing

Contributions are welcome! Fork the repository on GitHub and submit a pull request.

🔗 **GitHub Repo:** [https://github.com/brianvess/time_it.git](https://github.com/brianvess/time_it.git)  

1. **Fork** this repository.  
2. **Create a new branch:**  
   ```bash
   git checkout -b feature-branch
   ```
3. **Commit your changes:**  
   ```bash
   git commit -m "Added new feature"
   ```
4. **Push the changes:**  
   ```bash
   git push origin feature-branch
   ```
5. **Submit a pull request!** 🎉  

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 🌟 Credits

Developed by **Brian Vess**.  
If you find this useful, please ⭐ **star this repository** and contribute! 🚀