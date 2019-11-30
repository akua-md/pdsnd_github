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
    print('Hello Welcome to the Bikeshare Centre! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city_list=['new york city','chicago','washington']
    city_check =1
    while city_check == 1:
        try:
            city = str(input('Enter your City: new york city/chicago/washington:---  ').lower())
            if city in city_list:
                city_check += 1
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
            #print("Enter Letters Only to Proceed: ")
            #print("User Input Expected: ")
            
            

    # TO DO: get user input for month (all, january, february, ... , june)
    month_list=['all', 'january', 'february','march', 'april', 'may','june']
    month_entry_check = 1
    while  month_entry_check == 1:
        try:
            month = str(input("Enter the month : january to June:--- ").lower())
            if month in month_list:
                month_entry_check +=1
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
            
                  

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list=['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day_checker=1
    while day_checker == 1:        
        try:
            day = input('Select the day of the week from monday to friday :---  ').lower()
            if day in day_list:
                day_checker += 1   
        except:
            print("Unexpected error:", sys.exc_info()[0])
            raise
            
            
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
    
    #convert the start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #extract month and day of week from StartTime t crreate new columns
    df['month'] =df['Start Time'].dt.month
    df['day_of_week'] =df['Start Time'].dt.weekday_name
    
    #filter by month if applicable
    if month != 'all':
        #use the index of the month list to get the coreesponding int
        months =['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        
        df=df[df['month'] == month]
        
    if day !='all':
        df =df[df['day_of_week'] ==day.title()]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    pop_month =df['month'].mode()[0]
    print("The Most Common Month is: ", pop_month )
    

    # TO DO: display the most common day of week
    pop_day_of_week = df['day_of_week'].mode()[0]
    print("The Most Common Week is: ", pop_day_of_week )


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The Most Common Hour is: ", popular_hour )


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    station_count = df['Start Station'].value_counts()
    print("Most commonly used Start Station: ", station_count.head(1))    

    # TO DO: display most commonly used end station
    end_station_count = df['End Station'].value_counts()
    print("  Most commonly used End Station: ", end_station_count.head(1))  

    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    

    # TO DO: display total travel time
    x ="yes"
    i = 5
    while x == "yes":
        
        print("Calculating Total travel Time" )
        total_travel_time= df.groupby(['Start Time'])['Trip Duration'].sum()
        print(total_travel_time.head(i))
        i = i+ 5
        
        x=str(input("Do you want to continue? yes / no  --- ").lower())
    

    # TO DO: display mean travel time
    
    x ="yes"
    i = 5
    while x == "yes":
        print("Calculating  Mean travel Time")
        mean_travel_time= df.groupby(['Start Time'])['Trip Duration'].mean()
        print(mean_travel_time.head(i))
        i += 5
        
        x=str(input("Do you want to continue? yes / no  --- ").lower())
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print("Displaying UserType Count: ", user_type_count)
    
    #city,month,day=get_filters()
    
    if city == 'new york city' or city =='chicago':
        # TO DO: Display counts of gender
        gender_count = df['End Station'].value_counts()
        print(gender_count)
        
        # TO DO: Display earliest, most recent, and most common year of birth
        print('   Earliest Birth Year:',df['Birth Year'].min())
        print('Most Recent Birth Year:',df['Birth Year'].max())
        print('      Most Common Year:')
        common_year =df['Birth Year'].value_counts()
        print(common_year.head(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        global city

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
