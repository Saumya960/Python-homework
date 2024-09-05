def sum_of_list(numbers):
    total = 0
    for i in numbers:
        total += i
    return total

test_list = [1, 2, 1, 3, 1, 4]
sum_result = sum_of_list(test_list)
print(f"Sum of the list is: {sum_result}")
