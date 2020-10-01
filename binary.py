class BinarySearch(object):
    #  constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.alist = range(b, (a*b)+1, b)  # generate list here
        self.length = a
    # Method to ensure class object is accessed through indexing
    def __getitem__(self, item):
        return self.alist[item]
    def __setitem__(self, item, value):
        return self.alist[item] == value
    """Search method to find if the value is in the list"""
    def search(self, value):
        first_element = 0
        last_element = self.a - 1
        count = 0
        # check if value is equal to first or last elements first
        if self.alist[first_element] == value:
            return {'count': 0, 'index': first_element}
        if self.alist[last_element] == value:
            return {'count': 0, 'index': last_element}
        # an nested loop because if  list is not looped while updating the count
        while first_element <= last_element:
            mid_point = (first_element + last_element) // 2
            count += 1
            if self.alist[mid_point] == value:
                return {'count': count, 'index': mid_point}
            elif value > self.alist[mid_point]:
                first_element = mid_point + 1
            elif value < self.alist[mid_point]:
                last_element = mid_point - 1
        # for value > last item. value out of range
        if first_element > last_element :
            return {'count': 0, 'index': -1}
