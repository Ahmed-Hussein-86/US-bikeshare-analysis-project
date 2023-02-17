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
    city_selection = input('To view the available bikeshare data, kindly type:\n    The letter (ch) for Chicago\n    The letter (ny) for New York City\n    The letter (w) for Washington\n  ').lower()

    while city_selection not in ['ch','ny','w']:
        print('That\'s invalid input. Please Enter a valid option: ch or ny or w') # tell the user that the input is not right.
        city_selection = input('To view the available bikeshare data, kindly type:\n    The letter (ch) for Chicago\n    The letter (ny) for New York City\n    The letter (w) for Washington\n  ').lower()

    if city_selection == 'ch':
        city = 'chicago'
    if city_selection == 'ny':
        city = 'new_york_city'
    if city_selection == 'w':
        city = 'washington'

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    month = input('To filter {}\'s data by a particular month, please type the month name or all for not filtering by month: \n-January\n-February\n-March\n-April\n-May\n-June\n-All\n:'.format(city.title())).lower()
    while month not in months:
        print('That\'s invalid month input. Please Enter a valid month option.') # tell the user that the input is not right.
        month = input('To filter {}\'s data by a particular month, please type the month name or all for not filtering by month: \n-January\n-February\n-March\n-April\n-May\n-June\n-All\n\n:'.format(city.title())).lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    week_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    day = input('To filter {}\'s data by a particular day, please type the day name or all for not filtering by day: \n-Monday\n-Tuesday\n-Wednesday\n-Thursday\n-Friday\n-Saturday\n-Sunday\n-All\n:'.format(city.title())).lower()
    while day not in week_days:
        print('That\'s invalid day input. Please Enter a valid day option.') # tell the user that the input is not right.
        day = input('To filter {}\'s data by a particular day, please type the day name or all for not filtering by day: \n-Monday\n-Tuesday\n-Wednesday\n-Thursday\n-Friday\n-Saturday\n-Sunday\n-All\n:'.format(city.title())).lower()


    print('='*40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = pd.to_datetime(df['Start Time'], format='%H:%M:%S').dt.month
    df['day_of_week'] = pd.to_datetime(df['Start Time'], format='%H:%M:%S').dt.weekday_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'] = pd.to_datetime(df['Start Time'], format='%H:%M:%S').dt.month
    common_month = df['month'].mode()[0]
    print('Most common month :', common_month)



    # TO DO: display the most common day of week
    df['weekday'] = pd.to_datetime(df['Start Time'], format='%H:%M:%S').dt.weekday_name
    common_weekday = df['weekday'].mode()[0]
    print('Most common weekday:', common_weekday)


    # TO DO: display the most common start hour
    df['hour'] = pd.to_datetime(df['Start Time'], format='%H:%M:%S').dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Frequent Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_strt_startion = df['Start Station'].mode()[0]
    print('Most common Start Station :', common_strt_startion)

    # TO DO: display most commonly used end station
    common_end_startion = df['End Station'].mode()[0]
    print('Most common End Station :', common_end_startion)


    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df["Start Station"] + " <--> " + df["End Station"]
    #common_comb_stations = df.groupby(['Start Station','End Station']).count().sort_values(by=['Start Station','End Station'], axis = 0).iloc[0]
    freq_comb_stations = df['route'].mode()[0]
    print('Most frequent combination of start station and end station trip:', freq_comb_stations)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*40)

def format_seconds_to_hhmmss(seconds):
    hours = seconds // (60*60)
    seconds %= (60*60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    tot_trvl_time=df['Trip Duration'].sum()
    formated_tot_trvl_time = format_seconds_to_hhmmss(tot_trvl_time)
    print ("Total travel time in HH:MM:SS = ",formated_tot_trvl_time)


    # TO DO: display mean travel time
    avg_trvl_time=df['Trip Duration'].mean()
    #print ("Total travel time in seconds:",avg_trvl_time)
    formated_avg_trvl_time = format_seconds_to_hhmmss (avg_trvl_time)
    print ("Average travel time in HH:MM:SS =",formated_avg_trvl_time)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users_type = df['User Type'].value_counts().to_frame()
    print ("Count of user type:\n",users_type)

    try:
        # TO DO: Display counts of gender
        users_gender = df['Gender'].value_counts().to_frame()
        print ("Count of gender:\n",users_gender)


        # TO DO: Display earliest, most recent, and most common year of birth
        birth_year = df['Birth Year']
        # the most common birth year
        most_common_year = birth_year.mode()[0]
        print("The most common birth year:", int(most_common_year))
        # the most recent birth year
        most_recent = birth_year.max()
        print("The most recent birth year:", int(most_recent))
        # the most earliest birth year
        earliest_year = birth_year.min()
        print("The most earliest birth year:", int(earliest_year))

    except KeyError: # dealing with Washington
        print('Sorry! Geneder and Birth Year data are not available for Washington city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('='*40)


def display_raw_data(city):

    df = pd.read_csv(CITY_DATA[city])

    # setting counter for the rows
    start_loc = 0

    print('\nRaw data are available to check... \n')

    # collecting user input
    user_selected_opt = input('To view the availbale raw data in chuncks of 10 rows type (y) for Yes or type (n) for No if you wan\'t \n').lower()

   # Validating user input
    while user_selected_opt not in ['y', 'n']:
        print('That\'s invalid input, pleas type (y) for yes or (n) for no.')
        user_selected_opt = input('To view the availbale raw data in chuncks of 10 rows type (y) for Yes or type (n) for No if you wan\'t \n').lower()

    # action based on yes
    while user_selected_opt == 'y':
        print(df.iloc[start_loc:start_loc+10])
        start_loc+=10
        user_selected_opt = input('Do you want to display 5 more rows? type (y) for Yes or type (n) for No ').lower()

    # action based on no
    if user_selected_opt == 'n':
        print('\nYou have selected not to display any/other raw data!')

    print('='*40)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('You haven\'t select (y) to restart the program, it will exit now...exiting!')
            break
            
if __name__ == "__main__":
	main()
