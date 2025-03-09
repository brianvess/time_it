# `time_it` - Python Function Profiler

## 🚀 Overview

`time_it` is a lightweight Python decorator that measures **execution time, memory usage, and CPU time** of any function. It is designed to be **efficient** and **flexible**, allowing you to enable or disable profiling dynamically.

## 📌 Features

✅ **Execution Time Measurement** (High-precision timing with `perf_counter`)  
✅ **Memory Usage Tracking** (Peak memory usage in MB)  
✅ **CPU Time Monitoring** (User & System CPU time)  
✅ **Zero Overhead When Disabled** (`measure_time=False` bypasses all profiling logic)  
✅ **Easy to Use as a Decorator** (`@time_it`)  
✅ **Lightweight & No External Dependencies**  

---

## 📥 Installation

If using this as a standalone module, simply **clone the repository**:

```bash
git clone https://github.com/YOUR_USERNAME/time_it.git
cd time_it
```

Or install it as a package (when published to PyPI):

```bash
pip install time-it-profiler
```

---

## 📖 Usage

### ✅ **Basic Example**
```python
from timeit_function import time_it

@time_it(measure_time=True)  # Enable profiling
def sample_function():
    total = sum(range(1, 1000000))
    return total

sample_function()
```

**Example Output:**
```
Execution Time: 0.012345 seconds
Memory Usage: 1.23 MB
User CPU Time: 0.002345 seconds
System CPU Time: 0.000678 seconds
```

### ✅ **Disable Profiling (Zero Overhead)**
```python
@time_it(measure_time=False)  # No profiling, function runs normally
def quick_function():
    return sum(range(1, 100))

quick_function()
```

---

## 🔍 How It Works

### **`time_it` Function**
```python
import time
import resource
from functools import wraps

def time_it(measure_time=True):
    def decorator(func):
        if not measure_time:
            return func  # Return the function unmodified if profiling is disabled

        @wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            start_resources = resource.getrusage(resource.RUSAGE_SELF)
            
            result = func(*args, **kwargs)
            
            end_time = time.perf_counter()
            end_resources = resource.getrusage(resource.RUSAGE_SELF)

            memory = (end_resources.ru_maxrss - start_resources.ru_maxrss) / 1024  # Convert KB to MB
            user_time = end_resources.ru_utime - start_resources.ru_utime
            system_time = end_resources.ru_stime - start_resources.ru_stime

            print(
                f"Execution Time: {end_time - start_time:.6f} seconds\\n"
                f"Memory Usage: {memory:.2f} MB\\n"
                f"User CPU Time: {user_time:.6f} seconds\\n"
                f"System CPU Time: {system_time:.6f} seconds"
            )

            return result
        return wrapper
    return decorator
```

---

## 🛠️ Contributing

1. **Fork** this repository.
2. Create a new branch:  
   ```bash
   git checkout -b feature-branch
   ```
3. Commit your changes:  
   ```bash
   git commit -m "Added new feature"
   ```
4. Push the changes:  
   ```bash
   git push origin feature-branch
   ```
5. Submit a **pull request**! 🎉

---

## 📜 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 🌟 Credits

Developed by **Brian Vess**.  
If you find this useful, please ⭐ **star this repository** and contribute! 🚀
