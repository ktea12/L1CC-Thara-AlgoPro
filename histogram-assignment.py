import csv
import matplotlib.pyplot as plt
import statistics as stat
import pygal
import datetime as dtt
filename = 'activity.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dict = {}
    dictInterval = {}
    dictIntervalWeekEnd = {}
    dictIntervalWeekDays = {}
    for row in reader:
        steps = row[0]
        if(steps != "NA"):
            date = row[1]
            date2 = int(dtt.datetime.strptime(date, '%Y-%m-%d').day)
            interval = int(row[2])
            dict.setdefault(str(date), [])
            dict[str(date)].append(int(steps))
            dictInterval.setdefault(interval, [])
            dictInterval[interval].append(int(steps))
            if(date2 % 7 == 0):
                dictIntervalWeekEnd.setdefault(interval, [])
                dictIntervalWeekEnd[interval].append(int(steps))
            else:
                dictIntervalWeekDays.setdefault(interval, [])
                dictIntervalWeekDays[interval].append(int(steps))
 # print(len(dict.keys()))
    listDate = []
    listTotal = []
    listAvg = []
 # listMean = []
 # listMedian = []
    for i in dict.keys():
        listDate.append(i)
        listTotal.append(sum(dict.get(i)))
        listAvg.append(st.mean(dict.get(i)))
    plt.hist(listTotal)
    plt.title("Total Steps per day")
    plt.xlabel("Steps per day")
    plt.ylabel("Frequency")
    plt.yticks(range(0, 25, 5))
    plt.savefig('figure1-version1.svg')
    plt.show()
    plt.close()
 # plt.show()
    hist = pygal.Bar()
    hist.title = "Total steps per day"
    hist.x_title = "Steps per day"
    hist.y_title = "Frequency"
    hist.x_labels = listDate
    hist.add('Total Number of steps', listTotal)
    hist.render_to_file('figure1-version2.svg')
    print("Mean : " + str(st.mean(listTotal)))
    q = sorted(listTotal)
    print("Median : " + str(st.median(q)))
 # ------------------------ second case ------------------------
 # What is the average daily activity pattern?
    listAveragePerInterval = []
    for i in dictInterval.keys():
        listAveragePerInterval.append(stat.mean(dictInterval.get(i)))
    fig = plt.figure(dpi=80, figsize=(20, 6))
    plt.plot(list(dictInterval.keys()),listAveragePerInterval, c = 'blue')
    plt.title("Average daily activity")
    plt.xlabel("Time Interval")
    plt.ylabel("Average number of steps taken")
    fig.autofmt_xdate()
    plt.savefig("figure2.svg")
    plt.show()
    plt.close()
 # print(listAveragePerInterval)
    maxValue = max(listAveragePerInterval)
    n = 0
    max = ""
    indexMax = listAveragePerInterval.index(maxValue)
    for i in dictInterval.keys():
        if(n == indexMax):
            max = i
            break
        n+=1
    print("maximum number of steps in interval : " + str(max))
    # print("File saved to figure1-version1.svg and figure1-version2.svg")
    listWeekDays = []
    listWeekEnd = []
    for i in dictIntervalWeekDays.keys():
        listWeekDays.append(st.mean(dictIntervalWeekDays.get(i)))
    for i in dictIntervalWeekEnd.keys():
        listWeekEnd.append(st.mean(dictIntervalWeekEnd.get(i)))
    fig = plt.figure(dpi=80, figsize=(20, 6))
    plt.plot(list(dictInterval.keys()),listWeekDays, c = 'blue' , label = 'WeekDays')
    plt.plot(list(dictInterval.keys()),listWeekEnd, c = 'red' , label = 'WeekEnd')
    plt.legend(loc = 'upper left')
    plt.title("All week days and weekend days")
    plt.xlabel("Time Interval")
    plt.ylabel("Average number of steps taken")
    fig.autofmt_xdate()
    plt.savefig("figure4.svg")
    plt.show()
    plt.close()