class BubbleSort:
    def __init__(self, array):
        self.array = array

    def perform(self):
        for i in range(len(self.array)):
            swapped = False
            for j in range(0, len(self.array) - i - 1):
                if self.array[j] > self.array[j+1]:
                    swapped = True
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]

            if not swapped:
                break


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    s = BubbleSort(arr)
    s.perform()
    print(s.array)
