seasons = ("spring","summer","autumn","winter")
months ={
    "winter" : {12,1,2},
    "spring" : {3,4,5},
    "summer" : {6,7,8},
    "autumn" : {9,10,11} }

month_num = int(input("Enter the month number(1-12): "))

if 1 <= month_num <= 12:
    for season, months in months.items():
        if month_num in months:
            print(f"The season for month {month_num} is : {season}")
            break

else:
    print("Invalid month number")
