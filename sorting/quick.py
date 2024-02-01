class QuickSort:
    def __init__(self, array):
        self.array = array

    def partition(self, array, low, end):
        pivot = array[end]

        i = low - 1

        for j in range(low, end):
            if array[j] <= pivot:
                i += 1

                array[i], array[j] = array[j], array[i]

        array[i + 1], array[end] = array[end], array[i+1]

        return i + 1

    def sort_util(self, array, low, end):
        if low < end:
            pi = self. partition(array, low, end)

            self.sort_util(array, low, pi - 1)

            self.sort_util(array, pi, end)

        return array

    def perform(self):
        low = 0
        high = len(self.array) - 1

        self.array = self.sort_util(self.array, low, high)


if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    s = QuickSort(arr)
    s.perform()
    print(s.array)
