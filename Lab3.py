print("Lab 3 - Software Unit Testing with PyTest")

SORT_ASCENDING = 0
SORT_DESCENDING = 1
def bubble_sort(arr, sorting_order):
    # Check if no elements are entered
    if len(arr) == 0:
        return 0

    # Check if all elements in the list are integers
    if not all(isinstance(x, int) for x in arr):
        return 2

    # Check if 10 or more elements are entered
    if len(arr) >= 10:
        return 1

    # Check if the sorting order is valid
    if sorting_order not in [SORT_ASCENDING, SORT_DESCENDING]:
        return []

    # Copy input list to results list
    arr_result = arr.copy()
    n = len(arr_result);

    # Bubble Sort Algorithm
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if sorting_order == SORT_ASCENDING:
                if arr_result[j] > arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]
            elif sorting_order == SORT_DESCENDING:
                if arr_result[j] < arr_result[j + 1]:
                    arr_result[j], arr_result[j + 1] = arr_result[j + 1], arr_result[j]

    return arr_result;

def main():
    # Driver code to test above
    arr = [64, 34, 25, 12, 22, 11, 90]

    # Sort in ascending order
    result = bubble_sort(arr, SORT_ASCENDING)
    print("\nSorted array in ascending order: ")
    print(result)

    # Sort in descending order
    print("Sorted array in descending order: ")
    result = bubble_sort(arr, SORT_DESCENDING)
    print(result)

if __name__ == "__main__":
    main()  ;   
