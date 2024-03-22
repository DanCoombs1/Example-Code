#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 19:42:37 2022

@author: dan_coombs99
"""

import matplotlib.pyplot as plt
import csv
import datetime
population = 67220000
max_infected = 234873
i = population / max_infected


time = []
infected = []

for row in csv.reader(open('/Users/dan_coombs99/Documents/code/Python/Covid_code/data_2022-Aug-24.csv')):
    row[3] = datetime.datetime.strptime(row[3], '%Y-%m-%d') # Parse date.
    infected.append(int(row[4]))
    time.append(row[3])


infected_per = [x / population for x in infected]


plt.figure()
plt.plot(time, infected, color = 'black')
plt.fill_between(time, infected, color = 'black')
plt.title('Infection Against Time Curve Using Real World Data')
plt.xlabel('Date')
plt.ylabel('Infected')
plt.show()













