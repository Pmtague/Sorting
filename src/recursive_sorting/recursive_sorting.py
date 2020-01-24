# 1. While your data set contains more than one item, split it in half
# 2. Once you have gotten down to a single element, you have also *sorted* that element
#    (a single element cannot be "out of order")
# 3. Start merging your single lists of one element together into larger, sorted sets
# 4. Repeat step 3 until the entire data set has been reassembled

# TO-DO: complete the helper function below to merge 2 sorted arrays


def merge(arrA, arrB):
	elements = len(arrA) + len(arrB)
	merged_arr = [0] * elements
    # set counter variable for arrA and arrB
	a = 0
	b = 0
    # compare arrA(a) to arrB(b)
	for i in range(len(merged_arr)):
		if b == len(arrB):
			merged_arr[i] = arrA[a]
			a += 1
		elif a == len(arrA):
			merged_arr[i] = arrB[b]
			b += 1
		elif arrA[a] <= arrB[b]:
			merged_arr[i] = arrA[a]
			a += 1
		elif arrB[b] <= arrA[a]:
			merged_arr[i] = arrB[b]
			b += 1
	return merged_arr

# TO-DO: implement the Merge Sort function below USING RECURSION


def merge_sort(arr):
    # split array in half repeatedly until the data set has one item

    if len(arr) <= 1:
        return arr
    else:
        half = len(arr) // 2
        left = merge_sort(arr[:half])
        right = merge_sort(arr[half:])
        arr = merge(left, right)

    # compare the one item to the item it was most recently split from
    # merge the two sorted data sets in order so they become larger sorted data sets
    return arr


numbers = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(numbers))

# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
