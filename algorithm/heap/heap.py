

class Heap:

    @staticmethod
    def get_left(i):

        return i * 2 + 1
    @staticmethod
    def get_right(i):

        return i * 2 + 2

    @staticmethod
    def heapify(arr, i):

        left = Heap.get_left(i)
        right = Heap.get_right(i)
        max_index = i

        if left < len(arr) and arr[left] > arr[max_index]:
            max_index = left
        if right < len(arr) and arr[right] > arr[max_index]:
            max_index = right

        if max_index != i:
            arr[max_index],arr[i] = arr[i], arr[max_index]
            Heap.heapify(arr,max_index)

    @staticmethod
    def buildheap(arr):

        mid = len(arr)//2

        for i in range(mid,-1,-1):
            Heap.heapify(arr, i)

    @staticmethod
    def heapsort(arr):

        sorted_arr = []

        for _ in range(len(arr)):

            Heap.buildheap(arr)
            arr[0],arr[-1] = arr[-1],arr[0]
            sorted_arr.append(arr.pop())
        return sorted_arr
#arr = [4,5,7,3,8,9]
arr = [2,42,11,30,10,7,6,5,9]
Heap.buildheap(arr)
print(arr)
print(Heap.heapsort(arr))
print(arr)
#update comment









