o	# Program Name: Assignment1.py
o	# Course: IT3883/Section 01
o	# Student Name: Mina Bayramoglu
o	# Assignment Number: Lab1
o	# Due Date: 1/24/2026
o	# Purpose: Menu that displays or clears input provided in order to demonstrate input buffer
o	# Resources : https://agirlamonggeeks.com/how-to-make-menu-in-python/ https://www.geeksforgeeks.org/compiler-design/input-buffering-in-compiler-design/

def main():
    input = ""  #stores input

    while True:
        print("Menu")
        print("1. Append data to the input buffer")
        print("2. Clear the input buffer")
        print("3. Display the input buffer")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "Option 1":
            new_data = input("Enter a string to append: ")
            input += new_data
            print("Data appended successfully.")

        elif choice == "Option 2":
            input = ""
            print("Input buffer cleared.")

        elif choice == "Option 3":
            if input:
                print("Current input buffer:")
                print(input)
            else:
                print("Input is empty")

        elif choice == "Option 4":
            print("Exiting program")
            break

        else:
            print("Error Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()
