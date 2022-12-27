class BinarySearch:
    @staticmethod
    def binary_search(elem, array):
        right_border = len(array) - 1
        left_border = 0

        while right_border >= left_border:
            middle_index = left_border + (right_border - left_border) // 2
            middle_value = array[middle_index]
            if middle_value == elem:
                return middle_index
            elif middle_value < elem:
                left_border = middle_index + 1
            elif middle_value > elem:
                right_border = middle_index - 1
        return f'Element {elem} not fount'

# cls = BinarySearch()
# sorted_list = sorted([random.randint(0, 55) for _ in range(20)])
# print(cls.binary_search(34, sorted_list), sorted_list)
