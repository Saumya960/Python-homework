def main():
    names_set = set()
    while True :
        name = input("Enter a name: ")
        if name == "":
            break
        if name in names_set:
            print("Existing name")
        else:
            print("New name")
            names_set.add(name)

    print("List of the names entered: ")
    for name in names_set:
        print(name)

main()








