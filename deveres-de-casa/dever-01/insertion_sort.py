import random
import time

LIST_SIZES = [1000, 5000, 10000, 20000, 50000]

def insertion_sort(list_a):
    """
    Sorts a list using the Insertion Sort algorithm.

    Args:
        list_a (list): List of comparable elements.

    Returns:
        list: The sorted list in ascending order.
    """
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i > 0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i -= 1

    return list_a

def generate_random_list(size):
    """
    Generates a list of random integers.

    Args:
        size (int): Size of the list.

    Returns:
        list: List filled with random integers.
    """
    return [random.randint(0, 100000) for n in range(size)]

def time_measurement(sort_function, data):
    """
    Measures execution time of a sorting function.

    Args:
        sort_function (callable): Sorting function to test.
        data (list): List to be sorted.

    Returns:
        float: Execution time in seconds.
    """
    start_time = time.time()
    sort_function(data)
    end_time = time.time()

    return end_time - start_time


def main():
    for size in LIST_SIZES:
        list_base = generate_random_list(size)

        list_insertion = list_base.copy()
        list_timsort = list_base.copy()

        insertion_time = time_measurement(insertion_sort, list_insertion)
        sorted_time = time_measurement(sorted, list_timsort)

        print(f"\nList size: {size}")
        print(f"Insertion Sort: {insertion_time:.6f} seconds")
        print(f"Python sorted(): {sorted_time:.6f} seconds")

if __name__ == "__main__":
    main()