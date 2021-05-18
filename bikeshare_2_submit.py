import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which of the following cities would you like to know about? - Chicago, New York City or Washington: ")
        city = city.lower()
        if city in CITY_DATA.keys():
            break
        else:
            print("That is not a valid input. Try again!")

    # get user input for month (all, january, february, ... , june)

    month_list = ['all','january','february','march','april','may','june','july','august','september','october','november','december']

    while True:
        try:
            month_name = input("Next, please type the name of a month, e.g. 'january', or type 'all' to apply no filters: ")
            month_num = month_list.index(month_name.lower())
            break
        except:
            print("That is not a valid input. Try again!")

    # get user input for day of week (all, monday, tuesday, ... sunday)

    day_list = ['All','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

    while True:
        day_of_week = input("Finally, please enter the name of a day of the week, e.g. 'sunday', or type 'all' to apply no filters: ")
        day_of_week = day_of_week.title()
        if day_of_week in day_list:
            break
        else:
            print("That is not a valid input. Try again!")

    print('-'*40)
    print("Thanks! Your filters are - City: {}, Month: {}, Day of Week: {}\n".format(city.title(),month_name.title(),day_of_week))
    return city, month_num, day_of_week


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.day_name()

    if month != 0:
        df = df[df['Month'] == month]

    if day != 'All':
        df = df[df['Day of Week'] == day]

    return df

def show_raw_data(df):
    """ Shows the extracted raw data to users upon their choise five rows at a time """

    current_pos = 0
    go_on = input("Do you want to see the first five rows of the extracted dataset? (Type y/n)")
    while True:
        if go_on == 'y':
            print()
            print(df[current_pos:current_pos + 5])
            current_pos += 5
            if current_pos >= len(df):
                print("You have reached the end of the dataset!")
                break
            else:
                go_on = input("Do you want to see the next five rows? (Type y/n)")
        else:
            print("Noted!")
            break

def choose_function(df,func1,func2,func3,func4):
    """
    Lets users choose which statistic output they like to see
    Args in the order of extracted df, time_stats, station_stats, trip_duration_stats and user_stats
    """

    go_on = 'y'
    while go_on == 'y':
        choice = input("\
Let's look into some statistical information!\n\
Please type 1/2/3/4 from the following options:\n\
\n\
Statistics on the...\n\
1. The most frequent times of travel\n\
2. The most popular stations and trip\n\
3. The trip duration\n\
4. The user profiles:\n\
>>> Your choice: ")

        if choice == '1':
            func1(df)
        elif choice == '2':
            func2(df)
        elif choice == '3':
            func3(df)
        elif choice == '4':
            func4(df)
        else:
            print("Oops! Please choose from 1-4!")
        go_on = input("Do you want to continue? (Type (y/n))")

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    if __name__ == '__main__':

        print('\nCalculating The Most Frequent Times of Travel...\n')
        start_time = time.time()

        # display the most common month
        print("The most common month is {}.".format(df['Month'].mode()[0]))

        # display the most common day of week
        print("The most common day of week is {}.".format(df['Day of Week'].mode()[0]))

        # display the most common start hour
        df['Hour'] = df['Start Time'].dt.hour
        print("The most common start hour is {}.".format(df['Hour'].mode()[0]))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    if __name__ == '__main__':

        print('\nCalculating The Most Popular Stations and Trip...\n')
        start_time = time.time()

        # display most commonly used start station
        print("The most commonly used start station is {}.".format(df['Start Station'].mode()[0]))

        # display most commonly used end station
        print("The most commonly used end station is {}.".format(df['End Station'].mode()[0]))

        # display most frequent combination of start station and end station trip
        df['Route'] = df['Start Station'] + " + " + df['End Station']
        print("The most commonly used route is {}.".format(df['Route'].mode()[0]))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    if __name__ == '__main__':

        print('\nCalculating Trip Duration...\n')
        start_time = time.time()

        # display total travel time
        print("The total travel time is {} minutes.".format(df['Trip Duration'].sum()))

        # display mean travel time
        print("The mean travel time is {} minutes.".format(df['Trip Duration'].mean()))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    if __name__ == '__main__':

        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        print("The breakdown of user types is: \n{}\n".format(df['User Type'].value_counts()))

        try:
        # Display counts of gender
            print("The breakdown of gender is: \n{}\n".format(df['Gender'].value_counts()))

        # Display earliest, most recent, and most common year of birth
            print("The earliest year of birth in the data is {}.".format(str(df['Birth Year'].min()).split('.')[0]))
            print("The most recent year of birth in the data is {}.".format(str(df['Birth Year'].max()).split('.')[0]))
            print("The most common year of birth in the data is {}.".format(str(df['Birth Year'].mode()[0]).split('.')[0]))

        except:
            print("The data of Washington does not have the input of gender or birth years.")

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        df_rows = len(df.index)

        if df_rows > 0:
            print("\nYou have got {} rows in the extracted dataset.".format(df_rows))
            show_raw_data(df)
            choose_function(df,time_stats,station_stats,trip_duration_stats,user_stats)
        else:
            print("\nThere is no corresponding data for your filters. Try different ones!\n")

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Thank you for tyring our service!")
            break


if __name__ == "__main__":
	main()
