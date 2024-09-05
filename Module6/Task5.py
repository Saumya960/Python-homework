def list_num(numbers):
    print("Numbers of original list:")
    for number in numbers:
        print("- " + number)
    return

def remove_uneven_num(numbers):
    even_numbers = [num for num in numbers if int(num) % 2 == 0]
    return even_numbers


original_list = ["3", "4", "8", "13", "16", "25", "32"]
list_num(original_list)
even_numbers = remove_uneven_num(original_list)
print("cut-down list: ")
list_num(even_numbers)
