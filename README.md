# Python System Benchmark & Info Tool

---

## 🔧 Features

* ✅ CPU speed test (math-heavy task using `timeit`)
* ✅ RAM allocation and summation speed
* ✅ Disk write/read speed test (temporary file-based)
* ✅ Hardware info: OS, CPU model, RAM, disk space

---

## 🛠️ Requirements

Install the only dependency with:

```bash
pip install psutil
```

This script uses only built-in libraries except for `psutil`.

---

## ▶️ How to Run

Save the script as `benchmark.py` and run:

```bash
python benchmark.py
```

It will print:

* System Info
* CPU Benchmark result
* RAM Benchmark result
* Disk IO Benchmark result

---

## 📈 How to Read the Output

Here’s a quick guide to interpreting the numbers:

### 🧠 CPU Benchmark

```
Time to compute sum of squares (10 runs): X.XX seconds
```

* **< 1.5s** → Fast CPU (desktop-class or high-end VPS)
* **1.5–3s** → Moderate performance
* **> 3s** → Likely slow CPU (cheap/free hosting)

---

### 💾 RAM Benchmark

```
Allocation time: X.XX seconds  
Sum time: X.XX seconds
```

* **< 3s allocation** and **< 1.5s summing** → Good memory speed
* **Higher numbers** = memory or CPU bottleneck

---

### 💽 Disk Benchmark

```
Write speed: XXX MB/s  
Read speed: XXX MB/s
```

* **SSD**: 200–600 MB/s (SATA), 1000+ MB/s (NVMe)
* **HDD**: 80–150 MB/s
* **< 100 MB/s**: Likely cloud disk throttling or poor I/O

---

### 💻 System Info

```
CPU cores: 2 physical / 4 logical  
RAM: 4.0 GB  
Disk: 100 GB total
```

* **2+ cores** and **4 GB+ RAM** is ideal for most applications.
* Use this info to check what your provider gives vs what they advertise.

---

## 📊 How to Compare

You can:

* Run this script on multiple hosts (e.g., local PC vs VPS).
* Compare disk/CPU/RAM speed side by side.
* Use public benchmarks like [Geekbench](https://browser.geekbench.com/) or [PassMark](https://www.cpubenchmark.net/) for reference.

---

## ❓Why Use This

This is perfect if you want to:

* Benchmark a VPS before using it in production
* Compare free vs paid hosting performance
* Check if your Python environment is underperforming

---

## 📌 Notes

* The disk test writes temporary files in your default temp directory. It deletes them afterward.
* Results may vary slightly between runs, especially on shared/cloud systems.
* For a deeper test, extend the script with multi-threading or NumPy-based matrix operations.

---

Let me know if you want this exported to a `.md` file.
Sure! Here's a plain-text version of the `README.md` content for the Python system benchmark script:

---

# Python System Benchmark & Info Tool

This is a simple Python script that benchmarks the **CPU**, **RAM**, and **Disk I/O performance** of a system or hosting environment. It also prints out key **hardware details** such as the number of CPU cores, amount of RAM, and disk size. You can use it to compare the performance of different machines — especially useful when evaluating VPS providers, cloud hosting, or bare metal setups.

---

## 🔧 Features

* ✅ CPU speed test (math-heavy task using `timeit`)
* ✅ RAM allocation and summation speed
* ✅ Disk write/read speed test (temporary file-based)
* ✅ Hardware info: OS, CPU model, RAM, disk space

---

## 🛠️ Requirements

Install the only dependency with:

```bash
pip install psutil
```

This script uses only built-in libraries except for `psutil`.

---

## ▶️ How to Run

Save the script as `benchmark.py` and run:

```bash
python benchmark.py
```

It will print:

* System Info
* CPU Benchmark result
* RAM Benchmark result
* Disk IO Benchmark result

---

## 📈 How to Read the Output

Here’s a quick guide to interpreting the numbers:

### 🧠 CPU Benchmark

```
Time to compute sum of squares (10 runs): X.XX seconds
```

* **< 1.5s** → Fast CPU (desktop-class or high-end VPS)
* **1.5–3s** → Moderate performance
* **> 3s** → Likely slow CPU (cheap/free hosting)

---

### 💾 RAM Benchmark

```
Allocation time: X.XX seconds  
Sum time: X.XX seconds
```

* **< 3s allocation** and **< 1.5s summing** → Good memory speed
* **Higher numbers** = memory or CPU bottleneck

---

### 💽 Disk Benchmark

```
Write speed: XXX MB/s  
Read speed: XXX MB/s
```

* **SSD**: 200–600 MB/s (SATA), 1000+ MB/s (NVMe)
* **HDD**: 80–150 MB/s
* **< 100 MB/s**: Likely cloud disk throttling or poor I/O

---

### 💻 System Info

```
CPU cores: 2 physical / 4 logical  
RAM: 4.0 GB  
Disk: 100 GB total
```

* **2+ cores** and **4 GB+ RAM** is ideal for most applications.
* Use this info to check what your provider gives vs what they advertise.

---

## 📊 How to Compare

You can:

* Run this script on multiple hosts (e.g., local PC vs VPS).
* Compare disk/CPU/RAM speed side by side.
* Use public benchmarks like [Geekbench](https://browser.geekbench.com/) or [PassMark](https://www.cpubenchmark.net/) for reference.

---

## ❓Why Use This

This is perfect if you want to:

* Benchmark a VPS before using it in production
* Compare free vs paid hosting performance
* Check if your Python environment is underperforming

---

## 📌 Notes

* The disk test writes temporary files in your default temp directory. It deletes them afterward.
* Results may vary slightly between runs, especially on shared/cloud systems.
* For a deeper test, extend the script with multi-threading or NumPy-based matrix operations.
