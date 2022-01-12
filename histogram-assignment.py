import csv
import pandas as pan
import matplotlib.pyplot as plt
import random as rand

df=pan.read_csv('activity.csv')
print(df.info())
print(df)

def get_NA(df):
    return df.isnull().sum()

print('Number of NANS:')
print(get_NA(df))

def fill(): #fill in NA with random  values and create new dataset
    new_dataset =df.copy()
    new_dataset.fillna(rand.randint(0,100), inplace=True)
    return new_dataset

print('\n new_dataset \n')
new_dataset=fill() #df.dropna (so that inplace=True)

def get_steps_per_day(df):
    steps_per_day = df.groupby('date').sum()['steps']
    return steps_per_day.to_frame()

print('Daily Steps')
print(get_steps_per_day(df))

def histogram_of_total_steps_per_day(df):
    day_steps = get_steps_per_day(df)
    plt.hist(day_steps)
    plt.xlabel('Total Steps')
    plt.ylabel('Days')
    plt.title('Histogram of Total Steps Per Day')
    plt.legend()
    plt.show()

histogram_of_total_steps_per_day(df)

def get_mean_pday(df): #function to get mean of steps per day
    mean_pday=df.groupby('date').mean()['steps']
    return mean_pday.to_frame().dropna()

print('Mean')
print(get_mean_pday(df))
def get_median_pday(df):
    mean_pday=df.groupby('date').median()['steps']
    return mean_pday.to_frame().dropna()

print('Median')
print(get_median_pday(df))

#time series plot of the 5-minute interval (x-axis) and the average number of steps taken, averaged across all days (y-axis)
def plot_mean_of_total_steps_per_day():
    plt.plot(get_mean_pday(df), 'r')
    plt.xlabel('5-minute Interval')
    plt.ylabel('Mean Steps Per Day')
    plt.title('Mean of Total Steps Per Day')
    plt.legend()
    plt.show()

plot_mean_of_total_steps_per_day()

print('DAY THAT HAS MOST STEPS:')
def get_date_that_have_max_steps_per_5_minute_interval():
    steps_per_day = get_steps_per_day(df)
    return steps_per_day.idxmax()

print(get_date_that_have_max_steps_per_5_minute_interval())

histogram_of_total_steps_per_day(new_dataset)
print('MEAN OF NEW DATASET')
print(get_mean_pday(new_dataset))
print('MEDIAN OF NEW DATASET')
print(get_median_pday(new_dataset))

#classify dates to weekend or weekdays
df['WEEKDAY'] = pan.to_datetime(df['date']).dt.dayofweek
weekd=[]
weeknd=[]
weekd_avg=[] #empty list for weekday average steps
weeknd_avg=[]
print(df)

for i in range(len(df)):
    if df['WEEKDAY'][i]<=5:
        weekd.append(df['date'][i])
        weekd_avg.append(df['steps'][i])
    else:
        weeknd.append(df['date'][i])
        weeknd.append(df['steps'][i])
print(weekd)
print(weeknd)
print(weekd_avg)
print(weeknd_avg)


# plotting the average steps per day for weekdays and weekends
plt.figure(figsize=(30), dpi=150)
plt.plot(weekd, weekd_avg, 'ro')
plt.plot(weeknd, weeknd_avg, 'bo')
plt.xlabel('Date')
plt.ylabel('Average Steps Per Day')
plt.title('Average Steps Per Day for Weekdays and Weekends')
plt.show()