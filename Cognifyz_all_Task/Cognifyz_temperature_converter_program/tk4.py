def cel_to_fahr(celsius):
    return (celsius * 9/5) + 32

def fahr_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Temperature Converter")

    while True:
        print("\n****Main Menu****")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            celsius = float(input("Enter temp. in Celsius: "))
            fahrenheit = cel_to_fahr(celsius)
            print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit")

        elif choice == '2':
            fahrenheit = float(input("Enter temp. in Fahrenheit: "))
            celsius = fahr_to_cel(fahrenheit)
            print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again")

if __name__ == "__main__":
    main()
