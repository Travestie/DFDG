import pandas as pd
import random as rd
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm as tqdm

def Winner(array):
    #Randomly selects a winner and 'pops' them from the list
    index = rd.randrange(0,len(array))
    name = array[index]
    array = np.delete(array,[index])
    return name, array

def percdiff(array):
    max = np.amax(array)
    min = np.amin(array)
    perc = abs(min - max)/min*100
    return perc

#Importing Members List
members = pd.read_csv(r'dfdg.csv',sep=',',header=None).values
members = members[:,0]

#Creating Distribution
dist = np.zeros(len(members))
n=9999 #Number of sample points
with tqdm(total = n) as pbar:
    for i in range(n):
        rand = rd.randrange(0,len(dist))
        dist[rand] = dist[rand] + 1
        tqdm.update(pbar)
tqdm.close

#Plot Distribution
plt.style.use('dark_background')
plt.tight_layout()
fig=plt.figure('distribution')
ax=fig.add_subplot(211)
ax.set_title('Entered Members')
ax.set_ylabel('Distribution',style = 'italic')
ax.set_xticks(np.arange(len(members)))
ax.set_xticklabels(members, rotation = 'vertical')
ax.set_ylim((0,np.amax(dist)+0.2*np.amax(dist) if np.amax(dist) > 10 else 10))
text = "Mean: {}\nMax: {}\nMin: {}\nStandard Deviation: {}\nPercent Diff Between Max and Min: {:.3f}%".format(int(np.mean(dist)),int(np.amax(dist)),int(np.amin(dist)),int(np.std(dist)),percdiff(dist))
ax.text(len(dist)/2,np.amin(dist)/2 if np.amax(dist)>10 else 5,text, horizontalalignment='center',verticalalignment='center',style = 'italic')
line1, = ax.plot(members,dist,'r-o')
plt.show()
plt.close(1)

#Picking Winners!

#Amulet Winner
amulet_winner, members = Winner(members)
#Skull Winner
skull_winner, members = Winner(members)
#Painted VW Beetle Winner
pvwb_winner, members = Winner(members)

#Create Graphic of Winners
fig=plt.figure('winners')
ax=fig.add_subplot(111)
ax.set_title('Winners!', fontweight = 'bold',size = '24')
amulet_text = "Amulet Winner: {}".format(amulet_winner)
skull_text = "Skull Winner: {}".format(skull_winner)
pvwb_text = "Painted VW Beetle Winner: {}".format(pvwb_winner)
ax.set_xlim(0,10)
ax.set_ylim(0,10)
plt.axis('off')
ax.text(5,7,amulet_text,horizontalalignment='center',verticalalignment='center',style = 'italic',fontweight = 'bold',size = '18')
ax.text(5,5,skull_text,horizontalalignment='center',verticalalignment='center',style = 'italic',fontweight = 'bold',size = '18')
ax.text(5,3,pvwb_text,horizontalalignment='center',verticalalignment='center',style = 'italic',fontweight = 'bold',size = '18')