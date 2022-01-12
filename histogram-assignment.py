import csv
import pandas as pan
import matplotlib.pyplot as plt
import random as rand

df=pan.read_csv('activity.csv')
print(df.info())
print(df)

def get_number_of_Nans(df):
    return df.isnull().sum()

print('NUMBER OF NANS:')
print(get_number_of_Nans(df))

def fill_in_Nans_with_random_values_and_create_new_dataset():
    new_dataset =df.copy()
    new_dataset.fillna(rand.randint(0,100), inplace=True)
    return new_dataset

print('\n new_dataset \n')
new_dataset=fill_in_Nans_with_random_values_and_create_new_dataset()
# df.dropna(inplace=True)

def get_steps_per_day(df):
    steps_per_day = df.groupby('date').sum()['steps']
    return steps_per_day.to_frame()

print('steps_per_day')
print(get_steps_per_day(df))

def histogram_of_total_steps_per_day(df):
    steps_per_day = get_steps_per_day(df)
    plt.hist(steps_per_day)
    plt.xlabel('Total Steps')
    plt.ylabel('Days')
    plt.title('Histogram of Total Steps Per Day')
    plt.show()

histogram_of_total_steps_per_day(df)

def get_mean_of_steps_per_day(df):
    mean_per_day=df.groupby('date').mean()['steps']
    return mean_per_day.to_frame().dropna()

print('MEAN')
print(get_mean_of_steps_per_day(df))
def get_median_of_total_steps_per_day(df):
    mean_per_day=df.groupby('date').median()['steps']
    return mean_per_day.to_frame().dropna()

print('MEDIAN')
print(get_median_of_total_steps_per_day(df))

#time series plot of the 5-minute interval (x-axis) and the average number of steps taken, averaged across all days (y-axis)
def plot_mean_of_total_steps_per_day():
    plt.plot(get_mean_of_steps_per_day(df), 'r')
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
print(get_mean_of_steps_per_day(new_dataset))
print('MEDIAN OF NEW DATASET')
print(get_median_of_total_steps_per_day(new_dataset))

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