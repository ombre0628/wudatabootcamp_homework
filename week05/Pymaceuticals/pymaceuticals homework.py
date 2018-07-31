
# coding: utf-8

# ## Week5 Matplotlib Homework-Pymaceuticals
# 

# # summary 

# * From the plot of "Tumor volume over 45 days", only Capomulin and Ramicane reduced tumor size. Capomulin inhibited tumor growth from 45mm3 to 36mm3, and Ramicane inhibited tumor growth from 45mm3 to 35mm3. Ketapril, Naftisol, and Stelasyn were slightly worse than Placebo.
# 
# * According to the plot of "Metastatic Spread During Treatment", Capomulin and Ramicane both showed an effort to facilitate tumor cell arrest and metastasis. In contrast, Ketapril got the worst result in this test.
# 
# * In the "Survival During Treatment", the mice were used Capomulin increasing in survival rate (21/25) compared to the mice used Placebo(11/25) after 45 days. Ramicane's performance was second best(20/25). 
# 
# * Capomulin and Ramicane were both outstanding from others in reducing tumor size, attenuating tumor metastasis, and increasing the survival rate. 
# 

# In[1]:


# Dependencies and Setup
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats

# Hide warning messages in notebook
import warnings
warnings.filterwarnings('ignore')



# Read the Mouse and Drug Data and the Clinical Trial Data
mouse_drug_data_df=pd.read_csv("data/mouse_drug_data.csv")
clinical_trial_data_df=pd.read_csv("data/clinicaltrial_data.csv")

# Combine the data into a single dataset

combined_data=pd.merge(clinical_trial_data_df,mouse_drug_data_df,on="Mouse ID")



combined_data.head()


# ## Tumor Response to Treatment

# In[2]:


# Store the Mean Tumor Volume Data Grouped by Drug and Timepoint 

MeanofTumorVolume=combined_data.groupby(['Drug','Timepoint'])[['Tumor Volume (mm3)']].mean()

MeanofTumorVolume1=MeanofTumorVolume.reset_index()
MeanofTumorVolume1.head()




# In[3]:


# Store the Standard Error of Tumor Volumes Grouped by Drug and Timepoint
StandErrorTumorVolume = combined_data.groupby(['Drug','Timepoint'])[['Tumor Volume (mm3)']].sem()
StandErrorTumorVolume = StandErrorTumorVolume.reset_index()
StandErrorTumorVolume.head()




# In[4]:


# Minor Data Munging to Re-Format the Data Frames(Stand Error of Tumor Volumes)
StandErrorTumorVolume_reformat = StandErrorTumorVolume.pivot(index='Timepoint',columns='Drug', values='Tumor Volume (mm3)')

StandErrorTumorVolume_reformat.tail()


# In[20]:


# Minor Data Munging to Re-Format the Data Frames(Mean of Tumor Volumes)
MeanofTumorVolume_reformat=MeanofTumorVolume1.pivot(index='Timepoint',columns='Drug', values='Tumor Volume (mm3)')

MeanofTumorVolume_reformat.head(10)


# In[6]:


DrugName=MeanofTumorVolume1['Drug'].unique()
DrugName


# In[7]:


# Generate the Plot (with Error Bars)

DrugName=MeanofTumorVolume1['Drug'].unique()


plt.figure(figsize = (15,10))
plt.title('Tumor Volume Over Time')
plt.xlabel('Days') 
plt.ylabel('Tumor Volume (mm3)') 
plt.xticks(np.arange(0, 55 , 5)) 
plt.grid(True)
xvals = MeanofTumorVolume_reformat.index



for i in DrugName:
    plt.errorbar(xvals, 
                 MeanofTumorVolume_reformat[i], 
                 StandErrorTumorVolume_reformat[i], 
                 capthick = 2,
                 capsize = 5,
                 linestyle = '--',
                 marker =  "*") 
 
legend =plt.legend(loc="best")   

plt.show()




# ## Metastatic Response to Treatment

# In[8]:


# Store the Mean Met. Site Data Grouped by Drug and Timepoint 
Mean_Met_Site_Data=combined_data.groupby(['Drug','Timepoint'])[['Metastatic Sites']].mean()

Mean_Met_Site_Data.head()


# In[9]:


# Store the Standard Error associated with Met. Sites Grouped by Drug and Timepoint 
SEMet_Site_Data=combined_data.groupby(['Drug','Timepoint'])[['Metastatic Sites']].sem()
SEMet_Site_Data.head()



# In[10]:


# Minor Data Munging to Re-Format the Data Frames(Standard Error associated with Met.)
SEMet_Site_Data1=SEMet_Site_Data.reset_index()
SEMet_Site_Data_reform=SEMet_Site_Data1.pivot(index='Timepoint',columns='Drug', values='Metastatic Sites')
SEMet_Site_Data_reform


# In[11]:


# Minor Data Munging to Re-Format the Data Frames(Mean associated with Met.)
Mean_Met_Site_Data1=Mean_Met_Site_Data.reset_index()
Mean_Met_Site_Data_reform1=Mean_Met_Site_Data1.pivot(index='Timepoint',columns='Drug', values='Metastatic Sites')
Mean_Met_Site_Data_reform1


# In[12]:


# Generate the Plot (with Error Bars)

DrugName=MeanofTumorVolume1['Drug'].unique()


plt.figure(figsize = (15,10))
plt.title('Metastatic Spread During Treatment')
plt.xlabel('Treatment Duration(Days)') 
plt.ylabel('Met Sites') 
plt.xticks(np.arange(0, 55 , 5)) 
plt.grid(True)
xvals = Mean_Met_Site_Data_reform1.index



for i in DrugName:
    plt.errorbar(xvals, 
                 Mean_Met_Site_Data_reform1[i], 
                 SEMet_Site_Data_reform[i], 
                 linestyle = '--',
                 marker =  "o",
                 capthick = 2,
                 capsize = 3) 
 
legend1 =plt.legend(loc="best")   

plt.show()
plt.savefig('Metastatic Spread During Treatment')


# ## Survival Rates

# In[13]:


# Store the Count of Mice Grouped by Drug and Timepoint (W can pass any metric)
MouseCount_data=combined_data.groupby(['Drug','Timepoint'])[['Mouse ID']].count()
MouseCount_data1=MouseCount_data.rename(index=str, columns={"Mouse ID": "Mouse Count"})
MouseCount_data2=MouseCount_data1.reset_index()
MouseCount_data2.head()




# In[14]:


#change type of data
MouseCount_data2['Timepoint'] = MouseCount_data2['Timepoint'].astype(int)


# In[15]:


# Minor Data Munging to Re-Format the Data Frames(the Count of Mice Grouped)
MouseCount_data1_reform = MouseCount_data2.pivot(index='Timepoint',columns='Drug', values='Mouse Count')
MouseCount_data1_reform


# In[16]:


# Generate the Plot (Accounting for percentages)
DrugName=MeanofTumorVolume1['Drug'].unique()


plt.figure(figsize = (15,10))
plt.title('Survival During Treatment')
plt.xlabel('Time') 
plt.ylabel('Survival Rate%') 
plt.xticks(np.arange(0, 55 , 5)) 
plt.grid(True)
xvals= MouseCount_data1_reform.index
yvals= MouseCount_data1_reform[i]/MouseCount_data1_reform.loc[0,i] * 100

for i in DrugName:
    yvals= MouseCount_data1_reform[i]/MouseCount_data1_reform.loc[0,i] * 100
    plt.errorbar(xvals, 
                 yvals, 
                 linestyle = '-',
                 marker =  "o",
                 capthick = 2,
                 capsize = 3) 
    
legend1 =plt.legend(loc="best")   
# Show the Figure
plt.show()
plt.savefig('Survival During Treatment')


# In[17]:


#Step plot (Accounting for percentages)

DrugName=MeanofTumorVolume1['Drug'].unique()


plt.figure(figsize = (15,10))
plt.title('Survival During Treatment')
plt.xlabel('Time') 
plt.ylabel('Survival Rate%') 
plt.xticks(np.arange(0, 55 , 5)) 
plt.grid(True)
xvals= MouseCount_data1_reform.index
yvals= MouseCount_data1_reform[i]/MouseCount_data1_reform.loc[0,i] * 100

for i in DrugName:
    yvals= MouseCount_data1_reform[i]/MouseCount_data1_reform.loc[0,i] * 100
    plt.step(xvals, 
             yvals, 
             linestyle = '-',
             marker =  "o",
             where = 'post') 


legend1 =plt.legend(loc="best")  


# ## Summary Bar Graph

# In[18]:


# Calculate the percent changes for each drug
percentChangesTummor=(MeanofTumorVolume_reformat.loc[45]-MeanofTumorVolume_reformat.loc[0])/MeanofTumorVolume_reformat.loc[0]*100

percentChangesTummor


# In[19]:


# Store all Relevant Percent Changes into a Tuple
plt.figure(figsize = (15,10))
plt.title('Tumor Volume Change over 45 Day Treatment')
plt.xlabel('Drug name') 
plt.ylabel('Survival Rate%') 
plt.grid(True)
x_axis = np.arange(len(DrugName))

plt.hlines(0,0,10, color = 'black', linewidth = 0.5)


yvals= percentChangesTummor

plt.bar(x_axis, 
        yvals, 
        color=['red' if percentChangesTummor[i] > 0 else 'green' for i in np.arange(len(DrugName))])

tick_locations = [value for value in x_axis]

plt.xticks(tick_locations,DrugName)





count = 0

#loops through tumor change data and places the value in the correct position based on + or - values
for a in percentChangesTummor:

    plt.text(count, 0.5, str(round(a, 1)) + '%', fontsize=15, color = 'black', ha='center')
    count += 1

plt.show()
plt.savefig('Tumor Volume Change over 45 Day Treatment')

