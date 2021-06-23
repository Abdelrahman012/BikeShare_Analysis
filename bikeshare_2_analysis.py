import time
import pandas as pd

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Hello! Let\'s explore some US bikeshare data!')
    while True:
        city = input("Select the city that you want to explore:Chicago, New York City or Washington: ").lower()
        list_city = ['chicago', 'new york city', 'washington']
        
        if city in list_city:
            break
        else:
            print("please,be carful while entering the letters of your city")
            print("please, Repeat again")

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input("select in which month you want to explore: January, February, March, April, May, June or All: ").lower().title()
        months_list = ["January", "February", "March", "April", "May", "June", "All"]
        if month in months_list:
            break
        else:
            print("please,be carful while entering the letters of your month")
            print("please, Repeat again")

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("If you please, enter the day from Saturday, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or All: ").lower().title()
        list_days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "All"]
        if day in list_days:
            break
        else:
            print("please,be carful while entering the letters of your day")
            print("please, Repeat again")

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
    df["Start Time"]=pd.to_datetime(df["Start Time"])
    df["Pro Month"] = df["Start Time"].dt.month_name()
    df["Pro Day"] = df["Start Time"].dt.day_name()
    df["Pro Hour"] = df["Start Time"].dt.hour

    if month != "All":
        df = df[df["Pro Month"] == month]

    if day != "All":
        df = df[df["Pro Day"] == day]

    return df

def display_data(df):    
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    start_loc = 0
    while True:
        if view_data== "yes":
            print(df.iloc[0+start_loc:5+start_loc])  
            start_loc += 5
            view_display = input("Do you wish to continue? to show next 5 rows of data: ").lower()
            if view_display=="no":
                break
        
        
def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month == "All":
        com_month = df["Pro Month"].dropna()
        if com_month.empty:
            print("There's no common month in this data")
        else:
            com_month = com_month.mode()[0]
            print("The most common month in thi data is " + str(com_month))
    else:
        print("You have not chosen \"All\" to get the most common month in thid data")

        # display the most common day of week
    if day == "All":
        com_day = df["Pro Day"].dropna()
        if com_day.empty:
            print("There's no common day in this data")
        else:
            com_day = com_day.mode()[0]
        print("The most common day is " + str(com_day))
    else:
        print("You have not selected \"All\" choice to get the most common day in this data.")

    # display the most common start hour
    com_hour = df["Pro Hour"].dropna()
    if com_hour.empty:
        print("There's no common hour.")
    else:
        com_hour = com_hour.mode()[0]
        print("The most common hour in thid data is " + str(com_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)






def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # TO DO: display most commonly used start station
    
    com_Sta_Sta=df["Start Station"].dropna()
        
    if com_Sta_Sta.empty:
        print("There is no common Start Station")
    else:
        com_Sta_Sta=df["Start Station"].mode()[0]
        print("the most commonly used start station is: "+str(com_Sta_Sta))

    
    # TO DO: display most commonly used end station
    com_end_station=df["End Station"].dropna()
    if com_end_station.empty:
        print("there is no common  end station")
    else:
        com_end_station=df["End Station"].mode()[0]
        print("the most commonly used end station is: "+str(com_end_station))
    # TO DO: display most frequent combination of start station and end station trip
    most_freq_st_end = df[["Start Station", "End Station"]].dropna()
    if most_freq_st_end.empty:
        print("There's no most frequent start and end stations.")
    else:
        most_freq_st_end=most_freq_st_end.groupby(["Start Station","End Station"]).size().sort_values(ascending=False)
        numbers_of_trip=most_freq_st_end.iloc[0]
        stations=most_freq_st_end[numbers_of_trip==most_freq_st_end].index[0]

        Start,End= stations

        print("the most frequent start station is " + str(Start) + "and the most frequent end station is " + str(End)) 
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time=df["Trip Duration"].dropna()

    
    if travel_time.empty:
        print("there is no mean travel time")
    else:
        Total_travel_time=df["Trip Duration"].sum()
    # TO DO: display mean travel time
        mean_Travel_time=df["Trip Duration"].mean()

        print("the mean of travel time is "+ str(mean_Travel_time)+ " the total travel time is "+str(Total_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users_counts= df["User Type"].dropna()
    if users_counts.empty:
        print("there is no users")
    else:
        users_counts=df["User Type"].value_counts()           
        print("count of user types is "+str(users_counts))
    # TO DO: Display counts of gender
    if "Gender" in df:
        counts_of_gender=df["Gender"].dropna()
        if counts_of_gender.empty:
            print("There no data about gender")
        else:
            counts_of_gender=df["Gender"].value_counts()
            print("counts of gender is "+str(counts_of_gender))
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df:
        birth_year=df["Birth Year"].dropna()
        if birth_year.empty:
            print("there is no data about Birth Year")
        else:
            early_birth_years=df["Birth Year"].min()
            print("the earliest birth year is: "+str(early_birth_years))

            most_recent=df["Birth Year"].max()
            print("the most recent birth year is: "+ str(most_recent))

            com_birth_year=df["Birth Year"].mode()[0]
            print("the most common birth year is: "+str(com_birth_year))
    else:
        print('Birth Year stats cannot be calculated because Gender does not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

        



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
