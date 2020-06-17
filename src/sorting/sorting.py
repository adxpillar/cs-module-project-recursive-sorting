# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    p1,p2 = 0,0

    # loop through combined array 
    # compare values and increment pointers

    for i in range(len(merged_arr)):
        # check position of pointers
        # copy p1 array into p2 array if out of bounds
        if p1 >= len(arrA):
            merged_arr[i] = arrB[p2]
            p2 += 1
        elif p2 >= len(arrB):
            merged_arr[i] = arrA[p1]
            p1 += 1
        elif arrA[p1] < arrB[p2]:
            merged_arr[i] = arrA[p1]
            p1 += 1
        else:
            merged_arr[i] = arrB[p2]
            p2 += 1

    return merged_arr


# # TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

    if len(arr) > 1:
        leftside = merge_sort(arr[0:len(arr)//2])
        rightside = merge_sort(arr[len(arr)//2:])

        arr = merge(leftside,rightside)

    return arr


# def merge_sort(alist):

#     if len(alist)>1:
#         mid = len(alist)//2
#         lefthalf = alist[:mid]
#         righthalf = alist[mid:]

#         merge_sort(lefthalf)
#         merge_sort(righthalf)

#         i=0
#         j=0
#         k=0
#         while i < len(lefthalf) and j < len(righthalf):
            
#             if lefthalf[i] <= righthalf[j]:
#                 alist[k]=lefthalf[i]
#                 i=i+1
#             else:
#                 alist[k]=righthalf[j]
#                 j=j+1
#             k=k+1

#         while i < len(lefthalf):
#             alist[k]=lefthalf[i]
#             i=i+1
#             k=k+1

#         while j < len(righthalf):
#             alist[k]=righthalf[j]
#             j=j+1
#             k=k+1

#     return alist

# # STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# # utilize any extra memory
# # In other words, your implementation should not allocate any additional lists 
# # or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

