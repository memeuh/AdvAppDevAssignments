# Program Name: Assignment1.py
	# Course: IT3883/Section 01
	# Student Name: Mina Bayramoglu
	# Assignment Number: Lab1
    # Due Date: 1/24/2026
	# Purpose: Menu that displays or clears input provided in order to demonstrate input buffer
	# Resources : https://agirlamonggeeks.com/how-to-make-menu-in-python/ https://www.geeksforgeeks.org/compiler-design/input-buffering-in-compiler-design/

def main():
    user_input = ""  # stores input
#menu
    while True:
        print("Menu")
        print("1. Append data to the input buffer")
        print("2. Clear the input buffer")
        print("3. Display the input buffer")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            new_data = input("Enter a string to append: ")
            user_input += new_data #adds new string to input buffer
            print("Data appended successfully.")

        elif choice == "2":
            user_input = "" #clears input
            print("Input buffer cleared.")

        elif choice == "3":
            if user_input:
                print("Current input:")
                print(user_input) #displays input buffer
            else:
                print("Input is empty.")

        elif choice == "4":
            print("Exiting program")
            break #exits program

        else:
            print("Invalid choice. Please enter a number from 1 to 4.") #error code if user inputs option other than 1-4

if __name__ == "__main__":
    main()


