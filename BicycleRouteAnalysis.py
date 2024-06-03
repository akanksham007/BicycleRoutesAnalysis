#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Install Libraries like GoogleMaps, OpenStreetMap, GeoPandas, MatplotLib
get_ipython().system('pip install -U googlemaps')
get_ipython().system('pip install osmnx geopandas matplotlib')


# In[4]:


# Import Libraries

import pandas as pd
import numpy as np
import osmnx as ox
import geopandas as gpd
import matplotlib.pyplot as plt
import os
for dirname, _,filenames in os.walk('./data/'):
    for filename in filenames:
        print(os.path.join(dirname,filename))


data = pd.read_csv('./data/bicycleRoutesAnalysis.csv')


# In[5]:


data.info()


# In[7]:


# ox.plot_graph(ox.graph_from_place('Berlin, Germany'))


# In[23]:


# Specify Germany City Berlin coordinates (Latitude and Longitute)
latitude = 52.520008
longitude = 13.404954


G = ox.graph_from_point((latitude, longitude), dist=1000, network_type='drive', simplify=False)

nodes, edges = ox.graph_to_gdfs(G, nodes=True, edges=True)


# # Plot the bicycle routes
# fig, ax = plt.subplots(figsize=(10, 10))
# edges.plot(ax=ax, linewidth=2, edgecolor='black', facecolor='black')  # White edges with no facecolor
# nodes.plot(ax=ax, markersize=10, color='black')
# ax.set_facecolor('black')  # Set the background color to black
# plt.title('Bicycle Routes in Berlin City', color='white')  # Set title color to white
# plt.axis('off')
# plt.show()


fig1, ax1 = plt.subplots(figsize=(10, 10))
edges.plot(ax=ax1, linewidth=2, edgecolor='black')
nodes.plot(ax=ax1, markersize=10, color='black')
ax1.set_facecolor('black')
ax1.set_title('Bicycle Routes in Berlin City', color='white')
ax1.axis('off')

# Second plot
fig2, ax2 = plt.subplots(figsize=(10, 10))
edges.plot(ax=ax2, linewidth=2, edgecolor='tab:blue')
nodes.plot(ax=ax2, markersize=10, color='red')
ax2.set_title('Bicycle Routes in Berlin City')
ax2.axis('off')

# Display the plots
plt.show(fig1)
plt.show(fig2)


# In[21]:


# fig, ax = plt.subplots(figsize=(10, 10))
# edges.plot(ax=ax, linewidth=2, edgecolor='tab:blue')
# nodes.plot(ax=ax, markersize=10, color='red')
# plt.title('Bicycle Routes in Berlin City')
# plt.axis('off')
# plt.show()


# In[22]:





# In[ ]:




