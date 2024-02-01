class InsertionSort:
    def __init__(self, array, gap: int = 1):
        self.array = array
        self.gap = gap

    def perform(self):
        for i in range(self.gap, len(self.array)):
            v = self.array[i]
            j = i

            while j > self.gap - 1 and self.array[j - self.gap] > v:
                self.array[j] = self.array[j-self.gap]
                j -= self.gap

            self.array[j] = v


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 1, 2, 9]
    s = InsertionSort(arr)
    s.perform()
    print(s.array)
