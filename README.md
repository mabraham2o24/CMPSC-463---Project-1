 # <div align="center">Advanced Quick Sort - Combinging Quick and Insertion Sort</div>
# ***Basis of this Github/Introduction***
+ Advanced Quick Sort algorithm is an algorithm created to combine both the quick sort and insert sort algorthims to create a time efficient sorting method for us to use. It is more beneficial to use when it comes to different types of inputs such as sorted arrays. It implements different method to give the best optimized sorting possible for different inputs. For instance, this hybrid algorithm uses insertion method to sort through small subarrays which prevents overuse of the recursive calls and makes the sorting method much faster.
+ This repository contains a Readme.md file that contains the report. It also has the py file of my code for the algorithms and contains a PDF file of screenshots of my output. 
# ***Project Goals***
1. My project goal is to analyze the differences between each algorithm's runtime and time complexity to really see if the hybrid algorithm is more time effiecient than the individual sorting methods themselves. I also want to be able to really understand how the algorithm is implemented and the differences between combiining the quick sort and insertion sort versus using those methods individually and in its traditional form. 

# ***Algorithm Description***
The quick sort hybrid algorithm takes quick sort and insertion sort, combining both methods, and works as follows.
  + **Insertion Sort (insertion_sort)**
      + Takes an array, a lower index, and an upper index('arr', 'low', and 'n') and starts with the second element('low + 1') and iterates through the array.
      + As it is iterating through each element, it compares it to the elements in the left and moves each one to its corrected position to fully sort the array (this works best for small and nearly sorted arrays).
  + **Partition Function (partition)**
      + Used by the quick sort funtion to divide the array into two parts. It has an array, a lower index, and an upper index as its paramters('arr', 'low', and 'high').
      + The last element of the array('high') is chosen as the pivot element. The last element is chosen because it is the easiest way to get the pivot element without having to do other methods or calculations. 
      + Elements are arranged so that the ones less than the pivot is put to the right and the one that is greater than the pivot is put to the right. After all of that is done the pivot will be placed at the correct position.
  + **Quick Sort(quick_sort)**
      + This is a recursive implemention of the quick sort algorithm that takes an array , a lower index, and an upper index('arr', 'low', and 'high').
      + If the array has no elements or only one element, it is considered sorted, and the function returns. This is because in either scenarios there is nothing to sort and everything is in the right position.
      + If there is more than one element, using the partition function it chooses the pivot. Then the array is partitioned into two subarrays and quick sort is applied to each subarray.
    + **Hybrid Quick Sort(hybrid_quick_sort)**
      + This function combines the quick sort and insertion sort algorithms. It also takes an array, a lower index, and an upper index('arr', 'low', 'high').
      + It checks if the size of the array('high - low + 1') is less than a certaim threshold meaning the size that determines what method(quick sort or insertion sort) should be used to sort the subarray.
      + If the size is smaller, insertion sort is used to sort the subarray because this method is more optimal for small subarrays. If the size is larger, then it will sort the subarray using quick sort.
      + This function also uses 'partition' function to find the pivot element and applies the Quick Sort to the left and right subarrays in ways where the small subarray first.  
    

# ***Benchmarking Results***


# ***Numerical Result and Theoretical Analysis***
## Test Cases 1 - 6
| Test Cases| Advanced Quick Sort Time | Insertion Sort Time| Quick Sort Time|
| -------- | -------  | --------| --------| 
| Test Case 1  | 3.43 seconds      | 0.0 (Sec)  | 0.0 (Sec)| 
| Test Case 2 |  3.40 seconds     |0.0 (Sec)  | 0.0 (Sec)| 
|Test Case 3 |  2.00 seconds   |0.0025 (Sec)|0.0019 (Sec)| 
|Test Case 4| 4.05 seconds  |0.029 (Sec)| 0.0189 (Sec) |
|Test Case 5|  8.11 seconds|0.389 (Sec)| 0.572 (Sec)| 
|Test Case 6| 1.48 seconds |4.29 (Sec) |Failed: Max Recusion Depth| 

## Test Cases 7 - 12
| Test Cases| Advanced Quick Sort Time| Insertion Sort Time| Quick Sort Time|
| -------- | -------  | --------| --------| 
| Test Case 7  | 0.003 seconds      | 0.0 (Sec)  | 0.0 (Sec)| 
| Test Case 8 |  5.18 seconds     |0.0 (Sec)  | 0.0 (Sec)| 
|Test Case 9 |  1.88 seconds   |0.0025 (Sec)|0.0019 (Sec)| 
|Test Case 10| 0.003 seconds  |0.029 (Sec)| 0.0189 (Sec) |
|Test Case 11|  2.63 seconds|0.389 (Sec)| 0.572 (Sec)| 
|Test Case 12| 3.35 seconds |4.29 (Sec) |Failed: Max Recusion Depth| 

## Time Complexity For Advanced Quick Sort 
| Best Case| Average Case| Worse Case| 
| -------- | -------  | --------|
| Test Case 1  | 0.0 (Sec)      | 0.0 (Sec)  |

## Time Complexity For Quick Sort 
| Best Case| Average Case| Worse Case| 
| -------- | -------  | --------|
| Test Case 1  | 0.0 (Sec)      | 0.0 (Sec)  |

## Time Complexity For Insertion Sort 
| Best Case| Average Case| Worse Case| 
| -------- | -------  | --------|
| Test Case 1  | 0.0 (Sec)      | 0.0 (Sec)  |








