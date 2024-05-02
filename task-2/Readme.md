# Sort array of 0s, 1s and 2s without using extra space or sorting algo

Dutch national flag algorithm
- take three pointers: low, mid, high
- initially put low and mid to start of the array and high to last
- this algo descibes: all [0 to low-1] are 0s and all the [high+1 to n] are 2s
- iterate until the low pointer reaches the high pointer

- Here are the conditions
- in case of 0: swap(a[lower], b[mid]), then lower++, mid++
- in case of 1: onlh mid++
- in case of 2: swap(a[mid], a[high]), then high--
