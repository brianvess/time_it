
# 🚀 `time-it-profiler` – Python Execution & Memory Profiler

`time-it-profiler` is a lightweight Python decorator and context manager for measuring **execution time, memory usage, and CPU time** of any function or code block. This updated version adds:

✔ **Nanosecond Precision**  
✔ **Function & Code Block Identification** (Know exactly what was measured)  
✔ **Logging Support** (`log_file` or `logger`)  
✔ **Context Manager Feature** (`with time_it():`)  

---

## 📌 Features

✅ **High-Precision Execution Time** (Uses `time.perf_counter_ns()`)  
✅ **Memory Usage Tracking** (Peak memory in MB)  
✅ **CPU Time Monitoring** (User & System CPU time)  
✅ **Context Manager Support** (`with time_it(label="Block Name"):`)  
✅ **Function Name in Reports** (When used as a decorator)  
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

### ✅ **1. As a Decorator (Tracks Function Execution)**

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
========================================
Function: sample_function
----------------------------------------
Execution Time: 0.012345 sec
Memory Usage: 1.23 MB
User CPU Time: 0.002345 sec
System CPU Time: 0.000678 sec
========================================
```

---

### ✅ **2. As a Context Manager (Tracks Code Blocks)**

```python
with time_it(label="Sum Calculation"):
    result = sum(range(1, 1000000))
```

🔹 **Example Output:**

```
========================================
Code Block: Sum Calculation
----------------------------------------
Execution Time: 0.008765 sec
Memory Usage: 0.98 MB
User CPU Time: 0.001987 sec
System CPU Time: 0.000456 sec
========================================
```

---

### ✅ **3. With Logging to a File**

```python
@time_it(log_file="profile.log")
def test_logging():
    time.sleep(1)

test_logging()
```

---

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

---
## Version 1.1.1
### **What’s New in This Version?**

✅ **Function & Code Block Identification**  
✅ **Better Output Formatting**  
✅ **Same Lightweight Design – Now Even More Useful!**  
