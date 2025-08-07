import platform
import psutil
import timeit
import os
import tempfile
import shutil

def get_system_info():
    print("=== System Info ===")
    print(f"OS: {platform.system()} {platform.release()} ({platform.version()})")
    print(f"Processor: {platform.processor()}")
    print(f"CPU cores: {psutil.cpu_count(logical=False)} physical / {psutil.cpu_count()} logical")
    print(f"RAM: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")
    print(f"Disk: {shutil.disk_usage('/').total // (1024**3)} GB total")

def benchmark_cpu():
    print("\n=== CPU Benchmark ===")
    stmt = "total = sum(i*i for i in range(1000000))"
    duration = timeit.timeit(stmt, number=10)
    print(f"Time to compute sum of squares (10 runs): {duration:.4f} seconds")

def benchmark_disk():
    print("\n=== Disk IO Benchmark ===")
    temp_dir = tempfile.mkdtemp()
    file_path = os.path.join(temp_dir, "benchmark_file")

    # Write speed test
    data = b"0" * 1024 * 1024  # 1 MB
    write_start = timeit.default_timer()
    with open(file_path, "wb") as f:
        for _ in range(100):  # Write 100 MB total
            f.write(data)
    write_time = timeit.default_timer() - write_start
    print(f"Write speed: {100 / write_time:.2f} MB/s")

    # Read speed test
    read_start = timeit.default_timer()
    with open(file_path, "rb") as f:
        while f.read(1024 * 1024):  # Read 1 MB at a time
            pass
    read_time = timeit.default_timer() - read_start
    print(f"Read speed: {100 / read_time:.2f} MB/s")

    shutil.rmtree(temp_dir)

def benchmark_memory():
    print("\n=== Memory Benchmark ===")
    from array import array
    import random
    import time

    size = 100_000_000  # 100 million integers
    print("Allocating large array...")

    start = time.time()
    arr = array('i', (random.randint(0, 100) for _ in range(size)))
    print(f"Allocation time: {time.time() - start:.2f} seconds")

    start = time.time()
    _ = sum(arr)
    print(f"Sum time: {time.time() - start:.2f} seconds")

def main():
    get_system_info()
    benchmark_cpu()
    benchmark_memory()
    benchmark_disk()

if __name__ == "__main__":
    main()
