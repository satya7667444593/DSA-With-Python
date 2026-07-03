# matrix = [ [1,3,5,8,6], [3,5,-7,-8,-9], [3,-5,7,-8,9] ]
# n = len(matrix)
# m = len(matrix[0])  
# def kadane(arr):
#     Start = 0
#     End = 0
#     max_sum = 0
#     current_sum = 0
#     n = len(arr)
#     while End < n:
#         current_sum += arr[End]
#         if current_sum < 0:
#             current_sum -= arr[Start]
#             Start = End + 1
#         if current_sum > max_sum:
#             max_sum = current_sum
#         End += 1
#     return max_sum, Start, End
def kadane_1d(arr):
    """
    Standard 1D Kadane's algorithm that also tracks the start 
    and end indices of the maximum sum subarray.
    """
    max_ending_here = arr[0]
    max_so_far = arr[0]
    start = 0
    end = 0
    temp_start = 0

    for i in range(1, len(arr)):
        # If the current element alone is greater than the accumulated sum + current element,
        # we restart our contiguous subarray from the current element.
        if arr[i] > max_ending_here + arr[i]:
            max_ending_here = arr[i]
            temp_start = i
        else:
            max_ending_here += arr[i]

        # Update the global maximum and the bounding indices
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start = temp_start
            end = i

    return max_so_far, start, end

def max_submatrix(matrix):
    """
    Applies 2D Kadane's algorithm to find the maximum sum submatrix.
    """
    if not matrix or not matrix[0]:
        return 0
        
    rows = len(matrix)
    cols = len(matrix[0])
    
    max_sum = float('-inf')
    final_left = final_right = final_top = final_bottom = 0

    # Fix the left column
    for left in range(cols):
        # Initialize a temporary array to store row sums
        temp = [0] * rows
        
        # Fix the right column
        for right in range(left, cols):
            # Compress the 2D block into a 1D array by adding the current column
            for i in range(rows):
                temp[i] += matrix[i][right]
            
            # Run 1D Kadane's on the compressed row sums
            current_sum, start_row, end_row = kadane_1d(temp)
            
            # If we found a new global maximum, update our tracking variables
            if current_sum > max_sum:
                max_sum = current_sum
                final_left = left
                final_right = right
                final_top = start_row
                final_bottom = end_row
                
    return max_sum, (final_top, final_left, final_bottom, final_right)

# Your provided matrix
matrix = [
    [1,  3,  5,  8,  6],
    [3,  5, -7, -8, -9],
    [3, -5,  7, -8,  9]
]

# Execute the algorithm
max_val, bounds = max_submatrix(matrix)
top, left, bottom, right = bounds

print(f"Maximum Sum: {max_val}")
print(f"Submatrix Bounds (Row, Col): Top-Left({top}, {left}) to Bottom-Right({bottom}, {right})")