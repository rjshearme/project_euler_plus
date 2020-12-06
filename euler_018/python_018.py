# Enter your code here. Read input from STDIN. Print output to STDOUT

number_test_cases = int(input())


def get_max_path_value(triangle, index=0, row=0, value=0, maxfound=0):
    print(maxfound)
    if row >= len(triangle):
        return 0

    if index < 0 or index >= len(triangle[row]):
        return 0
    value = triangle[row][index]
    return value + max(
        get_max_path_value(triangle, index, row + 1, value, value+maxfound),
        get_max_path_value(triangle, index + 1, row + 1, value, value+maxfound)
    )


for _ in range(number_test_cases):
    number_of_triangle_rows = int(input())
    triangle_array = []
    for _ in range(number_of_triangle_rows):
        triangle_array.append([int(inp) for inp in input().split()])

    print(get_max_path_value(triangle_array))
