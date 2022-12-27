def heap_sort(arr):
    # Build max heap
    for i in range(len(arr) - 1, -1, -1):
        heapify(arr, i, len(arr))

    # Extract elements from heap
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)

def heapify(arr, index, heap_size):
    largest = index
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    if left_child < heap_size and arr[left_child] > arr[largest]:
        largest = left_child
    if right_child < heap_size and arr[right_child] > arr[largest]:
        largest = right_child
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, heap_size)

arr = [3, 2, 1]
heap_sort(arr)
print(arr)  # [1, 2, 3, 4, 5]