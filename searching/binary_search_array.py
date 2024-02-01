class BinarySearch:
    def __init__(self, array):
        self.array = array

    def is_element_present(self, target: int) -> bool:
        start = 0
        end = len(self.array) - 1

        while start <= end:
            mid = (start + end) // 2

            if self.array[mid] == target:
                return True

            if self.array[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return False

    def recursive_utils(self, start: int, end: int, target: int) -> bool:
        mid = (start + end) // 2

        if start <= end:
            if self.array[mid] == target:
                return True

            if self.array[mid] > target:
                return self.recursive_utils(start, mid - 1, target)
            elif self.array[mid] < target:
                return self.recursive_utils(mid + 1, end, target)

        return False

    def is_element_present_recursive(self, target: int) -> bool:
        start = 0
        end = len(self.array) - 1

        return self.recursive_utils(start, end, target)


if __name__ == '__main__':
    print("Binary Search using iterative")
    arr = [2, 3, 4, 10, 15, 18, 20, 22, 26, 27, 28, 34, 38, 40, 43, 45, 50, 53, 58, 60, 62, 87]
    b = BinarySearch(arr)
    print(b.is_element_present(10))
    print(b.is_element_present(12))
    print(b.is_element_present(34))
    print(b.is_element_present(49))
    print(b.is_element_present(62))

    print("Binary Search using Recursive")
    print(b.is_element_present_recursive(10))
    print(b.is_element_present_recursive(12))
    print(b.is_element_present_recursive(33))
    print(b.is_element_present_recursive(45))
    print(b.is_element_present_recursive(62))
