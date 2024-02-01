class MergeSort:
    def __init__(self, array):
        self.array = array

    def merge_sort_utils(self, array):
        if len(array) > 1:

            mid = len(array) // 2

            left = array[:mid]
            right = array[mid:]

            self.merge_sort_utils(left)
            self.merge_sort_utils(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] > right[j]:
                    array[k] = right[j]
                    j += 1
                else:
                    array[k] = left[i]
                    i += 1
                k += 1

            while i < len(left):
                array[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                array[k] = right[j]
                j += 1
                k += 1

        return array

    def perform(self):
        self.array = self.merge_sort_utils(self.array)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 1, 2, 9]
    s = MergeSort(arr)
    s.perform()
    print(s.array)
