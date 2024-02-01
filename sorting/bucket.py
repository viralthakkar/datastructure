from sorting.insertion import InsertionSort


class BucketSort:
    def __init__(self, array):
        self.array = array

    def perform(self):
        buckets = [[] for _ in range(10)]

        for num in self.array:
            idx = int(10 * num)
            buckets[idx].append(num)

        res = []

        for bucket in buckets:
            its = InsertionSort(bucket)
            res += its.array

        self.array = res


if __name__ == '__main__':
    arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    s = BucketSort(arr)
    s.perform()
    print(s.array)
