def main():
    airports = {}

    while True:
        print("The airport information system")
        print("a. Enter a new airport")
        print("b. Get airport information")
        print("c. Exit")

        choice = input("Please enter your choice(a, b, or c): ")
        if choice == "a":
            icao_code = input("Enter the ICAO code of the airport: ")
            airport_name = input("Enter the name of the airport: ")
            airports[icao_code] = airport_name
            print(f"Airport '{airport_name}' with ICAO code '{icao_code}' has been added.")

        elif choice == "b":
            icao_code = input("Enter the ICAO  code of the airport:")
            if icao_code in airports:
                airport_name = airports[icao_code]
                print(f"Airport with ICAO code '{icao_code}' is '{airport_name}'.")
            else:
                print(f"No airport found with ICAO code '{icao_code}'.")

        elif choice == 'c':
            print("End the program.")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()











