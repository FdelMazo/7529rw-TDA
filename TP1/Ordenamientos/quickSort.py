def quickSort(array):
    if len(array) < 2 :
        return array
    minors_list, pivot_list, major_list = _partition(array)
    return quickSort(minors_list) + pivot_list + quickSort(major_list)

def _partition(array):
    pivot = array[0]
    minors = []
    pivots = [array[0]]
    majors = []
    for element in array:
        if element < pivot:
            minors.append(element)
        if element == pivot:
            pivots.append(element)
        else:
            majors.append(element)
    return minors, pivots, majors