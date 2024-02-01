class CountingSort:
    def __init__(self, array):
        self.array = array

    def perform_string_elements(self):
        total_ele = 257

        counting_slots = [0] * total_ele
        sorted_string = [""] * len(self.array)

        for val in self.array:
            counting_slots[ord(val)] += 1

        for i in range(1, total_ele):
            counting_slots[i] += counting_slots[i-1]

        for val in self.array:
            idx = counting_slots[ord(val)] - 1
            sorted_string[idx] = val
            counting_slots[ord(val)] -= 1

        self.array = "".join(sorted_string)

    def perform_pos_neg_elements(self):
        max_ele = max(self.array)
        min_ele = min(self.array)

        total_ele = (max_ele - min_ele) + 1

        counting_array = [0] * total_ele
        sorted_array = [0] * len(self.array)

        for val in self.array:
            counting_array[val - min_ele] += 1

        for i in range(1, total_ele):
            counting_array[i] += counting_array[i - 1]

        for val in self.array:
            index = counting_array[val - min_ele] - 1
            sorted_array[index] = val
            counting_array[val - min_ele] -= 1

        self.array = sorted_array

    def perform_pos_elements(self):
        max_element = max(self.array)

        counting_slots = [0] * (max_element + 1)

        sorted_array = [0] * len(self.array)

        for ele in self.array:
            counting_slots[ele] += 1

        for i in range(1, max_element + 1):
            counting_slots[i] += counting_slots[i-1]

        for ele in self.array:
            idx = counting_slots[ele] - 1
            sorted_array[idx] = ele
            counting_slots[ele] -= 1

        self.array = sorted_array


if __name__ == '__main__':
    arr = [4, 2, 2, 8, 3, 3, 1]
    s = CountingSort(arr)
    print("Positive Integers")
    s.perform_pos_elements()
    print(s.array)

    arr = [-5, -10, 0, -3, 8, 5, -1, 10]
    s1 = CountingSort(arr)
    print("Negative Integers")
    s1.perform_pos_neg_elements()
    print(s1.array)

    arr = "geeksforgeeks"
    s = CountingSort(arr)
    print("Strings")
    s.perform_string_elements()
    print(s.array)



