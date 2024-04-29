# === === FUNCTIONS EXERCISE === ===
# Write a Python program that defines a function called `calculate_average` to calculate the average of a list of numbers. The program should take a list of numbers as input from the user and then call the `calculate_average` function to compute the average. Finally, it should print the average.

# Example Output:

# Enter the numbers separated by spaces: 10 20 30 40
# The average is: 25.0



def calculate_average():#defines a function called calculate_average
    num_string = input("Enter the numbers separated by spaces:")#instructions and place for the list of numbers input from the user
    num_list = num_string.split(" ")#changes the numbers entered into a list with spaces in between
    for i in range(len(num_list)):#for loop to go through those numbers (that are actually a string at this point)
        num_list[i] = int(num_list[i])#and changes them from a string to integers (so that we can manipulate with math, calculate the average )
    print(num_list)#prints the list of numbers with spaces in between
    sum = 0#start the next for loop with sum=0
    for num in num_list:#for each num (number) in the num_list do the following; set the variable sum to 
        sum = sum + num # 0 = 0+10(the first number in num_list) and do it again
                        # 10 = 10+20(second number) do it again
                        # 30 = 30+30(third number) do it again
                        # 60 = 60+40(fourth and final number) since 40 is the last number in num_list, end the loop and move on to line 20.
    print(sum)#tells the terminal to print out the sum of 60+40
    print(f"The average is: {sum / len(num_list)}")#prints the text and the average of those numbers using an f string, the calculation for the average is inside the {} 

"""
=== === FUNCTIONS EXERCISE === ===
Write a Python program that defines a function called `calculate_average` to calculate the average of a list of numbers. The program should take a list of numbers as input from the user and then call the `calculate_average` function to compute the average. Finally, it should print the average.

Example Output:

Enter the numbers separated by spaces: 10 20 30 40 50
The average is: 30.0
"""


def app():
    """
    This function is our entry-point. It calls all the
    other functions and prints the result.
    """
    num_string = prompt()
    num_int_list = split_string_into_list_of_ints(num_string)
    average = calculate_average(num_int_list)
    print(f"The average is: {average}")


def prompt():
    """
    This function prompts the user for numbers
    separated by commas and returns it.
    """
    print("Enter the numbers separated by spaces.")
    num_string = input()
    return num_string


def split_string_into_list_of_ints(string_with_spaces):
    """
    This function splits a string into a list at
    every space, converts each element into an
    integer, and returns the list.
    """
    num_string_list = string_with_spaces.split(" ")
    num_int_list = []
    for num_string in num_string_list:
        num_int_list.append(int(num_string))
    return num_int_list


def calculate_average(num_int_list):
    """
    This function takes in a list of integers and
    returns their average.
    """
    sum = 0
    for num in num_int_list:
        sum = sum + num
    average = sum / len(num_int_list)
    return average


# Down here, we call the app function to start the app
app()