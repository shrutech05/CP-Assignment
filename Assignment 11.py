# Program to repeatedly ask for an integer until correct input is given

while True:
    try:
        number = int(input("Enter an integer: "))
        print("You entered:", number)
        break 
    except ValueError:
        print("Error: That is not a valid integer. Please try again.")
