import random
import time
import matplotlib.pyplot as plt

# Deterministic QuickSort
def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Fixed pivot: middle element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)

# Randomized QuickSort
def randomized_quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # Random pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)

# Function to measure execution time
def measure_execution_time(sort_function, arr, repetitions=5):
    total_time = 0
    for _ in range(repetitions):
        arr_copy = arr.copy()
        start_time = time.time()
        sort_function(arr_copy)
        total_time += time.time() - start_time
    return total_time / repetitions

if __name__ == "__main__":
    # Array sizes for testing
    array_sizes = [10_000, 50_000, 100_000, 500_000]
    results = {"Deterministic QuickSort": [], "Randomized QuickSort": []}

    for size in array_sizes:
        print(f"Testing with array size: {size}")
        test_array = [random.randint(0, 1_000_000) for _ in range(size)]

        det_time = measure_execution_time(deterministic_quick_sort, test_array)
        rand_time = measure_execution_time(randomized_quick_sort, test_array)

        results["Deterministic QuickSort"].append(det_time)
        results["Randomized QuickSort"].append(rand_time)

        print(f"  Deterministic QuickSort: {det_time:.4f} seconds")
        print(f"  Randomized QuickSort: {rand_time:.4f} seconds")

    # Plotting results
    plt.figure(figsize=(10, 6))
    for label, times in results.items():
        plt.plot(array_sizes, times, label=label, marker='o')

    plt.title("Performance Comparison: Deterministic vs Randomized QuickSort")
    plt.xlabel("Array Size")
    plt.ylabel("Average Execution Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()
