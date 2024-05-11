from datetime import datetime

def input_travel_info():
    # Prompt the user to enter each piece of information
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    
    # Prompt for destination
    while True:
        destination = input("Enter your destination: ")

        # Check if the destination contains only alphabetic characters
        if destination.isalpha():
            break
        else:
            print("Destination should only contain letters. Please try again.")

    # Prompt for vaccination status
    vaccinated_input = input("Are you vaccinated? (Yes/No): ").strip().lower()

    # Check if the input is truthy
    truthy_values = {'yes', 'y', 'true', 't', '1'}
    vaccinated = vaccinated_input in truthy_values

    # Flag variable to indicate if the input date is valid
    date_valid = False

    # Continue prompting for the travel date until a valid date is provided
    while not date_valid:
        travel_date_str = input("Enter your travel date (DD/MM/YYYY): ")

        # Convert the travel date string to a datetime object
        try:
            travel_date = datetime.strptime(travel_date_str, "%d/%m/%Y").date()

            # Check if the travel date is in the future
            if travel_date > datetime.today().date():
                date_valid = True
            else:
                print("Travel date must be in the future.")
        except ValueError:
            print("Invalid date format. Please enter the date in the format DD/MM/YYYY.")

    # Return the collected data as a list
    return [name, age, destination, vaccinated, travel_date.strftime("%d/%m/%Y")]

# Example usage
info = input_travel_info()
if info:
    print("Travel information collected:", info)
