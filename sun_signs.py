# astrology sun sign calculator using file handling

#
## initialization
#

print("Checking your birthdays.txt file to calculate astrological sun signs for each person listed with a birthdate. Birthdate must be entered in YYYY-MM-DD format, with a comma separating persons name from date.")

#imports python module that supplies classes for manipulating dates and times
import datetime
#imports regex
import re


#
## functions
#

# function calculating out astrology sun signs from month and day of birth
def get_sign(birthdate):
    month, day = birthdate.month, birthdate.day
    if (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return "Pisces"
    elif (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    return None

# uses regex to check formatting
def validate_line_format(line):
    #checks that name is alphbetical input, and date format is YYYY-MM-DD
    pattern = r'^[A-Za-z ]+, \d{4}-\d{2}-\d{2}$'
    return re.match(pattern, line)

# read file birthdate data and use data to calculate what sign the birthdate goes to

def process_file(filename):
    updated_data = [] 
    #creates empty list for updated data
    with open(filename, 'r') as file:
            for line in file: #loop through each line in our file
                line = line.strip() 
                if validate_line_format(line): #uses our regex function to check if the data formatting is going to work
                    name, date_str = line.split(', ')
                    birthdate = datetime.datetime.strptime(date_str, '%Y-%m-%d')
                     # reads birthdate data and cleans up formatting and sets to a format readable by the get sign function
                    sun_sign = get_sign(birthdate)
                     #uses function to figure out what sun sign goes to our initially provided date read from the file
                    updated_data.append(f"{name}, {date_str}, {sun_sign}\n")
                     #append updated data list to include sun sign to follow birthdate
                else:
                    print(f"Invalid format: {line}") #throws error with line number if file text formatting does not work

     # adds updated date back to our file in write mode
    with open(filename, 'w') as file:
        file.writelines(updated_data) #writes to lines by grabbing data from updated data list we populated with the loop

#
## execution
#

filename = 'birthdays.txt'
process_file(filename)

print("done! check your birthdays.txt file for your updated data set, now including each person's sun sign appended on their line in the file.")