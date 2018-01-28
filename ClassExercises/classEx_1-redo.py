import sys

def main():
    # Calls the request_numbers function
    print("Let's get your numbers first.")
    user_input = request_numbers()

    # Converts the list items from string to float numbers, then prints list
    user_input_float = []
    for item in user_input:
        user_input_float.append(float(item))
    print("Here are your entered numbers:")
    print(user_input_float)

    # Calls the calculate_average function, sets input list
    average = calculate_average(user_input_float)
    print(f"The average of the numbers is: {average}")

# Request users to input numbers and insert them into list
def request_numbers():
    print("Enter a floating point number at each prompt. Type 'q' to stop entry.")
    user_input = []

    # While loop runs until 'q' is entered
    while True:
        number = input("> ")
        if number == 'q':
            break
        user_input.append(number)

    # List is returned to main
    return user_input


# Calculates the average of the list
def calculate_average(list_input):
    list_length = len(list_input)
    list_sum = 0

    # For loop adds the list numbers together until end of list
    for i in range (0, list_length):
        list_sum += list_input[i]

    # Average is calculated and returned to main
    average = list_sum / list_length
    return average

main()
