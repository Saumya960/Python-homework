length = float(input("Enter the length of a Zander in centimeters: "))
size_limit = 42
if length <= size_limit:
    print("Release the fish back into the lake")
below_limit = size_limit - length
print(f"The zander is {below_limit} centimeters below the size limit.")