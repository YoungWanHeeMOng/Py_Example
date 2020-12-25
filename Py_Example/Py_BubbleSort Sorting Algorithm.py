
a=[2,23,14,7,32,39]

def bubbleSort(arr):
    n=len(arr)

    for i in range(n):
        for j in range(n-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
        print(arr)

#print("The unosrted list is:")
#print(a)

bubbleSort(a)

#print("The sorted list is:")
#print(a)