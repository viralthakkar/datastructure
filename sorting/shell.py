from sorting.insertion import InsertionSort


class ShellSort:
    def __init__(self, array):
        self.array = array
        self.gap = 3

    def perform(self):
        arr = self.array

        while self.gap > 0:
            its = InsertionSort(arr, self.gap)
            its.perform()
            self.gap -= 1
            arr = its.array

        self.array = arr


if __name__ == '__main__':
    arr = [112, 114, 133, 556, 216, 231, 233, 944]
    s = ShellSort(arr)
    s.perform()
    print(s.array)
