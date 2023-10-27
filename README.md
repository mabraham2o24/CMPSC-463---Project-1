 # <div align="center">Advanced Quick Sort - Combining Quick and Insertion Sort</div>
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
## 12 TEST CASES USED FOR HYBRID, QUICK SORT, & INSERTION SORT ALGORITHM - CODE
![image](https://github.com/mabraham2o24/CMPSC-463---Project-1/assets/143213640/bf64f007-464a-478e-9e71-e2ee2a771c58)

![image](https://github.com/mabraham2o24/CMPSC-463---Project-1/assets/143213640/e71eb079-ae42-4528-98c2-b59d5ce040c7)

![image](https://github.com/mabraham2o24/CMPSC-463---Project-1/assets/143213640/5f537a32-bdbf-42af-8881-a9f5bcd2b4e8)

## RESULTS FOR THE 12 TEST CASES - ADVANCED QUICK SORT 
![image](https://github.com/mabraham2o24/CMPSC-463---Project-1/assets/143213640/776c28a1-e054-41ee-8785-b94100b9433c)

## RESULTS FOR THE 12 TEST CASES - QUICK SORT
![image](https://github.com/mabraham2o24/CMPSC-463---Project-1/assets/143213640/f021636e-f7c0-4143-a7a4-f6c67c27b777)

## RESULTS FOR THE 12 TEST CASES - INSERTION SORT
![image](https://github.com/mabraham2o24/CMPSC-463---Project-1/assets/143213640/b11779c4-585b-4d4c-88c6-cc5515a169ca)

-----------------------------------------------------------------------------------

# ***Numerical Result and Theoretical Analysis***
## Test Cases 1 - 6
| Test Cases| Advanced Quick Sort Time | Quick Sort Time| Insertion Sort Time|
| -------- | -------  | --------| --------| 
| Test Case 1  | 3.43 seconds      | 9.03 seconds  | 4.12 seconds| 
| Test Case 2 |  3.40 seconds     |1.66 seconds  | 5.25 seconds| 
|Test Case 3 |  2.00 seconds   |2.52 seconds|8.11 seconds| 
|Test Case 4| 4.05 seconds  |1.59 seconds| 2.86 seconds |
|Test Case 5|  8.11 seconds|1.58 seconds| 6.91 seconds| 
|Test Case 6| 1.48 seconds |2.17 seconds |1.12 seconds| 

## Test Cases 7 - 12
| Test Cases| Advanced Quick Sort Time| Quick Sort Time| Insertion Sort Time|
| -------------- | -----------  | ------------| ------------| 
| Test Case 7  | 0.003 seconds      | 0.003 seconds  | 0.27 seconds| 
| Test Case 8 |  5.18 seconds     |5.18 seconds  | 7.63 seconds| 
|Test Case 9 |  1.88 seconds   |1.88 seconds|5.48 seconds| 
|Test Case 10| 0.003 seconds  |0.003 seconds| 0.31 seconds |
|Test Case 11|  2.63 seconds|0.389 seconds| 6.84 seconds| 
|Test Case 12| 3.35 seconds |2.63 seconds |2.69 seconds| 
-----------------------------------------------------------------------------------------
## Time Complexity For Advanced Quick Sort 
| Best Case| Average Case| Worse Case| 
| -------- | -------  | --------|
| O(n log n) | O(n log n) | O(n^2)  |

## **When It Occurs**
+ **Best Case:** It occurs when the pivot elements are constantly leading to a balanced partitioning.
+ **Average Case:** It occurs depending on the randomized data but performs better than quick sort due to its ability to switch to insertion sort when dealing with smaller subarrays.
+ **Worse Case:** It occurs where the data is sorted or mostly sorted, the advanced quick sort might not be as efficient. By this I mean if for instance it has to sort through 100 elements, it might take 10,000 units of time to sort through it (O n^2 where n = 100). 
-----------------------------------------------------------------------------------------
## Time Complexity For Quick Sort 
| Best Case| Average Case| Worse Case| 
| -------- | -------  | --------|
| O(n log n)  | O(n log n)      | O(n^2)  |

## **When It Occurs**
+ **Best Case:** It occurs when the pivot elements divide the array into equal halves in each recursion, which results in a balanced partition. 
+ **Average Case:** It is based on random or mostly randomized data meaning that the pivot elements are randomly chosen so any element can be the pivot. This leads to an AVERAGE number of comparing and swapping the elements to be pretty small compared to other instances.
+ **Worse Case:** It occurs when the pivot elements is constantly dividing the array into severy unbalanced subarrays(i.e when the data is already sorted). This leads to such bad running time. 
----------------------------------------------------------------------------------------------
## Time Complexity For Insertion Sort 
| Best Case| Average Case| Worse Case| 
| -------- | -------  | --------|
| O(n)  | O(n^2)      | O(n^2)  |

## **When It Occurs**
+ **Best Case:** It occurs when the data is already or mostly sorted and not many comparisons and swapping is needed in order to sort the enitre array. 
+ **Average Case:** It occurs when the sorting might not require significant amounts of comapring and swapping make the sort to have a quadratic time complexity. 
+ **Worse Case:** It occurs when the data is in reverse order(descending order) leading to such significant runtimes due to the high amount of comparing and swapping involved.

## Memory Usage
+ Advance Sorting Algorithm: The memory usage depends on the impelementation and how memory is managed while the data is being sorted. Most of the memory usage happens when the recursion occurs during the quick sort.
+ Quick Sort Algorithm: It does not involve addtional memory usage because of it being an in-place algorithm. This means that the data is sorted, modified, and the output is returned using the same memory space.
+ Insertion Sort Algorithm: Is a pure in-place sorting algorithm, as it does not require any additional memory space and sorts the data directly within the original array.
-----------------------------------------------------------------------------------------
# ***Conclusion***
Doing this project I was able to really understand the difference between the hybrid algorithm and the individual sorting algorithms. The algorithms run time and time complexity all depends on what kind of input it has to sort through. In a lot of the test cases I conducted, the Advanced Quick Sort was quicker than one of the other individual sorts. Sometimes they were even the same time. There are times where the hybrid algorithm was the slowest out of all them. For instance, in Test Case 5(reverse sorted order) the hybrid algorithm was about 8 seconds while the other two were about 2-3 seconds. 

Advanced Quick Sort algorithm could be the most effiecient when it comes to ceratin scenarios due to some of these following reasons:
1. The algorithm has the ability to switch to using the Insertion Sort when it comes to smaller subarray which leads to faster and more efficient sorting of the dataset.
2. When there is highly unbalanced partitions, it could lead to siginificant increase in memory usage and increase overhead due to the recursive function calls.
3. The method ensures that the data, after its been sorted, produces the same output because of it being able to switch between insertion and quick sort depending on the size of the dataset.
4. Due to the method's ability to choose random pivot elements, it helps the time complexity to not encounter many worse case scenarios. 







