import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    while True:
        city = input("Enter the city that you want to explore: \n")
        city = city.lower()
        if city in ["chicago","new york city","washington", '\n \n']:
            break
        else:
            print("Unknown City, Enter a valid city: \n")


    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("Please enter the month needed, or type all to apply no month filter \n")
        month = month.lower()
        if month in ["all","january","february","march","april","may","june","july","august","september","october","november","december"]:
            if month != 'all':
                month = month.title()
            break
        else:
            print("wrong input, please try again \n")



    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter the day needed, or type all to apply no day filter \n")
        day = day.lower()
        if day in ["all","monday","tuesday","wednesday","thursday","friday","saturday","sunday"]:
            if day != 'all':
                day = day.title()
            break
        else:
            print("wrong input, please try again \n")


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != "all":
        df = df[df['month'] == month]

    if day != "all":
        df = df[df['day_of_week'] == day]

    return df

def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('the most common month is, ', df['month'].mode()[0] ,'\n')


    # display the most common day of week
    print('the most common day is, ' ,df['day_of_week'].mode()[0] ,'\n')


    # display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    print('the most common hour is, ' ,df['hour'].mode()[0],'\n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most common start station used was: ' , df['Start Station'].mode()[0])


    # display most commonly used end station
    print('The most common end station used was: ' , df['End Station'].mode()[0])


    # display most frequent combination of start station and end station trip
    df['combination_start_end'] = df['Start Station'] + " " + df['End Station']
    print('The most common combination between stations used was: ' , df['combination_start_end'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time is: ", df['Trip Duration'].sum())


    # display mean travel time
    print("The mean of the travel time is: ", df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("There are %s types of users \n" % df['User Type'].nunique())


    # Display counts of gender

    try:
        print("These are the genders on the data: \n \n %s"  % df['Gender'].value_counts())
    except KeyError:
        print("No data available for the genders for the chosen city")


    # Display earliest, most recent, and most common year of birth
    try:
        print("The most recent year of birth is %s \n \n" % df['Birth Year'].max())
        print("The earliest year of birth is %s \n \n" % df['Birth Year'].min())
        print("The most common year of birth is %s \n \n" % df['Birth Year'].mode()[0])
    except KeyError:
        print("No data available for year of birth for the selected city")




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?")
    view_data.lower()
    start_loc = 0
    while (view_data == 'yes'):
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_display = input("Do you wish to continue?: ").lower()
        if view_display == 'no':
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
