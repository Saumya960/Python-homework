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
biological_gender = input("Enter the biological gender(adult_male,adult_female): ")
hemoglobin_value = float(input("Enter the hemoglobin value: "))
if biological_gender == "adult_female":
    if 117 <= hemoglobin_value <= 155:
        print("Hemoglobin value is normal")
    elif hemoglobin_value < 117:
        print("Hemoglobin value is law")
    else:
        print("Hemoglobin value is high")
elif biological_gender == "adult female":
    if 134 <= hemoglobin_value <= 167:
        print("Hemoglobin value is normal")
    elif hemoglobin_value < 134:
        print("Hemoglobin value is law")
    else:
        print("Hemoglobin value is high")
else:
    print("You entered an invalid biological gender")





