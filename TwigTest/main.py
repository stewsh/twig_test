
def divide_array(arr, n):
    """
    Divides the list of items arr into n sublists, returning the result as a list of lists.
    :param arr: a list of 0 or more items
    :param n: a positive integer
    :return: a list of n sublists which, when combined, will equal arr
    :raise: ValueError if n is less than or equal to 0
    """
    if n <= 0:
        raise ValueError("Number of elements value must be greater than 0")

    if len(arr) % n > 0:
        output_size = len(arr) // n + 1    # python 3 integer division
        last_output_size = output_size - (len(arr) % n)
    else:
        output_size = len(arr) // n
        last_output_size = output_size

    output_arr = []
    slice_start = 0
    slice_end = output_size
    i = 0

    while i < n:
        if i < (n - 1):
            output_item = arr[slice_start : slice_end]
            output_arr.append(output_item)
            slice_start += output_size
            slice_end += output_size
        else:
            slice_end = slice_start + last_output_size
            output_item = arr[slice_start : slice_end]
            output_arr.append(output_item)
        i += 1

    return output_arr

def get_data():
    my_data = input("Enter a character: ")
    my_length = input("Enter a length: ")
    my_number = input("How many sublists: ")

    out_arr = divide_array(list(my_data) * int(my_length), int(my_number))
    print(out_arr)

get_data()
