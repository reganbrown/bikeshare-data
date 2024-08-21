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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''

    while city != 'new york city' and city != 'washington' and city != 'chicago':
        city = input('Please type one of the following to begin: new york city, washington, chicago\n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ''

    while month != 'all' and month != 'january' and month != 'february' and month != 'march' and month != 'april' and month != 'may' and month != 'june':
        month = input('Please enter a month between January and June to filter by, or type all to filter by all months\n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ''
    while day != 'all' and day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day != 'friday' and day != 'saturday' and day != 'sunday':
        day = input('Please enter a day of the week to filter by, or type all to filter by all days\n').lower()

    print('-'*40)
    return city, month, day


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

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]
  
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    
    print('Most Popular Month: ', popular_month)


    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    
    print('Most Popular Day: ', popular_day)

    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    
    print('Most Popular Hour: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    
    print('Most Popular Start Station: ', popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    
    print('Most Popular End Station: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = (df['Start Station'] + ' ' + df['End Station']).mode()[0]

    print('Most Popular Trip: ', popular_trip) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time {} seconds".format(total_travel_time))

    # TO DO: display mean travel time
    average_travel_time = df['Trip Duration'].mean()
    print("Average trip duration is {} seconds".format(average_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print(user_types)


    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print(gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth = df['Birth Year'].min()
        recent_birth = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()[0]
    
        print('The earliest date of birth is {}, the most recent date of birth is {} and the most common date of birth is {}'.format(int(earliest_birth), int(recent_birth), int(common_birth)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def data_rows(df): 
    last_index = len(df) - 1
    print("There are {} rows of data in your filters\n".format(last_index))
    
    x = 0
    y = 0
    user_confirmation = ''
    user_confirmation = input('Would you like to check the first 5 rows of the dataset related to the chosen city? Type "yes" to continue\n').lower()
    if user_confirmation == 'yes':
        print(df.head())
        x = 5
        y = 10
        user_confirmation = input('Would you like the next 5 rows? Type "yes" to continue\n').lower()
        while user_confirmation == 'yes':
            if x > last_index:
                print("no additional rows remaining")
                break
            else:
                print(df.iloc[x:y])
                x = y
                y += 4000
                user_confirmation = input('Would you like the next 5 rows? Type "yes" to continue\n').lower()


       

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data_rows(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
