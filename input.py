from datetime import datetime


#Basic user input collecting the information which will allow us to search for the nearest blockheight.
#Exceptions are included for births before the start of the bitcoin timechain and for ValueErrors.
user_input = ''
while user_input != 'p':
    try:
        child_name = input('Enter the name of the wallet owner as it should be printed:\n')
        birth_year = int(input('Enter the year of birth in four digit format ie 1971\n'))
        if birth_year < 2009: print('Sorry, the bitcoin time chain started in 2009 so your blockheight will not be accurate.')
        birth_month = int(input('Enter the month of birth in two digit format ie 04 for April\n'))
        if birth_month > 12: raise ValueError('Invalid Month')
        birth_day = int(input('Enter the day of birth in two digit format ie 05 for the 5th\n'))
        if birth_day > 31: raise ValueError('Invalid Date')
        birth_hour = int(input('Enter the birth hour in 24 hour format (ie 15 for 3pm or 06 for 6am\n'))
        if birth_hour >= 24: raise ValueError('Invalid Time')
        birth_min = int(input('Enter the minute of birth in two digit format ie 05 for :05\n'))
        if birth_min >= 60: raise ValueError('Invalid Time')
        time_zone = int(input('What timezone/Region was the child born?\n 1 = Arizona 2 = Pacific Time, 3 = Mountain Time, 4 = Central Time, 5 = Eastern Time\n'))
        adjusted_time = ''


#The timestamp information I collected is based on UTC time. Even though I do not have all of the blocks in my dictionary,
# I wanted to account for timezone variations. The easiest way I could determine without having potential cascading date changes
#for end of month and end of day births were to use unix time.
        def get_info():
            global adjusted_time
            global birth_month
            if time_zone == 1: adjusted_time = 25200
            elif time_zone == 2:
                if 3 < birth_month < 11: adjusted_time = 25200
                else: adjusted_time = 28800
            elif time_zone == 3:
                if 3 < birth_month < 11: adjusted_time = 21600
                else: adjusted_time = 25200
            elif time_zone == 4:
                if 3 < birth_month < 11: adjusted_time = 18000
                else: adjusted_time = 21600
            elif time_zone == 5:
                if 3 < birth_month < 11: adjusted_time = 14400
                else: adjusted_time = 18000
            else: pass
        get_info()

#This is where the final time is calculated
        def timeconv():
            global adjusted_time
            defualt_date = datetime(birth_year, birth_month, birth_day, birth_hour, birth_min)
            unix_time = int(defualt_date.timestamp())
            time_adjusted = (unix_time + int(adjusted_time))
            return time_adjusted
        timeconv()

#Exception handeling.
    except ValueError as excpt:
        print(excpt)
        print('Please enter a valid date & time field')

#Confirmation screen before printing to file.
    print(child_name, 'Bitcoin Wallet')
    print(f"{birth_year}-{birth_month}-{birth_day} {birth_hour}:{birth_min}")
    user_input = input('If this information is correct, press p to print or press any key to start over.')
