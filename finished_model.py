#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 14:05:12 2022

@author: dan_coombs99
"""
import matplotlib.pyplot as plt
import csv
import datetime

time = []
timee = list(range(0,365))
population = 3000

infected = []
for row in csv.reader(open('/Users/dan_coombs99/Documents/masters/diss/data_2022-Aug-24.csv')):
    row[3] = datetime.datetime.strptime(row[3], '%Y-%m-%d') # Parse date.
    infected.append(int(row[4]))
    time.append(row[3])
        
infected_per = [x / population for x in infected]

i = [0, 365]
element = []
for index in range(0,365):
    element.append(infected[index])
#print(element)

infected_per2 = [x / population for x in element]

zero = 100
list_of_zeros = [0] * zero

#all imports
import math
import random
import numpy
import copy
from random import gauss
from random import randint
from scipy.integrate import simpson

random.seed(19)

#Parameters
Day = 730 #- zero#number of days
heard_immunity = 60
vac_day = 272  #how many days the vaccine took to be released
vac_pop_percent = 0.00434587375 #how quickly the vaccine was distributed
#vac_pop_percent = 0.0035 #2 vaccines
#vac_pop_percent = 0.0065188106 #1.5 rate
#vac_pop_percent = 0.0144 #maximum distribution
vaccine_eff = 0.487
#vaccine_eff = 0.77 #Moderna
vaccine_eff_2 = 0.841 #GOV
#vaccine_eff_2 = 0.937 #Pfizer
#vaccine_eff_2 = 0.745 #Oxford
#vaccine_eff_2 = 0.984 #Moderna
percent_of_pop_1 = 0.7521 #percent of population that would want the vaccine
percent_of_pop_2 = 0.7989
beta = 0.56 #contagionist
h = -1.882 #contracting the disease outside of neighbours
infectedDays = 10
infectedDays_vaccine = 5
immunityChance = 0.5
immunityChance_vac = 0.8
unimmuneDay = 90


#create a grid
row = 100
col = 100
N = row*col

grid = numpy.asarray([[0 for i in range(col)] for j in range(row)])
immune = [[0 for i in range(col)] for j in range(row)] #stores immunity
immune_days = [[0 for i in range(col)] for j in range(row)]
vaccine_grid = numpy.asarray([[0 for i in range(col)] for j in range(row)])
daysSinceFirstDose = [[0 for i in range(col)] for j in range(row)]
unimmune_grid = [[0 for i in range(col)] for j in range(row)]
DaysBetweenDoses = numpy.asarray([[0 for i in range(col)] for j in range(row)])
immune_grid = [[0 for i in range(col)] for j in range(row)]

for cell in grid:
    ('   '.join(map(str, cell)))
 
 
def agents_neighbours(x,y):
    infectedNeighbours = 0
    #               UP     RIGHT    DOWN    LEFT
    neighbours = [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
 
    for z in range(len(neighbours)):
        if(neighbours[z][0] >= 0 and neighbours[z][0] < row):
            if(neighbours[z][1] >= 0 and neighbours[z][1] < col):
                if(grid[neighbours[z][0]][neighbours[z][1]] >= 1 and grid[neighbours[z][0]][neighbours[z][1]] < 99):
                    infectedNeighbours += 1
    return infectedNeighbours
 

def percent_vac(): #function to calculate percent of population that is vaccinated
     total = 0
     vac_total = 0
     for x in range(col):
         for y in range(row):
             total += 1
             if vaccine_grid[x][y] > 0:
                 vac_total += 1
     return vac_total / total
 
    
#daysBetweenDoses = 21 
def doseinterval():
    for x in range(col):
        for y in range(row):
            DaysBetweenDoses[x][y] = randint(21, 84)
            
    return DaysBetweenDoses
            
doseinterval()
#for cell in DaysBetweenDoses:
#    ('   '.join(map(str, cell)))


#def vaccination():
#    res = percent_vac()
#    interval = doseinterval()
#    infection_grid = copy.deepcopy(grid)
#    global days
#    if res <= percent_of_pop_1:
#        vac_going_ahead = True #not everyone vaccinated
#    else:
#        vac_going_ahead = False #enough of population vaccinated
#    for x in range(col):
#        for y in range(row):
#            if vaccine_grid[x][y] == 0 and vac_going_ahead == True and days > vac_day and infection_grid[x][y] == 0: #add here grid = 0 or 99 maybe  can only be vaccinated is not infected
#                ran = random.uniform(0,1)
 #               if ran <= vac_pop_percent: #certain percentage of the population getting vaccinated every day
 #                   vaccine_grid[x][y] = 1   
                    
 #           elif vaccine_grid[x][y] == 1 and daysSinceFirstDose[x][y] < interval[x][y]:
#                daysSinceFirstDose[x][y] += 1
                
 #           if daysSinceFirstDose[x][y] == interval[x][y] and vaccine_grid[x][y] == 1 and res <= percent_of_pop_2 and infection_grid[x][y] == 0:
 #               vaccine_grid[x][y] = 2
 #               immune[x][y] = 2
            

def vaccination():
    res = percent_vac()
    
    global days
    if res <= percent_of_pop_1:
        vac_going_ahead = True #not everyone vaccinated
    else:
        vac_going_ahead = False #enough of population vaccinated
    for x in range(col):
        for y in range(row):
            if vaccine_grid[x][y] == 0 and vac_going_ahead == True and days > vac_day and grid[x][y] == 0: #add here grid = 0 or 99 maybe  can only be vaccinated is not infected
                ran = random.uniform(0,1)
                if ran <= vac_pop_percent: #certain percentage of the population getting vaccinated every day
                    vaccine_grid[x][y] = 1   
                    
            elif vaccine_grid[x][y] == 1 and daysSinceFirstDose[x][y] < DaysBetweenDoses[x][y]:
                daysSinceFirstDose[x][y] += 1
                
            if daysSinceFirstDose[x][y] == DaysBetweenDoses[x][y] and vaccine_grid[x][y] == 1 and res <= percent_of_pop_2 and grid[x][y] == 0:
                vaccine_grid[x][y] = 2
                immune[x][y] = 2



def infection():
    infection_grid = copy.deepcopy(grid)
    #global days
    for x in range(col):
        for y in range(row):
            
            if(immune[x][y] == 0) and (vaccine_grid[x][y] == 0): #probability if not vaccinated
                Probability = math.exp(4*beta*agents_neighbours(x,y) + 2*h )/(1 + math.exp(4*beta*agents_neighbours(x,y) + 2*h )) #probability it will infect
    
            elif (immune[x][y] == 0) and (vaccine_grid[x][y] == 1): #probability if vaccinated
                Probability=(1-vaccine_eff)*(math.exp(4*beta*agents_neighbours(x,y)+2*h)/(1+math.exp(4*beta*agents_neighbours(x,y)+2*h))) 
            
            elif (immune[x][y] == 0) and (vaccine_grid[x][y] == 2): #probability if vaccinated
                Probability=(1-vaccine_eff_2)*(math.exp(4*beta*agents_neighbours(x,y)+2*h)/(1+math.exp(4*beta*agents_neighbours(x,y)+2*h))) 
            else:
                continue
            
            u = random.uniform(0,1)
            #random number generated to compare probability to
            if(u < Probability): #If probability of being infected is greater than u 
                infection_grid[x][y] += 1 #Infect Cell
                            
            else: #(u >= Probability):
                infection_grid[x][y] = 0 
    return infection_grid
    
def unimmuneDayz():
    for x in range(col):
        for y in range(row):
            unimmune_grid[x][y] = gauss(unimmuneDay,10)
                
    return unimmune_grid

    
def immunity():
    infection_grid = copy.deepcopy(grid)
    for x in range(col):
        for y in range(row):
            
            if immune[x][y] == 0:
                if(infection_grid[x][y] >= infectedDays) and (vaccine_grid[x][y] == 0): #if cell reaches 11 then cell may become immune
                    if(random.uniform(0,1) < immunityChance):#immunityChance% chance cell will become immune
                        infection_grid[x][y] = 99
                        immune[x][y] = 1
                        
                if (infection_grid[x][y] >= infectedDays_vaccine) and (vaccine_grid[x][y] == 1):
                    if(random.uniform(0,1) < immunityChance_vac):#immunityChance_vac% chance cell will become immune
                        infection_grid[x][y] = 99
                        immune[x][y] = 1   
                        
                if (vaccine_grid[x][y] == 2):
                    infection_grid[x][y] = 99
                    immune[x][y] = 2  
                    
            else:
                immune_days[x][y] +=1
                
            if immune_days[x][y] > unimmune_grid[x][y] and immune[x][y] != 2:
                immune[x][y] = 0
                infection_grid[x][y] = 0
                immune_days[x][y] = 0
    return infection_grid
                


total_agent_list = []
Days_of_pandemic = []
susceptible_agent = []
infected_agent = []
infected_agent_total = []
immune_agent = []
vaccinated_agent = []


days = 1
for i in range(0,Day):   
    
    pandemic_days = str(i)
    unimmuneDayz()
    vaccination()
    grid = infection()
    grid = immunity()
    #random.shuffle(grid)
   # print(days)
    #for cell in grid:
     #   print('   '.join(map(str, cell)))
    im_agent = str(numpy.count_nonzero(immune))
    im_agent
    im_agent_per = (float(im_agent)/N) * 100
    #print("Number of immune agents = " + im_agent)
    immune_agent.append(im_agent_per)
    inf_agent = str(numpy.count_nonzero(grid)-numpy.count_nonzero(grid == 99))
    inf_agent_int = int(inf_agent)
    inf_agent_per = (float(inf_agent)/N) * 100
    #print("Number of currently infected agents = " + inf_agent) 
    infected_agent.append(inf_agent_per)
    infected_agent_total.append(inf_agent_int)
    sus_agent = str((col*row)-numpy.count_nonzero(grid))
    sus_agent_per = (float(sus_agent)/N) * 100
    susceptible_agent.append(sus_agent_per)
    #print("Number of currently non-infected agents = " + str((col*row)-numpy.count_nonzero(grid)+numpy.count_nonzero(grid == 99)))
    vac_agent = str(numpy.count_nonzero(vaccine_grid))
    vac_agent_1 = str(numpy.count_nonzero(vaccine_grid == 1))
    vac_agent_2 = str(numpy.count_nonzero(vaccine_grid == 2))
    vac_agent_per = (float(vac_agent)/N) * 100
    #print("Number of Vaccinated agents = " + vac_agent)
    #print("1st Dose = " + vac_agent_1)
    #print("2nd Dose = " + vac_agent_2)
    vaccinated_agent.append(vac_agent_per)
    total_agents = 100
    total_agent_list.append(total_agents)
    
    days = days + 1
    Days_of_pandemic.append(pandemic_days)
    
    
#print("UnImmune Grid ")
#for cell in unimmune_grid:
#    print('   '.join(map(str, cell)))

#print("Immunity Grid - 1 = Immune, 0 = Susceptible")
#for cell in immune:
#    print('   '.join(map(str, cell)))
    
#print("Vaccine Grid - 1 = Vaccinated, 0 = Susceptible")
#for cell in vaccine_grid:
#    print('   '.join(map(str, cell)))
#("Number of Vaccinated agents = " + str(numpy.count_nonzero(vaccine_grid)))
#("1st Dose = " + vac_agent_1)
#("2nd Dose = " + vac_agent_2)
#("ImmuneDays Grid")
for cell in immune_days:
    ('   '.join(map(str, cell)))


#infection grid
color_dict = {0: numpy.array([0, 255, 0]), 
              1: numpy.array([255, 0, 0]),
              2: numpy.array([255, 0, 0]),
              3: numpy.array([255, 0, 0]),
              4: numpy.array([255, 0, 0]),
              5: numpy.array([255, 0, 0]),
              6: numpy.array([255, 0, 0]),
              7: numpy.array([255, 0, 0]),
              8: numpy.array([255, 0, 0]),
              9: numpy.array([255, 0, 0]),
              10: numpy.array([255, 0, 0]),
              11: numpy.array([255, 0, 0]),
              12: numpy.array([255, 0, 0]),
              13: numpy.array([255, 0, 0]),
              14: numpy.array([255, 0, 0]),
              15: numpy.array([255, 0, 0]),
              16: numpy.array([255, 0, 0]),
              17: numpy.array([255, 0, 0]),
              18: numpy.array([255, 0, 0]),
              19: numpy.array([255, 0, 0]),
              20: numpy.array([255, 0, 0]),
              21: numpy.array([255, 0, 0]),
              22: numpy.array([255, 0, 0]),
              23: numpy.array([255, 0, 0]),
              24: numpy.array([255, 0, 0]),
              99: numpy.array([0, 0, 255])} 

        
data_3d = numpy.ndarray(shape=(grid.shape[0], grid.shape[1], 3), dtype=int)
for i in range(0, grid.shape[0]):
    for j in range(0, grid.shape[1]):
        data_3d[i][j] = color_dict[grid[i][j]]  
    
plt.title("Stochastic Simulation of a Pandemic")
plt.imshow(data_3d)

total_infected = sum(infected_agent_total)
total_string = str(total_infected)
buffer_infected = list_of_zeros + infected_agent

plt.figure()

plt.plot(Days_of_pandemic, total_agent_list, color = 'green', label = 'Susceptible')
plt.plot(Days_of_pandemic, infected_agent, color = 'red', label = 'Infected')
#plt.plot(Days_of_pandemic, buffer_infected[:365], color = 'red', label = 'Infected')
plt.plot(Days_of_pandemic, immune_agent, color = 'blue', label = 'Immune')
#plt.fill_between(timee, infected_per2, color = 'black', label = 'Real Data')
#plt.plot(Days_of_pandemic, vaccinated_agent, color = 'orange', label = 'Vaccinated')
plt.hlines(heard_immunity, 0, Day, colors = 'black' , linestyles = 'dotted')
plt.axvline(x=vac_day, ymin = 0, ymax = 0.6, color = 'black', linestyle = 'dotted')

inf_max = max(infected_agent)
half_inf_max = 0.5 * inf_max
inf_max2 = '{0:.2f}'.format(inf_max)
xpos_inf = infected_agent.index(inf_max)
xmax_inf = Days_of_pandemic[xpos_inf]
half_xmax_inf = 0.5 * int(xmax_inf)


plt.annotate(('Max Infected Percentage: ' + str(inf_max2)) + '%', xy=(xmax_inf, inf_max), xytext=(60, 80),
 arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate(('Day: ' + str(xmax_inf)), xy=(xmax_inf, inf_max), xytext=(73, 75))

im_above_line = list(filter(lambda k: k > heard_immunity, immune_agent))[0]
herd_day = immune_agent.index(im_above_line)
plt.annotate(("""Herd Immunity Day:
              """ + str(herd_day)), xy=(herd_day + 1, heard_immunity), xytext=(herd_day - 60, heard_immunity - 35),
 arrowprops=dict(facecolor='black', shrink=0.05))


plt.annotate(('Vaccination Day: ' + str(vac_day)), xy=(vac_day, heard_immunity - 10), xytext=(vac_day - 210, heard_immunity - 10),
 arrowprops=dict(facecolor='black', shrink=0.05))#

area = simpson(infected_agent_total)
area = int(area)
death = area * 0.00878

death_percent = death / N
death_percent = '{0:.2f}'.format(death_percent)

plt.annotate(("""       Death Count:       
              """ + str(area)), xy=(half_xmax_inf, half_inf_max), xytext=(360, 88))
plt.annotate(("""Percent of Population: 
              """ + str(death_percent)) + '%', xy=(half_xmax_inf, half_inf_max), xytext=(360, 74))

plt.text(440, heard_immunity + 3, "Herd Immunity Line")

plt.legend(loc='upper right')

x_ticks = [1, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600,630, 660, 690, 720]
x_labels = ['0','1', '2', '3', '4', '5','6', '7', '8', '9', '10', '11', '12',
            '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
plt.xticks(ticks=x_ticks, labels=x_labels)

plt.fill_between(Days_of_pandemic, total_agent_list, color = 'lime')
plt.fill_between(Days_of_pandemic, infected_agent, color = 'red')

plt.title("SIRSV Curve Simulating The Covid-19 Outbreak Using Only The AstraZeneca Vaccine")
plt.xlabel("Month of Pandemic")
plt.ylabel("Population Percentage")

plt.show()
