import csv
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

# Configure graph
NUM_BARS = 240
list_str = []

def buy_first(changes, i, buy_index, sell_index, change_diff, before10_down):

    if i >= 10 and buy_index == -1:
        if before10_down < 3:
            buy_index = i
        elif i < 30 and ((changes[i-2] <= -0.25 and changes[i-1] <= 0) or (changes[i-2] <= 0 and changes[i-1] <= -0.25)) and changes[i] > 0.25:
            buy_index = i

    elif buy_index != -1 and sell_index == -1:

        if i < 110:
            if before10_down < 3 and change_diff > 2:
                sell_index = i
            elif ((changes[i-2] >= 0.25 and changes[i-1] >= 0) or (changes[i-2] >= 0 and changes[i-1] >= 0.25)) and changes[i] < -0.25 and change_diff > 2:
                sell_index = i
        elif i < 230 and change_diff > 1:
            sell_index = i
        elif change_diff >= 0.5:
            sell_index = i

    return buy_index, sell_index

def sell_first(changes, i, buy_index, sell_index, change_diff, before10_up):

    if i >= 10 and sell_index == -1:
        if before10_up < 3:
            sell_index = i
        elif i < 30 and ((changes[i-2] >= 0.25 and changes[i-1] >= 0) or (changes[i-2] >= 0 and changes[i-1] >= 0.25)) and changes[i] > 0.25:
            sell_index = i

    elif sell_index != -1 and buy_index == -1:

        if i < 110:
            if before10_up < 3 and change_diff > 2:
                buy_index = i
            elif ((changes[i-2] <= -0.25 and changes[i-1] <= 0) or (changes[i-2] <= 0 and changes[i-1] <= -0.25)) and changes[i] > 0.25 and change_diff > 2:
                buy_index = i
        elif i < 230 and change_diff > 1:
            buy_index = i
        elif change_diff >= 0.5:
            buy_index = i

    return buy_index, sell_index

# Check each row
def row_checker(row):

    # Create array of change values
    change_list = []
    change = 0.0
    for i in range(NUM_BARS):
        change_str = 'c{}'.format(i)
        change += row[change_str]
        change_list.append(row[change_str])
    changes = np.array(change_list)

    if changes[0] < -1.0:
        list_str.append(row['Date'])

    tot_change = 0
    max_change = -100
    min_change = 100
    buy_index = -1
    sell_index = -1
    change_diff = 0
    before10_up = 0
    before10_down = 0
    for i, change in enumerate(changes):

        tot_change += change
        if tot_change > max_change:
            max_change = tot_change
        if tot_change < min_change:
            min_change = tot_change
        if buy_index != -1 and sell_index == -1:
            change_diff += change
        elif sell_index != -1 and buy_index == -1:
            change_diff += -1*change

        # Check up/down before 10 bars
        if i < 10:
            if change > 0:
                before10_up += 1
            elif change < 0:
                before10_down += 1

        # Big green at start
        if changes[0] >= 1.0:
            if changes[2] > 0:
                buy_index, sell_index = buy_first(changes, i, buy_index, sell_index, change_diff, before10_down)
            elif changes[2] < -0.25:
                buy_index, sell_index = sell_first(changes, i, buy_index, sell_index, change_diff, before10_up)

        # Between 1 and -1
        '''
        elif changes[0] < 1.0 and changes[0] > -1.0 and changes[1] > -1.0 and changes[1] < 1.0:
            if changes[2] < -0.5:
            elif changes[2] > 0.5:
        '''
        
        # Big red at start
        # elif changes[0] <= -1.0:
            
    return buy_index, sell_index, change_diff
    
    
# Iterate through rows
total = 0.0
df = pd.read_csv('wheat_bars.csv')
df['Date'] = df.astype({'Date': 'str'})
df.set_index('Date')

# ['20190314', '20190318', '20190320', '20190409', '20190423', '20190506', '20190509', '20190603', '20190611', '20190617', '20190624', '20190709', '20190716', '20190718', '20190729', '20190730', '20190801', '20190815', '20190903', '20190924', '20191021', '20191112', '20191114', '20191118']

# Create list of change values
x_vals = range(0, NUM_BARS)
axes = plt.gca()
axes.set_xlim([0, NUM_BARS])
axes.set_ylim([-12, 12])

row = df[df['Date'] == '20191118']
print('{}: {}, {}, {}'.format(row['Date'].values[0], row['c0'].values[0], row['c1'].values[0], row['c2'].values[0]))
changes = []
change = 0.0
for i in range(NUM_BARS):
    change_str = 'c{}'.format(i)
    change += row[change_str].values[0]
    changes.append(change)
  
plt.xticks(np.arange(0, NUM_BARS, 10)) 
plt.plot(x_vals, changes)
plt.show()
'''

for i, row in df.iterrows():
    res = row_checker(row)
print(list_str)
'''