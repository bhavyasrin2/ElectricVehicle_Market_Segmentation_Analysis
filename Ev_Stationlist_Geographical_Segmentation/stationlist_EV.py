#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
data=pd.read_csv("C:/Users/raghu/Downloads/ev-charging-stations-india.csv")
data


# In[2]:


data.describe()


# In[3]:


data.info()


# In[4]:


import numpy as np
print(data["state"].unique())
print("enter total no of states: ",np.size(data["state"].unique()))


# In[5]:


data["state"] = data['state'].replace(['AndhraPradesh'],'Andhra Pradesh')
data["state"] = data['state'].replace(['Andra Pradesh'],'Andhra Pradesh')
data["state"] = data['state'].replace(['Andra Pradesh '],'Andhra Pradesh')
data["state"] = data['state'].replace(['Andhra Pradesh '],'Andhra Pradesh')
data["state"] = data['state'].replace(['Andhra pradesh '],'Andhra Pradesh')
data["state"] = data['state'].replace(['Andhra pradesh'],'Andhra Pradesh')
data["state"] = data['state'].replace(['Rajahmundry'],'Andhra Pradesh')
data["state"] = data['state'].replace(['Bhubhaneswar'],'Odisha')
data["state"] = data['state'].replace(['Jammu'],'Jammu and Kashmir')
data["state"] = data['state'].replace(['Jammu & Kashmir'],'Jammu and Kashmir')
data["state"] = data['state'].replace(['TamiNadu'],'TamilNadu')
data["state"] = data['state'].replace(['Tamil Nadu'],'TamilNadu')
data["state"] = data['state'].replace(['TAMIL NADU'],'TamilNadu')
data["state"] = data['state'].replace(['Uttarkhand'],'Uttarakhand')
data["state"] = data['state'].replace(['Uttrakhand'],'Uttarakhand')
data["state"] = data['state'].replace(['Uttarakhand '],'Uttarakhand')
data["state"] = data['state'].replace(['Maharashra'],'Maharashtra')
data["state"] = data['state'].replace(['Chikhali'],'Maharashtra')
data["state"] = data['state'].replace(['Hyderabad'],'Telangana')
data["state"] = data['state'].replace(['Hyderabadu00a0'],'Telangana')
data["state"] = data['state'].replace(['TELENGANA'],'Telangana')
data["state"] = data['state'].replace(['Karala'],'Kerala')
data["state"] = data['state'].replace(['Ernakulam'],'Kerala')
data["state"] = data['state'].replace(['Kochi'],'Kerala')
data["state"] = data['state'].replace(['chattisgarh'],'Chhattisgarh')
data["state"] = data['state'].replace(['Chattisgarh'],'Chhattisgarh')
data["state"] = data['state'].replace(['Bhubhaneswar'],'Odisha')
data["state"] = data['state'].replace(['PUNJAB'],'Punjab')
data["state"] = data['state'].replace(['Jajpur'],'Jaipur')
data["state"] = data['state'].replace(['Harayana'],'Haryana')
data["state"] = data['state'].replace(['Hisar'],'Haryana')
data["state"] = data['state'].replace(['Delhi NCR'],'Delhi')
data["state"] = data['state'].replace(['WestBengal'],'West Bengal')
data["state"] = data['state'].replace(['Limbdi'],'Gujarat')
data["state"] = data['state'].replace(['Tripura'],'Agartala')


# In[6]:


print(data["state"].unique())
print("enter total no of states: ",np.size(data["state"].unique()))


# In[7]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[8]:


fig=plt.figure(figsize=(40,20))
sns.countplot(data["state"])
fig.show()


# States with more than 50 Electric Vehicle Charging Station

# ANDHRA PRADESH

# In[9]:


Ap_df=data[data["state"]=="Andhra Pradesh"]
Ap_df


# In[10]:


fig=plt.figure(figsize=(10,10))
sns.scatterplot(Ap_df["lattitude"],Ap_df["longitude"]).set(title="plotting the ev stations in ANDHRA PRADESH")


# In[11]:


ap_freq_li=pd.DataFrame(Ap_df["city"].value_counts())
ap_freq_li=ap_freq_li.head()
print(ap_freq_li)


# Maharashtra

# In[12]:


maha_df=data[data["state"]=="Maharashtra"]
maha_df


# In[13]:


fig=plt.figure(figsize=(10,10))
sns.scatterplot(maha_df["lattitude"],maha_df["longitude"]).set(title="plotting the ev stations in Maharashtra")


# In[14]:


maha_freq_li=pd.DataFrame(maha_df["city"].value_counts())
maha_freq_li=maha_freq_li.head()
print(maha_freq_li)


# In[15]:


delhi_df=data[data["state"]=="Delhi"]
print(delhi_df)
delhi_freq_li=pd.DataFrame(delhi_df["city"].value_counts())
delhi_freq_li=delhi_freq_li.head()
print(delhi_freq_li) 
fig=plt.figure(figsize=(10,10))
sns.scatterplot(delhi_df["lattitude"],delhi_df["longitude"]).set(title="plotting the ev stations in Maharashtra")
maha_freq_li=pd.DataFrame(maha_df["city"].value_counts())


# In[16]:


TamilNadu_df=data[data["state"]=="TamilNadu"]
print(TamilNadu_df)
TamilNadu_freq_li=pd.DataFrame(TamilNadu_df["city"].value_counts())
TamilNadu_freq_li=TamilNadu_freq_li.head()
print(TamilNadu_freq_li) 
fig=plt.figure(figsize=(10,10))
sns.scatterplot(TamilNadu_df["lattitude"],TamilNadu_df["longitude"]).set(title="plotting the ev stations in TamilNadu")


# In[17]:


Kerala_df=data[data["state"]=="Kerala"]
print(Kerala_df)
Kerala_freq_li=pd.DataFrame(Kerala_df["city"].value_counts())
Kerala_freq_li=Kerala_freq_li.head()
print(Kerala_freq_li) 
fig=plt.figure(figsize=(10,10))
sns.scatterplot(Kerala_df["lattitude"],Kerala_df["longitude"]).set(title="plotting the ev stations in Kerala")


# In[18]:


Karnataka_df=data[data["state"]=="Karnataka"]
print(Karnataka_df)
Karnataka_freq_li=pd.DataFrame(Karnataka_df["city"].value_counts())
Karnataka_freq_li=Karnataka_freq_li.head()
print(Karnataka_freq_li) 
fig=plt.figure(figsize=(10,10))
sns.scatterplot(Karnataka_df["lattitude"],Karnataka_df["longitude"]).set(title="plotting the ev stations in Karnataka")


# In[19]:


Telangana_df=data[data["state"]=="Telangana"]
print(Telangana_df)
Telangana_freq_li=pd.DataFrame(Telangana_df["city"].value_counts())
Telangana_freq_li=Telangana_freq_li.head()
print(Telangana_freq_li) 
fig=plt.figure(figsize=(10,10))
sns.scatterplot(Telangana_df["lattitude"],Telangana_df["longitude"]).set(title="plotting the ev stations in Telangana")


# In[20]:


Gujarat_df=data[data["state"]=="Gujarat"]
print(Gujarat_df)
Gujarat_freq_li=pd.DataFrame(Gujarat_df["city"].value_counts())
Gujarat_freq_li=Gujarat_freq_li.head()
print(Gujarat_freq_li) 
fig=plt.figure(figsize=(10,10))
sns.scatterplot(Gujarat_df["lattitude"],Gujarat_df["longitude"]).set(title="plotting the ev stations in Gujarat")


# In[21]:


Rajasthan_df=data[data["state"]=="Rajasthan"]
print(Rajasthan_df)
Rajasthan_freq_li=pd.DataFrame(Rajasthan_df["city"].value_counts())
Rajasthan_freq_li=Rajasthan_freq_li.head()
print(Rajasthan_freq_li) 
fig=plt.figure(figsize=(10,10))
sns.scatterplot(Rajasthan_df["lattitude"],Rajasthan_df["longitude"]).set(title="plotting the ev stations in Rajasthan")


# In[22]:


Uttar_df=data[data["state"]=="Uttar Pradesh"]
print(Uttar_df)
Uttar_freq_li=pd.DataFrame(Uttar_df["city"].value_counts())
Uttar_freq_li=Uttar_freq_li.head()
print(Uttar_freq_li) 
fig=plt.figure(figsize=(10,10))
sns.scatterplot(Uttar_df["lattitude"],Uttar_df["longitude"]).set(title="plotting the ev stations in Uttar Pradesh")


# In[23]:


Haryana_df=data[data["state"]=="Haryana"]
print(Haryana_df)
Haryana_freq_li=pd.DataFrame(Haryana_df["city"].value_counts())
Haryana_freq_li=Haryana_freq_li.head()
print(Haryana_freq_li) 
fig=plt.figure(figsize=(10,10))
sns.scatterplot(Haryana_df["lattitude"],Haryana_df["longitude"]).set(title="plotting the ev stations in Haryana")


# In[26]:


import geopandas


# In[ ]:





# In[ ]:




