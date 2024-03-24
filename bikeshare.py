import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }
Cities=['Chicago','New York City','Washington']
Months=['All','January','February','March','April','May','June']
Days  =['All', 'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thurusday', 'Friday']

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        
        try:
            city=input("What city? Chicago, New York City, Washington\n")
            city=city.title()
            month=input("What month? All, January ,February, March, April, May, June\n")
            month=month.title()
            day=input("What day? All, Saturday, Sunday, Monday, Tuesday, Wednesday, Thurusday, Friday\n")
            day=day.title()
            if city in Cities and month in Months and day in Days:
                break
            else:
                print("invalid input try again\n")
        except:
            
            print("Enter Valid City Please \n")    
       
        
       
        
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

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'All':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

 
    popular_month = df['month'].mode()[0]
    print(f"Most Repeated Month Is : {popular_month}")
   
 
    repeated_day = df['day_of_week'].mode()[0]
    print(f"\nMost Repeated Day Is : {repeated_day}")

   
    repeated_hour = df['hour'].mode()[0]
    print(f"\nMost Repeated Start Hour Is : {repeated_hour}") 
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

 
    Start_Station = df['Start Station'].mode()[0]
    print(f"Most Common Start Staion Is : {Start_Station}")

 
    End_Station = df['End Station'].mode()[0]
    print(f"\nThe most commonly used end station: {End_Station}")

    
    df['Start With End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    Start_and_End = df['Start With End'].mode()[0]
    print(f"\n Most Repeated Start And End Station Combined IS : {Start_and_End}.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

  
    Total_Trip_Duration = df['Trip Duration'].sum()
    print(f"\n Total Trip Duration Is :{Total_Trip_Duration} ")
   
    Total_Mean_Time = df['Trip Duration'].mean()
    print(f"\n Total Trip Duration Is :{Total_Mean_Time} ")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    try:
        user_type = df['User Type'].value_counts()
        print(f"Number Of Users Is : {user_type}")
    except:
        print("No Users ?\n")
    
    try:
        gender_count = df['Gender'].value_counts()
        print(f"Number Of Gender Count Is : {gender_count}")
    except:
        print("No Gender? \n")
   
    try:
        earliest = int(df['Birth Year'].min())
        most_recent = int(df['Birth Year'].max())
        most_common_year = int(df['Birth Year'].mode()[0])
        print(f"\n\nThe Earliest Year Is: {earliest}\n\nThe Most Recent Year Is : {most_recent}\n\nThe Most Common Year Is : {most_common_year}\n\n")
    except:
        print("Error \n")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        row = 0
        do = pd.read_csv(CITY_DATA[city])
        while True:
            viewData = input("Would you like to see raw data in the city you entered? Type 'Yes' or 'No'.")
            if viewData.title() == "Yes":
                print(do.iloc[row:(row+5)])
                row+=5
            elif viewData.title() == "No":
                break
                
           
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
