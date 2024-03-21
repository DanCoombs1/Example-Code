#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 21:50:25 2024

@author: dan_coombs99
"""

#all imports
import math
import random
import numpy
import copy
from random import gauss
from random import randint
from scipy.integrate import simpson
import matplotlib.pyplot as plt
import csv
import datetime

# a seed is set to ensure results can be repeated
random.seed(19)


Day = 730 #number of days of simulation
heard_immunity = 62 # days until herd immunity
vac_day = 730  #how many days the vaccine took to be released - as there is no vaccine this is set to the same amount of days as the simulation



#size of the grid being created
row = 250
col = 250
N = row*col

#different grids to keep track of each variable
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
    """
    function to count the number of infected neighbours for each person on the grid 
    goes through each point on the grid and checks the 4 neighbours (up, down, left, and right) to see
    if they are infected and totals them up

    """
    infectedNeighbours = 0
    #               UP     RIGHT    DOWN    LEFT
    neighbours = [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
 
    for z in range(len(neighbours)):
        if(neighbours[z][0] >= 0 and neighbours[z][0] < row):
            if(neighbours[z][1] >= 0 and neighbours[z][1] < col):
                if(grid[neighbours[z][0]][neighbours[z][1]] >= 1 and grid[neighbours[z][0]][neighbours[z][1]] < 99):
                    infectedNeighbours += 1
    return infectedNeighbours
 

def percent_vac():
    """ 
    function to calculate percent of population that is vaccinated
    calculatsthe total number of people on the grid
    calculates the total number of vaccinated people on grid
    returns the percentage of people vaccinated
    """
    total = 0
    vac_total = 0
    for x in range(col):
        for y in range(row):
            total += 1
            if vaccine_grid[x][y] > 0:
                vac_total += 1
    return vac_total / total
 
    
def doseinterval():
    """
    function that creates a random integer between 1 week and 12 weeks for each individual person 
    until they are allowed to recieve the second vaccine
    """
    for x in range(col):
        for y in range(row):
            DaysBetweenDoses[x][y] = randint(21, 84)
            
    return DaysBetweenDoses
            
doseinterval()
for cell in DaysBetweenDoses:
    ('   '.join(map(str, cell)))



beta = 0.54 #contagionist
h = -1.882 #contracting the disease outside of neighbours

def infection():
    """
    function that infects people based on probability 
    there are 3 different probabilities depending on whether the person has had 0,1, or 2 vaccines
    The function decides if a person becomes vaccinated by pseudo-random number generation
    a random number is generated for each individual every day
    if this number generated is lower than the probability of infection then they will become infected
    
    """
    infection_grid = copy.deepcopy(grid)
    #global days
    for x in range(col):
        for y in range(row):
            
            if(immune[x][y] == 0) and (vaccine_grid[x][y] == 0): #probability if not vaccinated
                Probability = math.exp(4*beta*agents_neighbours(x,y) + 2*h )/(1 + math.exp(4*beta*agents_neighbours(x,y) + 2*h )) #probability it will infect
    
            else:
                continue
            
            u = random.uniform(0,1)
            #random number generated to compare probability to
            if(u < Probability): #If probability of being infected is greater than u 
                infection_grid[x][y] += 1 #Infect Cell
                            
            else: #(u >= Probability):
                infection_grid[x][y] = 0 
    return infection_grid
    

unimmuneDay = 90
def unimmuneDayz():
    """
    this function decides how long somebody will remain immune for 
    a grid is created that will hold a random number generated with a normal distribution around the unimmuneDay number for each individual 
    """
    for x in range(col):
        for y in range(row):
            unimmune_grid[x][y] = gauss(unimmuneDay,10)
                
    return unimmune_grid

infectedDays = 10
infectedDays_vaccine = 5
immunityChance = 0.5
immunityChance_vac = 0.8

def immunity():
    """
    this function grants individuals immunity from the virus 
    if a person holds the virus for longer than 10 days their body has built up enough anti bodies to become immune
    however if a person does not reach the 10th day they will still be susceptible to contracting the virus again
    however if the person has had 1 vaccine then the number of days decreases
    if a person reaches the final day they are generated a number - if this number is lower than the immunity chance then they become immune
    if the person has had both vaccines they automatically become immune from the virus
    
    a person is only immune for the time given in the unimmuneDayz function
    once this time is up they will become susceptible to the disease again

    """
    infection_grid = copy.deepcopy(grid)
    for x in range(col):
        for y in range(row):
            
            if immune[x][y] == 0:
                if(infection_grid[x][y] >= infectedDays) and (vaccine_grid[x][y] == 0): #if cell reaches 11 then cell may become immune
                    if(random.uniform(0,1) < immunityChance):
                        infection_grid[x][y] = 99
                        immune[x][y] = 1
                        
                if (infection_grid[x][y] >= infectedDays_vaccine) and (vaccine_grid[x][y] == 1):
                    if(random.uniform(0,1) < immunityChance_vac):
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
                

#empty lists that stores all the vslues from the for loop below
total_agent_list = []
Days_of_pandemic = []
susceptible_agent = []
infected_agent = []
infected_agent_total = []
immune_agent = []
vaccinated_agent = []


#for loop that goes through each day and calculates the number of immune, infected and vaccinated people on the grid
days = 1
for i in range(0,Day):   
    
    pandemic_days = str(i)
    unimmuneDayz()
    grid = infection()
    grid = immunity()

    im_agent = str(numpy.count_nonzero(immune))
    im_agent
    im_agent_per = (float(im_agent)/N) * 100

    immune_agent.append(im_agent_per)
    inf_agent = str(numpy.count_nonzero(grid)-numpy.count_nonzero(grid == 99))
    inf_agent_int = int(inf_agent)
    inf_agent_per = (float(inf_agent)/N) * 100

    infected_agent.append(inf_agent_per)
    infected_agent_total.append(inf_agent_int)
    sus_agent = str((col*row)-numpy.count_nonzero(grid))
    sus_agent_per = (float(sus_agent)/N) * 100
    susceptible_agent.append(sus_agent_per)
   
    total_agents = 100
    total_agent_list.append(total_agents)
    
    days = days + 1
    Days_of_pandemic.append(pandemic_days)
    
 
for cell in immune_days:
    ('   '.join(map(str, cell)))


#color dictionary for immune, infected and susceptible people
#where susceptible people are green, infected people are red, and immune people are blue 
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


#gives each person a color from the color dictionary based on if theyre infected, immune or susceptible and creates a new grid
data_3d = numpy.ndarray(shape=(grid.shape[0], grid.shape[1], 3), dtype=int)
for i in range(0, grid.shape[0]):
    for j in range(0, grid.shape[1]):
        data_3d[i][j] = color_dict[grid[i][j]]  
    
plt.title("Stochastic Simulation of a Pandemic")
plt.imshow(data_3d)

#imports the real_data_graph file to be used in the main file
import real_data_graph

#all the code below is used to create charts showing how the susceptible, infected and immune numbers vary over the simulation
#sums up the number of infected people and turns it into a string
total_infected = sum(infected_agent_total)
total_string = str(total_infected)
buffer_infected = list_of_zeros + infected_agent

#plots the diagram using matplotlib
plt.figure()

#labels susceptible, infected and immune people and gives the line the correct colour
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

#annotates the graph at the max infected percentage point
plt.annotate(('Max Infected Percentage: ' + str(inf_max2)) + '%', xy=(xmax_inf, inf_max), xytext=(60, 80),
 arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate(('Day: ' + str(xmax_inf)), xy=(xmax_inf, inf_max), xytext=(73, 75))

#annotates the graph at the herd immunity day
im_above_line = list(filter(lambda k: k > heard_immunity, immune_agent))[0]
herd_day = immune_agent.index(im_above_line)
plt.annotate(("""Herd Immunity Day:
              """ + str(herd_day)), xy=(herd_day + 1, heard_immunity), xytext=(herd_day - 60, heard_immunity - 35),
 arrowprops=dict(facecolor='black', shrink=0.05))

#annotates the graph at the vaccination day
plt.annotate(('Vaccination Day: ' + str(vac_day)), xy=(vac_day, heard_immunity - 10), xytext=(vac_day - 210, heard_immunity - 10),
 arrowprops=dict(facecolor='black', shrink=0.05))

#calculates the area under the infected line and times by the death rate to calculate total deaths
area = simpson(infected_agent_total)
area = int(area)
death = area * 0.00878

death_percent = death / N
death_percent = '{0:.2f}'.format(death_percent)

#annotates the number of deaths onto the graph as well as the percent of the population this was
plt.annotate(("""       Death Count:       
              """ + str(area)), xy=(half_xmax_inf, half_inf_max), xytext=(360, 88))
plt.annotate(("""Percent of Population: 
              """ + str(death_percent)) + '%', xy=(half_xmax_inf, half_inf_max), xytext=(360, 74))

#creates a line to see how many people need to become immune in order to reach herd immunity 
plt.text(440, heard_immunity + 3, "Herd Immunity Line")


plt.legend(loc='upper right')

#changes the x axis to months instead of days 
x_ticks = [1, 30, 60, 90, 120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450, 480, 510, 540, 570, 600,630, 660, 690, 720]
x_labels = ['0','1', '2', '3', '4', '5','6', '7', '8', '9', '10', '11', '12',
            '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24']
plt.xticks(ticks=x_ticks, labels=x_labels)

plt.fill_between(Days_of_pandemic, total_agent_list, color = 'lime')
plt.fill_between(Days_of_pandemic, infected_agent, color = 'red')

#labels the axis of the graph and gives it a title
plt.title("SIRSV Curve Simulating The Covid-19 Outbreak Using Only The AstraZeneca Vaccine")
plt.xlabel("Month of Pandemic")
plt.ylabel("Population Percentage")

plt.show()
