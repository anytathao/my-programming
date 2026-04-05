
#Q1. Lists - Removing Duplicates and Sorting

def remove_duplicates_and_sort(list):
    """
    Takes a list of numbers and returns
    a sorted list with duplicates removed.
    """
    return sorted(set(list))

#Q2. Single-Dimensional Arrays - Cumulative Sum

def cumulative_sum(array):
    """
    Takes a list of numbers and returns a new list
    where each element is the cumulative sum up to that index.
    """
    result = []
    total = 0
    for x in array:
        total += x
        result.append(total)
    return result

#Q3. Slicing - Extracting Every Nth Element

def slice_every_nth(list, n):
    """
    Takes a list and step value n, returns every nth element.
    """
    if n <= 0:
        raise ValueError("n must be grater than 0")
    return list[n - 1 :: n]
    
#Q4. Arithmetic Operations with Arrays - Dot Product:

def dot_product(a, b):
    """
    Takes two lists of the same length and returns their dot product.
    """
    if len(a) != len(b):
        raise ValueError("Lists must be of the same length")
    return sum(x * y for x, y in zip(a, b))

#Q5. Arithmetic Operations with Arrays - Matrix Multiplication

def matrix_multiply(A, B):
    """
    Takes two 2D lists (matrices) and
    returns thir matrix product.
    """
    # Number of columns in A must equal number of rows in B
    if not A or not B or len(A[0]) != len(B):
        raise ValueError("Incompatible matrix sizes for multiplication")
    
    # Transpose B to make dot products easier
    B_T = list(zip(*B))

    # Multiply
    result = []
    for row in A:
        new_row = []
        for col in B_T:
            new_row.append(sum(elem_a * elem_b for elem_a, elem_b in zip(row, col)))
        result.append(new_row)
    return result

# Examples:
if __name__ == "__main__":
    print("1. Remove duplicates and sort: ")
    print(remove_duplicates_and_sort([4, 2, 2, 5, 1, 4]))

    print("2. Cumulative sum: ")
    print(cumulative_sum([1, 2, 3, 4]))

    print("3. Slice every nthn element: ")
    print(slice_every_nth([10, 20, 30, 40, 50, 60], 2))

    print("4. Dot product: ")
    print(dot_product([1, 2, 3], [4, 5, 6]))

    print("5. Matrix Multiplications: ")
    print(matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]]))
