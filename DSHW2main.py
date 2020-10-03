import Definitions as fini
import pandas as pd
import matplotlib.pyplot as plt
import powerlaw as pwl
import statistics
from scipy.stats import expon
import scipy.stats as statss
import numpy as np
from random import sample


#Variables airports
col_listA= ["Airport", "NumberOfRoutes"]
Airport_Spread = pd.read_csv("airport_routes.csv", usecols=col_listA)
route=Airport_Spread['NumberOfRoutes']
airports=Airport_Spread['Airport']
routes=route.to_list()
routessample=sample(routes,500)
routes.sort(reverse=True)
routessample.sort(reverse=True)
sdev_airport= statistics.stdev(routes)
mua, stda = statss.norm.fit(routes)

#variables movies
col_listB=["Movie", "AverageVote"]
Movies_Spread= pd.read_csv("movie_votes.csv", usecols=col_listB)
movies=Movies_Spread['Movie']
votess=Movies_Spread['AverageVote']
votes=votess.to_list()
votessample= sample(votes,500)
votes.sort(reverse=True)
votessample.sort(reverse=True)
sdev_movies= statistics.stdev(votes)
mum, stdm = statss.norm.fit(votes)

#variables Birthdays text files
f= open("birthdates.txt", 'r')
birthdates = f.read().split('\n')
f.close()

print ('Hello! Welcome to Data Science Homework 2 ! \n\n')

#part A-Aiport
print('A) Suppose the given data points follow a power law distribution. Estimate the corresponding alpha parameter: ')
np.seterr(divide='ignore', invalid='ignore')
fit = pwl.Fit(routes)
print('The alpha for airports is: ')
print(str(fit.power_law.alpha))
#part A-Movies
np.seterr(divide='ignore', invalid='ignore')
fitm = pwl.Fit(votes)
print('The alpha for movies is: ')
print(str(fitm.power_law.alpha))



#part B-Airport
print('\nB) Suppose the given data points follow an exponential distribution. Estimate the corresponding lambda parameter.')
mean_airports= statistics.mean(routes)
myLambdaA= 1/mean_airports
print('The lambda for Airports is: ')
print(myLambdaA)
#part B-Movies
mean_movies= statistics.mean(votes)
myLambdaM= 1/mean_movies
print('The lambda for Movies is: ')
print(myLambdaM)


#part C
print('\nC) Suppose the given data points follow a uniform distribution. Estimate the corresponding range parameters [a, b] of the uniform distribution.')
#ranche= routes.interval(mean_airports, 0, 1)

#part D-Airport and Movies
print('\nD) Suppose the given data points follow a normal distribution. Estimate the corresponding μ and σ parameters. \n')
print('The mean for Airports routes is: ')
print(mua)
print('and the standard deviation is: ')
print(stda)
print('\nThe mean for Movies votes is: ')
print(mum)
print('and the standard deviation is: ')
print(stdm)



#print graphs
# x_a=airports
# y_a=routessample
# x_m=movies
# y_m=votessample
#
# plt.subplot(221)
# plt.plot(y_a)
# plt.title('Airport Routes')
# plt.grid(True)
#
# plt.subplot(222)
# plt.plot(y_m)
# plt.title('Movies votes')
# plt.grid(True)
#
# plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)

#plt.show()

#Question #2
print('\n\nQuestion #2')
print('The data on the following set is arranged as birthdays with the format MM/DD/YYYY')

#obtain data sample 500
day=[]
month=[]
year=[]
ages=[]
for i in range(len(birthdates)):
    date = birthdates[i].split('-')
    year.append(date)

now='2020'
for x in range(len(year)-2):
    yer=int(year[x][2])
    neww=(int(now)-int(yer))
    ages.append(yer)

Age=sample(ages, 1000)
Age.sort(reverse=True)
plt.hist(Age, bins=90)
plt.title('Ages')
plt.show()


