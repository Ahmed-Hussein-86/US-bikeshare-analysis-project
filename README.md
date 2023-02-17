# US-bikeshare-analysis-project
This is a python project to analyze US bikeshare using pandas and numpy 


This code was wriiten following the predefined template provided by Udity during Data Analysis Professional track

- Naming of functions are same.
- Some additional functions has been added for time formatting "format_seconds_to_hhmmss" to make the time data human readable
- There are many comments between codes lines for further illustrations.
- For raw data displaying, I have load the data of selected 'city' without filttering options, as it's raw data should show data as it..
- Some modifications have been done on printed output statements for adding more interactive and nice appearnce while dealing with user's input.
- The main code strcture is as below:

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(city)
        
        restart = input('\nWould you like to restart? Enter (y) for yes or (n) for no.\n')
        if restart.lower() != 'y':
            print('You didn\'t select (y) to restart...exiting!')
            break

if __name__ == "__main__":
	main()


