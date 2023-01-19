#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!\navailable cities are:\nchicago\nnew york city\nwashington')

    while True:        
        city=input('correctly type name of city to filter by:\n ').lower()
        if city in CITY_DATA.keys():
            break
            
    months=['January','February','March','April','May','June','All']
    days=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','All']
    
    print('\n you can filter by month if you want!')
    while True:        
        month=input(' correctly type month name or "all" to skip:\n ').title()        
        if month in months:
            break    

    print('\n you can filter by day if you want!')
    while True:
        day=input(' correctly type day name or "all" to skip:\n ').title()        
        if day in days:
            break

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    df=pd.read_csv(CITY_DATA[city])
    rawdata=df
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month_name()
    df['day']=df['Start Time'].dt.day_name() 
    df['hour']=df['Start Time'].dt.hour
    df['start_to_end']=df['Start Station']+' to '+df['End Station']
    
    if month!='All':      
        df=df[df['month']==month.title()]
    if day!='All':        
        df=df[df['day']==day.title()]   
    
    return df,rawdata
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('statistics on The Most Frequent Times of Travel...\n')
    
    # display the most common month
    print('the most popular month: ',df['month'].mode()[0])
    
    # display the most common day of week
    print('the most popular day of week: ',df['day'].mode()[0])

    # display the most common start hour
    print('the most popular hour: ',df['hour'].mode()[0])
    print('-'*40)    

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('statistics on the total and average trip duration\n')

    # display most commonly used start station
    print('the most popular start station: ',df['Start Station'].mode()[0])

    # display most commonly used end station
    print('the most popular used end station: ',df['End Station'].mode()[0])
    
    # display most frequent combination of start station and end station trip
    print('the most popular frequent combination of start station and end station trip: ',df['start_to_end'].mode()[0])

    print('-'*40)
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('Trip Duration Metrics...\n')    

    # display total travel time    
    print('total travel time:',df['Trip Duration'].sum())
    
    # display mean travel time
    print('mean travel time:',df['Trip Duration'].mean())
    print('-'*40)


def user_stats(df,city):
    if city!='washington':
        
        print('statistics on bikeshare users.\n')
# Display counts of user type
        print('counts of user types as:\n',df['User Type'].value_counts().to_frame())
        
# Display counts of gender
        print('\ncounts of gender as:\n',df['Gender'].value_counts().to_frame())
# Display earliest, most recent, and most common year of birth
        print('\nearliest year of birth:',df['Birth Year'].min())
        print('most recent year of birth:',df['Birth Year'].max())
        print('most common year of birth:',df['Birth Year'].mode()[0])

    
        print('-'*40)
def disply_raw_data(df):
    print('\n you can display raw data if you want!')
    first_desplayed_line=0
    while True:        
        result=input('type yes to continue displaying data or no to skip:\n').title()        
        if result == 'Yes':
            print(df.loc[first_desplayed_line:first_desplayed_line+4])
            first_desplayed_line+=5
        else:
            break
        


def main():
    while True:
        city, month, day = get_filters()
#        print(city,month,day)

        df,rawdata = load_data(city,month,day)
#        print(df)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        disply_raw_data(rawdata)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
if __name__ == "__main__":
    main()           


# In[ ]:





# In[ ]:





# In[ ]:




