# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 10:19:47 2021

@author: Gökhan Akay
"""

import matplotlib.pyplot as plt
import numpy as np

x=[1,2,3,4]
y=[1,4,9,16]

#plt.plot(x,y, color = "red", linewidth = "5")
plt.plot(x,y,"o--r" )

#axis'in limitlerini set ediyoruz.
plt.axis([0,6,0,20])

plt.title("Graph Title")
plt.xlabel("x label")
plt.ylabel("y label")

plt.show()

#-------------------------------



x= np.linspace(0,2,100)

plt.plot(x,x,label = "linear", color = 'red')
plt.plot(x,pow(x,2),label = "quadratic", color = 'yellow')
plt.plot(x,pow(x,3),label = "cubic", color = "blue")

plt.xlabel("x label")
plt.ylabel("y label")
plt.title("Graph Title")
plt.legend()

plt.show()


#-------------------------------

x= np.linspace(0,2,100)

fig, ax = plt.subplots(3)

ax[0].plot(x,x,color="red")
ax[0].set_title("linear")

ax[1].plot(x,pow(x,2),color="green")
ax[1].set_title("quadratic")

ax[2].plot(x,pow(x,3),color="yellow")
ax[2].set_title("cubic")

plt.tight_layout()
plt.show()


#-------------------------------
x= np.linspace(0,2,100)

fig, ax = plt.subplots(2,2)
fig.suptitle("Graph Title")

ax[0,0].plot(x,x,color="red")
ax[0,0].set_title("linear")

ax[0,1].plot(x,pow(x,2),color="green")
ax[0,1].set_title("quadratic")

ax[1,0].plot(x,pow(x,3),color="yellow")
ax[1,0].set_title("cubic")

ax[1,1].plot(x,pow(x,4),color="yellow")
ax[1,1].set_title("üzeri 4")

plt.tight_layout()
plt.show()

#-------------------------------

#csv kayıp :/
import pandas as pd

df=pd.read_csv("nba.csv")
df=df.drop(["Number"], axis = 1).groupby("Team")
df.plot(subplots = True)
plt.legend()
plt.show()


#-------------------------------
#figure oluşturma.


x=np.linspace(-10,9,20)
y = x**3
z = x**2

figure = plt.figure()

#şöyle okunuyor, figür oluştu, axes alttan yüzde 20 soldan yüzde 20
#genişlik ve yükseklik olarak da yüzde 80ini alacak şekilde yerleştiriliyor.
#yani axes'i figürün tam neresine oturtayım diyor.
#axes = figure.add_axes([0.2,0.5,.4,.8])

axes_cube = figure.add_axes([0.1,0.1,0.8,0.8])
axes_cube.plot(x,y,"b")
axes_cube.set_xlabel("x axis")
axes_cube.set_ylabel("y axis")
axes_cube.set_title("cube")

axes_square = figure.add_axes([.15,.6,.25,.25])
axes_square.plot(x,z,"r")
axes_square.set_xlabel("x axis")
axes_square.set_ylabel("y axis")
axes_square.set_title("square")

plt.show()



#-------------------------------
figure = plt.figure()
axes = figure.add_axes([0,0,1,1])
axes.plot(x,z,label="Square")
axes.plot(x,y,label="Cube")
axes.legend(loc=4)

plt.show()


#-------------------------------
fig, ax = plt.subplots(nrows = 2, ncols = 1, figsize = (4,4))

ax[0].plot(x,y)
ax[0].set_title("cubic")

ax[1].plot(x,z)
ax[1].set_title("square")

plt.tight_layout()
fig.savefig("sample_fig_2.png")
plt.show()


#-------------------------------

year = [2011,2012,2013,2014,2015]
player1 = [8,10,12,7,9]
player2 = [7,12,5,15,21]
player3 = [18,20,22,25,19]

#Stack plot.
plt.plot([],[], color = "y", label = "player1")
plt.plot([],[], color = "r", label = "player2")
plt.plot([],[], color = "b", label = "player3")

plt.stackplot(year,player1,player2,player3, colors = ['y','r','b'])
plt.title("Goals scored by years")
plt.xlabel("Year")
plt.ylabel("Goals")
plt.legend()
plt.show()


#Pie plot.

goal_types = ['Penalty','Header','Free Kick']
goals = [12,35,7]
colors = ['y','r','b']
plt.pie(goals, 
        labels = goal_types, 
        colors = colors, 
        shadow = True, 
        explode = (.05,.05,.05),
        autopct = "%1.1f%%")
plt.show()


#Bar plot.

plt.bar([0.25,1.25,2.25,3.25,4.25],
        [50,40,70,80,20],
        label = "BMW",
        width = .5)

plt.bar([0.75,1.75,2.75,3.75,4.75],
        [80,20,20,50,60],
        label = "Audi",
        width = .5)

plt.legend()
plt.xlabel("Day")
plt.ylabel("Distance")
plt.title("Car info")

plt.show()


#Hist

ages = np.random.randint(0,100,50)
age_groups = np.linspace(0,100,11)

plt.hist(ages, age_groups, histtype= "bar", rwidth = .8)
plt.xlabel="Age groups"
plt.ylabel="Number of people"
plt.title("Histogram Sample")
plt.show()

