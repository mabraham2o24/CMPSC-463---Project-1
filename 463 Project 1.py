#source : https://www.geeksforgeeks.org/advanced-quick-sort-hybrid-algorithm/

"""
Advanced Quick Sort
"""
print("\n----------------12 Test Cases - Advanced Quick Sort------------------")
import time #calculate cpu time
import random #using this for one the test cases

#performs the insertion sort on a subarray of 'arr' between indices 'low' and 'n'. It iterates through the array and inserts each element at its correct position
def insertion_sort(arr, low, n):
    for i in range(low + 1, n + 1):
        val = arr[i]
        j = i
        while j > low and arr[j - 1] > val:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = val



# This function is used to apply the partition sort on the array. It choses the pivot element(rightmost element), rearranges the elements in the subarray so that the elements smaller than the pivot to its left and the elements that are greater to its right. Then the pivot's final position is returned. 
def partition(arr, low, high):
    pivot = arr[high]
    i = j = low
    for i in range(low, high):
        if arr[i] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[high] = arr[high], arr[j]
    return j

#calls the partition function and then recursively sorts the subarrays on the left and right of the pivot.
def quick_sort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, high)
        return arr

# combination of quick sort and insertion sort. if the size of the array is less than a threshold, it applies insertion sort and stops the recursion. 
def hybrid_quick_sort(arr, low, high):
    while low < high:

        if high - low + 1 < 10:
            insertion_sort(arr, low, high)
            break
        else:
            pivot = partition(arr, low, high)
            # Optimized quicksort which works on
            # the smaller arrays first
            # If the left side of the pivot
            # is less than the right, sort the left part
            # and move to the right part of the array
            if pivot - low < high - pivot:
                hybrid_quick_sort(arr, low, pivot - 1)
                low = pivot + 1
            else:
                # If the right side of pivot is less
                # than the left, sort the right side and
                # move to the left side
                hybrid_quick_sort(arr, pivot + 1, high)
                high = pivot - 1

# Calculate the runtime for each of the test cases
def measure_runtime(test_function, *args):
    start_time = time.time()
    test_function(*args)
    end_time = time.time()
    return end_time - start_time

# Test Case 1: Array with mixed values
a1 = [24, 97, 40, 67, 88, 85, 15, 66, 53, 44, 26, 48, 16, 52, 45, 23, 90, 18, 49, 80, 23]
runtime1 = measure_runtime(hybrid_quick_sort, a1, 0, 20)
print("Test Case 1:", a1)
print("Test Case 1 Runtime:", runtime1, "seconds")

# Test Case 2: Reverse sorted array
a2 = [5, 4, 3, 2, 1]
runtime2 = measure_runtime(hybrid_quick_sort, a2, 0, 4)
print("\nTest Case 2:", a2)
print("Test Case 2 Runtime:", runtime2, "seconds")

# Test Case 3: Array with duplicate values
a3 = [5, 2, 1, 3, 2, 4, 5, 1, 4, 3]
runtime3 = measure_runtime(hybrid_quick_sort, a3, 0, 9)
print("\nTest Case 3:", a3)
print("Test Case 3 Runtime:", runtime3, "seconds")

# Test Case 4: Already sorted array
a4 = [1, 2, 3, 4, 5]
runtime4 = measure_runtime(hybrid_quick_sort, a4, 0, 4)
print("\nTest Case 4:", a4)
print("Test Case 4 Runtime:", runtime4, "seconds")

# Test Case 5: Reverse sorted array
a5 = [5, 4, 3, 2, 1]
runtime5 = measure_runtime(hybrid_quick_sort, a5, 0, 4)
print("\nTest Case 5:", a5)
print("Test Case 5 Runtime:", runtime5, "seconds")

# Test Case 6: Array with duplicate values
a6 = [5, 2, 1, 3, 2, 4, 5, 1, 4, 3]
runtime6 = measure_runtime(hybrid_quick_sort, a6, 0, 9)
print("\nTest Case 6:", a6)
print("Test Case 6 Runtime:", runtime6, "seconds")

# Test Case 7: Large random array
a7 = [random.randint(1, 1000) for _ in range(1000)]
runtime7 = measure_runtime(hybrid_quick_sort, a7, 0, 999)
print("\nTest Case 7 (First 10 elements):", a7[:10], "...")
print("Test Case 7 Runtime:", runtime7, "seconds")

# Test Case 8: Empty array
a8 = []
runtime8 = measure_runtime(hybrid_quick_sort, a8, 0, 0)
print("\nTest Case 8:", a8)
print("Test Case 8 Runtime:", runtime8, "seconds")

# Test Case 9: Array with all identical elements
a9 = [5, 5, 5, 5, 5]
runtime9 = measure_runtime(hybrid_quick_sort, a9, 0, 4)
print("\nTest Case 9:", a9)
print("Test Case 9 Runtime:", runtime9, "seconds")

# Test Case 10: Large random array
a10 = [random.randint(1, 1000) for _ in range(1000)]
runtime10 = measure_runtime(hybrid_quick_sort, a10, 0, 999)
print("\nTest Case 10 (First 10 elements):", a10[:10], "...")
print("Test Case 10 Runtime:", runtime10, "seconds")

# Test Case 11: Array with negative values
a11 = [10, -5, 3, -8, 0, 7, -2, 1, -6, 4]
runtime11 = measure_runtime(hybrid_quick_sort, a11, 0, 9)
print("\nTest Case 11:", a11)
print("Test Case 11 Runtime:", runtime11, "seconds")

# Test Case 12: Array with float values
a12 = [3.2, 1.5, 0.7, 2.1, 4.8, 3.7, 2.9, 4.5]
runtime12 = measure_runtime(hybrid_quick_sort, a12, 0, 7)
print("\nTest Case 12:", a12)
print("Test Case 12 Runtime:", runtime12, "seconds")

#-------------------------------------------------------------------------------------------------------------------
"""
Quick Sort
"""
# Function to perform the quicksort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    less = [x for x in arr[1:] if x <= pivot]
    greater = [x for x in arr[1:] if x > pivot]

    return quick_sort(less) + [pivot] + quick_sort(greater)

# Function to measure the runtime of a test case
def measure_cpu_time(sort_function, arr):
    start_time = time.process_time()
    sorted_arr = sort_function(arr.copy())
    end_time = time.process_time()
    return sorted_arr, end_time - start_time

# Function to print the output with a limit
def print_output_with_limit(arr, limit=10):
    if len(arr) <= limit:
        print(arr)
    else:
        print(arr[:limit], "...")


# Test Cases
test_cases = [
    # Test Case 1: Array with mixed values
    [24, 97, 40, 67, 88, 85, 15, 66, 53, 44, 26, 48, 16, 52, 45, 23, 90, 18, 49, 80, 23],
    # Test Case 2: Reverse sorted array
    [5, 4, 3, 2, 1],
    # Test Case 3: Array with duplicate values
    [5, 2, 1, 3, 2, 4, 5, 1, 4, 3],
    # Test Case 4: Already sorted array
    [1, 2, 3, 4, 5],
    # Test Case 5: Reverse sorted array
    [5, 4, 3, 2, 1],
    # Test Case 6: Array with duplicate values
    [5, 2, 1, 3, 2, 4, 5, 1, 4, 3],
    # Test Case 7: Large random array
    [random.randint(1, 1000) for _ in range(1000)],
    # Test Case 8: Empty array
    [],
    # Test Case 9: Array with all identical elements
    [5, 5, 5, 5, 5],
    # Test Case 10: Large random array
    [random.randint(1, 1000) for _ in range(1000)],
    # Test Case 11: Array with negative values
    [10, -5, 3, -8, 0, 7, -2, 1, -6, 4],
    # Test Case 12: Array with float values
    [3.2, 1.5, 0.7, 2.1, 4.8, 3.7, 2.9, 4.5]
]
print("\n-------------------!2 Test Cases - Quick Sort---------------------------")
# Run the test cases and measure CPU time
for i, test_case in enumerate(test_cases, start=1):
    sorted_arr, cpu_time = measure_cpu_time(quick_sort, test_case)
    print(f"Test Case {i}: ", end="")
    print_output_with_limit(sorted_arr, limit=10)
    print(f"CPU Time: {cpu_time} seconds")
    print()


#-----------------------------------------------------------------------------------------------------
"""
Insertion Sort
"""

print("\n-----------------------12 Test Cases - Insertion Sort----------------------------\n")


# Function to perform the insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        val = arr[i]
        j = i
        while j > 0 and arr[j - 1] > val:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = val

# Function to measure the runtime of a test case
def measure_runtime(test_function, *args):
    start_time = time.time()
    test_function(*args)
    end_time = time.time()
    return end_time - start_time

# Define the test cases

# Test Case 1: Array with mixed values
a1 = [24, 97, 40, 67, 88, 85, 15, 66, 53, 44, 26, 48, 16, 52, 45, 23, 90, 18, 49, 80, 23]
runtime1 = measure_runtime(insertion_sort, a1)
print("Insertion Sort - Test Case 1:", a1)
print("Test Case 1 Runtime:", runtime1, "seconds")

# Test Case 2: Reverse sorted array
a2 = [5, 4, 3, 2, 1]
runtime2 = measure_runtime(insertion_sort, a2)
print("\nInsertion Sort - Test Case 2:", a2)
print("Test Case 2 Runtime:", runtime2, "seconds")

# Test Case 3: Array with duplicate values
a3 = [5, 2, 1, 3, 2, 4, 5, 1, 4, 3]
runtime3 = measure_runtime(insertion_sort, a3)
print("\nInsertion Sort - Test Case 3:", a3)
print("Test Case 3 Runtime:", runtime3, "seconds")

# Test Case 4: Already sorted array
a4 = [1, 2, 3, 4, 5]
runtime4 = measure_runtime(insertion_sort, a4)
print("\nInsertion Sort - Test Case 4:", a4)
print("Test Case 4 Runtime:", runtime4, "seconds")

# Test Case 5: Reverse sorted array
a5 = [5, 4, 3, 2, 1]
runtime5 = measure_runtime(insertion_sort, a5)
print("\nInsertion Sort - Test Case 5:", a5)
print("Test Case 5 Runtime:", runtime5, "seconds")

# Test Case 6: Array with duplicate values
a6 = [5, 2, 1, 3, 2, 4, 5, 1, 4, 3]
runtime6 = measure_runtime(insertion_sort, a6)
print("\nInsertion Sort - Test Case 6:", a6)
print("Test Case 6 Runtime:", runtime6, "seconds")

# Test Case 7: Large random array
a7 = [random.randint(1, 1000) for _ in range(1000)]
runtime7 = measure_runtime(insertion_sort, a7)
print("\nInsertion Sort - Test Case 7 (First 10 elements):", a7[:10], "...")
print("Test Case 7 Runtime:", runtime7, "seconds")

# Test Case 8: Empty array
a8 = []
runtime8 = measure_runtime(insertion_sort, a8)
print("\nInsertion Sort - Test Case 8:", a8)
print("Test Case 8 Runtime:", runtime8, "seconds")

# Test Case 9: Array with all identical elements
a9 = [5, 5, 5, 5, 5]
runtime9 = measure_runtime(insertion_sort, a9)
print("\nInsertion Sort - Test Case 9:", a9)
print("Test Case 9 Runtime:", runtime9, "seconds")

# Test Case 10: Large random array
a10 = [random.randint(1, 1000) for _ in range(1000)]
runtime10 = measure_runtime(insertion_sort, a10)
print("\nInsertion Sort - Test Case 10 (First 10 elements):", a10[:10], "...")
print("Test Case 10 Runtime:", runtime10, "seconds")

# Test Case 11: Array with negative values
a11 = [10, -5, 3, -8, 0, 7, -2, 1, -6, 4]
runtime11 = measure_runtime(insertion_sort, a11)
print("\nInsertion Sort - Test Case 11:", a11)
print("Test Case 11 Runtime:", runtime11, "seconds")

# Test Case 12: Array with float values
a12 = [3.2, 1.5, 0.7, 2.1, 4.8, 3.7, 2.9, 4.5]
runtime12 = measure_runtime(insertion_sort, a12)
print("\nInsertion Sort - Test Case 12:", a12)
print("Test Case 12 Runtime:", runtime12, "seconds")