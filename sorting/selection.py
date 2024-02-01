class SelectionSort:
    def __init__(self, array):
        self.array = array

    def perform(self):
        for i in range(len(self.array)):
            min_idx = i
            for j in range(i+1, len(self.array)):
                if self.array[min_idx] > self.array[j]:
                    min_idx = j

            self.array[min_idx], self.array[i] = self.array[i], self.array[min_idx]


if __name__ == '__main__':
    arr = [6, 7, 5, 2, 3, 1, 9]
    s = SelectionSort(arr)
    s.perform()
    print(s.array)
