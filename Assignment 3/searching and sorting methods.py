def binarySearch(A,v,l,r):
    m=(l+r)//2
    if v==A[m]:
        return m
    elif v<A[m]:
        binarySearch(A,v,l,m)
    elif v>A[m]:
        binarySeacrh(A,v,m+1,r)
    return False
def selectionSort(A):
    for i in range(len(A)):
        j=i
        for k in range(i,len(A)):
            if A[k]<A[j]:
                j=k
        A[i],A[j]=A[j],A[i]
def insertionSort(A):
    for i in range(len(A)):
        j=i
        while j>0 and A[j]<A[j-1]:
            A[j],A[j-1]=A[j-1],A[j]
            j=j-1
def  merge(A,B):
    (C,m,n)=([],len(A),len(B))
    (i,j)=(0,0)
    while i+j  < m+n:
        if i==m:
            C.append(B[j])
            j=j+1
        elif j==n:
            C.append(A[i])
            i=i+1
        elif A[i] <= B[j]:
            C.append(A[i])
            i=i+1
        elif A[i] > B[j]:
            C.append(B[j])
            j=j+1
    return C
def mergesort(A,l,r):
    if r-l <= 1:
        return (A[l:r])
    if r-l > 1:
        m=(l+r)//2
        L=mergesort(A,l,m)
        R=mergesort(A,m,r)
        return (merge(L,R))
def quicksort(A,l,r):
    if r-l <= 1:
        return ()
    pivot=l
    i=l+1
    for j in range(i,r):
        if A[j] <= A[pivot]:
            (A[i],A[j])=(A[j],A[i])
            i=i+1
    (A[pivot],A[i-1])=(A[i-1],A[pivot])
    quicksort(A,l,i-1)
    quicksort(A,i,r)

print("Binary Search")
A=[10,20,30,40,50,60]
print(A)
v=30
l=0
r=len(A)-1
b=binarySearch(A,v,l,r)
if b:
    print(v,' is present in list at ',b)
else:
    print(v,' is not present in list')
print("\n\nSelection Sort")
A=[1,7,5,6,3,8,9]
print(A)
selectionSort(A)
print(A)
print("\n\nInsertion Sort")
A=[74,32,89,55,21,64]
print(A)
insertionSort(A)
print(A)
print("\n\nMerge Sort")
A=list(range(0,100,2))+list(range(1,100,2))
print(A)
A=mergesort(A,0,len(A))
print(A)
print("\n\nQuick Sort")
A=[43,32,22,78,63,57,91,13]
print(A)
quicksort(A,0,len(A))
print(A)
