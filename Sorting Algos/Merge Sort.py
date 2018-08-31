#Merge-Sort
n = [int(x) for x in input("Give Integers/n").split()]
r = len(n)
def  Merge_Sort(n,p,r):
    if p<r:                          # termination condition        
        q = int((p+r-1)/2)        # the middle point to divide the array into two halves
        Merge_Sort(n,p,q)    # mergeSort for first half
        Merge_Sort(n,q+1,r)  # mergeSort for second half
        Merge(n,p,q,r)          # Merge the two halves sorted
def Merge(n,p,q,r):
    l1 = q - p + 1
    r1 = r- q
 
    # create temp arrays
    L = [0] * (l1)
    R = [0] * (r1)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0 , l1):
        L[i] = n[p + i]
 
    for j in range(0 , r1):
        R[j] = n[q + 1 + j]
 
    # Merge the temp arrays back into n[p..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = p     # Initial index of merged subarray
 
    while i < l1 and j < r1 :
        if L[i] <= R[j]:
            n[k] = L[i]
            i += 1
        else:
            n[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there are any
    while i < l1:
        n[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there are any
    while j < r1:
        n[k] = R[j]
        j += 1
        k += 1
        
Merge_Sort(n,0,r-1)  # calling Merge sort function
print(n)
# TIME COMPLEXCITY O(r * log(r))
# Auxilary Space O(r)
# Stable
