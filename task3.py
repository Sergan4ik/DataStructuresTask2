class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    def remove_min(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")

        min_value = self.heap[0]
        last_value = self.heap.pop()
        if len(self.heap) > 0:
            self.heap[0] = last_value
            self._heapify_down(0)

        return min_value

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[parent_index] > self.heap[index]:
                self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        while index < len(self.heap):
            smallest = index
            left_child_index = 2 * index + 1
            right_child_index = 2 * index + 2

            if left_child_index < len(self.heap) and self.heap[left_child_index] < self.heap[smallest]:
                smallest = left_child_index

            if right_child_index < len(self.heap) and self.heap[right_child_index] < self.heap[smallest]:
                smallest = right_child_index

            if smallest != index:
                self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
                index = smallest
            else:
                break

    def print_heap(self):
        print("Binary Heap:")
        for item in self.heap:
            print(item, end=" ")
        print()


heap = MinHeap()

keys = [47, 25, 78, 50, 30, 11, 59, 18, 36, 94]
for key in keys:
    heap.insert(key)

heap.print_heap()

min_element = heap.remove_min()
print("\nMinimum element removed:", min_element)
heap.print_heap()
