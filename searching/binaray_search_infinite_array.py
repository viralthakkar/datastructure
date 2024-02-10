class BinarySearchInfinite:
    def __init__(self, array):
        self.array = array

    def binary_search(self, start, end, target):
        if start <= end:

            mid = (start + end) // 2

            if self.array[mid] == target:
                return True

            if self.array[mid] > target:
                self.binary_search(start, mid - 1, target)
            else:
                self.binary_search(mid + 1, end, target)

        return False

    def find_pos(self, target):

        start = 0
        end = 1
        val = self.array[0]

        while val < target:
            start = end
            end = 2 * end
            if self.array and self.array[end]:
                val = self.array[end]
            else:
                val = float('inf')

        return self.binary_search(start, end, target)


if __name__ == '__main__':
    arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170, float('inf')]
    b = BinarySearchInfinite(arr)
    print(b.find_pos(10))
    print(b.find_pos(999))



