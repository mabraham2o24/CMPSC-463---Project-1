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
      + Elements are arranged so that the ones less than the 
    

# ***Benchmarking Results***
+ start here

# ***Numerical Result and Theoretical Analysis***
+ start here


