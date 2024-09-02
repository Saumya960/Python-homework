#Question1
length = float(input("Enter the length of a Zander in centimeters: "))
if length >= 42:
    print('Pocket the fish')
else:
    print("Release the fish back into the lake")
below_limit = 42 - length
print(f"The zander is {below_limit} centimeters below the size limit.")


#Question2
cabin_class = input("Enter the cabin class(LUX,A,B,C: ")
if cabin_class == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print ("A: above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("B: windowless cabin above the car deck.")
elif cabin_class == "C":
    print("C: windowless cabin below the car deck.")
else :
    print("You entered an invalid cabin class")

#Question3
biological_gender = input("Enter the biological gender(male/female): ")
hemoglobin_value = float(input("Enter the hemoglobin value: "))
if biological_gender == "female":
    if hemoglobin_value < 117:
        print("Hemoglobin value is law")
    elif 117 <= hemoglobin_value <= 155:
        print("Hemoglobin value is normal")
    else:
        print("Hemoglobin value is high")
elif biological_gender == "male":
    if hemoglobin_value < 134:
        print("Hemoglobin value is law")
    elif 134 <= hemoglobin_value <= 167:
        print("Hemoglobin value is normal")
    else:
        print("Hemoglobin value is high")
else:
    print("You entered an invalid biological gender")

#Question4
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"The input year is a leap year.")
else:
    print(f"The input year is not a leap year.")








