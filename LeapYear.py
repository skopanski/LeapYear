########################################
# Salaheddin Kopanski
# Lab 1             
# This program is designed to ask the user's name and the month and year they were born.
# The program then determines the season of the month and whether it was a leap year or not.
# Once the program has determined the following, it will respond with a text message greeting the user by name, the season and if it was a leap year.                                             
########################################

# Read user's name
name = input("Enter user's name: ")

# Read when user was born
print("Enter month of birth for:", name, end='')
month_born = int(input(": "))

# Read year born
year_born = float(input("Enter year of birth for " + name + ": "))

# Calculate the leap year

leap_year = year_born%4
leap_year2 = year_born%400


century_test = year_born%100

print()

# Determine the season of the month
# Determine if it was a leap year and respond with the result


# Read winter season

if month_born <= 2:
    print(f'Hello, {name}! You were born in the winter and ')
    if century_test == 0:
        if leap_year2 == 0:
            print(f'{year_born:.0f} was a leap year.')
        else:
            print(f'{year_born:.0f} was not a leap year.')
    else:
        if leap_year == 0:
            print(f'{year_born:.0f} was a leap year.')
        else:
            print(f'{year_born:.0f} was not a leap year.')

elif month_born == 12:
    print(f'Hello, {name}! You were born in the winter and ')
    if century_test == 0:
        if leap_year2 == 0:
            print(f'{year_born:.0f} was a leap year.')
        else:
            print(f'{year_born:.0f} was not a leap year.')
    else:
        if leap_year == 0:
            print(f'{year_born:.0f} was a leap year.')
        else:
            print(f'{year_born:.0f} was not a leap year.')

# Read spring season
        
elif month_born <= 5:
    print(f'Hello, {name}! You were born in the spring and ')
    if century_test == 0:
        if leap_year2 == 0:
            print(f'{year_born:.0f} was a leap year.')
        else:
            print(f'{year_born:.0f} was not a leap year.')
    else:
        if leap_year == 0:
            print(f'{year_born:.0f} was a leap year.')
        else:
            print(f'{year_born:.0f} was not a leap year.')

# Read summer season
        
elif month_born <= 8:
    print(f'Hello, {name}! You were born in the summer and ')
    if century_test == 0:
        if leap_year2 == 0:
            print(f'{year_born:.0f} was a leap year.')
        else:
            print(f'{year_born:.0f} was not a leap year.')
    else:
        if leap_year == 0:
            print(f'{year_born:.0f} was a leap year.')
        else:
            print(f'{year_born:.0f} was not a leap year.')
            
# Read fall season

elif month_born <= 11:
    print(f'Hello, {name}! You were born in the fall and ')
    if century_test == 0:
        if leap_year2 == 0:
            print(f'{year_born:.0f} was a leap year.')
        else:
            print(f'{year_born:.0f} was not a leap year.')
    else:
        if leap_year == 0:
            print(f'{year_born:.0f} was a leap year.')
        else:
            print(f'{year_born:.0f} was not a leap year.')

# Read invalid season
        
else:
    print(f'Hello, {name}! {month_born} does not match the months in a year and ')
    if century_test == 0:
        if leap_year2 == 0:
            print(f'{year_born:.0f} was a leap year.')
        else:
            print(f'{year_born:.0f} was not a leap year.')
    else:
        if leap_year == 0:
            print(f'{year_born:.0f} was a leap year.')
        else:
            print(f'{year_born:.0f} was not a leap year.')




