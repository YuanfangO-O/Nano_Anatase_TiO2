#!/usr/bin/env python
# coding: utf-8

# futurize
# from __future__ import print_function

# In[1]:


#######################################
startYear = 2000
Tperiods = 21      # total time range considered, also for np.arange, important for development of  Accumulation, release, Concentration 
                    # if Tperiods is changed, the import settings of the production data in the model must also be changed (if Tperiods get higher)
RUNs=100 # 10000  
Speriod=20        # specific period for concentrations and Mass-flows, either 14 for 2014 or 20 for 2020
########################################


# In[2]:


import nano_anatase_TiO2_model_product0 as TiO2model # here space is not allowed in model name
import Simulator as sc
import numpy as np
import matplotlib.pyplot as plt
import numpy.random as nr
from scipy.stats import gaussian_kde 
import pandas as pd

# In[3]:


print('Results here in console for period: '+str(Speriod))


# In[4]:


plt.close() # 
model = TiO2model.model
model.checkModelValidity()


# In[5]:


simulator = sc.Simulator(RUNs, Tperiods, 2250, True, True) # 2250 is just a seed
simulator.setModel(model)
simulator.runSimulation()


# In[6]:


sinks = simulator.getSinks()
stocks = simulator.getStocks()


# In[7]:


#print "logged Inflows called"
loggedInflows = simulator.getLoggedInflows() # compartment with loggedInflows


# In[8]:


#print "loggedInflows" + str(loggedInflows)
Comp_with_loggedOutflows = simulator.getLoggedOutflows() # compartment with LoggedOutflows


# In[9]:


## this part is used to display all flows! 
print('logged Outflows:')
for Comp in Comp_with_loggedOutflows: # loggedOutflows is the compartment list of compartmensts with loggedoutflows
    print('Flows from ' + Comp.name +':' )
    for Target_name, value in Comp.outflowRecord.items(): # in this case name is the key, value is the matrix(data), in this case .items is needed
        print(Comp.name + ' --> ' + str(Target_name)) 

        print('Mean-->'+str(round(np.mean(value[:,Speriod]),4)))
        print('Q50--> '+str(round(np.percentile(value[:,Speriod],50),4)))
        print('Q25--> '+str(round(np.percentile(value[:,Speriod],25),4)))
        print('Q75--> '+str(round(np.percentile(value[:,Speriod],75),4)))
        print(' ')        
    print(' ')
print(' ')


# In[10]:


############### ALL DISAGGREGATED FLOWS ######################


# In[11]:


# export all flows to an excel - means
import csv
Flows = []
for Comp in Comp_with_loggedOutflows: # loggedOutflows is the compartment list of compartmensts with loggedoutflows
    for Target_name, value in Comp.outflowRecord.items(): # in this case name is the key, value is the matrix(data), in this case .items is needed     
        x = [] 
        for i in np.arange(0,Tperiods):
            x.append((np.mean(value[:,i])))  
            z = [Comp.name, 'to',Target_name]
            y= x + z
        Flows.append(y)
    with open('AllFlows_TiO2_mean_2000_2020_AUT_2.csv', 'w') as RM :
        a = csv.writer(RM, delimiter=' ')
        data = np.asarray(Flows)
        a.writerows(data)


# In[12]:


# VA: export all flows to an excel - Q5
Flows_Q5 = []
for Comp in Comp_with_loggedOutflows:
    for Target_name, value in Comp.outflowRecord.items():
        x = []
        for i in np.arange(0, Tperiods):
            x.append(np.percentile(value[:,i], 5))
            z = [Comp.name, 'to', Target_name]
            y = x + z
        Flows_Q5.append(y)
    with open('AllFlows_TiO2_Q5_2000_2020_AUT_2.csv', 'w') as RM:
        a = csv.writer(RM, delimiter = ' ')
        data = np.asarray(Flows_Q5)
        a.writerows(data)


# In[13]:


# VA: export all flows to an excel - Q25
Flows_Q25 = []
for Comp in Comp_with_loggedOutflows:
    for Target_name, value in Comp.outflowRecord.items():
        x = []
        for i in np.arange(0, Tperiods):
            x.append(np.percentile(value[:,i], 25))
            z = [Comp.name, 'to', Target_name]
            y = x + z
        Flows_Q25.append(y)
    with open('AllFlows_TiO2_Q25_2000_2020_AUT_2.csv', 'w') as RM:
        a = csv.writer(RM, delimiter = ' ')
        data = np.asarray(Flows_Q25)
        a.writerows(data)


# In[14]:


# VA: export all flows to an excel - Q75
Flows_Q75 = []
for Comp in Comp_with_loggedOutflows:
    for Target_name, value in Comp.outflowRecord.items():
        x = []
        for i in np.arange(0, Tperiods):
            x.append(np.percentile(value[:,i], 75))
            z = [Comp.name, 'to', Target_name]
            y = x + z
        Flows_Q75.append(y)
    with open('AllFlows_TiO2_Q75_2000_2020_AUT_2.csv', 'w') as RM:
        a = csv.writer(RM, delimiter = ' ')
        data = np.asarray(Flows_Q75)
        a.writerows(data)


# In[15]:


# VA: export all flows to an excel - Q95
Flows_Q95 = []
for Comp in Comp_with_loggedOutflows:
    for Target_name, value in Comp.outflowRecord.items():
        x = []
        for i in np.arange(0, Tperiods):
            x.append(np.percentile(value[:,i], 95))
            z = [Comp.name, 'to', Target_name]
            y = x + z
        Flows_Q95.append(y)
    with open('AllFlows_TiO2_Q95_2000_2020_AUT_2.csv', 'w') as RM:
        a = csv.writer(RM, delimiter = ' ')
        data = np.asarray(Flows_Q95)
        a.writerows(data)


# In[16]:


# VA: export all flows to an excel - min
Flows_min = []
for Comp in Comp_with_loggedOutflows:
    for Target_name, value in Comp.outflowRecord.items():
        x = []
        for i in np.arange(0, Tperiods):
            x.append(min(value[:,i]))
            z = [Comp.name, 'to', Target_name]
            y = x + z
        Flows_min.append(y)
    with open('AllFlows_TiO2_min_2000_2020_AUT_2.csv', 'w') as RM:
        a = csv.writer(RM, delimiter = ' ')
        data = np.asarray(Flows_min)
        a.writerows(data)


# In[17]:


# VA: export all flows to an excel - max
Flows_max = []
for Comp in Comp_with_loggedOutflows:
    for Target_name, value in Comp.outflowRecord.items():
        x = []
        for i in np.arange(0, Tperiods):
            x.append(max(value[:,i]))
            z = [Comp.name, 'to', Target_name]
            y = x + z
        Flows_max.append(y)
    with open('AllFlows_TiO2_max_2000_2020_AUT_2.csv', 'w') as RM:
        a = csv.writer(RM, delimiter = ' ')
        data = np.asarray(Flows_max)
        a.writerows(data)


# In[18]:


# VA: export all flows to an excel - medians
Flows_med = []
for Comp in Comp_with_loggedOutflows:
    for Target_name, value in Comp.outflowRecord.items():
        x = []
        for i in np.arange(0, Tperiods):
            x.append(np.percentile(value[:,i], 50))
            z = [Comp.name, 'to', Target_name]
            y = x + z
        Flows_med.append(y)
    with open('AllFlows_TiO2_median_2000_2020_AUT_2.csv', 'w') as RM:
        a = csv.writer(RM, delimiter = ' ')
        data = np.asarray(Flows_med)
        a.writerows(data)


# In[19]:


################# DISAGGREGATED FLOWS TO SINKS #####################


# In[20]:


Comp_with_loggedInflows = simulator.getLoggedInflows()


# In[21]:


# In[13]:
# sum up all inflows to sinks
Prod_to_Air_as_N = Comp_with_loggedInflows['Pristine from Production to Air']
Manuf_to_Air_as_N = Comp_with_loggedInflows['Pristine from Manufacturing to Air']
Paints_to_Air_as_N = Comp_with_loggedInflows['Pristine in Air from Paints']
Paints_to_Air_as_M = Comp_with_loggedInflows['Matrix-embedded in Air from Paints']
Glass_to_Air_as_N = Comp_with_loggedInflows['Pristine from Glass coating to Air']
Glass_to_Air_as_M = Comp_with_loggedInflows['Matrix-embedded from Glass coating to Air']
Ceram_to_Air_as_N = Comp_with_loggedInflows['Pristine from Ceramics coating to Air']
Ceram_to_Air_as_M = Comp_with_loggedInflows['Matrix-embedded from Ceramics coating to Air']
RubPlas_to_Air_as_N = Comp_with_loggedInflows['Pristine from RubPlas to Air']
RubPlas_to_Air_as_M = Comp_with_loggedInflows['Matrix-embedded from RubPlas to Air']
Textiles_to_Air_as_N = Comp_with_loggedInflows['Pristine from Textiles to Air']
Textiles_to_Air_as_M = Comp_with_loggedInflows['Matrix-embedded from Textiles to Air']
WIP_to_Air_as_N = Comp_with_loggedInflows['From WIP to Air as Pristine']
WIP_to_Air_as_T = Comp_with_loggedInflows['From WIP to Air as Transformed']
Repr_to_Air_as_N = Comp_with_loggedInflows['Pristine particles in air from reprocessing systems']
Repr_to_Air_as_M = Comp_with_loggedInflows['Matrix-embedded particles in air from reprocessing systems']

Paints_to_NUSoil_as_N = Comp_with_loggedInflows['Pristine in Soil from Paints']
Paints_to_NUSoil_as_M = Comp_with_loggedInflows['Matrix-embedded in Soil from Paints']
Glass_to_NUSoil_as_N = Comp_with_loggedInflows['Pristine from Glass coating to NU Soil']
Glass_to_NUSoil_as_M = Comp_with_loggedInflows['Matrix-embedded from Glass coating to NU Soil']
Ceram_to_NUSoil_as_N = Comp_with_loggedInflows['Pristine from Ceramics coating to NU Soil']
Ceram_to_NUSoil_as_M = Comp_with_loggedInflows['Matrix-embedded from Ceramics coating to NU Soil']

Sewer_to_Subsurf_as_N = Comp_with_loggedInflows['Pristine from Sewer to Subsurface']
Sewer_to_Subsurf_as_M = Comp_with_loggedInflows['Matrix-embedded from Sewer to Subsurface']
Sewer_to_Subsurf_as_T = Comp_with_loggedInflows['Transformed from Sewer to Subsurface']
OnSiteTreat_to_Subsurf_as_N = Comp_with_loggedInflows['Pristine from On-site treatment to Subsurface']
OnSiteTreat_to_Subsurf_as_M = Comp_with_loggedInflows['Matrix-embedded from On-site treatment to Subsurface']
OnSiteTreat_to_Subsurf_as_T = Comp_with_loggedInflows['Transformed from On-site treatment to Subsurface']

STSoil_N = Comp_with_loggedInflows['Pristine in Sludge treated soil']
STSoil_M = Comp_with_loggedInflows['Matrix-embedded in Sludge treated soil']
STSoil_T = Comp_with_loggedInflows['Transformed in Sludge treated soil']

OnSiteSludge_N = Comp_with_loggedInflows['Pristine in OnsiteSludge']
OnSiteSludge_M = Comp_with_loggedInflows['Matrix-embedded in OnsiteSludge']
OnSiteSludge_T = Comp_with_loggedInflows['Transformed in OnsiteSludge']

PersCare_to_SurfWater_as_N = Comp_with_loggedInflows['Pristine in Surfacewater from PersCare']
NoSewer_to_SurfWater_as_N = Comp_with_loggedInflows['Pristine from no sewer to surface water']
NoSewer_to_SurfWater_as_M = Comp_with_loggedInflows['Matrix-embedded from no sewer to surface water']
NoSewer_to_SurfWater_as_T = Comp_with_loggedInflows['Transformed from no sewer to surface water']
EndSewer_to_SurfWater_as_N = Comp_with_loggedInflows['Pristine from sewer to surface water']
EndSewer_to_SurfWater_as_M = Comp_with_loggedInflows['Matrix-embedded from sewer to surface water']
EndSewer_to_SurfWater_as_T = Comp_with_loggedInflows['Transformed from sewer to surface water']
Overflow_to_SurfWater_as_N = Comp_with_loggedInflows['Pristine to STPoverflow and Surface water']
Overflow_to_SurfWater_as_M = Comp_with_loggedInflows['Matrix-embedded to STPoverflow and Surface water']
Overflow_to_SurfWater_as_T = Comp_with_loggedInflows['Transformed to STPoverflow and Surface water']
STPEffluent_to_SurfWater_as_N = Comp_with_loggedInflows['Pristine to STPeffluent and Surface water']
STPEffluent_to_SurfWater_as_M = Comp_with_loggedInflows['Matrix-embedded to STPeffluent and Surface water']
STPEffluent_to_SurfWater_as_T = Comp_with_loggedInflows['Transformed to STPeffluent and Surface water']

ManufTextW_to_Landfill_as_P = Comp_with_loggedInflows['Product-embedded from Textile manufacturing waste to Landfill']
ManufPlasW_to_Landfill_as_P = Comp_with_loggedInflows['Product-embedded from Plastics manufacturing waste to Landfill']
STPSlud_to_Landfill_as_N = Comp_with_loggedInflows['Pristine from STP Sludge to Landfill']
STPSlud_to_Landfill_as_M = Comp_with_loggedInflows['Matrix-embedded from STP Sludge to Landfill']
STPSlud_to_Landfill_as_T = Comp_with_loggedInflows['Transformed from STP Sludge to Landfill']
MMSW_to_Landfill_as_P = Comp_with_loggedInflows['Product-embedded from MMSW to Landfill']
CDW_to_Landfill_as_P = Comp_with_loggedInflows['Product-embedded from CDW to Landfill']
SortCDWGlass_to_Landfill_as_P = Comp_with_loggedInflows['Product-embedded from Sorted CDW glass to Landfill']
SortCDWMiner_to_Landfill_as_P = Comp_with_loggedInflows['Product-embedded from Sorted CDW minerals to Landfill']
SortDisp_to_Landfill_as_P = Comp_with_loggedInflows['Product-embedded from other sorting to Landfill']
GranuPlas_to_Landfill_as_P = Comp_with_loggedInflows['Product-embedded from Plastic granulation to Landfill']
BaliText_to_Landfill_as_P = Comp_with_loggedInflows['Product-embedded from Textile baling to Landfill']
Purislag_to_Landfill_as_P = Comp_with_loggedInflows['Product-embedded from Purification slag to Landfill']
Purislag_to_Landfill_as_T = Comp_with_loggedInflows['Transformed from Purification slag to Landfill']
SortMiner_to_Landfill_as_P = Comp_with_loggedInflows['Product-embedded from Sorted minerals to Landfill']
Filterash_to_Landfill_as_N = Comp_with_loggedInflows['Pristine from Filter ash to Landfill']
Filterash_to_Landfill_as_T = Comp_with_loggedInflows['Transformed from Filter ash to Landfill']
Bottomash_to_Landfill_as_N = Comp_with_loggedInflows['Pristine from Bottom ash to Landfill']
Bottomash_to_Landfill_as_T = Comp_with_loggedInflows['Transformed from Bottom ash to Landfill']

ManufTextW_to_Reuse_as_P = Comp_with_loggedInflows['Product-embedded from Textile manufacturing to reprocessing and reuse']
ManufPlasW_to_Reuse_as_P = Comp_with_loggedInflows['Product-embedded from Plastic manufacturing to reprocessing and reuse']
ManufSolidW_to_Reuse_as_P = Comp_with_loggedInflows['Product-embedded from Other solids manufacturing to reprocessing and reuse']
Filterash_to_Reuse_as_N = Comp_with_loggedInflows['Pristine from Filter ash to Reuse']
Filterash_to_Reuse_as_T = Comp_with_loggedInflows['Transformed from Filter ash to Reuse']
Bottomash_to_Reuse_as_N = Comp_with_loggedInflows['Pristine from Bottom ash to Reuse']
Bottomash_to_Reuse_as_T = Comp_with_loggedInflows['Transformed from Bottom ash to Reuse']
GranuPlas_to_Reuse_as_P = Comp_with_loggedInflows['Product-embedded from Plastic granulation to Reuse']
BaliText_to_Reuse_as_P = Comp_with_loggedInflows['Product-embedded from Textile baling to Reuse']
PuriMetal_to_Reuse_as_T = Comp_with_loggedInflows['Transformed from Metal purification to Reuse']
PuriMetal_to_Reuse_as_P = Comp_with_loggedInflows['Product-embedded from Metal purification to Reuse']
PuriSlag_to_Reuse_as_T = Comp_with_loggedInflows['Transformed from Purification slag to Reuse']
PuriSlag_to_Reuse_as_P = Comp_with_loggedInflows['Product-embedded from Purification slag to Reuse']
MeltGlass_to_Reuse_as_T = Comp_with_loggedInflows['Transformed from Glass melting to Reuse']
SortMiner_to_Reuse_as_P = Comp_with_loggedInflows['Product-embedded from Sorted minerals to Reuse']

SortWEEE_to_Export_as_P = Comp_with_loggedInflows['From Sorting WEEE to Export']
SortTextW_to_Export_as_P = Comp_with_loggedInflows['From Sorting Textile waste to Export']


# In[22]:


# Extract means to sinks for each year

Means_To_Sinks = np.zeros(shape=(83,Tperiods))

for i in np.arange(0,Tperiods):
    Means_To_Sinks[0,i]=np.mean(Prod_to_Air_as_N[:,i])
    Means_To_Sinks[1,i]=np.mean(Manuf_to_Air_as_N[:,i])
    Means_To_Sinks[2,i]=np.mean(Paints_to_Air_as_N[:,i])
    Means_To_Sinks[3,i]=np.mean(Paints_to_Air_as_M[:,i])
    Means_To_Sinks[4,i]=np.mean(Glass_to_Air_as_N[:,i])
    Means_To_Sinks[5,i]=np.mean(Glass_to_Air_as_M[:,i])
    Means_To_Sinks[6,i]=np.mean(Ceram_to_Air_as_N[:,i])
    Means_To_Sinks[7,i]=np.mean(Ceram_to_Air_as_M[:,i])
    Means_To_Sinks[8,i]=np.mean(RubPlas_to_Air_as_N[:,i])
    Means_To_Sinks[9,i]=np.mean(RubPlas_to_Air_as_M[:,i])
    Means_To_Sinks[10,i]=np.mean(Textiles_to_Air_as_N[:,i])
    Means_To_Sinks[11,i]=np.mean(Textiles_to_Air_as_M[:,i])
    Means_To_Sinks[12,i]=np.mean(WIP_to_Air_as_N[:,i])
    Means_To_Sinks[13,i]=np.mean(WIP_to_Air_as_T[:,i])
    Means_To_Sinks[14,i]=np.mean(Repr_to_Air_as_N[:,i])
    Means_To_Sinks[15,i]=np.mean(Repr_to_Air_as_M[:,i])
    Means_To_Sinks[16,i]=np.mean(Paints_to_NUSoil_as_N[:,i])
    Means_To_Sinks[17,i]=np.mean(Paints_to_NUSoil_as_M[:,i])
    Means_To_Sinks[18,i]=np.mean(Glass_to_NUSoil_as_N[:,i])
    Means_To_Sinks[19,i]=np.mean(Glass_to_NUSoil_as_M[:,i])
    Means_To_Sinks[20,i]=np.mean(Ceram_to_NUSoil_as_N[:,i])
    Means_To_Sinks[21,i]=np.mean(Ceram_to_NUSoil_as_M[:,i])
    Means_To_Sinks[22,i]=np.mean(Sewer_to_Subsurf_as_N[:,i])
    Means_To_Sinks[23,i]=np.mean(Sewer_to_Subsurf_as_M[:,i])
    Means_To_Sinks[24,i]=np.mean(Sewer_to_Subsurf_as_T[:,i])
    Means_To_Sinks[25,i]=np.mean(OnSiteTreat_to_Subsurf_as_N[:,i])
    Means_To_Sinks[26,i]=np.mean(OnSiteTreat_to_Subsurf_as_M[:,i])
    Means_To_Sinks[27,i]=np.mean(OnSiteTreat_to_Subsurf_as_T[:,i])
    Means_To_Sinks[28,i]=np.mean(STSoil_N[:,i])
    Means_To_Sinks[29,i]=np.mean(STSoil_M[:,i])
    Means_To_Sinks[30,i]=np.mean(STSoil_T[:,i])
    Means_To_Sinks[31,i]=np.mean(OnSiteSludge_N[:,i])
    Means_To_Sinks[32,i]=np.mean(OnSiteSludge_M[:,i])
    Means_To_Sinks[33,i]=np.mean(OnSiteSludge_T[:,i])
    Means_To_Sinks[34,i]=np.mean(PersCare_to_SurfWater_as_N[:,i])
    Means_To_Sinks[35,i]=np.mean(NoSewer_to_SurfWater_as_N[:,i])
    Means_To_Sinks[36,i]=np.mean(NoSewer_to_SurfWater_as_M[:,i])
    Means_To_Sinks[37,i]=np.mean(NoSewer_to_SurfWater_as_T[:,i])
    Means_To_Sinks[38,i]=np.mean(EndSewer_to_SurfWater_as_N[:,i])
    Means_To_Sinks[39,i]=np.mean(EndSewer_to_SurfWater_as_M[:,i])
    Means_To_Sinks[40,i]=np.mean(EndSewer_to_SurfWater_as_T[:,i])
    Means_To_Sinks[41,i]=np.mean(Overflow_to_SurfWater_as_N[:,i])
    Means_To_Sinks[42,i]=np.mean(Overflow_to_SurfWater_as_M[:,i])
    Means_To_Sinks[43,i]=np.mean(Overflow_to_SurfWater_as_T[:,i])
    Means_To_Sinks[44,i]=np.mean(STPEffluent_to_SurfWater_as_N[:,i])
    Means_To_Sinks[45,i]=np.mean(STPEffluent_to_SurfWater_as_M[:,i])
    Means_To_Sinks[46,i]=np.mean(STPEffluent_to_SurfWater_as_T[:,i])
    Means_To_Sinks[47,i]=np.mean(ManufTextW_to_Landfill_as_P[:,i])
    Means_To_Sinks[48,i]=np.mean(ManufPlasW_to_Landfill_as_P[:,i])
    Means_To_Sinks[49,i]=np.mean(STPSlud_to_Landfill_as_N[:,i])
    Means_To_Sinks[50,i]=np.mean(STPSlud_to_Landfill_as_M[:,i])
    Means_To_Sinks[51,i]=np.mean(STPSlud_to_Landfill_as_T[:,i])
    Means_To_Sinks[52,i]=np.mean(MMSW_to_Landfill_as_P[:,i])
    Means_To_Sinks[53,i]=np.mean(CDW_to_Landfill_as_P[:,i])
    Means_To_Sinks[54,i]=np.mean(SortCDWGlass_to_Landfill_as_P[:,i])
    Means_To_Sinks[55,i]=np.mean(SortCDWMiner_to_Landfill_as_P[:,i])
    Means_To_Sinks[56,i]=np.mean(SortDisp_to_Landfill_as_P[:,i])
    Means_To_Sinks[57,i]=np.mean(GranuPlas_to_Landfill_as_P[:,i])
    Means_To_Sinks[58,i]=np.mean(BaliText_to_Landfill_as_P[:,i])
    Means_To_Sinks[59,i]=np.mean(Purislag_to_Landfill_as_P[:,i])
    Means_To_Sinks[60,i]=np.mean(Purislag_to_Landfill_as_T[:,i])
    Means_To_Sinks[61,i]=np.mean(SortMiner_to_Landfill_as_P[:,i])
    Means_To_Sinks[62,i]=np.mean(Filterash_to_Landfill_as_N[:,i])
    Means_To_Sinks[63,i]=np.mean(Filterash_to_Landfill_as_T[:,i])
    Means_To_Sinks[64,i]=np.mean(Bottomash_to_Landfill_as_N[:,i])
    Means_To_Sinks[65,i]=np.mean(Bottomash_to_Landfill_as_T[:,i])
    Means_To_Sinks[66,i]=np.mean(ManufTextW_to_Reuse_as_P[:,i])
    Means_To_Sinks[67,i]=np.mean(ManufPlasW_to_Reuse_as_P[:,i])
    Means_To_Sinks[68,i]=np.mean(ManufSolidW_to_Reuse_as_P[:,i])
    Means_To_Sinks[69,i]=np.mean(Filterash_to_Reuse_as_N[:,i])
    Means_To_Sinks[70,i]=np.mean(Filterash_to_Reuse_as_T[:,i])
    Means_To_Sinks[71,i]=np.mean(Bottomash_to_Reuse_as_N[:,i])
    Means_To_Sinks[72,i]=np.mean(Bottomash_to_Reuse_as_T[:,i])
    Means_To_Sinks[73,i]=np.mean(GranuPlas_to_Reuse_as_P[:,i])
    Means_To_Sinks[74,i]=np.mean(BaliText_to_Reuse_as_P[:,i])
    Means_To_Sinks[75,i]=np.mean(PuriMetal_to_Reuse_as_T[:,i])
    Means_To_Sinks[76,i]=np.mean(PuriMetal_to_Reuse_as_P[:,i])
    Means_To_Sinks[77,i]=np.mean(PuriSlag_to_Reuse_as_T[:,i])
    Means_To_Sinks[78,i]=np.mean(PuriSlag_to_Reuse_as_P[:,i])
    Means_To_Sinks[79,i]=np.mean(MeltGlass_to_Reuse_as_T[:,i])
    Means_To_Sinks[80,i]=np.mean(SortMiner_to_Reuse_as_P[:,i])
    Means_To_Sinks[81,i]=np.mean(SortWEEE_to_Export_as_P[:,i])
    Means_To_Sinks[82,i]=np.mean(SortTextW_to_Export_as_P[:,i])


# In[23]:


Means_To_Sinks_DF = pd.DataFrame({'Pristine to Air from Production':Means_To_Sinks[0,:],
                               'Pristine to Air from Manufacturing':Means_To_Sinks[1,:],
                               'Pristine to Air from Paints':Means_To_Sinks[2,:],
                               'Matrix-embedded to Air from Paints':Means_To_Sinks[3,:],
                               'Pristine to Air from Glass':Means_To_Sinks[4,:],
                               'Matrix-embedded to Air from Glass':Means_To_Sinks[5,:],
                               'Pristine to Air from Ceramics':Means_To_Sinks[6,:],
                               'Matrix-embedded to Air from Ceramics':Means_To_Sinks[7,:],
                               'Pristine to Air from Rubber & Plastics':Means_To_Sinks[8,:],
                               'Matrix-embedded to Air from Rubber & Plastics':Means_To_Sinks[9,:],
                              'Pristine to Air from Textiles':Means_To_Sinks[10,:],
                              'Matrix-embedded to Air from Textiles':Means_To_Sinks[11,:],
                              'Pristine to Air from WIP':Means_To_Sinks[12,:],
                              'Transformed to Air from WIP':Means_To_Sinks[13,:],
                              'Pristine particles to Air from Reprocessing':Means_To_Sinks[14,:],
                              'Matrix-embedded particles to Air from Reprocessing':Means_To_Sinks[15,:],
                              'Pristine to NUSoil from Paints':Means_To_Sinks[16,:],
                              'Matrix-embedded to NUSoil from Paints':Means_To_Sinks[17,:],
                               'Pristine to NUSoil from Glass':Means_To_Sinks[18,:],
                              'Matrix-embedded to NUSoil from Glass':Means_To_Sinks[19,:],
                               'Pristine to NUSoil from Ceramics':Means_To_Sinks[20,:],
                              'Matrix-embedded to NUSoil from Ceramics':Means_To_Sinks[21,:],
                              'Pristine to Subsurface from Sewer':Means_To_Sinks[22,:],
                              'Matrix-embedded to Subsurface from Sewer':Means_To_Sinks[23,:],
                              'Transformed to Subsurface from Sewer':Means_To_Sinks[24,:],
                              'Pristine to Subsurface from OnSite treatment':Means_To_Sinks[25,:],
                              'Matrix-embedded to Subsurface from OnSite treatment':Means_To_Sinks[26,:],
                              'Transformed to Subsurface from OnSite treatment':Means_To_Sinks[27,:],
                              'Pristine to Sludge treated soil':Means_To_Sinks[28,:],
                               'Matrix-embedded to Sludge treated soil':Means_To_Sinks[29,:],
                              'Transformed to Sludge treated soil':Means_To_Sinks[30,:],
                              'Pristine to OnsiteSludge':Means_To_Sinks[31,:],
                               'Matrix-embedded to OnsiteSludge':Means_To_Sinks[32,:],
                              'Transformed to OnsiteSludge':Means_To_Sinks[33,:],
                              'Pristine to Surface water from PersCareLiquids':Means_To_Sinks[34,:],
                              'Pristine to Surface water from No sewer':Means_To_Sinks[35,:],
                              'Matrix-embedded to Surface water from No sewer':Means_To_Sinks[36,:],
                              'Transformed to Surface water from No sewer':Means_To_Sinks[37,:],
                              'Pristine to Surface water from Sewer':Means_To_Sinks[38,:],
                               'Matrix-embedded to Surface water from Sewer':Means_To_Sinks[39,:],
                              'Transformed to Surface water from Sewer':Means_To_Sinks[40,:],
                              'Pristine to STP overflow and Surface water':Means_To_Sinks[41,:],
                              'Matrix-embedded to STP overflow and Surface water':Means_To_Sinks[42,:],
                              'Transformed to STP overflow and Surface water':Means_To_Sinks[43,:],
                              'Pristine to STP effluent and Surface water':Means_To_Sinks[44,:],
                              'Matrix-embedded to STP effluent and Surface water':Means_To_Sinks[45,:],
                              'Transformed to STP effluent and Surface water':Means_To_Sinks[46,:],
                              'Product-embedded to Landfill from Textiles manufacturing waste':Means_To_Sinks[47,:],
                               'Product-embedded to Landfill from Plastic manufacturing waste':Means_To_Sinks[48,:],
                              'Pristine to Landfill from STP sludge':Means_To_Sinks[49,:],
                               'Matrix-embedded to Landfill from STP sludge':Means_To_Sinks[50,:],
                              'Transformed to Landfill from STP sludge':Means_To_Sinks[51,:],
                              'Product-embedded to Landfill from MMSW':Means_To_Sinks[52,:],
                              'Product-embedded to Landfill from CDW':Means_To_Sinks[53,:],
                              'Product-embedded to Landfill from Sorted CDW Glass':Means_To_Sinks[54,:],
                              'Product-embedded to Landfill from Sorted CDW Mineral':Means_To_Sinks[55,:],
                              'Product-embedded to Landfill from Other sorting':Means_To_Sinks[56,:],
                               'Product-embedded to Landfill from Plastic granulation':Means_To_Sinks[57,:],
                               'Product-embedded to Landfill from Textile baling':Means_To_Sinks[58,:],
                               'Product-embedded to Landfill from Purification slag':Means_To_Sinks[59,:],
                               'Transformed to Landfill from Purification slag':Means_To_Sinks[60,:],
                               'Product-embedded to Landfill from Sorted mineral':Means_To_Sinks[61,],
                               'Pristine to Landfill from Filter ash':Means_To_Sinks[62,:],
                              'Transformed to Landfill from Filter ash':Means_To_Sinks[63,:],
                              'Pristine to Landfill from Bottom ash':Means_To_Sinks[64,:],
                              'Transformed to Landfill from Bottom ash':Means_To_Sinks[65,:],
                              'Product-embedded to Reuse from Manufacturing textile waste':Means_To_Sinks[66,:],
                               'Product-embedded to Reuse from Manufacturing plastic waste':Means_To_Sinks[67,:],
                              'Product-embedded to Reuse from Manufacturing other solid waste':Means_To_Sinks[68,:],
                              'Pristine from Filter ash to Reuse':Means_To_Sinks[69,:],
                              'Transformed to Reuse from Filter ash':Means_To_Sinks[70,:],
                              'Pristine to Reuse from Bottom ash':Means_To_Sinks[71,:],
                              'Transformed to Reuse from Bottom ash':Means_To_Sinks[72,:],
                              'Product-embedded to Reuse from Plastic granulation':Means_To_Sinks[73,:],
                              'Product-embedded to Reuse from Baling textiles':Means_To_Sinks[74,:],
                              'Transformed to Reuse from Metal purification':Means_To_Sinks[75,:],
                               'Product-embedded to Reuse from Metal purification':Means_To_Sinks[76,:],
                              'Transformed to Reuse from Slag purification':Means_To_Sinks[77,:],
                               'Product-embedded to Reuse from Slag purification':Means_To_Sinks[78,:],
                              'Transformed to Reuse from Melting glass':Means_To_Sinks[79,:],
                              'Product-embedded to Reuse from Sorting minerals':Means_To_Sinks[80,:],
                              'Product-embedded to Export from Sorting WEEE':Means_To_Sinks[81,:],
                              'Product-embedded to Export from Sorting textile waste':Means_To_Sinks[82,:],})


Means_To_Sinks_DF_Transp = pd.DataFrame.transpose(Means_To_Sinks_DF)
Means_To_Sinks_DF_Transp.to_csv('Means to Sinks - TiO2 - AUT_2.csv',index=True, sep=',')


# In[24]:


# Extract means to sinks for each year

Min_To_Sinks = np.zeros(shape=(83,Tperiods))

for i in np.arange(0,Tperiods):
    Min_To_Sinks[0,i]=min(Prod_to_Air_as_N[:,i])
    Min_To_Sinks[1,i]=min(Manuf_to_Air_as_N[:,i])
    Min_To_Sinks[2,i]=min(Paints_to_Air_as_N[:,i])
    Min_To_Sinks[3,i]=min(Paints_to_Air_as_M[:,i])
    Min_To_Sinks[4,i]=min(Glass_to_Air_as_N[:,i])
    Min_To_Sinks[5,i]=min(Glass_to_Air_as_M[:,i])
    Min_To_Sinks[6,i]=min(Ceram_to_Air_as_N[:,i])
    Min_To_Sinks[7,i]=min(Ceram_to_Air_as_M[:,i])
    Min_To_Sinks[8,i]=min(RubPlas_to_Air_as_N[:,i])
    Min_To_Sinks[9,i]=min(RubPlas_to_Air_as_M[:,i])
    Min_To_Sinks[10,i]=min(Textiles_to_Air_as_N[:,i])
    Min_To_Sinks[11,i]=min(Textiles_to_Air_as_M[:,i])
    Min_To_Sinks[12,i]=min(WIP_to_Air_as_N[:,i])
    Min_To_Sinks[13,i]=min(WIP_to_Air_as_T[:,i])
    Min_To_Sinks[14,i]=min(Repr_to_Air_as_N[:,i])
    Min_To_Sinks[15,i]=min(Repr_to_Air_as_M[:,i])
    Min_To_Sinks[16,i]=min(Paints_to_NUSoil_as_N[:,i])
    Min_To_Sinks[17,i]=min(Paints_to_NUSoil_as_M[:,i])
    Min_To_Sinks[18,i]=min(Glass_to_NUSoil_as_N[:,i])
    Min_To_Sinks[19,i]=min(Glass_to_NUSoil_as_M[:,i])
    Min_To_Sinks[20,i]=min(Ceram_to_NUSoil_as_N[:,i])
    Min_To_Sinks[21,i]=min(Ceram_to_NUSoil_as_M[:,i])
    Min_To_Sinks[22,i]=min(Sewer_to_Subsurf_as_N[:,i])
    Min_To_Sinks[23,i]=min(Sewer_to_Subsurf_as_M[:,i])
    Min_To_Sinks[24,i]=min(Sewer_to_Subsurf_as_T[:,i])
    Min_To_Sinks[25,i]=min(OnSiteTreat_to_Subsurf_as_N[:,i])
    Min_To_Sinks[26,i]=min(OnSiteTreat_to_Subsurf_as_M[:,i])
    Min_To_Sinks[27,i]=min(OnSiteTreat_to_Subsurf_as_T[:,i])
    Min_To_Sinks[28,i]=min(STSoil_N[:,i])
    Min_To_Sinks[29,i]=min(STSoil_M[:,i])
    Min_To_Sinks[30,i]=min(STSoil_T[:,i])
    Min_To_Sinks[31,i]=min(OnSiteSludge_N[:,i])
    Min_To_Sinks[32,i]=min(OnSiteSludge_M[:,i])
    Min_To_Sinks[33,i]=min(OnSiteSludge_T[:,i])
    Min_To_Sinks[34,i]=min(PersCare_to_SurfWater_as_N[:,i])
    Min_To_Sinks[35,i]=min(NoSewer_to_SurfWater_as_N[:,i])
    Min_To_Sinks[36,i]=min(NoSewer_to_SurfWater_as_M[:,i])
    Min_To_Sinks[37,i]=min(NoSewer_to_SurfWater_as_T[:,i])
    Min_To_Sinks[38,i]=min(EndSewer_to_SurfWater_as_N[:,i])
    Min_To_Sinks[39,i]=min(EndSewer_to_SurfWater_as_M[:,i])
    Min_To_Sinks[40,i]=min(EndSewer_to_SurfWater_as_T[:,i])
    Min_To_Sinks[41,i]=min(Overflow_to_SurfWater_as_N[:,i])
    Min_To_Sinks[42,i]=min(Overflow_to_SurfWater_as_M[:,i])
    Min_To_Sinks[43,i]=min(Overflow_to_SurfWater_as_T[:,i])
    Min_To_Sinks[44,i]=min(STPEffluent_to_SurfWater_as_N[:,i])
    Min_To_Sinks[45,i]=min(STPEffluent_to_SurfWater_as_M[:,i])
    Min_To_Sinks[46,i]=min(STPEffluent_to_SurfWater_as_T[:,i])
    Min_To_Sinks[47,i]=min(ManufTextW_to_Landfill_as_P[:,i])
    Min_To_Sinks[48,i]=min(ManufPlasW_to_Landfill_as_P[:,i])
    Min_To_Sinks[49,i]=min(STPSlud_to_Landfill_as_N[:,i])
    Min_To_Sinks[50,i]=min(STPSlud_to_Landfill_as_M[:,i])
    Min_To_Sinks[51,i]=min(STPSlud_to_Landfill_as_T[:,i])
    Min_To_Sinks[52,i]=min(MMSW_to_Landfill_as_P[:,i])
    Min_To_Sinks[53,i]=min(CDW_to_Landfill_as_P[:,i])
    Min_To_Sinks[54,i]=min(SortCDWGlass_to_Landfill_as_P[:,i])
    Min_To_Sinks[55,i]=min(SortCDWMiner_to_Landfill_as_P[:,i])
    Min_To_Sinks[56,i]=min(SortDisp_to_Landfill_as_P[:,i])
    Min_To_Sinks[57,i]=min(GranuPlas_to_Landfill_as_P[:,i])
    Min_To_Sinks[58,i]=min(BaliText_to_Landfill_as_P[:,i])
    Min_To_Sinks[59,i]=min(Purislag_to_Landfill_as_P[:,i])
    Min_To_Sinks[60,i]=min(Purislag_to_Landfill_as_T[:,i])
    Min_To_Sinks[61,i]=min(SortMiner_to_Landfill_as_P[:,i])
    Min_To_Sinks[62,i]=min(Filterash_to_Landfill_as_N[:,i])
    Min_To_Sinks[63,i]=min(Filterash_to_Landfill_as_T[:,i])
    Min_To_Sinks[64,i]=min(Bottomash_to_Landfill_as_N[:,i])
    Min_To_Sinks[65,i]=min(Bottomash_to_Landfill_as_T[:,i])
    Min_To_Sinks[66,i]=min(ManufTextW_to_Reuse_as_P[:,i])
    Min_To_Sinks[67,i]=min(ManufPlasW_to_Reuse_as_P[:,i])
    Min_To_Sinks[68,i]=min(ManufSolidW_to_Reuse_as_P[:,i])
    Min_To_Sinks[69,i]=min(Filterash_to_Reuse_as_N[:,i])
    Min_To_Sinks[70,i]=min(Filterash_to_Reuse_as_T[:,i])
    Min_To_Sinks[71,i]=min(Bottomash_to_Reuse_as_N[:,i])
    Min_To_Sinks[72,i]=min(Bottomash_to_Reuse_as_T[:,i])
    Min_To_Sinks[73,i]=min(GranuPlas_to_Reuse_as_P[:,i])
    Min_To_Sinks[74,i]=min(BaliText_to_Reuse_as_P[:,i])
    Min_To_Sinks[75,i]=min(PuriMetal_to_Reuse_as_T[:,i])
    Min_To_Sinks[76,i]=min(PuriMetal_to_Reuse_as_P[:,i])
    Min_To_Sinks[77,i]=min(PuriSlag_to_Reuse_as_T[:,i])
    Min_To_Sinks[78,i]=min(PuriSlag_to_Reuse_as_P[:,i])
    Min_To_Sinks[79,i]=min(MeltGlass_to_Reuse_as_T[:,i])
    Min_To_Sinks[80,i]=min(SortMiner_to_Reuse_as_P[:,i])
    Min_To_Sinks[81,i]=min(SortWEEE_to_Export_as_P[:,i])
    Min_To_Sinks[82,i]=min(SortTextW_to_Export_as_P[:,i])


# In[25]:


Min_To_Sinks_DF = pd.DataFrame({'Pristine to Air from Production':Min_To_Sinks[0,:],
                               'Pristine to Air from Manufacturing':Min_To_Sinks[1,:],
                               'Pristine to Air from Paints':Min_To_Sinks[2,:],
                               'Matrix-embedded to Air from Paints':Min_To_Sinks[3,:],
                               'Pristine to Air from Glass':Min_To_Sinks[4,:],
                               'Matrix-embedded to Air from Glass':Min_To_Sinks[5,:],
                               'Pristine to Air from Ceramics':Min_To_Sinks[6,:],
                               'Matrix-embedded to Air from Ceramics':Min_To_Sinks[7,:],
                               'Pristine to Air from Rubber & Plastics':Min_To_Sinks[8,:],
                               'Matrix-embedded to Air from Rubber & Plastics':Min_To_Sinks[9,:],
                              'Pristine to Air from Textiles':Min_To_Sinks[10,:],
                              'Matrix-embedded to Air from Textiles':Min_To_Sinks[11,:],
                              'Pristine to Air from WIP':Min_To_Sinks[12,:],
                              'Transformed to Air from WIP':Min_To_Sinks[13,:],
                              'Pristine particles to Air from Reprocessing':Min_To_Sinks[14,:],
                              'Matrix-embedded particles to Air from Reprocessing':Min_To_Sinks[15,:],
                              'Pristine to NUSoil from Paints':Min_To_Sinks[16,:],
                              'Matrix-embedded to NUSoil from Paints':Min_To_Sinks[17,:],
                               'Pristine to NUSoil from Glass':Min_To_Sinks[18,:],
                              'Matrix-embedded to NUSoil from Glass':Min_To_Sinks[19,:],
                               'Pristine to NUSoil from Ceramics':Min_To_Sinks[20,:],
                              'Matrix-embedded to NUSoil from Ceramics':Min_To_Sinks[21,:],
                              'Pristine to Subsurface from Sewer':Min_To_Sinks[22,:],
                              'Matrix-embedded to Subsurface from Sewer':Min_To_Sinks[23,:],
                              'Transformed to Subsurface from Sewer':Min_To_Sinks[24,:],
                              'Pristine to Subsurface from OnSite treatment':Min_To_Sinks[25,:],
                              'Matrix-embedded to Subsurface from OnSite treatment':Min_To_Sinks[26,:],
                              'Transformed to Subsurface from OnSite treatment':Min_To_Sinks[27,:],
                              'Pristine to Sludge treated soil':Min_To_Sinks[28,:],
                               'Matrix-embedded to Sludge treated soil':Min_To_Sinks[29,:],
                              'Transformed to Sludge treated soil':Min_To_Sinks[30,:],
                              'Pristine to OnsiteSludge':Min_To_Sinks[31,:],
                               'Matrix-embedded to OnsiteSludge':Min_To_Sinks[32,:],
                              'Transformed to OnsiteSludge':Min_To_Sinks[33,:],
                              'Pristine to Surface water from PersCareLiquids':Min_To_Sinks[34,:],
                              'Pristine to Surface water from No sewer':Min_To_Sinks[35,:],
                              'Matrix-embedded to Surface water from No sewer':Min_To_Sinks[36,:],
                              'Transformed to Surface water from No sewer':Min_To_Sinks[37,:],
                              'Pristine to Surface water from Sewer':Min_To_Sinks[38,:],
                               'Matrix-embedded to Surface water from Sewer':Min_To_Sinks[39,:],
                              'Transformed to Surface water from Sewer':Min_To_Sinks[40,:],
                              'Pristine to STP overflow and Surface water':Min_To_Sinks[41,:],
                              'Matrix-embedded to STP overflow and Surface water':Min_To_Sinks[42,:],
                              'Transformed to STP overflow and Surface water':Min_To_Sinks[43,:],
                              'Pristine to STP effluent and Surface water':Min_To_Sinks[44,:],
                              'Matrix-embedded to STP effluent and Surface water':Min_To_Sinks[45,:],
                              'Transformed to STP effluent and Surface water':Min_To_Sinks[46,:],
                              'Product-embedded to Landfill from Textiles manufacturing waste':Min_To_Sinks[47,:],
                               'Product-embedded to Landfill from Plastic manufacturing waste':Min_To_Sinks[48,:],
                              'Pristine to Landfill from STP sludge':Min_To_Sinks[49,:],
                               'Matrix-embedded to Landfill from STP sludge':Min_To_Sinks[50,:],
                              'Transformed to Landfill from STP sludge':Min_To_Sinks[51,:],
                              'Product-embedded to Landfill from MMSW':Min_To_Sinks[52,:],
                              'Product-embedded to Landfill from CDW':Min_To_Sinks[53,:],
                              'Product-embedded to Landfill from Sorted CDW Glass':Min_To_Sinks[54,:],
                              'Product-embedded to Landfill from Sorted CDW Mineral':Min_To_Sinks[55,:],
                              'Product-embedded to Landfill from Other sorting':Min_To_Sinks[56,:],
                               'Product-embedded to Landfill from Plastic granulation':Min_To_Sinks[57,:],
                               'Product-embedded to Landfill from Textile baling':Min_To_Sinks[58,:],
                               'Product-embedded to Landfill from Purification slag':Min_To_Sinks[59,:],
                               'Transformed to Landfill from Purification slag':Min_To_Sinks[60,:],
                               'Product-embedded to Landfill from Sorted mineral':Min_To_Sinks[61,],
                               'Pristine to Landfill from Filter ash':Min_To_Sinks[62,:],
                              'Transformed to Landfill from Filter ash':Min_To_Sinks[63,:],
                              'Pristine to Landfill from Bottom ash':Min_To_Sinks[64,:],
                              'Transformed to Landfill from Bottom ash':Min_To_Sinks[65,:],
                              'Product-embedded to Reuse from Manufacturing textile waste':Min_To_Sinks[66,:],
                               'Product-embedded to Reuse from Manufacturing plastic waste':Min_To_Sinks[67,:],
                              'Product-embedded to Reuse from Manufacturing other solid waste':Min_To_Sinks[68,:],
                              'Pristine from Filter ash to Reuse':Min_To_Sinks[69,:],
                              'Transformed to Reuse from Filter ash':Min_To_Sinks[70,:],
                              'Pristine to Reuse from Bottom ash':Min_To_Sinks[71,:],
                              'Transformed to Reuse from Bottom ash':Min_To_Sinks[72,:],
                              'Product-embedded to Reuse from Plastic granulation':Min_To_Sinks[73,:],
                              'Product-embedded to Reuse from Baling textiles':Min_To_Sinks[74,:],
                              'Transformed to Reuse from Metal purification':Min_To_Sinks[75,:],
                               'Product-embedded to Reuse from Metal purification':Min_To_Sinks[76,:],
                              'Transformed to Reuse from Slag purification':Min_To_Sinks[77,:],
                               'Product-embedded to Reuse from Slag purification':Min_To_Sinks[78,:],
                              'Transformed to Reuse from Melting glass':Min_To_Sinks[79,:],
                              'Product-embedded to Reuse from Sorting minerals':Min_To_Sinks[80,:],
                              'Product-embedded to Export from Sorting WEEE':Min_To_Sinks[81,:],
                              'Product-embedded to Export from Sorting textile waste':Min_To_Sinks[82,:],})


Min_To_Sinks_DF_Transp = pd.DataFrame.transpose(Min_To_Sinks_DF)
Min_To_Sinks_DF_Transp.to_csv('Min to Sinks - TiO2 - AUT.csv',index=True, sep=',')


# In[26]:


# Extract means to sinks for each year

Max_To_Sinks = np.zeros(shape=(83,Tperiods))

for i in np.arange(0,Tperiods):
    Max_To_Sinks[0,i]=max(Prod_to_Air_as_N[:,i])
    Max_To_Sinks[1,i]=max(Manuf_to_Air_as_N[:,i])
    Max_To_Sinks[2,i]=max(Paints_to_Air_as_N[:,i])
    Max_To_Sinks[3,i]=max(Paints_to_Air_as_M[:,i])
    Max_To_Sinks[4,i]=max(Glass_to_Air_as_N[:,i])
    Max_To_Sinks[5,i]=max(Glass_to_Air_as_M[:,i])
    Max_To_Sinks[6,i]=max(Ceram_to_Air_as_N[:,i])
    Max_To_Sinks[7,i]=max(Ceram_to_Air_as_M[:,i])
    Max_To_Sinks[8,i]=max(RubPlas_to_Air_as_N[:,i])
    Max_To_Sinks[9,i]=max(RubPlas_to_Air_as_M[:,i])
    Max_To_Sinks[10,i]=max(Textiles_to_Air_as_N[:,i])
    Max_To_Sinks[11,i]=max(Textiles_to_Air_as_M[:,i])
    Max_To_Sinks[12,i]=max(WIP_to_Air_as_N[:,i])
    Max_To_Sinks[13,i]=max(WIP_to_Air_as_T[:,i])
    Max_To_Sinks[14,i]=max(Repr_to_Air_as_N[:,i])
    Max_To_Sinks[15,i]=max(Repr_to_Air_as_M[:,i])
    Max_To_Sinks[16,i]=max(Paints_to_NUSoil_as_N[:,i])
    Max_To_Sinks[17,i]=max(Paints_to_NUSoil_as_M[:,i])
    Max_To_Sinks[18,i]=max(Glass_to_NUSoil_as_N[:,i])
    Max_To_Sinks[19,i]=max(Glass_to_NUSoil_as_M[:,i])
    Max_To_Sinks[20,i]=max(Ceram_to_NUSoil_as_N[:,i])
    Max_To_Sinks[21,i]=max(Ceram_to_NUSoil_as_M[:,i])
    Max_To_Sinks[22,i]=max(Sewer_to_Subsurf_as_N[:,i])
    Max_To_Sinks[23,i]=max(Sewer_to_Subsurf_as_M[:,i])
    Max_To_Sinks[24,i]=max(Sewer_to_Subsurf_as_T[:,i])
    Max_To_Sinks[25,i]=max(OnSiteTreat_to_Subsurf_as_N[:,i])
    Max_To_Sinks[26,i]=max(OnSiteTreat_to_Subsurf_as_M[:,i])
    Max_To_Sinks[27,i]=max(OnSiteTreat_to_Subsurf_as_T[:,i])
    Max_To_Sinks[28,i]=max(STSoil_N[:,i])
    Max_To_Sinks[29,i]=max(STSoil_M[:,i])
    Max_To_Sinks[30,i]=max(STSoil_T[:,i])
    Max_To_Sinks[31,i]=max(OnSiteSludge_N[:,i])
    Max_To_Sinks[32,i]=max(OnSiteSludge_M[:,i])
    Max_To_Sinks[33,i]=max(OnSiteSludge_T[:,i])
    Max_To_Sinks[34,i]=max(PersCare_to_SurfWater_as_N[:,i])
    Max_To_Sinks[35,i]=max(NoSewer_to_SurfWater_as_N[:,i])
    Max_To_Sinks[36,i]=max(NoSewer_to_SurfWater_as_M[:,i])
    Max_To_Sinks[37,i]=max(NoSewer_to_SurfWater_as_T[:,i])
    Max_To_Sinks[38,i]=max(EndSewer_to_SurfWater_as_N[:,i])
    Max_To_Sinks[39,i]=max(EndSewer_to_SurfWater_as_M[:,i])
    Max_To_Sinks[40,i]=max(EndSewer_to_SurfWater_as_T[:,i])
    Max_To_Sinks[41,i]=max(Overflow_to_SurfWater_as_N[:,i])
    Max_To_Sinks[42,i]=max(Overflow_to_SurfWater_as_M[:,i])
    Max_To_Sinks[43,i]=max(Overflow_to_SurfWater_as_T[:,i])
    Max_To_Sinks[44,i]=max(STPEffluent_to_SurfWater_as_N[:,i])
    Max_To_Sinks[45,i]=max(STPEffluent_to_SurfWater_as_M[:,i])
    Max_To_Sinks[46,i]=max(STPEffluent_to_SurfWater_as_T[:,i])
    Max_To_Sinks[47,i]=max(ManufTextW_to_Landfill_as_P[:,i])
    Max_To_Sinks[48,i]=max(ManufPlasW_to_Landfill_as_P[:,i])
    Max_To_Sinks[49,i]=max(STPSlud_to_Landfill_as_N[:,i])
    Max_To_Sinks[50,i]=max(STPSlud_to_Landfill_as_M[:,i])
    Max_To_Sinks[51,i]=max(STPSlud_to_Landfill_as_T[:,i])
    Max_To_Sinks[52,i]=max(MMSW_to_Landfill_as_P[:,i])
    Max_To_Sinks[53,i]=max(CDW_to_Landfill_as_P[:,i])
    Max_To_Sinks[54,i]=max(SortCDWGlass_to_Landfill_as_P[:,i])
    Max_To_Sinks[55,i]=max(SortCDWMiner_to_Landfill_as_P[:,i])
    Max_To_Sinks[56,i]=max(SortDisp_to_Landfill_as_P[:,i])
    Max_To_Sinks[57,i]=max(GranuPlas_to_Landfill_as_P[:,i])
    Max_To_Sinks[58,i]=max(BaliText_to_Landfill_as_P[:,i])
    Max_To_Sinks[59,i]=max(Purislag_to_Landfill_as_P[:,i])
    Max_To_Sinks[60,i]=max(Purislag_to_Landfill_as_T[:,i])
    Max_To_Sinks[61,i]=max(SortMiner_to_Landfill_as_P[:,i])
    Max_To_Sinks[62,i]=max(Filterash_to_Landfill_as_N[:,i])
    Max_To_Sinks[63,i]=max(Filterash_to_Landfill_as_T[:,i])
    Max_To_Sinks[64,i]=max(Bottomash_to_Landfill_as_N[:,i])
    Max_To_Sinks[65,i]=max(Bottomash_to_Landfill_as_T[:,i])
    Max_To_Sinks[66,i]=max(ManufTextW_to_Reuse_as_P[:,i])
    Max_To_Sinks[67,i]=max(ManufPlasW_to_Reuse_as_P[:,i])
    Max_To_Sinks[68,i]=max(ManufSolidW_to_Reuse_as_P[:,i])
    Max_To_Sinks[69,i]=max(Filterash_to_Reuse_as_N[:,i])
    Max_To_Sinks[70,i]=max(Filterash_to_Reuse_as_T[:,i])
    Max_To_Sinks[71,i]=max(Bottomash_to_Reuse_as_N[:,i])
    Max_To_Sinks[72,i]=max(Bottomash_to_Reuse_as_T[:,i])
    Max_To_Sinks[73,i]=max(GranuPlas_to_Reuse_as_P[:,i])
    Max_To_Sinks[74,i]=max(BaliText_to_Reuse_as_P[:,i])
    Max_To_Sinks[75,i]=max(PuriMetal_to_Reuse_as_T[:,i])
    Max_To_Sinks[76,i]=max(PuriMetal_to_Reuse_as_P[:,i])
    Max_To_Sinks[77,i]=max(PuriSlag_to_Reuse_as_T[:,i])
    Max_To_Sinks[78,i]=max(PuriSlag_to_Reuse_as_P[:,i])
    Max_To_Sinks[79,i]=max(MeltGlass_to_Reuse_as_T[:,i])
    Max_To_Sinks[80,i]=max(SortMiner_to_Reuse_as_P[:,i])
    Max_To_Sinks[81,i]=max(SortWEEE_to_Export_as_P[:,i])
    Max_To_Sinks[82,i]=max(SortTextW_to_Export_as_P[:,i])


# In[27]:


Max_To_Sinks_DF = pd.DataFrame({'Pristine to Air from Production':Max_To_Sinks[0,:],
                               'Pristine to Air from Manufacturing':Max_To_Sinks[1,:],
                               'Pristine to Air from Paints':Max_To_Sinks[2,:],
                               'Matrix-embedded to Air from Paints':Max_To_Sinks[3,:],
                               'Pristine to Air from Glass':Max_To_Sinks[4,:],
                               'Matrix-embedded to Air from Glass':Max_To_Sinks[5,:],
                               'Pristine to Air from Ceramics':Max_To_Sinks[6,:],
                               'Matrix-embedded to Air from Ceramics':Max_To_Sinks[7,:],
                               'Pristine to Air from Rubber & Plastics':Max_To_Sinks[8,:],
                               'Matrix-embedded to Air from Rubber & Plastics':Max_To_Sinks[9,:],
                              'Pristine to Air from Textiles':Max_To_Sinks[10,:],
                              'Matrix-embedded to Air from Textiles':Max_To_Sinks[11,:],
                              'Pristine to Air from WIP':Max_To_Sinks[12,:],
                              'Transformed to Air from WIP':Max_To_Sinks[13,:],
                              'Pristine particles to Air from Reprocessing':Max_To_Sinks[14,:],
                              'Matrix-embedded particles to Air from Reprocessing':Max_To_Sinks[15,:],
                              'Pristine to NUSoil from Paints':Max_To_Sinks[16,:],
                              'Matrix-embedded to NUSoil from Paints':Max_To_Sinks[17,:],
                               'Pristine to NUSoil from Glass':Max_To_Sinks[18,:],
                              'Matrix-embedded to NUSoil from Glass':Max_To_Sinks[19,:],
                               'Pristine to NUSoil from Ceramics':Max_To_Sinks[20,:],
                              'Matrix-embedded to NUSoil from Ceramics':Max_To_Sinks[21,:],
                              'Pristine to Subsurface from Sewer':Max_To_Sinks[22,:],
                              'Matrix-embedded to Subsurface from Sewer':Max_To_Sinks[23,:],
                              'Transformed to Subsurface from Sewer':Max_To_Sinks[24,:],
                              'Pristine to Subsurface from OnSite treatment':Max_To_Sinks[25,:],
                              'Matrix-embedded to Subsurface from OnSite treatment':Max_To_Sinks[26,:],
                              'Transformed to Subsurface from OnSite treatment':Max_To_Sinks[27,:],
                              'Pristine to Sludge treated soil':Max_To_Sinks[28,:],
                               'Matrix-embedded to Sludge treated soil':Max_To_Sinks[29,:],
                              'Transformed to Sludge treated soil':Max_To_Sinks[30,:],
                              'Pristine to OnsiteSludge':Max_To_Sinks[31,:],
                               'Matrix-embedded to OnsiteSludge':Max_To_Sinks[32,:],
                              'Transformed to OnsiteSludge':Max_To_Sinks[33,:],
                              'Pristine to Surface water from PersCareLiquids':Max_To_Sinks[34,:],
                              'Pristine to Surface water from No sewer':Max_To_Sinks[35,:],
                              'Matrix-embedded to Surface water from No sewer':Max_To_Sinks[36,:],
                              'Transformed to Surface water from No sewer':Max_To_Sinks[37,:],
                              'Pristine to Surface water from Sewer':Max_To_Sinks[38,:],
                               'Matrix-embedded to Surface water from Sewer':Max_To_Sinks[39,:],
                              'Transformed to Surface water from Sewer':Max_To_Sinks[40,:],
                              'Pristine to STP overflow and Surface water':Max_To_Sinks[41,:],
                              'Matrix-embedded to STP overflow and Surface water':Max_To_Sinks[42,:],
                              'Transformed to STP overflow and Surface water':Max_To_Sinks[43,:],
                              'Pristine to STP effluent and Surface water':Max_To_Sinks[44,:],
                              'Matrix-embedded to STP effluent and Surface water':Max_To_Sinks[45,:],
                              'Transformed to STP effluent and Surface water':Max_To_Sinks[46,:],
                              'Product-embedded to Landfill from Textiles manufacturing waste':Max_To_Sinks[47,:],
                               'Product-embedded to Landfill from Plastic manufacturing waste':Max_To_Sinks[48,:],
                              'Pristine to Landfill from STP sludge':Max_To_Sinks[49,:],
                               'Matrix-embedded to Landfill from STP sludge':Max_To_Sinks[50,:],
                              'Transformed to Landfill from STP sludge':Max_To_Sinks[51,:],
                              'Product-embedded to Landfill from MMSW':Max_To_Sinks[52,:],
                              'Product-embedded to Landfill from CDW':Max_To_Sinks[53,:],
                              'Product-embedded to Landfill from Sorted CDW Glass':Max_To_Sinks[54,:],
                              'Product-embedded to Landfill from Sorted CDW Mineral':Max_To_Sinks[55,:],
                              'Product-embedded to Landfill from Other sorting':Max_To_Sinks[56,:],
                               'Product-embedded to Landfill from Plastic granulation':Max_To_Sinks[57,:],
                               'Product-embedded to Landfill from Textile baling':Max_To_Sinks[58,:],
                               'Product-embedded to Landfill from Purification slag':Max_To_Sinks[59,:],
                               'Transformed to Landfill from Purification slag':Max_To_Sinks[60,:],
                               'Product-embedded to Landfill from Sorted mineral':Max_To_Sinks[61,],
                               'Pristine to Landfill from Filter ash':Max_To_Sinks[62,:],
                              'Transformed to Landfill from Filter ash':Max_To_Sinks[63,:],
                              'Pristine to Landfill from Bottom ash':Max_To_Sinks[64,:],
                              'Transformed to Landfill from Bottom ash':Max_To_Sinks[65,:],
                              'Product-embedded to Reuse from Manufacturing textile waste':Max_To_Sinks[66,:],
                               'Product-embedded to Reuse from Manufacturing plastic waste':Max_To_Sinks[67,:],
                              'Product-embedded to Reuse from Manufacturing other solid waste':Max_To_Sinks[68,:],
                              'Pristine from Filter ash to Reuse':Max_To_Sinks[69,:],
                              'Transformed to Reuse from Filter ash':Max_To_Sinks[70,:],
                              'Pristine to Reuse from Bottom ash':Max_To_Sinks[71,:],
                              'Transformed to Reuse from Bottom ash':Max_To_Sinks[72,:],
                              'Product-embedded to Reuse from Plastic granulation':Max_To_Sinks[73,:],
                              'Product-embedded to Reuse from Baling textiles':Max_To_Sinks[74,:],
                              'Transformed to Reuse from Metal purification':Max_To_Sinks[75,:],
                               'Product-embedded to Reuse from Metal purification':Max_To_Sinks[76,:],
                              'Transformed to Reuse from Slag purification':Max_To_Sinks[77,:],
                               'Product-embedded to Reuse from Slag purification':Max_To_Sinks[78,:],
                              'Transformed to Reuse from Melting glass':Max_To_Sinks[79,:],
                              'Product-embedded to Reuse from Sorting minerals':Max_To_Sinks[80,:],
                              'Product-embedded to Export from Sorting WEEE':Max_To_Sinks[81,:],
                              'Product-embedded to Export from Sorting textile waste':Max_To_Sinks[82,:],})


Max_To_Sinks_DF_Transp = pd.DataFrame.transpose(Max_To_Sinks_DF)
Max_To_Sinks_DF_Transp.to_csv('Max to Sinks - TiO2 - AUT.csv', index=True, sep=',')


# In[28]:


# Extract medians to sinks for each year

Medians_To_Sinks = np.zeros(shape=(83,Tperiods))

for i in np.arange(0,Tperiods):
    Medians_To_Sinks[0,i]=np.percentile(Prod_to_Air_as_N[:,i], 50)
    Medians_To_Sinks[1,i]=np.percentile(Manuf_to_Air_as_N[:,i], 50)
    Medians_To_Sinks[2,i]=np.percentile(Paints_to_Air_as_N[:,i], 50)
    Medians_To_Sinks[3,i]=np.percentile(Paints_to_Air_as_M[:,i], 50)
    Medians_To_Sinks[4,i]=np.percentile(Glass_to_Air_as_N[:,i], 50)
    Medians_To_Sinks[5,i]=np.percentile(Glass_to_Air_as_M[:,i], 50)
    Medians_To_Sinks[6,i]=np.percentile(Ceram_to_Air_as_N[:,i], 50)
    Medians_To_Sinks[7,i]=np.percentile(Ceram_to_Air_as_M[:,i], 50)
    Medians_To_Sinks[8,i]=np.percentile(RubPlas_to_Air_as_N[:,i], 50)
    Medians_To_Sinks[9,i]=np.percentile(RubPlas_to_Air_as_M[:,i], 50)
    Medians_To_Sinks[10,i]=np.percentile(Textiles_to_Air_as_N[:,i], 50)
    Medians_To_Sinks[11,i]=np.percentile(Textiles_to_Air_as_M[:,i], 50)
    Medians_To_Sinks[12,i]=np.percentile(WIP_to_Air_as_N[:,i], 50)
    Medians_To_Sinks[13,i]=np.percentile(WIP_to_Air_as_T[:,i], 50)
    Medians_To_Sinks[14,i]=np.percentile(Repr_to_Air_as_N[:,i], 50)
    Medians_To_Sinks[15,i]=np.percentile(Repr_to_Air_as_M[:,i], 50)
    Medians_To_Sinks[16,i]=np.percentile(Paints_to_NUSoil_as_N[:,i], 50)
    Medians_To_Sinks[17,i]=np.percentile(Paints_to_NUSoil_as_M[:,i], 50)
    Medians_To_Sinks[18,i]=np.percentile(Glass_to_NUSoil_as_N[:,i], 50)
    Medians_To_Sinks[19,i]=np.percentile(Glass_to_NUSoil_as_M[:,i], 50)
    Medians_To_Sinks[20,i]=np.percentile(Ceram_to_NUSoil_as_N[:,i], 50)
    Medians_To_Sinks[21,i]=np.percentile(Ceram_to_NUSoil_as_M[:,i], 50)
    Medians_To_Sinks[22,i]=np.percentile(Sewer_to_Subsurf_as_N[:,i], 50)
    Medians_To_Sinks[23,i]=np.percentile(Sewer_to_Subsurf_as_M[:,i], 50)
    Medians_To_Sinks[24,i]=np.percentile(Sewer_to_Subsurf_as_T[:,i], 50)
    Medians_To_Sinks[25,i]=np.percentile(OnSiteTreat_to_Subsurf_as_N[:,i], 50)
    Medians_To_Sinks[26,i]=np.percentile(OnSiteTreat_to_Subsurf_as_M[:,i], 50)
    Medians_To_Sinks[27,i]=np.percentile(OnSiteTreat_to_Subsurf_as_T[:,i], 50)
    Medians_To_Sinks[28,i]=np.percentile(STSoil_N[:,i], 50)
    Medians_To_Sinks[29,i]=np.percentile(STSoil_M[:,i], 50)
    Medians_To_Sinks[30,i]=np.percentile(STSoil_T[:,i], 50)
    Medians_To_Sinks[31,i]=np.percentile(OnSiteSludge_N[:,i], 50)
    Medians_To_Sinks[32,i]=np.percentile(OnSiteSludge_M[:,i], 50)
    Medians_To_Sinks[33,i]=np.percentile(OnSiteSludge_T[:,i], 50)
    Medians_To_Sinks[34,i]=np.percentile(PersCare_to_SurfWater_as_N[:,i], 50)
    Medians_To_Sinks[35,i]=np.percentile(NoSewer_to_SurfWater_as_N[:,i], 50)
    Medians_To_Sinks[36,i]=np.percentile(NoSewer_to_SurfWater_as_M[:,i], 50)
    Medians_To_Sinks[37,i]=np.percentile(NoSewer_to_SurfWater_as_T[:,i], 50)
    Medians_To_Sinks[38,i]=np.percentile(EndSewer_to_SurfWater_as_N[:,i], 50)
    Medians_To_Sinks[39,i]=np.percentile(EndSewer_to_SurfWater_as_M[:,i], 50)
    Medians_To_Sinks[40,i]=np.percentile(EndSewer_to_SurfWater_as_T[:,i], 50)
    Medians_To_Sinks[41,i]=np.percentile(Overflow_to_SurfWater_as_N[:,i], 50)
    Medians_To_Sinks[42,i]=np.percentile(Overflow_to_SurfWater_as_M[:,i], 50)
    Medians_To_Sinks[43,i]=np.percentile(Overflow_to_SurfWater_as_T[:,i], 50)
    Medians_To_Sinks[44,i]=np.percentile(STPEffluent_to_SurfWater_as_N[:,i], 50)
    Medians_To_Sinks[45,i]=np.percentile(STPEffluent_to_SurfWater_as_M[:,i], 50)
    Medians_To_Sinks[46,i]=np.percentile(STPEffluent_to_SurfWater_as_T[:,i], 50)
    Medians_To_Sinks[47,i]=np.percentile(ManufTextW_to_Landfill_as_P[:,i], 50)
    Medians_To_Sinks[48,i]=np.percentile(ManufPlasW_to_Landfill_as_P[:,i], 50)
    Medians_To_Sinks[49,i]=np.percentile(STPSlud_to_Landfill_as_N[:,i], 50)
    Medians_To_Sinks[50,i]=np.percentile(STPSlud_to_Landfill_as_M[:,i], 50)
    Medians_To_Sinks[51,i]=np.percentile(STPSlud_to_Landfill_as_T[:,i], 50)
    Medians_To_Sinks[52,i]=np.percentile(MMSW_to_Landfill_as_P[:,i], 50)
    Medians_To_Sinks[53,i]=np.percentile(CDW_to_Landfill_as_P[:,i], 50)
    Medians_To_Sinks[54,i]=np.percentile(SortCDWGlass_to_Landfill_as_P[:,i], 50)
    Medians_To_Sinks[55,i]=np.percentile(SortCDWMiner_to_Landfill_as_P[:,i], 50)
    Medians_To_Sinks[56,i]=np.percentile(SortDisp_to_Landfill_as_P[:,i], 50)
    Medians_To_Sinks[57,i]=np.percentile(GranuPlas_to_Landfill_as_P[:,i], 50)
    Medians_To_Sinks[58,i]=np.percentile(BaliText_to_Landfill_as_P[:,i], 50)
    Medians_To_Sinks[59,i]=np.percentile(Purislag_to_Landfill_as_P[:,i], 50)
    Medians_To_Sinks[60,i]=np.percentile(Purislag_to_Landfill_as_T[:,i], 50)
    Medians_To_Sinks[61,i]=np.percentile(SortMiner_to_Landfill_as_P[:,i], 50)
    Medians_To_Sinks[62,i]=np.percentile(Filterash_to_Landfill_as_N[:,i], 50)
    Medians_To_Sinks[63,i]=np.percentile(Filterash_to_Landfill_as_T[:,i], 50)
    Medians_To_Sinks[64,i]=np.percentile(Bottomash_to_Landfill_as_N[:,i], 50)
    Medians_To_Sinks[65,i]=np.percentile(Bottomash_to_Landfill_as_T[:,i], 50)
    Medians_To_Sinks[66,i]=np.percentile(ManufTextW_to_Reuse_as_P[:,i], 50)
    Medians_To_Sinks[67,i]=np.percentile(ManufPlasW_to_Reuse_as_P[:,i], 50)
    Medians_To_Sinks[68,i]=np.percentile(ManufSolidW_to_Reuse_as_P[:,i], 50)
    Medians_To_Sinks[69,i]=np.percentile(Filterash_to_Reuse_as_N[:,i], 50)
    Medians_To_Sinks[70,i]=np.percentile(Filterash_to_Reuse_as_T[:,i], 50)
    Medians_To_Sinks[71,i]=np.percentile(Bottomash_to_Reuse_as_N[:,i], 50)
    Medians_To_Sinks[72,i]=np.percentile(Bottomash_to_Reuse_as_T[:,i], 50)
    Medians_To_Sinks[73,i]=np.percentile(GranuPlas_to_Reuse_as_P[:,i], 50)
    Medians_To_Sinks[74,i]=np.percentile(BaliText_to_Reuse_as_P[:,i], 50)
    Medians_To_Sinks[75,i]=np.percentile(PuriMetal_to_Reuse_as_T[:,i], 50)
    Medians_To_Sinks[76,i]=np.percentile(PuriMetal_to_Reuse_as_P[:,i], 50)
    Medians_To_Sinks[77,i]=np.percentile(PuriSlag_to_Reuse_as_T[:,i], 50)
    Medians_To_Sinks[78,i]=np.percentile(PuriSlag_to_Reuse_as_P[:,i], 50)
    Medians_To_Sinks[79,i]=np.percentile(MeltGlass_to_Reuse_as_T[:,i], 50)
    Medians_To_Sinks[80,i]=np.percentile(SortMiner_to_Reuse_as_P[:,i], 50)
    Medians_To_Sinks[81,i]=np.percentile(SortWEEE_to_Export_as_P[:,i], 50)
    Medians_To_Sinks[82,i]=np.percentile(SortTextW_to_Export_as_P[:,i], 50)


# In[29]:


Medians_To_Sinks_DF = pd.DataFrame({'Pristine to Air from Production':Medians_To_Sinks[0,:],
                               'Pristine to Air from Manufacturing':Medians_To_Sinks[1,:],
                               'Pristine to Air from Paints':Medians_To_Sinks[2,:],
                               'Matrix-embedded to Air from Paints':Medians_To_Sinks[3,:],
                               'Pristine to Air from Glass':Medians_To_Sinks[4,:],
                               'Matrix-embedded to Air from Glass':Medians_To_Sinks[5,:],
                               'Pristine to Air from Ceramics':Medians_To_Sinks[6,:],
                               'Matrix-embedded to Air from Ceramics':Medians_To_Sinks[7,:],
                               'Pristine to Air from Rubber & Plastics':Medians_To_Sinks[8,:],
                               'Matrix-embedded to Air from Rubber & Plastics':Medians_To_Sinks[9,:],
                              'Pristine to Air from Textiles':Medians_To_Sinks[10,:],
                              'Matrix-embedded to Air from Textiles':Medians_To_Sinks[11,:],
                              'Pristine to Air from WIP':Medians_To_Sinks[12,:],
                              'Transformed to Air from WIP':Medians_To_Sinks[13,:],
                              'Pristine particles to Air from Reprocessing':Medians_To_Sinks[14,:],
                              'Matrix-embedded particles to Air from Reprocessing':Medians_To_Sinks[15,:],
                              'Pristine to NUSoil from Paints':Medians_To_Sinks[16,:],
                              'Matrix-embedded to NUSoil from Paints':Medians_To_Sinks[17,:],
                               'Pristine to NUSoil from Glass':Medians_To_Sinks[18,:],
                              'Matrix-embedded to NUSoil from Glass':Medians_To_Sinks[19,:],
                               'Pristine to NUSoil from Ceramics':Medians_To_Sinks[20,:],
                              'Matrix-embedded to NUSoil from Ceramics':Medians_To_Sinks[21,:],
                              'Pristine to Subsurface from Sewer':Medians_To_Sinks[22,:],
                              'Matrix-embedded to Subsurface from Sewer':Medians_To_Sinks[23,:],
                              'Transformed to Subsurface from Sewer':Medians_To_Sinks[24,:],
                              'Pristine to Subsurface from OnSite treatment':Medians_To_Sinks[25,:],
                              'Matrix-embedded to Subsurface from OnSite treatment':Medians_To_Sinks[26,:],
                              'Transformed to Subsurface from OnSite treatment':Medians_To_Sinks[27,:],
                              'Pristine to Sludge treated soil':Medians_To_Sinks[28,:],
                               'Matrix-embedded to Sludge treated soil':Medians_To_Sinks[29,:],
                              'Transformed to Sludge treated soil':Medians_To_Sinks[30,:],
                              'Pristine to OnsiteSludge':Medians_To_Sinks[31,:],
                               'Matrix-embedded to OnsiteSludge':Medians_To_Sinks[32,:],
                              'Transformed to OnsiteSludge':Medians_To_Sinks[33,:],
                              'Pristine to Surface water from PersCareLiquids':Medians_To_Sinks[34,:],
                              'Pristine to Surface water from No sewer':Medians_To_Sinks[35,:],
                              'Matrix-embedded to Surface water from No sewer':Medians_To_Sinks[36,:],
                              'Transformed to Surface water from No sewer':Medians_To_Sinks[37,:],
                              'Pristine to Surface water from Sewer':Medians_To_Sinks[38,:],
                               'Matrix-embedded to Surface water from Sewer':Medians_To_Sinks[39,:],
                              'Transformed to Surface water from Sewer':Medians_To_Sinks[40,:],
                              'Pristine to STP overflow and Surface water':Medians_To_Sinks[41,:],
                              'Matrix-embedded to STP overflow and Surface water':Medians_To_Sinks[42,:],
                              'Transformed to STP overflow and Surface water':Medians_To_Sinks[43,:],
                              'Pristine to STP effluent and Surface water':Medians_To_Sinks[44,:],
                              'Matrix-embedded to STP effluent and Surface water':Medians_To_Sinks[45,:],
                              'Transformed to STP effluent and Surface water':Medians_To_Sinks[46,:],
                              'Product-embedded to Landfill from Textiles manufacturing waste':Medians_To_Sinks[47,:],
                               'Product-embedded to Landfill from Plastic manufacturing waste':Medians_To_Sinks[48,:],
                              'Pristine to Landfill from STP sludge':Medians_To_Sinks[49,:],
                               'Matrix-embedded to Landfill from STP sludge':Medians_To_Sinks[50,:],
                              'Transformed to Landfill from STP sludge':Medians_To_Sinks[51,:],
                              'Product-embedded to Landfill from MMSW':Medians_To_Sinks[52,:],
                              'Product-embedded to Landfill from CDW':Medians_To_Sinks[53,:],
                              'Product-embedded to Landfill from Sorted CDW Glass':Medians_To_Sinks[54,:],
                              'Product-embedded to Landfill from Sorted CDW Mineral':Medians_To_Sinks[55,:],
                              'Product-embedded to Landfill from Other sorting':Medians_To_Sinks[56,:],
                               'Product-embedded to Landfill from Plastic granulation':Medians_To_Sinks[57,:],
                               'Product-embedded to Landfill from Textile baling':Medians_To_Sinks[58,:],
                               'Product-embedded to Landfill from Purification slag':Medians_To_Sinks[59,:],
                               'Transformed to Landfill from Purification slag':Medians_To_Sinks[60,:],
                               'Product-embedded to Landfill from Sorted mineral':Medians_To_Sinks[61,],
                               'Pristine to Landfill from Filter ash':Medians_To_Sinks[62,:],
                              'Transformed to Landfill from Filter ash':Medians_To_Sinks[63,:],
                              'Pristine to Landfill from Bottom ash':Medians_To_Sinks[64,:],
                              'Transformed to Landfill from Bottom ash':Medians_To_Sinks[65,:],
                              'Product-embedded to Reuse from Manufacturing textile waste':Medians_To_Sinks[66,:],
                               'Product-embedded to Reuse from Manufacturing plastic waste':Medians_To_Sinks[67,:],
                              'Product-embedded to Reuse from Manufacturing other solid waste':Medians_To_Sinks[68,:],
                              'Pristine from Filter ash to Reuse':Medians_To_Sinks[69,:],
                              'Transformed to Reuse from Filter ash':Medians_To_Sinks[70,:],
                              'Pristine to Reuse from Bottom ash':Medians_To_Sinks[71,:],
                              'Transformed to Reuse from Bottom ash':Medians_To_Sinks[72,:],
                              'Product-embedded to Reuse from Plastic granulation':Medians_To_Sinks[73,:],
                              'Product-embedded to Reuse from Baling textiles':Medians_To_Sinks[74,:],
                              'Transformed to Reuse from Metal purification':Medians_To_Sinks[75,:],
                               'Product-embedded to Reuse from Metal purification':Medians_To_Sinks[76,:],
                              'Transformed to Reuse from Slag purification':Medians_To_Sinks[77,:],
                               'Product-embedded to Reuse from Slag purification':Medians_To_Sinks[78,:],
                              'Transformed to Reuse from Melting glass':Medians_To_Sinks[79,:],
                              'Product-embedded to Reuse from Sorting minerals':Medians_To_Sinks[80,:],
                              'Product-embedded to Export from Sorting WEEE':Medians_To_Sinks[81,:],
                              'Product-embedded to Export from Sorting textile waste':Medians_To_Sinks[82,:],})


Medians_To_Sinks_DF_Transp = pd.DataFrame.transpose(Medians_To_Sinks_DF)
Medians_To_Sinks_DF_Transp.to_csv('Medians to Sinks - TiO2 - AUT_2.csv',index=True, sep=',')


# In[30]:


# Extract Q5 to sinks for each year

Q5_To_Sinks = np.zeros(shape=(83,Tperiods))

for i in np.arange(0,Tperiods):
    Q5_To_Sinks[0,i]=np.percentile(Prod_to_Air_as_N[:,i], 5)
    Q5_To_Sinks[1,i]=np.percentile(Manuf_to_Air_as_N[:,i], 5)
    Q5_To_Sinks[2,i]=np.percentile(Paints_to_Air_as_N[:,i], 5)
    Q5_To_Sinks[3,i]=np.percentile(Paints_to_Air_as_M[:,i], 5)
    Q5_To_Sinks[4,i]=np.percentile(Glass_to_Air_as_N[:,i], 5)
    Q5_To_Sinks[5,i]=np.percentile(Glass_to_Air_as_M[:,i], 5)
    Q5_To_Sinks[6,i]=np.percentile(Ceram_to_Air_as_N[:,i], 5)
    Q5_To_Sinks[7,i]=np.percentile(Ceram_to_Air_as_M[:,i], 5)
    Q5_To_Sinks[8,i]=np.percentile(RubPlas_to_Air_as_N[:,i], 5)
    Q5_To_Sinks[9,i]=np.percentile(RubPlas_to_Air_as_M[:,i], 5)
    Q5_To_Sinks[10,i]=np.percentile(Textiles_to_Air_as_N[:,i], 5)
    Q5_To_Sinks[11,i]=np.percentile(Textiles_to_Air_as_M[:,i], 5)
    Q5_To_Sinks[12,i]=np.percentile(WIP_to_Air_as_N[:,i], 5)
    Q5_To_Sinks[13,i]=np.percentile(WIP_to_Air_as_T[:,i], 5)
    Q5_To_Sinks[14,i]=np.percentile(Repr_to_Air_as_N[:,i], 5)
    Q5_To_Sinks[15,i]=np.percentile(Repr_to_Air_as_M[:,i], 5)
    Q5_To_Sinks[16,i]=np.percentile(Paints_to_NUSoil_as_N[:,i], 5)
    Q5_To_Sinks[17,i]=np.percentile(Paints_to_NUSoil_as_M[:,i], 5)
    Q5_To_Sinks[18,i]=np.percentile(Glass_to_NUSoil_as_N[:,i], 5)
    Q5_To_Sinks[19,i]=np.percentile(Glass_to_NUSoil_as_M[:,i], 5)
    Q5_To_Sinks[20,i]=np.percentile(Ceram_to_NUSoil_as_N[:,i], 5)
    Q5_To_Sinks[21,i]=np.percentile(Ceram_to_NUSoil_as_M[:,i], 5)
    Q5_To_Sinks[22,i]=np.percentile(Sewer_to_Subsurf_as_N[:,i], 5)
    Q5_To_Sinks[23,i]=np.percentile(Sewer_to_Subsurf_as_M[:,i], 5)
    Q5_To_Sinks[24,i]=np.percentile(Sewer_to_Subsurf_as_T[:,i], 5)
    Q5_To_Sinks[25,i]=np.percentile(OnSiteTreat_to_Subsurf_as_N[:,i], 5)
    Q5_To_Sinks[26,i]=np.percentile(OnSiteTreat_to_Subsurf_as_M[:,i], 5)
    Q5_To_Sinks[27,i]=np.percentile(OnSiteTreat_to_Subsurf_as_T[:,i], 5)
    Q5_To_Sinks[28,i]=np.percentile(STSoil_N[:,i], 5)
    Q5_To_Sinks[29,i]=np.percentile(STSoil_M[:,i], 5)
    Q5_To_Sinks[30,i]=np.percentile(STSoil_T[:,i], 5)
    Q5_To_Sinks[31,i]=np.percentile(OnSiteSludge_N[:,i], 5)
    Q5_To_Sinks[32,i]=np.percentile(OnSiteSludge_M[:,i], 5)
    Q5_To_Sinks[33,i]=np.percentile(OnSiteSludge_T[:,i], 5)
    Q5_To_Sinks[34,i]=np.percentile(PersCare_to_SurfWater_as_N[:,i], 5)
    Q5_To_Sinks[35,i]=np.percentile(NoSewer_to_SurfWater_as_N[:,i], 5)
    Q5_To_Sinks[36,i]=np.percentile(NoSewer_to_SurfWater_as_M[:,i], 5)
    Q5_To_Sinks[37,i]=np.percentile(NoSewer_to_SurfWater_as_T[:,i], 5)
    Q5_To_Sinks[38,i]=np.percentile(EndSewer_to_SurfWater_as_N[:,i], 5)
    Q5_To_Sinks[39,i]=np.percentile(EndSewer_to_SurfWater_as_M[:,i], 5)
    Q5_To_Sinks[40,i]=np.percentile(EndSewer_to_SurfWater_as_T[:,i], 5)
    Q5_To_Sinks[41,i]=np.percentile(Overflow_to_SurfWater_as_N[:,i], 5)
    Q5_To_Sinks[42,i]=np.percentile(Overflow_to_SurfWater_as_M[:,i], 5)
    Q5_To_Sinks[43,i]=np.percentile(Overflow_to_SurfWater_as_T[:,i], 5)
    Q5_To_Sinks[44,i]=np.percentile(STPEffluent_to_SurfWater_as_N[:,i], 5)
    Q5_To_Sinks[45,i]=np.percentile(STPEffluent_to_SurfWater_as_M[:,i], 5)
    Q5_To_Sinks[46,i]=np.percentile(STPEffluent_to_SurfWater_as_T[:,i], 5)
    Q5_To_Sinks[47,i]=np.percentile(ManufTextW_to_Landfill_as_P[:,i], 5)
    Q5_To_Sinks[48,i]=np.percentile(ManufPlasW_to_Landfill_as_P[:,i], 5)
    Q5_To_Sinks[49,i]=np.percentile(STPSlud_to_Landfill_as_N[:,i], 5)
    Q5_To_Sinks[50,i]=np.percentile(STPSlud_to_Landfill_as_M[:,i], 5)
    Q5_To_Sinks[51,i]=np.percentile(STPSlud_to_Landfill_as_T[:,i], 5)
    Q5_To_Sinks[52,i]=np.percentile(MMSW_to_Landfill_as_P[:,i], 5)
    Q5_To_Sinks[53,i]=np.percentile(CDW_to_Landfill_as_P[:,i], 5)
    Q5_To_Sinks[54,i]=np.percentile(SortCDWGlass_to_Landfill_as_P[:,i], 5)
    Q5_To_Sinks[55,i]=np.percentile(SortCDWMiner_to_Landfill_as_P[:,i], 5)
    Q5_To_Sinks[56,i]=np.percentile(SortDisp_to_Landfill_as_P[:,i], 5)
    Q5_To_Sinks[57,i]=np.percentile(GranuPlas_to_Landfill_as_P[:,i], 5)
    Q5_To_Sinks[58,i]=np.percentile(BaliText_to_Landfill_as_P[:,i], 5)
    Q5_To_Sinks[59,i]=np.percentile(Purislag_to_Landfill_as_P[:,i], 5)
    Q5_To_Sinks[60,i]=np.percentile(Purislag_to_Landfill_as_T[:,i], 5)
    Q5_To_Sinks[61,i]=np.percentile(SortMiner_to_Landfill_as_P[:,i], 5)
    Q5_To_Sinks[62,i]=np.percentile(Filterash_to_Landfill_as_N[:,i], 5)
    Q5_To_Sinks[63,i]=np.percentile(Filterash_to_Landfill_as_T[:,i], 5)
    Q5_To_Sinks[64,i]=np.percentile(Bottomash_to_Landfill_as_N[:,i], 5)
    Q5_To_Sinks[65,i]=np.percentile(Bottomash_to_Landfill_as_T[:,i], 5)
    Q5_To_Sinks[66,i]=np.percentile(ManufTextW_to_Reuse_as_P[:,i], 5)
    Q5_To_Sinks[67,i]=np.percentile(ManufPlasW_to_Reuse_as_P[:,i], 5)
    Q5_To_Sinks[68,i]=np.percentile(ManufSolidW_to_Reuse_as_P[:,i], 5)
    Q5_To_Sinks[69,i]=np.percentile(Filterash_to_Reuse_as_N[:,i], 5)
    Q5_To_Sinks[70,i]=np.percentile(Filterash_to_Reuse_as_T[:,i], 5)
    Q5_To_Sinks[71,i]=np.percentile(Bottomash_to_Reuse_as_N[:,i], 5)
    Q5_To_Sinks[72,i]=np.percentile(Bottomash_to_Reuse_as_T[:,i], 5)
    Q5_To_Sinks[73,i]=np.percentile(GranuPlas_to_Reuse_as_P[:,i], 5)
    Q5_To_Sinks[74,i]=np.percentile(BaliText_to_Reuse_as_P[:,i], 5)
    Q5_To_Sinks[75,i]=np.percentile(PuriMetal_to_Reuse_as_T[:,i], 5)
    Q5_To_Sinks[76,i]=np.percentile(PuriMetal_to_Reuse_as_P[:,i], 5)
    Q5_To_Sinks[77,i]=np.percentile(PuriSlag_to_Reuse_as_T[:,i], 5)
    Q5_To_Sinks[78,i]=np.percentile(PuriSlag_to_Reuse_as_P[:,i], 5)
    Q5_To_Sinks[79,i]=np.percentile(MeltGlass_to_Reuse_as_T[:,i], 5)
    Q5_To_Sinks[80,i]=np.percentile(SortMiner_to_Reuse_as_P[:,i], 5)
    Q5_To_Sinks[81,i]=np.percentile(SortWEEE_to_Export_as_P[:,i], 5)
    Q5_To_Sinks[82,i]=np.percentile(SortTextW_to_Export_as_P[:,i], 5)


# In[31]:


Q5_To_Sinks_DF = pd.DataFrame({'Pristine to Air from Production':Q5_To_Sinks[0,:],
                               'Pristine to Air from Manufacturing':Q5_To_Sinks[1,:],
                               'Pristine to Air from Paints':Q5_To_Sinks[2,:],
                               'Matrix-embedded to Air from Paints':Q5_To_Sinks[3,:],
                               'Pristine to Air from Glass':Q5_To_Sinks[4,:],
                               'Matrix-embedded to Air from Glass':Q5_To_Sinks[5,:],
                               'Pristine to Air from Ceramics':Q5_To_Sinks[6,:],
                               'Matrix-embedded to Air from Ceramics':Q5_To_Sinks[7,:],
                               'Pristine to Air from Rubber & Plastics':Q5_To_Sinks[8,:],
                               'Matrix-embedded to Air from Rubber & Plastics':Q5_To_Sinks[9,:],
                              'Pristine to Air from Textiles':Q5_To_Sinks[10,:],
                              'Matrix-embedded to Air from Textiles':Q5_To_Sinks[11,:],
                              'Pristine to Air from WIP':Q5_To_Sinks[12,:],
                              'Transformed to Air from WIP':Q5_To_Sinks[13,:],
                              'Pristine particles to Air from Reprocessing':Q5_To_Sinks[14,:],
                              'Matrix-embedded particles to Air from Reprocessing':Q5_To_Sinks[15,:],
                              'Pristine to NUSoil from Paints':Q5_To_Sinks[16,:],
                              'Matrix-embedded to NUSoil from Paints':Q5_To_Sinks[17,:],
                               'Pristine to NUSoil from Glass':Q5_To_Sinks[18,:],
                              'Matrix-embedded to NUSoil from Glass':Q5_To_Sinks[19,:],
                               'Pristine to NUSoil from Ceramics':Q5_To_Sinks[20,:],
                              'Matrix-embedded to NUSoil from Ceramics':Q5_To_Sinks[21,:],
                              'Pristine to Subsurface from Sewer':Q5_To_Sinks[22,:],
                              'Matrix-embedded to Subsurface from Sewer':Q5_To_Sinks[23,:],
                              'Transformed to Subsurface from Sewer':Q5_To_Sinks[24,:],
                              'Pristine to Subsurface from OnSite treatment':Q5_To_Sinks[25,:],
                              'Matrix-embedded to Subsurface from OnSite treatment':Q5_To_Sinks[26,:],
                              'Transformed to Subsurface from OnSite treatment':Q5_To_Sinks[27,:],
                              'Pristine to Sludge treated soil':Q5_To_Sinks[28,:],
                               'Matrix-embedded to Sludge treated soil':Q5_To_Sinks[29,:],
                              'Transformed to Sludge treated soil':Q5_To_Sinks[30,:],
                              'Pristine to OnsiteSludge':Q5_To_Sinks[31,:],
                               'Matrix-embedded to OnsiteSludge':Q5_To_Sinks[32,:],
                              'Transformed to OnsiteSludge':Q5_To_Sinks[33,:],
                              'Pristine to Surface water from PersCareLiquids':Q5_To_Sinks[34,:],
                              'Pristine to Surface water from No sewer':Q5_To_Sinks[35,:],
                              'Matrix-embedded to Surface water from No sewer':Q5_To_Sinks[36,:],
                              'Transformed to Surface water from No sewer':Q5_To_Sinks[37,:],
                              'Pristine to Surface water from Sewer':Q5_To_Sinks[38,:],
                               'Matrix-embedded to Surface water from Sewer':Q5_To_Sinks[39,:],
                              'Transformed to Surface water from Sewer':Q5_To_Sinks[40,:],
                              'Pristine to STP overflow and Surface water':Q5_To_Sinks[41,:],
                              'Matrix-embedded to STP overflow and Surface water':Q5_To_Sinks[42,:],
                              'Transformed to STP overflow and Surface water':Q5_To_Sinks[43,:],
                              'Pristine to STP effluent and Surface water':Q5_To_Sinks[44,:],
                              'Matrix-embedded to STP effluent and Surface water':Q5_To_Sinks[45,:],
                              'Transformed to STP effluent and Surface water':Q5_To_Sinks[46,:],
                              'Product-embedded to Landfill from Textiles manufacturing waste':Q5_To_Sinks[47,:],
                               'Product-embedded to Landfill from Plastic manufacturing waste':Q5_To_Sinks[48,:],
                              'Pristine to Landfill from STP sludge':Q5_To_Sinks[49,:],
                               'Matrix-embedded to Landfill from STP sludge':Q5_To_Sinks[50,:],
                              'Transformed to Landfill from STP sludge':Q5_To_Sinks[51,:],
                              'Product-embedded to Landfill from MMSW':Q5_To_Sinks[52,:],
                              'Product-embedded to Landfill from CDW':Q5_To_Sinks[53,:],
                              'Product-embedded to Landfill from Sorted CDW Glass':Q5_To_Sinks[54,:],
                              'Product-embedded to Landfill from Sorted CDW Mineral':Q5_To_Sinks[55,:],
                              'Product-embedded to Landfill from Other sorting':Q5_To_Sinks[56,:],
                               'Product-embedded to Landfill from Plastic granulation':Q5_To_Sinks[57,:],
                               'Product-embedded to Landfill from Textile baling':Q5_To_Sinks[58,:],
                               'Product-embedded to Landfill from Purification slag':Q5_To_Sinks[59,:],
                               'Transformed to Landfill from Purification slag':Q5_To_Sinks[60,:],
                               'Product-embedded to Landfill from Sorted mineral':Q5_To_Sinks[61,],
                               'Pristine to Landfill from Filter ash':Q5_To_Sinks[62,:],
                              'Transformed to Landfill from Filter ash':Q5_To_Sinks[63,:],
                              'Pristine to Landfill from Bottom ash':Q5_To_Sinks[64,:],
                              'Transformed to Landfill from Bottom ash':Q5_To_Sinks[65,:],
                              'Product-embedded to Reuse from Manufacturing textile waste':Q5_To_Sinks[66,:],
                               'Product-embedded to Reuse from Manufacturing plastic waste':Q5_To_Sinks[67,:],
                              'Product-embedded to Reuse from Manufacturing other solid waste':Q5_To_Sinks[68,:],
                              'Pristine from Filter ash to Reuse':Q5_To_Sinks[69,:],
                              'Transformed to Reuse from Filter ash':Q5_To_Sinks[70,:],
                              'Pristine to Reuse from Bottom ash':Q5_To_Sinks[71,:],
                              'Transformed to Reuse from Bottom ash':Q5_To_Sinks[72,:],
                              'Product-embedded to Reuse from Plastic granulation':Q5_To_Sinks[73,:],
                              'Product-embedded to Reuse from Baling textiles':Q5_To_Sinks[74,:],
                              'Transformed to Reuse from Metal purification':Q5_To_Sinks[75,:],
                               'Product-embedded to Reuse from Metal purification':Q5_To_Sinks[76,:],
                              'Transformed to Reuse from Slag purification':Q5_To_Sinks[77,:],
                               'Product-embedded to Reuse from Slag purification':Q5_To_Sinks[78,:],
                              'Transformed to Reuse from Melting glass':Q5_To_Sinks[79,:],
                              'Product-embedded to Reuse from Sorting minerals':Q5_To_Sinks[80,:],
                              'Product-embedded to Export from Sorting WEEE':Q5_To_Sinks[81,:],
                              'Product-embedded to Export from Sorting textile waste':Q5_To_Sinks[82,:],})


Q5_To_Sinks_DF_Transp = pd.DataFrame.transpose(Q5_To_Sinks_DF)
Q5_To_Sinks_DF_Transp.to_csv('Q5 to Sinks - TiO2 - AUT_2.csv',index=True, sep=',')


# In[32]:


# Extract Q25 to sinks for each year

Q25_To_Sinks = np.zeros(shape=(83,Tperiods))

for i in np.arange(0,Tperiods):
    Q25_To_Sinks[0,i]=np.percentile(Prod_to_Air_as_N[:,i], 25)
    Q25_To_Sinks[1,i]=np.percentile(Manuf_to_Air_as_N[:,i], 25)
    Q25_To_Sinks[2,i]=np.percentile(Paints_to_Air_as_N[:,i], 25)
    Q25_To_Sinks[3,i]=np.percentile(Paints_to_Air_as_M[:,i], 25)
    Q25_To_Sinks[4,i]=np.percentile(Glass_to_Air_as_N[:,i], 25)
    Q25_To_Sinks[5,i]=np.percentile(Glass_to_Air_as_M[:,i], 25)
    Q25_To_Sinks[6,i]=np.percentile(Ceram_to_Air_as_N[:,i], 25)
    Q25_To_Sinks[7,i]=np.percentile(Ceram_to_Air_as_M[:,i], 25)
    Q25_To_Sinks[8,i]=np.percentile(RubPlas_to_Air_as_N[:,i], 25)
    Q25_To_Sinks[9,i]=np.percentile(RubPlas_to_Air_as_M[:,i], 25)
    Q25_To_Sinks[10,i]=np.percentile(Textiles_to_Air_as_N[:,i], 25)
    Q25_To_Sinks[11,i]=np.percentile(Textiles_to_Air_as_M[:,i], 25)
    Q25_To_Sinks[12,i]=np.percentile(WIP_to_Air_as_N[:,i], 25)
    Q25_To_Sinks[13,i]=np.percentile(WIP_to_Air_as_T[:,i], 25)
    Q25_To_Sinks[14,i]=np.percentile(Repr_to_Air_as_N[:,i], 25)
    Q25_To_Sinks[15,i]=np.percentile(Repr_to_Air_as_M[:,i], 25)
    Q25_To_Sinks[16,i]=np.percentile(Paints_to_NUSoil_as_N[:,i], 25)
    Q25_To_Sinks[17,i]=np.percentile(Paints_to_NUSoil_as_M[:,i], 25)
    Q25_To_Sinks[18,i]=np.percentile(Glass_to_NUSoil_as_N[:,i], 25)
    Q25_To_Sinks[19,i]=np.percentile(Glass_to_NUSoil_as_M[:,i], 25)
    Q25_To_Sinks[20,i]=np.percentile(Ceram_to_NUSoil_as_N[:,i], 25)
    Q25_To_Sinks[21,i]=np.percentile(Ceram_to_NUSoil_as_M[:,i], 25)
    Q25_To_Sinks[22,i]=np.percentile(Sewer_to_Subsurf_as_N[:,i], 25)
    Q25_To_Sinks[23,i]=np.percentile(Sewer_to_Subsurf_as_M[:,i], 25)
    Q25_To_Sinks[24,i]=np.percentile(Sewer_to_Subsurf_as_T[:,i], 25)
    Q25_To_Sinks[25,i]=np.percentile(OnSiteTreat_to_Subsurf_as_N[:,i], 25)
    Q25_To_Sinks[26,i]=np.percentile(OnSiteTreat_to_Subsurf_as_M[:,i], 25)
    Q25_To_Sinks[27,i]=np.percentile(OnSiteTreat_to_Subsurf_as_T[:,i], 25)
    Q25_To_Sinks[28,i]=np.percentile(STSoil_N[:,i], 25)
    Q25_To_Sinks[29,i]=np.percentile(STSoil_M[:,i], 25)
    Q25_To_Sinks[30,i]=np.percentile(STSoil_T[:,i], 25)
    Q25_To_Sinks[31,i]=np.percentile(OnSiteSludge_N[:,i], 25)
    Q25_To_Sinks[32,i]=np.percentile(OnSiteSludge_M[:,i], 25)
    Q25_To_Sinks[33,i]=np.percentile(OnSiteSludge_T[:,i], 25)
    Q25_To_Sinks[34,i]=np.percentile(PersCare_to_SurfWater_as_N[:,i], 25)
    Q25_To_Sinks[35,i]=np.percentile(NoSewer_to_SurfWater_as_N[:,i], 25)
    Q25_To_Sinks[36,i]=np.percentile(NoSewer_to_SurfWater_as_M[:,i], 25)
    Q25_To_Sinks[37,i]=np.percentile(NoSewer_to_SurfWater_as_T[:,i], 25)
    Q25_To_Sinks[38,i]=np.percentile(EndSewer_to_SurfWater_as_N[:,i], 25)
    Q25_To_Sinks[39,i]=np.percentile(EndSewer_to_SurfWater_as_M[:,i], 25)
    Q25_To_Sinks[40,i]=np.percentile(EndSewer_to_SurfWater_as_T[:,i], 25)
    Q25_To_Sinks[41,i]=np.percentile(Overflow_to_SurfWater_as_N[:,i], 25)
    Q25_To_Sinks[42,i]=np.percentile(Overflow_to_SurfWater_as_M[:,i], 25)
    Q25_To_Sinks[43,i]=np.percentile(Overflow_to_SurfWater_as_T[:,i], 25)
    Q25_To_Sinks[44,i]=np.percentile(STPEffluent_to_SurfWater_as_N[:,i], 25)
    Q25_To_Sinks[45,i]=np.percentile(STPEffluent_to_SurfWater_as_M[:,i], 25)
    Q25_To_Sinks[46,i]=np.percentile(STPEffluent_to_SurfWater_as_T[:,i], 25)
    Q25_To_Sinks[47,i]=np.percentile(ManufTextW_to_Landfill_as_P[:,i], 25)
    Q25_To_Sinks[48,i]=np.percentile(ManufPlasW_to_Landfill_as_P[:,i], 25)
    Q25_To_Sinks[49,i]=np.percentile(STPSlud_to_Landfill_as_N[:,i], 25)
    Q25_To_Sinks[50,i]=np.percentile(STPSlud_to_Landfill_as_M[:,i], 25)
    Q25_To_Sinks[51,i]=np.percentile(STPSlud_to_Landfill_as_T[:,i], 25)
    Q25_To_Sinks[52,i]=np.percentile(MMSW_to_Landfill_as_P[:,i], 25)
    Q25_To_Sinks[53,i]=np.percentile(CDW_to_Landfill_as_P[:,i], 25)
    Q25_To_Sinks[54,i]=np.percentile(SortCDWGlass_to_Landfill_as_P[:,i], 25)
    Q25_To_Sinks[55,i]=np.percentile(SortCDWMiner_to_Landfill_as_P[:,i], 25)
    Q25_To_Sinks[56,i]=np.percentile(SortDisp_to_Landfill_as_P[:,i], 25)
    Q25_To_Sinks[57,i]=np.percentile(GranuPlas_to_Landfill_as_P[:,i], 25)
    Q25_To_Sinks[58,i]=np.percentile(BaliText_to_Landfill_as_P[:,i], 25)
    Q25_To_Sinks[59,i]=np.percentile(Purislag_to_Landfill_as_P[:,i], 25)
    Q25_To_Sinks[60,i]=np.percentile(Purislag_to_Landfill_as_T[:,i], 25)
    Q25_To_Sinks[61,i]=np.percentile(SortMiner_to_Landfill_as_P[:,i], 25)
    Q25_To_Sinks[62,i]=np.percentile(Filterash_to_Landfill_as_N[:,i], 25)
    Q25_To_Sinks[63,i]=np.percentile(Filterash_to_Landfill_as_T[:,i], 25)
    Q25_To_Sinks[64,i]=np.percentile(Bottomash_to_Landfill_as_N[:,i], 25)
    Q25_To_Sinks[65,i]=np.percentile(Bottomash_to_Landfill_as_T[:,i], 25)
    Q25_To_Sinks[66,i]=np.percentile(ManufTextW_to_Reuse_as_P[:,i], 25)
    Q25_To_Sinks[67,i]=np.percentile(ManufPlasW_to_Reuse_as_P[:,i], 25)
    Q25_To_Sinks[68,i]=np.percentile(ManufSolidW_to_Reuse_as_P[:,i], 25)
    Q25_To_Sinks[69,i]=np.percentile(Filterash_to_Reuse_as_N[:,i], 25)
    Q25_To_Sinks[70,i]=np.percentile(Filterash_to_Reuse_as_T[:,i], 25)
    Q25_To_Sinks[71,i]=np.percentile(Bottomash_to_Reuse_as_N[:,i], 25)
    Q25_To_Sinks[72,i]=np.percentile(Bottomash_to_Reuse_as_T[:,i], 25)
    Q25_To_Sinks[73,i]=np.percentile(GranuPlas_to_Reuse_as_P[:,i], 25)
    Q25_To_Sinks[74,i]=np.percentile(BaliText_to_Reuse_as_P[:,i], 25)
    Q25_To_Sinks[75,i]=np.percentile(PuriMetal_to_Reuse_as_T[:,i], 25)
    Q25_To_Sinks[76,i]=np.percentile(PuriMetal_to_Reuse_as_P[:,i], 25)
    Q25_To_Sinks[77,i]=np.percentile(PuriSlag_to_Reuse_as_T[:,i], 25)
    Q25_To_Sinks[78,i]=np.percentile(PuriSlag_to_Reuse_as_P[:,i], 25)
    Q25_To_Sinks[79,i]=np.percentile(MeltGlass_to_Reuse_as_T[:,i], 25)
    Q25_To_Sinks[80,i]=np.percentile(SortMiner_to_Reuse_as_P[:,i], 25)
    Q25_To_Sinks[81,i]=np.percentile(SortWEEE_to_Export_as_P[:,i], 25)
    Q25_To_Sinks[82,i]=np.percentile(SortTextW_to_Export_as_P[:,i], 25)


# In[33]:


Q25_To_Sinks_DF = pd.DataFrame({'Pristine to Air from Production':Q25_To_Sinks[0,:],
                               'Pristine to Air from Manufacturing':Q25_To_Sinks[1,:],
                               'Pristine to Air from Paints':Q25_To_Sinks[2,:],
                               'Matrix-embedded to Air from Paints':Q25_To_Sinks[3,:],
                               'Pristine to Air from Glass':Q25_To_Sinks[4,:],
                               'Matrix-embedded to Air from Glass':Q25_To_Sinks[5,:],
                               'Pristine to Air from Ceramics':Q25_To_Sinks[6,:],
                               'Matrix-embedded to Air from Ceramics':Q25_To_Sinks[7,:],
                               'Pristine to Air from Rubber & Plastics':Q25_To_Sinks[8,:],
                               'Matrix-embedded to Air from Rubber & Plastics':Q25_To_Sinks[9,:],
                              'Pristine to Air from Textiles':Q25_To_Sinks[10,:],
                              'Matrix-embedded to Air from Textiles':Q25_To_Sinks[11,:],
                              'Pristine to Air from WIP':Q25_To_Sinks[12,:],
                              'Transformed to Air from WIP':Q25_To_Sinks[13,:],
                              'Pristine particles to Air from Reprocessing':Q25_To_Sinks[14,:],
                              'Matrix-embedded particles to Air from Reprocessing':Q25_To_Sinks[15,:],
                              'Pristine to NUSoil from Paints':Q25_To_Sinks[16,:],
                              'Matrix-embedded to NUSoil from Paints':Q25_To_Sinks[17,:],
                               'Pristine to NUSoil from Glass':Q25_To_Sinks[18,:],
                              'Matrix-embedded to NUSoil from Glass':Q25_To_Sinks[19,:],
                               'Pristine to NUSoil from Ceramics':Q25_To_Sinks[20,:],
                              'Matrix-embedded to NUSoil from Ceramics':Q25_To_Sinks[21,:],
                              'Pristine to Subsurface from Sewer':Q25_To_Sinks[22,:],
                              'Matrix-embedded to Subsurface from Sewer':Q25_To_Sinks[23,:],
                              'Transformed to Subsurface from Sewer':Q25_To_Sinks[24,:],
                              'Pristine to Subsurface from OnSite treatment':Q25_To_Sinks[25,:],
                              'Matrix-embedded to Subsurface from OnSite treatment':Q25_To_Sinks[26,:],
                              'Transformed to Subsurface from OnSite treatment':Q25_To_Sinks[27,:],
                              'Pristine to Sludge treated soil':Q25_To_Sinks[28,:],
                               'Matrix-embedded to Sludge treated soil':Q25_To_Sinks[29,:],
                              'Transformed to Sludge treated soil':Q25_To_Sinks[30,:],
                              'Pristine to OnsiteSludge':Q25_To_Sinks[31,:],
                               'Matrix-embedded to OnsiteSludge':Q25_To_Sinks[32,:],
                              'Transformed to OnsiteSludge':Q25_To_Sinks[33,:],
                              'Pristine to Surface water from PersCareLiquids':Q25_To_Sinks[34,:],
                              'Pristine to Surface water from No sewer':Q25_To_Sinks[35,:],
                              'Matrix-embedded to Surface water from No sewer':Q25_To_Sinks[36,:],
                              'Transformed to Surface water from No sewer':Q25_To_Sinks[37,:],
                              'Pristine to Surface water from Sewer':Q25_To_Sinks[38,:],
                               'Matrix-embedded to Surface water from Sewer':Q25_To_Sinks[39,:],
                              'Transformed to Surface water from Sewer':Q25_To_Sinks[40,:],
                              'Pristine to STP overflow and Surface water':Q25_To_Sinks[41,:],
                              'Matrix-embedded to STP overflow and Surface water':Q25_To_Sinks[42,:],
                              'Transformed to STP overflow and Surface water':Q25_To_Sinks[43,:],
                              'Pristine to STP effluent and Surface water':Q25_To_Sinks[44,:],
                              'Matrix-embedded to STP effluent and Surface water':Q25_To_Sinks[45,:],
                              'Transformed to STP effluent and Surface water':Q25_To_Sinks[46,:],
                              'Product-embedded to Landfill from Textiles manufacturing waste':Q25_To_Sinks[47,:],
                               'Product-embedded to Landfill from Plastic manufacturing waste':Q25_To_Sinks[48,:],
                              'Pristine to Landfill from STP sludge':Q25_To_Sinks[49,:],
                               'Matrix-embedded to Landfill from STP sludge':Q25_To_Sinks[50,:],
                              'Transformed to Landfill from STP sludge':Q25_To_Sinks[51,:],
                              'Product-embedded to Landfill from MMSW':Q25_To_Sinks[52,:],
                              'Product-embedded to Landfill from CDW':Q25_To_Sinks[53,:],
                              'Product-embedded to Landfill from Sorted CDW Glass':Q25_To_Sinks[54,:],
                              'Product-embedded to Landfill from Sorted CDW Mineral':Q25_To_Sinks[55,:],
                              'Product-embedded to Landfill from Other sorting':Q25_To_Sinks[56,:],
                               'Product-embedded to Landfill from Plastic granulation':Q25_To_Sinks[57,:],
                               'Product-embedded to Landfill from Textile baling':Q25_To_Sinks[58,:],
                               'Product-embedded to Landfill from Purification slag':Q25_To_Sinks[59,:],
                               'Transformed to Landfill from Purification slag':Q25_To_Sinks[60,:],
                               'Product-embedded to Landfill from Sorted mineral':Q25_To_Sinks[61,],
                               'Pristine to Landfill from Filter ash':Q25_To_Sinks[62,:],
                              'Transformed to Landfill from Filter ash':Q25_To_Sinks[63,:],
                              'Pristine to Landfill from Bottom ash':Q25_To_Sinks[64,:],
                              'Transformed to Landfill from Bottom ash':Q25_To_Sinks[65,:],
                              'Product-embedded to Reuse from Manufacturing textile waste':Q25_To_Sinks[66,:],
                               'Product-embedded to Reuse from Manufacturing plastic waste':Q25_To_Sinks[67,:],
                              'Product-embedded to Reuse from Manufacturing other solid waste':Q25_To_Sinks[68,:],
                              'Pristine from Filter ash to Reuse':Q25_To_Sinks[69,:],
                              'Transformed to Reuse from Filter ash':Q25_To_Sinks[70,:],
                              'Pristine to Reuse from Bottom ash':Q25_To_Sinks[71,:],
                              'Transformed to Reuse from Bottom ash':Q25_To_Sinks[72,:],
                              'Product-embedded to Reuse from Plastic granulation':Q25_To_Sinks[73,:],
                              'Product-embedded to Reuse from Baling textiles':Q25_To_Sinks[74,:],
                              'Transformed to Reuse from Metal purification':Q25_To_Sinks[75,:],
                               'Product-embedded to Reuse from Metal purification':Q25_To_Sinks[76,:],
                              'Transformed to Reuse from Slag purification':Q25_To_Sinks[77,:],
                               'Product-embedded to Reuse from Slag purification':Q25_To_Sinks[78,:],
                              'Transformed to Reuse from Melting glass':Q25_To_Sinks[79,:],
                              'Product-embedded to Reuse from Sorting minerals':Q25_To_Sinks[80,:],
                              'Product-embedded to Export from Sorting WEEE':Q25_To_Sinks[81,:],
                              'Product-embedded to Export from Sorting textile waste':Q25_To_Sinks[82,:],})


Q25_To_Sinks_DF_Transp = pd.DataFrame.transpose(Q25_To_Sinks_DF)
Q25_To_Sinks_DF_Transp.to_csv('Q25 to Sinks - TiO2 - AUT_2.csv',index=True, sep=',')


# In[34]:


# Extract Q75 to sinks for each year

Q75_To_Sinks = np.zeros(shape=(83,Tperiods))

for i in np.arange(0,Tperiods):
    Q75_To_Sinks[0,i]=np.percentile(Prod_to_Air_as_N[:,i], 75)
    Q75_To_Sinks[1,i]=np.percentile(Manuf_to_Air_as_N[:,i], 75)
    Q75_To_Sinks[2,i]=np.percentile(Paints_to_Air_as_N[:,i], 75)
    Q75_To_Sinks[3,i]=np.percentile(Paints_to_Air_as_M[:,i], 75)
    Q75_To_Sinks[4,i]=np.percentile(Glass_to_Air_as_N[:,i], 75)
    Q75_To_Sinks[5,i]=np.percentile(Glass_to_Air_as_M[:,i], 75)
    Q75_To_Sinks[6,i]=np.percentile(Ceram_to_Air_as_N[:,i], 75)
    Q75_To_Sinks[7,i]=np.percentile(Ceram_to_Air_as_M[:,i], 75)
    Q75_To_Sinks[8,i]=np.percentile(RubPlas_to_Air_as_N[:,i], 75)
    Q75_To_Sinks[9,i]=np.percentile(RubPlas_to_Air_as_M[:,i], 75)
    Q75_To_Sinks[10,i]=np.percentile(Textiles_to_Air_as_N[:,i], 75)
    Q75_To_Sinks[11,i]=np.percentile(Textiles_to_Air_as_M[:,i], 75)
    Q75_To_Sinks[12,i]=np.percentile(WIP_to_Air_as_N[:,i], 75)
    Q75_To_Sinks[13,i]=np.percentile(WIP_to_Air_as_T[:,i], 75)
    Q75_To_Sinks[14,i]=np.percentile(Repr_to_Air_as_N[:,i], 75)
    Q75_To_Sinks[15,i]=np.percentile(Repr_to_Air_as_M[:,i], 75)
    Q75_To_Sinks[16,i]=np.percentile(Paints_to_NUSoil_as_N[:,i], 75)
    Q75_To_Sinks[17,i]=np.percentile(Paints_to_NUSoil_as_M[:,i], 75)
    Q75_To_Sinks[18,i]=np.percentile(Glass_to_NUSoil_as_N[:,i], 75)
    Q75_To_Sinks[19,i]=np.percentile(Glass_to_NUSoil_as_M[:,i], 75)
    Q75_To_Sinks[20,i]=np.percentile(Ceram_to_NUSoil_as_N[:,i], 75)
    Q75_To_Sinks[21,i]=np.percentile(Ceram_to_NUSoil_as_M[:,i], 75)
    Q75_To_Sinks[22,i]=np.percentile(Sewer_to_Subsurf_as_N[:,i], 75)
    Q75_To_Sinks[23,i]=np.percentile(Sewer_to_Subsurf_as_M[:,i], 75)
    Q75_To_Sinks[24,i]=np.percentile(Sewer_to_Subsurf_as_T[:,i], 75)
    Q75_To_Sinks[25,i]=np.percentile(OnSiteTreat_to_Subsurf_as_N[:,i], 75)
    Q75_To_Sinks[26,i]=np.percentile(OnSiteTreat_to_Subsurf_as_M[:,i], 75)
    Q75_To_Sinks[27,i]=np.percentile(OnSiteTreat_to_Subsurf_as_T[:,i], 75)
    Q75_To_Sinks[28,i]=np.percentile(STSoil_N[:,i], 75)
    Q75_To_Sinks[29,i]=np.percentile(STSoil_M[:,i], 75)
    Q75_To_Sinks[30,i]=np.percentile(STSoil_T[:,i], 75)
    Q75_To_Sinks[31,i]=np.percentile(OnSiteSludge_N[:,i], 75)
    Q75_To_Sinks[32,i]=np.percentile(OnSiteSludge_M[:,i], 75)
    Q75_To_Sinks[33,i]=np.percentile(OnSiteSludge_T[:,i], 75)
    Q75_To_Sinks[34,i]=np.percentile(PersCare_to_SurfWater_as_N[:,i], 75)
    Q75_To_Sinks[35,i]=np.percentile(NoSewer_to_SurfWater_as_N[:,i], 75)
    Q75_To_Sinks[36,i]=np.percentile(NoSewer_to_SurfWater_as_M[:,i], 75)
    Q75_To_Sinks[37,i]=np.percentile(NoSewer_to_SurfWater_as_T[:,i], 75)
    Q75_To_Sinks[38,i]=np.percentile(EndSewer_to_SurfWater_as_N[:,i], 75)
    Q75_To_Sinks[39,i]=np.percentile(EndSewer_to_SurfWater_as_M[:,i], 75)
    Q75_To_Sinks[40,i]=np.percentile(EndSewer_to_SurfWater_as_T[:,i], 75)
    Q75_To_Sinks[41,i]=np.percentile(Overflow_to_SurfWater_as_N[:,i], 75)
    Q75_To_Sinks[42,i]=np.percentile(Overflow_to_SurfWater_as_M[:,i], 75)
    Q75_To_Sinks[43,i]=np.percentile(Overflow_to_SurfWater_as_T[:,i], 75)
    Q75_To_Sinks[44,i]=np.percentile(STPEffluent_to_SurfWater_as_N[:,i], 75)
    Q75_To_Sinks[45,i]=np.percentile(STPEffluent_to_SurfWater_as_M[:,i], 75)
    Q75_To_Sinks[46,i]=np.percentile(STPEffluent_to_SurfWater_as_T[:,i], 75)
    Q75_To_Sinks[47,i]=np.percentile(ManufTextW_to_Landfill_as_P[:,i], 75)
    Q75_To_Sinks[48,i]=np.percentile(ManufPlasW_to_Landfill_as_P[:,i], 75)
    Q75_To_Sinks[49,i]=np.percentile(STPSlud_to_Landfill_as_N[:,i], 75)
    Q75_To_Sinks[50,i]=np.percentile(STPSlud_to_Landfill_as_M[:,i], 75)
    Q75_To_Sinks[51,i]=np.percentile(STPSlud_to_Landfill_as_T[:,i], 75)
    Q75_To_Sinks[52,i]=np.percentile(MMSW_to_Landfill_as_P[:,i], 75)
    Q75_To_Sinks[53,i]=np.percentile(CDW_to_Landfill_as_P[:,i], 75)
    Q75_To_Sinks[54,i]=np.percentile(SortCDWGlass_to_Landfill_as_P[:,i], 75)
    Q75_To_Sinks[55,i]=np.percentile(SortCDWMiner_to_Landfill_as_P[:,i], 75)
    Q75_To_Sinks[56,i]=np.percentile(SortDisp_to_Landfill_as_P[:,i], 75)
    Q75_To_Sinks[57,i]=np.percentile(GranuPlas_to_Landfill_as_P[:,i], 75)
    Q75_To_Sinks[58,i]=np.percentile(BaliText_to_Landfill_as_P[:,i], 75)
    Q75_To_Sinks[59,i]=np.percentile(Purislag_to_Landfill_as_P[:,i], 75)
    Q75_To_Sinks[60,i]=np.percentile(Purislag_to_Landfill_as_T[:,i], 75)
    Q75_To_Sinks[61,i]=np.percentile(SortMiner_to_Landfill_as_P[:,i], 75)
    Q75_To_Sinks[62,i]=np.percentile(Filterash_to_Landfill_as_N[:,i], 75)
    Q75_To_Sinks[63,i]=np.percentile(Filterash_to_Landfill_as_T[:,i], 75)
    Q75_To_Sinks[64,i]=np.percentile(Bottomash_to_Landfill_as_N[:,i], 75)
    Q75_To_Sinks[65,i]=np.percentile(Bottomash_to_Landfill_as_T[:,i], 75)
    Q75_To_Sinks[66,i]=np.percentile(ManufTextW_to_Reuse_as_P[:,i], 75)
    Q75_To_Sinks[67,i]=np.percentile(ManufPlasW_to_Reuse_as_P[:,i], 75)
    Q75_To_Sinks[68,i]=np.percentile(ManufSolidW_to_Reuse_as_P[:,i], 75)
    Q75_To_Sinks[69,i]=np.percentile(Filterash_to_Reuse_as_N[:,i], 75)
    Q75_To_Sinks[70,i]=np.percentile(Filterash_to_Reuse_as_T[:,i], 75)
    Q75_To_Sinks[71,i]=np.percentile(Bottomash_to_Reuse_as_N[:,i], 75)
    Q75_To_Sinks[72,i]=np.percentile(Bottomash_to_Reuse_as_T[:,i], 75)
    Q75_To_Sinks[73,i]=np.percentile(GranuPlas_to_Reuse_as_P[:,i], 75)
    Q75_To_Sinks[74,i]=np.percentile(BaliText_to_Reuse_as_P[:,i], 75)
    Q75_To_Sinks[75,i]=np.percentile(PuriMetal_to_Reuse_as_T[:,i], 75)
    Q75_To_Sinks[76,i]=np.percentile(PuriMetal_to_Reuse_as_P[:,i], 75)
    Q75_To_Sinks[77,i]=np.percentile(PuriSlag_to_Reuse_as_T[:,i], 75)
    Q75_To_Sinks[78,i]=np.percentile(PuriSlag_to_Reuse_as_P[:,i], 75)
    Q75_To_Sinks[79,i]=np.percentile(MeltGlass_to_Reuse_as_T[:,i], 75)
    Q75_To_Sinks[80,i]=np.percentile(SortMiner_to_Reuse_as_P[:,i], 75)
    Q75_To_Sinks[81,i]=np.percentile(SortWEEE_to_Export_as_P[:,i], 75)
    Q75_To_Sinks[82,i]=np.percentile(SortTextW_to_Export_as_P[:,i], 75)


# In[35]:


Q75_To_Sinks_DF = pd.DataFrame({'Pristine to Air from Production':Q75_To_Sinks[0,:],
                               'Pristine to Air from Manufacturing':Q75_To_Sinks[1,:],
                               'Pristine to Air from Paints':Q75_To_Sinks[2,:],
                               'Matrix-embedded to Air from Paints':Q75_To_Sinks[3,:],
                               'Pristine to Air from Glass':Q75_To_Sinks[4,:],
                               'Matrix-embedded to Air from Glass':Q75_To_Sinks[5,:],
                               'Pristine to Air from Ceramics':Q75_To_Sinks[6,:],
                               'Matrix-embedded to Air from Ceramics':Q75_To_Sinks[7,:],
                               'Pristine to Air from Rubber & Plastics':Q75_To_Sinks[8,:],
                               'Matrix-embedded to Air from Rubber & Plastics':Q75_To_Sinks[9,:],
                              'Pristine to Air from Textiles':Q75_To_Sinks[10,:],
                              'Matrix-embedded to Air from Textiles':Q75_To_Sinks[11,:],
                              'Pristine to Air from WIP':Q75_To_Sinks[12,:],
                              'Transformed to Air from WIP':Q75_To_Sinks[13,:],
                              'Pristine particles to Air from Reprocessing':Q75_To_Sinks[14,:],
                              'Matrix-embedded particles to Air from Reprocessing':Q75_To_Sinks[15,:],
                              'Pristine to NUSoil from Paints':Q75_To_Sinks[16,:],
                              'Matrix-embedded to NUSoil from Paints':Q75_To_Sinks[17,:],
                               'Pristine to NUSoil from Glass':Q75_To_Sinks[18,:],
                              'Matrix-embedded to NUSoil from Glass':Q75_To_Sinks[19,:],
                               'Pristine to NUSoil from Ceramics':Q75_To_Sinks[20,:],
                              'Matrix-embedded to NUSoil from Ceramics':Q75_To_Sinks[21,:],
                              'Pristine to Subsurface from Sewer':Q75_To_Sinks[22,:],
                              'Matrix-embedded to Subsurface from Sewer':Q75_To_Sinks[23,:],
                              'Transformed to Subsurface from Sewer':Q75_To_Sinks[24,:],
                              'Pristine to Subsurface from OnSite treatment':Q75_To_Sinks[25,:],
                              'Matrix-embedded to Subsurface from OnSite treatment':Q75_To_Sinks[26,:],
                              'Transformed to Subsurface from OnSite treatment':Q75_To_Sinks[27,:],
                              'Pristine to Sludge treated soil':Q75_To_Sinks[28,:],
                               'Matrix-embedded to Sludge treated soil':Q75_To_Sinks[29,:],
                              'Transformed to Sludge treated soil':Q75_To_Sinks[30,:],
                              'Pristine to OnsiteSludge':Q75_To_Sinks[31,:],
                               'Matrix-embedded to OnsiteSludge':Q75_To_Sinks[32,:],
                              'Transformed to OnsiteSludge':Q75_To_Sinks[33,:],
                              'Pristine to Surface water from PersCareLiquids':Q75_To_Sinks[34,:],
                              'Pristine to Surface water from No sewer':Q75_To_Sinks[35,:],
                              'Matrix-embedded to Surface water from No sewer':Q75_To_Sinks[36,:],
                              'Transformed to Surface water from No sewer':Q75_To_Sinks[37,:],
                              'Pristine to Surface water from Sewer':Q75_To_Sinks[38,:],
                               'Matrix-embedded to Surface water from Sewer':Q75_To_Sinks[39,:],
                              'Transformed to Surface water from Sewer':Q75_To_Sinks[40,:],
                              'Pristine to STP overflow and Surface water':Q75_To_Sinks[41,:],
                              'Matrix-embedded to STP overflow and Surface water':Q75_To_Sinks[42,:],
                              'Transformed to STP overflow and Surface water':Q75_To_Sinks[43,:],
                              'Pristine to STP effluent and Surface water':Q75_To_Sinks[44,:],
                              'Matrix-embedded to STP effluent and Surface water':Q75_To_Sinks[45,:],
                              'Transformed to STP effluent and Surface water':Q75_To_Sinks[46,:],
                              'Product-embedded to Landfill from Textiles manufacturing waste':Q75_To_Sinks[47,:],
                               'Product-embedded to Landfill from Plastic manufacturing waste':Q75_To_Sinks[48,:],
                              'Pristine to Landfill from STP sludge':Q75_To_Sinks[49,:],
                               'Matrix-embedded to Landfill from STP sludge':Q75_To_Sinks[50,:],
                              'Transformed to Landfill from STP sludge':Q75_To_Sinks[51,:],
                              'Product-embedded to Landfill from MMSW':Q75_To_Sinks[52,:],
                              'Product-embedded to Landfill from CDW':Q75_To_Sinks[53,:],
                              'Product-embedded to Landfill from Sorted CDW Glass':Q75_To_Sinks[54,:],
                              'Product-embedded to Landfill from Sorted CDW Mineral':Q75_To_Sinks[55,:],
                              'Product-embedded to Landfill from Other sorting':Q75_To_Sinks[56,:],
                               'Product-embedded to Landfill from Plastic granulation':Q75_To_Sinks[57,:],
                               'Product-embedded to Landfill from Textile baling':Q75_To_Sinks[58,:],
                               'Product-embedded to Landfill from Purification slag':Q75_To_Sinks[59,:],
                               'Transformed to Landfill from Purification slag':Q75_To_Sinks[60,:],
                               'Product-embedded to Landfill from Sorted mineral':Q75_To_Sinks[61,],
                               'Pristine to Landfill from Filter ash':Q75_To_Sinks[62,:],
                              'Transformed to Landfill from Filter ash':Q75_To_Sinks[63,:],
                              'Pristine to Landfill from Bottom ash':Q75_To_Sinks[64,:],
                              'Transformed to Landfill from Bottom ash':Q75_To_Sinks[65,:],
                              'Product-embedded to Reuse from Manufacturing textile waste':Q75_To_Sinks[66,:],
                               'Product-embedded to Reuse from Manufacturing plastic waste':Q75_To_Sinks[67,:],
                              'Product-embedded to Reuse from Manufacturing other solid waste':Q75_To_Sinks[68,:],
                              'Pristine from Filter ash to Reuse':Q75_To_Sinks[69,:],
                              'Transformed to Reuse from Filter ash':Q75_To_Sinks[70,:],
                              'Pristine to Reuse from Bottom ash':Q75_To_Sinks[71,:],
                              'Transformed to Reuse from Bottom ash':Q75_To_Sinks[72,:],
                              'Product-embedded to Reuse from Plastic granulation':Q75_To_Sinks[73,:],
                              'Product-embedded to Reuse from Baling textiles':Q75_To_Sinks[74,:],
                              'Transformed to Reuse from Metal purification':Q75_To_Sinks[75,:],
                               'Product-embedded to Reuse from Metal purification':Q75_To_Sinks[76,:],
                              'Transformed to Reuse from Slag purification':Q75_To_Sinks[77,:],
                               'Product-embedded to Reuse from Slag purification':Q75_To_Sinks[78,:],
                              'Transformed to Reuse from Melting glass':Q75_To_Sinks[79,:],
                              'Product-embedded to Reuse from Sorting minerals':Q75_To_Sinks[80,:],
                              'Product-embedded to Export from Sorting WEEE':Q75_To_Sinks[81,:],
                              'Product-embedded to Export from Sorting textile waste':Q75_To_Sinks[82,:],})


Q75_To_Sinks_DF_Transp = pd.DataFrame.transpose(Q75_To_Sinks_DF)
Q75_To_Sinks_DF_Transp.to_csv('Q75 to Sinks - TiO2 - AUT_2.csv',index=True, sep=',')


# In[36]:


# Extract Q95 to sinks for each year

Q95_To_Sinks = np.zeros(shape=(83,Tperiods))

for i in np.arange(0,Tperiods):
    Q95_To_Sinks[0,i]=np.percentile(Prod_to_Air_as_N[:,i], 95)
    Q95_To_Sinks[1,i]=np.percentile(Manuf_to_Air_as_N[:,i], 95)
    Q95_To_Sinks[2,i]=np.percentile(Paints_to_Air_as_N[:,i], 95)
    Q95_To_Sinks[3,i]=np.percentile(Paints_to_Air_as_M[:,i], 95)
    Q95_To_Sinks[4,i]=np.percentile(Glass_to_Air_as_N[:,i], 95)
    Q95_To_Sinks[5,i]=np.percentile(Glass_to_Air_as_M[:,i], 95)
    Q95_To_Sinks[6,i]=np.percentile(Ceram_to_Air_as_N[:,i], 95)
    Q95_To_Sinks[7,i]=np.percentile(Ceram_to_Air_as_M[:,i], 95)
    Q95_To_Sinks[8,i]=np.percentile(RubPlas_to_Air_as_N[:,i], 95)
    Q95_To_Sinks[9,i]=np.percentile(RubPlas_to_Air_as_M[:,i], 95)
    Q95_To_Sinks[10,i]=np.percentile(Textiles_to_Air_as_N[:,i], 95)
    Q95_To_Sinks[11,i]=np.percentile(Textiles_to_Air_as_M[:,i], 95)
    Q95_To_Sinks[12,i]=np.percentile(WIP_to_Air_as_N[:,i], 95)
    Q95_To_Sinks[13,i]=np.percentile(WIP_to_Air_as_T[:,i], 95)
    Q95_To_Sinks[14,i]=np.percentile(Repr_to_Air_as_N[:,i], 95)
    Q95_To_Sinks[15,i]=np.percentile(Repr_to_Air_as_M[:,i], 95)
    Q95_To_Sinks[16,i]=np.percentile(Paints_to_NUSoil_as_N[:,i], 95)
    Q95_To_Sinks[17,i]=np.percentile(Paints_to_NUSoil_as_M[:,i], 95)
    Q95_To_Sinks[18,i]=np.percentile(Glass_to_NUSoil_as_N[:,i], 95)
    Q95_To_Sinks[19,i]=np.percentile(Glass_to_NUSoil_as_M[:,i], 95)
    Q95_To_Sinks[20,i]=np.percentile(Ceram_to_NUSoil_as_N[:,i], 95)
    Q95_To_Sinks[21,i]=np.percentile(Ceram_to_NUSoil_as_M[:,i], 95)
    Q95_To_Sinks[22,i]=np.percentile(Sewer_to_Subsurf_as_N[:,i], 95)
    Q95_To_Sinks[23,i]=np.percentile(Sewer_to_Subsurf_as_M[:,i], 95)
    Q95_To_Sinks[24,i]=np.percentile(Sewer_to_Subsurf_as_T[:,i], 95)
    Q95_To_Sinks[25,i]=np.percentile(OnSiteTreat_to_Subsurf_as_N[:,i], 95)
    Q95_To_Sinks[26,i]=np.percentile(OnSiteTreat_to_Subsurf_as_M[:,i], 95)
    Q95_To_Sinks[27,i]=np.percentile(OnSiteTreat_to_Subsurf_as_T[:,i], 95)
    Q95_To_Sinks[28,i]=np.percentile(STSoil_N[:,i], 95)
    Q95_To_Sinks[29,i]=np.percentile(STSoil_M[:,i], 95)
    Q95_To_Sinks[30,i]=np.percentile(STSoil_T[:,i], 95)
    Q95_To_Sinks[31,i]=np.percentile(OnSiteSludge_N[:,i], 95)
    Q95_To_Sinks[32,i]=np.percentile(OnSiteSludge_M[:,i], 95)
    Q95_To_Sinks[33,i]=np.percentile(OnSiteSludge_T[:,i], 95)
    Q95_To_Sinks[34,i]=np.percentile(PersCare_to_SurfWater_as_N[:,i], 95)
    Q95_To_Sinks[35,i]=np.percentile(NoSewer_to_SurfWater_as_N[:,i], 95)
    Q95_To_Sinks[36,i]=np.percentile(NoSewer_to_SurfWater_as_M[:,i], 95)
    Q95_To_Sinks[37,i]=np.percentile(NoSewer_to_SurfWater_as_T[:,i], 95)
    Q95_To_Sinks[38,i]=np.percentile(EndSewer_to_SurfWater_as_N[:,i], 95)
    Q95_To_Sinks[39,i]=np.percentile(EndSewer_to_SurfWater_as_M[:,i], 95)
    Q95_To_Sinks[40,i]=np.percentile(EndSewer_to_SurfWater_as_T[:,i], 95)
    Q95_To_Sinks[41,i]=np.percentile(Overflow_to_SurfWater_as_N[:,i], 95)
    Q95_To_Sinks[42,i]=np.percentile(Overflow_to_SurfWater_as_M[:,i], 95)
    Q95_To_Sinks[43,i]=np.percentile(Overflow_to_SurfWater_as_T[:,i], 95)
    Q95_To_Sinks[44,i]=np.percentile(STPEffluent_to_SurfWater_as_N[:,i], 95)
    Q95_To_Sinks[45,i]=np.percentile(STPEffluent_to_SurfWater_as_M[:,i], 95)
    Q95_To_Sinks[46,i]=np.percentile(STPEffluent_to_SurfWater_as_T[:,i], 95)
    Q95_To_Sinks[47,i]=np.percentile(ManufTextW_to_Landfill_as_P[:,i], 95)
    Q95_To_Sinks[48,i]=np.percentile(ManufPlasW_to_Landfill_as_P[:,i], 95)
    Q95_To_Sinks[49,i]=np.percentile(STPSlud_to_Landfill_as_N[:,i], 95)
    Q95_To_Sinks[50,i]=np.percentile(STPSlud_to_Landfill_as_M[:,i], 95)
    Q95_To_Sinks[51,i]=np.percentile(STPSlud_to_Landfill_as_T[:,i], 95)
    Q95_To_Sinks[52,i]=np.percentile(MMSW_to_Landfill_as_P[:,i], 95)
    Q95_To_Sinks[53,i]=np.percentile(CDW_to_Landfill_as_P[:,i], 95)
    Q95_To_Sinks[54,i]=np.percentile(SortCDWGlass_to_Landfill_as_P[:,i], 95)
    Q95_To_Sinks[55,i]=np.percentile(SortCDWMiner_to_Landfill_as_P[:,i], 95)
    Q95_To_Sinks[56,i]=np.percentile(SortDisp_to_Landfill_as_P[:,i], 95)
    Q95_To_Sinks[57,i]=np.percentile(GranuPlas_to_Landfill_as_P[:,i], 95)
    Q95_To_Sinks[58,i]=np.percentile(BaliText_to_Landfill_as_P[:,i], 95)
    Q95_To_Sinks[59,i]=np.percentile(Purislag_to_Landfill_as_P[:,i], 95)
    Q95_To_Sinks[60,i]=np.percentile(Purislag_to_Landfill_as_T[:,i], 95)
    Q95_To_Sinks[61,i]=np.percentile(SortMiner_to_Landfill_as_P[:,i], 95)
    Q95_To_Sinks[62,i]=np.percentile(Filterash_to_Landfill_as_N[:,i], 95)
    Q95_To_Sinks[63,i]=np.percentile(Filterash_to_Landfill_as_T[:,i], 95)
    Q95_To_Sinks[64,i]=np.percentile(Bottomash_to_Landfill_as_N[:,i], 95)
    Q95_To_Sinks[65,i]=np.percentile(Bottomash_to_Landfill_as_T[:,i], 95)
    Q95_To_Sinks[66,i]=np.percentile(ManufTextW_to_Reuse_as_P[:,i], 95)
    Q95_To_Sinks[67,i]=np.percentile(ManufPlasW_to_Reuse_as_P[:,i], 95)
    Q95_To_Sinks[68,i]=np.percentile(ManufSolidW_to_Reuse_as_P[:,i], 95)
    Q95_To_Sinks[69,i]=np.percentile(Filterash_to_Reuse_as_N[:,i], 95)
    Q95_To_Sinks[70,i]=np.percentile(Filterash_to_Reuse_as_T[:,i], 95)
    Q95_To_Sinks[71,i]=np.percentile(Bottomash_to_Reuse_as_N[:,i], 95)
    Q95_To_Sinks[72,i]=np.percentile(Bottomash_to_Reuse_as_T[:,i], 95)
    Q95_To_Sinks[73,i]=np.percentile(GranuPlas_to_Reuse_as_P[:,i], 95)
    Q95_To_Sinks[74,i]=np.percentile(BaliText_to_Reuse_as_P[:,i], 95)
    Q95_To_Sinks[75,i]=np.percentile(PuriMetal_to_Reuse_as_T[:,i], 95)
    Q95_To_Sinks[76,i]=np.percentile(PuriMetal_to_Reuse_as_P[:,i], 95)
    Q95_To_Sinks[77,i]=np.percentile(PuriSlag_to_Reuse_as_T[:,i], 95)
    Q95_To_Sinks[78,i]=np.percentile(PuriSlag_to_Reuse_as_P[:,i], 95)
    Q95_To_Sinks[79,i]=np.percentile(MeltGlass_to_Reuse_as_T[:,i], 95)
    Q95_To_Sinks[80,i]=np.percentile(SortMiner_to_Reuse_as_P[:,i], 95)
    Q95_To_Sinks[81,i]=np.percentile(SortWEEE_to_Export_as_P[:,i], 95)
    Q95_To_Sinks[82,i]=np.percentile(SortTextW_to_Export_as_P[:,i], 95)


# In[37]:


Q95_To_Sinks_DF = pd.DataFrame({'Pristine to Air from Production':Q95_To_Sinks[0,:],
                               'Pristine to Air from Manufacturing':Q95_To_Sinks[1,:],
                               'Pristine to Air from Paints':Q95_To_Sinks[2,:],
                               'Matrix-embedded to Air from Paints':Q95_To_Sinks[3,:],
                               'Pristine to Air from Glass':Q95_To_Sinks[4,:],
                               'Matrix-embedded to Air from Glass':Q95_To_Sinks[5,:],
                               'Pristine to Air from Ceramics':Q95_To_Sinks[6,:],
                               'Matrix-embedded to Air from Ceramics':Q95_To_Sinks[7,:],
                               'Pristine to Air from Rubber & Plastics':Q95_To_Sinks[8,:],
                               'Matrix-embedded to Air from Rubber & Plastics':Q95_To_Sinks[9,:],
                              'Pristine to Air from Textiles':Q95_To_Sinks[10,:],
                              'Matrix-embedded to Air from Textiles':Q95_To_Sinks[11,:],
                              'Pristine to Air from WIP':Q95_To_Sinks[12,:],
                              'Transformed to Air from WIP':Q95_To_Sinks[13,:],
                              'Pristine particles to Air from Reprocessing':Q95_To_Sinks[14,:],
                              'Matrix-embedded particles to Air from Reprocessing':Q95_To_Sinks[15,:],
                              'Pristine to NUSoil from Paints':Q95_To_Sinks[16,:],
                              'Matrix-embedded to NUSoil from Paints':Q95_To_Sinks[17,:],
                               'Pristine to NUSoil from Glass':Q95_To_Sinks[18,:],
                              'Matrix-embedded to NUSoil from Glass':Q95_To_Sinks[19,:],
                               'Pristine to NUSoil from Ceramics':Q95_To_Sinks[20,:],
                              'Matrix-embedded to NUSoil from Ceramics':Q95_To_Sinks[21,:],
                              'Pristine to Subsurface from Sewer':Q95_To_Sinks[22,:],
                              'Matrix-embedded to Subsurface from Sewer':Q95_To_Sinks[23,:],
                              'Transformed to Subsurface from Sewer':Q95_To_Sinks[24,:],
                              'Pristine to Subsurface from OnSite treatment':Q95_To_Sinks[25,:],
                              'Matrix-embedded to Subsurface from OnSite treatment':Q95_To_Sinks[26,:],
                              'Transformed to Subsurface from OnSite treatment':Q95_To_Sinks[27,:],
                              'Pristine to Sludge treated soil':Q95_To_Sinks[28,:],
                               'Matrix-embedded to Sludge treated soil':Q95_To_Sinks[29,:],
                              'Transformed to Sludge treated soil':Q95_To_Sinks[30,:],
                              'Pristine to OnsiteSludge':Q95_To_Sinks[31,:],
                               'Matrix-embedded to OnsiteSludge':Q95_To_Sinks[32,:],
                              'Transformed to OnsiteSludge':Q95_To_Sinks[33,:],
                              'Pristine to Surface water from PersCareLiquids':Q95_To_Sinks[34,:],
                              'Pristine to Surface water from No sewer':Q95_To_Sinks[35,:],
                              'Matrix-embedded to Surface water from No sewer':Q95_To_Sinks[36,:],
                              'Transformed to Surface water from No sewer':Q95_To_Sinks[37,:],
                              'Pristine to Surface water from Sewer':Q95_To_Sinks[38,:],
                               'Matrix-embedded to Surface water from Sewer':Q95_To_Sinks[39,:],
                              'Transformed to Surface water from Sewer':Q95_To_Sinks[40,:],
                              'Pristine to STP overflow and Surface water':Q95_To_Sinks[41,:],
                              'Matrix-embedded to STP overflow and Surface water':Q95_To_Sinks[42,:],
                              'Transformed to STP overflow and Surface water':Q95_To_Sinks[43,:],
                              'Pristine to STP effluent and Surface water':Q95_To_Sinks[44,:],
                              'Matrix-embedded to STP effluent and Surface water':Q95_To_Sinks[45,:],
                              'Transformed to STP effluent and Surface water':Q95_To_Sinks[46,:],
                              'Product-embedded to Landfill from Textiles manufacturing waste':Q95_To_Sinks[47,:],
                               'Product-embedded to Landfill from Plastic manufacturing waste':Q95_To_Sinks[48,:],
                              'Pristine to Landfill from STP sludge':Q95_To_Sinks[49,:],
                               'Matrix-embedded to Landfill from STP sludge':Q95_To_Sinks[50,:],
                              'Transformed to Landfill from STP sludge':Q95_To_Sinks[51,:],
                              'Product-embedded to Landfill from MMSW':Q95_To_Sinks[52,:],
                              'Product-embedded to Landfill from CDW':Q95_To_Sinks[53,:],
                              'Product-embedded to Landfill from Sorted CDW Glass':Q95_To_Sinks[54,:],
                              'Product-embedded to Landfill from Sorted CDW Mineral':Q95_To_Sinks[55,:],
                              'Product-embedded to Landfill from Other sorting':Q95_To_Sinks[56,:],
                               'Product-embedded to Landfill from Plastic granulation':Q95_To_Sinks[57,:],
                               'Product-embedded to Landfill from Textile baling':Q95_To_Sinks[58,:],
                               'Product-embedded to Landfill from Purification slag':Q95_To_Sinks[59,:],
                               'Transformed to Landfill from Purification slag':Q95_To_Sinks[60,:],
                               'Product-embedded to Landfill from Sorted mineral':Q95_To_Sinks[61,],
                               'Pristine to Landfill from Filter ash':Q95_To_Sinks[62,:],
                              'Transformed to Landfill from Filter ash':Q95_To_Sinks[63,:],
                              'Pristine to Landfill from Bottom ash':Q95_To_Sinks[64,:],
                              'Transformed to Landfill from Bottom ash':Q95_To_Sinks[65,:],
                              'Product-embedded to Reuse from Manufacturing textile waste':Q95_To_Sinks[66,:],
                               'Product-embedded to Reuse from Manufacturing plastic waste':Q95_To_Sinks[67,:],
                              'Product-embedded to Reuse from Manufacturing other solid waste':Q95_To_Sinks[68,:],
                              'Pristine from Filter ash to Reuse':Q95_To_Sinks[69,:],
                              'Transformed to Reuse from Filter ash':Q95_To_Sinks[70,:],
                              'Pristine to Reuse from Bottom ash':Q95_To_Sinks[71,:],
                              'Transformed to Reuse from Bottom ash':Q95_To_Sinks[72,:],
                              'Product-embedded to Reuse from Plastic granulation':Q95_To_Sinks[73,:],
                              'Product-embedded to Reuse from Baling textiles':Q95_To_Sinks[74,:],
                              'Transformed to Reuse from Metal purification':Q95_To_Sinks[75,:],
                               'Product-embedded to Reuse from Metal purification':Q95_To_Sinks[76,:],
                              'Transformed to Reuse from Slag purification':Q95_To_Sinks[77,:],
                               'Product-embedded to Reuse from Slag purification':Q95_To_Sinks[78,:],
                              'Transformed to Reuse from Melting glass':Q95_To_Sinks[79,:],
                              'Product-embedded to Reuse from Sorting minerals':Q95_To_Sinks[80,:],
                              'Product-embedded to Export from Sorting WEEE':Q95_To_Sinks[81,:],
                              'Product-embedded to Export from Sorting textile waste':Q95_To_Sinks[82,:],})


Q95_To_Sinks_DF_Transp = pd.DataFrame.transpose(Q95_To_Sinks_DF)
Q95_To_Sinks_DF_Transp.to_csv('Q95 to Sinks - TiO2 - AUT_2.csv',index=True, sep=',')


# In[38]:


###################### AGGREGATED FLOWS TO SINKS ########################


# In[39]:


Comp_with_loggedInflows = simulator.getLoggedInflows()

ImpoMatrix_raw = simulator.getLoggedCategoryInflows('Import')
ProdMatrix_raw = simulator.getLoggedCategoryInflows('Production') # summed up inflows to CATEGORY production in a matrix 20 years x 100 000 simulations
ManufMatrix_raw = Comp_with_loggedInflows['Manufacture'] # summed up inflows to COMPARTMENT manufacture in a matrix 20 years x 100 000 simulations
ConsMatrix_raw = Comp_with_loggedInflows['Consumption'] # summed up inflows to COMPARTMENT consumption in a matrix 20 years x 100 000 simulations
WWMatrix_raw = simulator.getLoggedCategoryInflows('AllWastewater') # summed up inflows to CATEGORY wastewater in a matrix 20 years x 100 000 simulations
SewMatrix_raw = simulator.getLoggedCategoryInflows('SewageSystem') # summed up inflows to CATEGORY sewage system in a matrix 20 years x 100 000 simulations
WWTPMatrix_raw = simulator.getLoggedCategoryInflows('WWTP') # summed up inflows to CATEGORY WWTP in a matrix 20 years x 100 000 simulations
OSTreatMatrix_raw = simulator.getLoggedCategoryInflows('OnsiteTreat') # summed up inflows to CATEGORY OnsiteTreat in a matrix 20 years x 100 000 simulations
OSSludMatrix_raw = simulator.getLoggedCategoryInflows('OnsiteSludge') # summed up inflows to CATEGORY OnsiteSludge in a matrix 20 years x 100 000 simulations
SubsurfMatrix_raw = simulator.getLoggedCategoryInflows('Subsurface') # summed up inflows to CATEGORY Subsurface in a matrix 20 years x 100 000 simulations
SortMatrix_raw = simulator.getLoggedCategoryInflows('Sorting1') # summed up inflows to CATEGORY Sorting1 in a matrix 20 years x 100 000 simulations
ReprMatrix_raw = simulator.getLoggedCategoryInflows('Reprocessing') # summed up inflows to CATEGORY Reprocessing in a matrix 20 years x 100 000 simulations
ReusMatrix_raw = simulator.getLoggedCategoryInflows('Reuse')
WIPMatrix_raw = simulator.getLoggedCategoryInflows('WIP') # summed up inflows to COMPARTMENT WIP in a matrix 20 years x 100 000 simulations
LandfMatrix_raw = simulator.getLoggedCategoryInflows('Landfill') # summed up inflows to COMPARTMENT Landfill in a matrix 20 years x 100 000 simulations
ExpMatrix_raw = simulator.getLoggedCategoryInflows('Export') # summed up inflows to CATEGORY export in a matrix 20 years x 100 000 simulations
AirMatrix_raw = simulator.getLoggedCategoryInflows('Air') # summed up inflows to CATEGORY air in a matrix 20 years x 100 000 simulations
NUSoilMatrix_raw = simulator.getLoggedCategoryInflows('NU Soil') # summed up inflows to CATEGORY air in a matrix 20 years x 100 000 simulations
STSoilMatrix_raw = simulator.getLoggedCategoryInflows('ST Soil') # summed up inflows to CATEGORY air in a matrix 20 years x 100 000 simulations
SurfWatMatrix_raw = simulator.getLoggedCategoryInflows('Surfacewater') # summed up inflows to CATEGORY air in a matrix 20 years x 100 000 simulations

WWMatrix_N_raw = simulator.getLoggedCategoryInflows('AllWastewater_N')
WWMatrix_M_raw = simulator.getLoggedCategoryInflows('AllWastewater_M')
WWMatrix_T_raw = simulator.getLoggedCategoryInflows('AllWastewater_T')

SewMatrix_N_raw = simulator.getLoggedCategoryInflows('SewageSystem_N')
SewMatrix_M_raw = simulator.getLoggedCategoryInflows('SewageSystem_M')
SewMatrix_T_raw = simulator.getLoggedCategoryInflows('SewageSystem_T')

WWTPMatrix_N_raw = simulator.getLoggedCategoryInflows('WWTP_N')
WWTPMatrix_M_raw = simulator.getLoggedCategoryInflows('WWTP_M')
WWTPMatrix_T_raw = simulator.getLoggedCategoryInflows('WWTP_T')

OSTreatMatrix_N_raw = simulator.getLoggedCategoryInflows('OnsiteTreat_N')
OSTreatMatrix_M_raw = simulator.getLoggedCategoryInflows('OnsiteTreat_M')
OSTreatMatrix_T_raw = simulator.getLoggedCategoryInflows('OnsiteTreat_T')

OSSludMatrix_N_raw = simulator.getLoggedCategoryInflows('OnsiteSludge_N')
OSSludMatrix_M_raw = simulator.getLoggedCategoryInflows('OnsiteSludge_M')
OSSludMatrix_T_raw = simulator.getLoggedCategoryInflows('OnsiteSludge_T')

SubsurfMatrix_N_raw = simulator.getLoggedCategoryInflows('Subsurface_N')
SubsurfMatrix_M_raw = simulator.getLoggedCategoryInflows('Subsurface_M')
SubsurfMatrix_T_raw = simulator.getLoggedCategoryInflows('Subsurface_T')

ReusMatrix_N_raw = simulator.getLoggedCategoryInflows('Reuse_N')
ReusMatrix_T_raw = simulator.getLoggedCategoryInflows('Reuse_T')
ReusMatrix_P_raw = simulator.getLoggedCategoryInflows('Reuse_P')

WIPMatrix_N_raw = simulator.getLoggedCategoryInflows('WIP_N')
WIPMatrix_M_raw = simulator.getLoggedCategoryInflows('WIP_M')
WIPMatrix_T_raw = simulator.getLoggedCategoryInflows('WIP_T')
WIPMatrix_P_raw = simulator.getLoggedCategoryInflows('WIP_P')

LandfMatrix_N_raw = simulator.getLoggedCategoryInflows('Landfill_N')
LandfMatrix_M_raw = simulator.getLoggedCategoryInflows('Landfill_M')
LandfMatrix_T_raw = simulator.getLoggedCategoryInflows('Landfill_T')
LandfMatrix_P_raw = simulator.getLoggedCategoryInflows('Landfill_P')

AirMatrix_N_raw = simulator.getLoggedCategoryInflows('Air_N')
AirMatrix_M_raw = simulator.getLoggedCategoryInflows('Air_M')
AirMatrix_T_raw = simulator.getLoggedCategoryInflows('Air_T')

NUSoilMatrix_N_raw = simulator.getLoggedCategoryInflows('NU Soil_N')
NUSoilMatrix_M_raw = simulator.getLoggedCategoryInflows('NU Soil_M')

STSoilMatrix_N_raw = simulator.getLoggedCategoryInflows('ST Soil_N')
STSoilMatrix_M_raw = simulator.getLoggedCategoryInflows('ST Soil_M')
STSoilMatrix_T_raw = simulator.getLoggedCategoryInflows('ST Soil_T')

SurfWatMatrix_N_raw = simulator.getLoggedCategoryInflows('Surfacewater_N')
SurfWatMatrix_M_raw = simulator.getLoggedCategoryInflows('Surfacewater_M')
SurfWatMatrix_T_raw = simulator.getLoggedCategoryInflows('Surfacewater_T')


# In[40]:


Mean_agg = np.zeros(shape=(60, Tperiods))
Std_agg = np.zeros(shape=(60, Tperiods))
RelUnc_agg = np.zeros(shape=(60, Tperiods))
for i in np.arange(0,Tperiods):
    Mean_agg[0, i] = np.mean(ImpoMatrix_raw[:,i])
    Mean_agg[1, i] = np.mean(ProdMatrix_raw[:,i])
    Mean_agg[2, i] = np.mean(ManufMatrix_raw[:,i])
    Mean_agg[3, i] = np.mean(ConsMatrix_raw[:,i])
    Mean_agg[4, i] = np.mean(WWMatrix_raw[:,i])
    Mean_agg[5, i] = np.mean(SewMatrix_raw[:,i])
    Mean_agg[6, i] = np.mean(WWTPMatrix_raw[:,i])
    Mean_agg[7, i] = np.mean(OSTreatMatrix_raw[:,i])
    Mean_agg[8, i] = np.mean(OSSludMatrix_raw[:,i])
    Mean_agg[9, i] = np.mean(SubsurfMatrix_raw[:,i])
    Mean_agg[10, i] = np.mean(SortMatrix_raw[:,i])
    Mean_agg[11, i] = np.mean(ReprMatrix_raw[:,i])
    Mean_agg[12, i] = np.mean(ReusMatrix_raw[:,i])
    Mean_agg[13, i] = np.mean(WIPMatrix_raw[:,i])
    Mean_agg[14, i] = np.mean(LandfMatrix_raw[:,i])
    Mean_agg[15, i] = np.mean(ExpMatrix_raw[:,i])
    Mean_agg[16, i] = np.mean(AirMatrix_raw[:,i])
    Mean_agg[17, i] = np.mean(NUSoilMatrix_raw[:,i])
    Mean_agg[18, i] = np.mean(STSoilMatrix_raw[:,i])
    Mean_agg[19, i] = np.mean(SurfWatMatrix_raw[:,i])
    Mean_agg[20, i] = np.mean(WWMatrix_N_raw[:,i])
    Mean_agg[21, i] = np.mean(WWMatrix_M_raw[:,i])
    Mean_agg[22, i] = np.mean(WWMatrix_T_raw[:,i])
    Mean_agg[23, i] = np.mean(SewMatrix_N_raw[:,i])
    Mean_agg[24, i] = np.mean(SewMatrix_M_raw[:,i])
    Mean_agg[25, i] = np.mean(SewMatrix_T_raw[:,i])
    Mean_agg[26, i] = np.mean(WWTPMatrix_N_raw[:,i])
    Mean_agg[27, i] = np.mean(WWTPMatrix_M_raw[:,i])
    Mean_agg[28, i] = np.mean(WWTPMatrix_T_raw[:,i])
    Mean_agg[29, i] = np.mean(OSTreatMatrix_N_raw[:,i])
    Mean_agg[30, i] = np.mean(OSTreatMatrix_M_raw[:,i])
    Mean_agg[31, i] = np.mean(OSTreatMatrix_T_raw[:,i])
    Mean_agg[32, i] = np.mean(OSSludMatrix_N_raw[:,i])
    Mean_agg[33, i] = np.mean(OSSludMatrix_M_raw[:,i])
    Mean_agg[34, i] = np.mean(OSSludMatrix_T_raw[:,i])
    Mean_agg[35, i] = np.mean(SubsurfMatrix_N_raw[:,i])
    Mean_agg[36, i] = np.mean(SubsurfMatrix_M_raw[:,i])
    Mean_agg[37, i] = np.mean(SubsurfMatrix_T_raw[:,i])
    Mean_agg[38, i] = np.mean(ReusMatrix_N_raw[:,i])
    Mean_agg[39, i] = np.mean(ReusMatrix_T_raw[:,i])
    Mean_agg[40, i] = np.mean(ReusMatrix_P_raw[:,i])
    Mean_agg[41, i] = np.mean(WIPMatrix_N_raw[:,i])
    Mean_agg[42, i] = np.mean(WIPMatrix_M_raw[:,i])
    Mean_agg[43, i] = np.mean(WIPMatrix_T_raw[:,i])
    Mean_agg[44, i] = np.mean(WIPMatrix_P_raw[:,i])
    Mean_agg[45, i] = np.mean(LandfMatrix_N_raw[:,i])
    Mean_agg[46, i] = np.mean(LandfMatrix_M_raw[:,i])
    Mean_agg[47, i] = np.mean(LandfMatrix_T_raw[:,i])
    Mean_agg[48, i] = np.mean(LandfMatrix_P_raw[:,i])
    Mean_agg[49, i] = np.mean(AirMatrix_N_raw[:,i])
    Mean_agg[50, i] = np.mean(AirMatrix_M_raw[:,i])
    Mean_agg[51, i] = np.mean(AirMatrix_T_raw[:,i])
    Mean_agg[52, i] = np.mean(NUSoilMatrix_N_raw[:,i])
    Mean_agg[53, i] = np.mean(NUSoilMatrix_M_raw[:,i])
    Mean_agg[54, i] = np.mean(STSoilMatrix_N_raw[:,i])
    Mean_agg[55, i] = np.mean(STSoilMatrix_M_raw[:,i])
    Mean_agg[56, i] = np.mean(STSoilMatrix_T_raw[:,i])
    Mean_agg[57, i] = np.mean(SurfWatMatrix_N_raw[:,i])
    Mean_agg[58, i] = np.mean(SurfWatMatrix_M_raw[:,i])
    Mean_agg[59, i] = np.mean(SurfWatMatrix_T_raw[:,i])

    Std_agg[0, i] = np.std(ImpoMatrix_raw[:,i])
    Std_agg[1, i] = np.std(ProdMatrix_raw[:,i])
    Std_agg[2, i] = np.std(ManufMatrix_raw[:,i])
    Std_agg[3, i] = np.std(ConsMatrix_raw[:,i])
    Std_agg[4, i] = np.std(WWMatrix_raw[:,i])
    Std_agg[5, i] = np.std(SewMatrix_raw[:,i])
    Std_agg[6, i] = np.std(WWTPMatrix_raw[:,i])
    Std_agg[7, i] = np.std(OSTreatMatrix_raw[:,i])
    Std_agg[8, i] = np.std(OSSludMatrix_raw[:,i])
    Std_agg[9, i] = np.std(SubsurfMatrix_raw[:,i])
    Std_agg[10, i] = np.std(SortMatrix_raw[:,i])
    Std_agg[11, i] = np.std(ReprMatrix_raw[:,i])
    Std_agg[12, i] = np.std(ReusMatrix_raw[:,i])
    Std_agg[13, i] = np.std(WIPMatrix_raw[:,i])
    Std_agg[14, i] = np.std(LandfMatrix_raw[:,i])
    Std_agg[15, i] = np.std(ExpMatrix_raw[:,i])
    Std_agg[16, i] = np.std(AirMatrix_raw[:,i])
    Std_agg[17, i] = np.std(NUSoilMatrix_raw[:,i])
    Std_agg[18, i] = np.std(STSoilMatrix_raw[:,i])
    Std_agg[19, i] = np.std(SurfWatMatrix_raw[:,i])
    Std_agg[20, i] = np.std(WWMatrix_N_raw[:,i])
    Std_agg[21, i] = np.std(WWMatrix_M_raw[:,i])
    Std_agg[22, i] = np.std(WWMatrix_T_raw[:,i])
    Std_agg[23, i] = np.std(SewMatrix_N_raw[:,i])
    Std_agg[24, i] = np.std(SewMatrix_M_raw[:,i])
    Std_agg[25, i] = np.std(SewMatrix_T_raw[:,i])
    Std_agg[26, i] = np.std(WWTPMatrix_N_raw[:,i])
    Std_agg[27, i] = np.std(WWTPMatrix_M_raw[:,i])
    Std_agg[28, i] = np.std(WWTPMatrix_T_raw[:,i])
    Std_agg[29, i] = np.std(OSTreatMatrix_N_raw[:,i])
    Std_agg[30, i] = np.std(OSTreatMatrix_M_raw[:,i])
    Std_agg[31, i] = np.std(OSTreatMatrix_T_raw[:,i])
    Std_agg[32, i] = np.std(OSSludMatrix_N_raw[:,i])
    Std_agg[33, i] = np.std(OSSludMatrix_M_raw[:,i])
    Std_agg[34, i] = np.std(OSSludMatrix_T_raw[:,i])
    Std_agg[35, i] = np.std(SubsurfMatrix_N_raw[:,i])
    Std_agg[36, i] = np.std(SubsurfMatrix_M_raw[:,i])
    Std_agg[37, i] = np.std(SubsurfMatrix_T_raw[:,i])
    Std_agg[38, i] = np.std(ReusMatrix_N_raw[:,i])
    Std_agg[39, i] = np.std(ReusMatrix_T_raw[:,i])
    Std_agg[40, i] = np.std(ReusMatrix_P_raw[:,i])
    Std_agg[41, i] = np.std(WIPMatrix_N_raw[:,i])
    Std_agg[42, i] = np.std(WIPMatrix_M_raw[:,i])
    Std_agg[43, i] = np.std(WIPMatrix_T_raw[:,i])
    Std_agg[44, i] = np.std(WIPMatrix_P_raw[:,i])
    Std_agg[45, i] = np.std(LandfMatrix_N_raw[:,i])
    Std_agg[46, i] = np.std(LandfMatrix_M_raw[:,i])
    Std_agg[47, i] = np.std(LandfMatrix_T_raw[:,i])
    Std_agg[48, i] = np.std(LandfMatrix_P_raw[:,i])
    Std_agg[49, i] = np.std(AirMatrix_N_raw[:,i])
    Std_agg[50, i] = np.std(AirMatrix_M_raw[:,i])
    Std_agg[51, i] = np.std(AirMatrix_T_raw[:,i])
    Std_agg[52, i] = np.std(NUSoilMatrix_N_raw[:,i])
    Std_agg[53, i] = np.std(NUSoilMatrix_M_raw[:,i])
    Std_agg[54, i] = np.std(STSoilMatrix_N_raw[:,i])
    Std_agg[55, i] = np.std(STSoilMatrix_M_raw[:,i])
    Std_agg[56, i] = np.std(STSoilMatrix_T_raw[:,i])
    Std_agg[57, i] = np.std(SurfWatMatrix_N_raw[:,i])
    Std_agg[58, i] = np.std(SurfWatMatrix_M_raw[:,i])
    Std_agg[59, i] = np.std(SurfWatMatrix_T_raw[:,i])
    
    RelUnc_agg[0, i] = np.std(ImpoMatrix_raw[:,i])/np.mean(ImpoMatrix_raw[:,i])
    RelUnc_agg[1, i] = np.std(ProdMatrix_raw[:,i])/np.mean(ProdMatrix_raw[:,i])
    RelUnc_agg[2, i] = np.std(ManufMatrix_raw[:,i])/np.mean(ManufMatrix_raw[:,i])
    RelUnc_agg[3, i] = np.std(ConsMatrix_raw[:,i])/np.mean(ConsMatrix_raw[:,i])
    RelUnc_agg[4, i] = np.std(WWMatrix_raw[:,i])/np.mean(WWMatrix_raw[:,i])
    RelUnc_agg[5, i] = np.std(SewMatrix_raw[:,i])/np.mean(SewMatrix_raw[:,i])
    RelUnc_agg[6, i] = np.std(WWTPMatrix_raw[:,i])/np.mean(WWTPMatrix_raw[:,i])
    RelUnc_agg[7, i] = np.std(OSTreatMatrix_raw[:,i])/np.mean(OSTreatMatrix_raw[:,i])
    RelUnc_agg[8, i] = np.std(OSSludMatrix_raw[:,i])/np.mean(OSSludMatrix_raw[:,i])
    RelUnc_agg[9, i] = np.std(SubsurfMatrix_raw[:,i])/np.mean(SubsurfMatrix_raw[:,i])
    RelUnc_agg[10, i] = np.std(SortMatrix_raw[:,i])/np.mean(SortMatrix_raw[:,i])
    RelUnc_agg[11, i] = np.std(ReprMatrix_raw[:,i])/np.mean(ReprMatrix_raw[:,i])
    RelUnc_agg[12, i] = np.std(ReusMatrix_raw[:,i])/np.mean(ReusMatrix_raw[:,i])
    RelUnc_agg[13, i] = np.std(WIPMatrix_raw[:,i])/np.mean(WIPMatrix_raw[:,i])
    RelUnc_agg[14, i] = np.std(LandfMatrix_raw[:,i])/np.mean(LandfMatrix_raw[:,i])
    RelUnc_agg[15, i] = np.std(ExpMatrix_raw[:,i])/np.mean(ExpMatrix_raw[:,i])
    RelUnc_agg[16, i] = np.std(AirMatrix_raw[:,i])/np.mean(AirMatrix_raw[:,i])
    RelUnc_agg[17, i] = np.std(NUSoilMatrix_raw[:,i])/np.mean(NUSoilMatrix_raw[:,i])
    RelUnc_agg[18, i] = np.std(STSoilMatrix_raw[:,i])/np.mean(STSoilMatrix_raw[:,i])
    RelUnc_agg[19, i] = np.std(SurfWatMatrix_raw[:,i])/np.mean(SurfWatMatrix_raw[:,i])
    RelUnc_agg[20, i] = np.std(WWMatrix_N_raw[:,i])/np.mean(WWMatrix_N_raw[:,i])
    RelUnc_agg[21, i] = np.std(WWMatrix_M_raw[:,i])/np.mean(WWMatrix_M_raw[:,i])
    RelUnc_agg[22, i] = np.std(WWMatrix_T_raw[:,i])/np.mean(WWMatrix_T_raw[:,i])
    RelUnc_agg[23, i] = np.std(SewMatrix_N_raw[:,i])/np.mean(SewMatrix_N_raw[:,i])
    RelUnc_agg[24, i] = np.std(SewMatrix_M_raw[:,i])/np.mean(SewMatrix_M_raw[:,i])
    RelUnc_agg[25, i] = np.std(SewMatrix_T_raw[:,i])/np.mean(SewMatrix_T_raw[:,i])
    RelUnc_agg[26, i] = np.std(WWTPMatrix_N_raw[:,i])/np.mean(WWTPMatrix_N_raw[:,i])
    RelUnc_agg[27, i] = np.std(WWTPMatrix_M_raw[:,i])/np.mean(WWTPMatrix_M_raw[:,i])
    RelUnc_agg[28, i] = np.std(WWTPMatrix_T_raw[:,i])/np.mean(WWTPMatrix_T_raw[:,i])
    RelUnc_agg[29, i] = np.std(OSTreatMatrix_N_raw[:,i])/np.mean(OSTreatMatrix_N_raw[:,i])
    RelUnc_agg[30, i] = np.std(OSTreatMatrix_M_raw[:,i])/np.mean(OSTreatMatrix_M_raw[:,i])
    RelUnc_agg[31, i] = np.std(OSTreatMatrix_T_raw[:,i])/np.mean(OSTreatMatrix_T_raw[:,i])
    RelUnc_agg[32, i] = np.std(OSSludMatrix_N_raw[:,i])/np.mean(OSSludMatrix_N_raw[:,i])
    RelUnc_agg[33, i] = np.std(OSSludMatrix_M_raw[:,i])/np.mean(OSSludMatrix_M_raw[:,i])
    RelUnc_agg[34, i] = np.std(OSSludMatrix_T_raw[:,i])/np.mean(OSSludMatrix_T_raw[:,i])
    RelUnc_agg[35, i] = np.std(SubsurfMatrix_N_raw[:,i])/np.mean(SubsurfMatrix_N_raw[:,i])
    RelUnc_agg[36, i] = np.std(SubsurfMatrix_M_raw[:,i])/np.mean(SubsurfMatrix_M_raw[:,i])
    RelUnc_agg[37, i] = np.std(SubsurfMatrix_T_raw[:,i])/np.mean(SubsurfMatrix_T_raw[:,i])
    RelUnc_agg[38, i] = np.std(ReusMatrix_N_raw[:,i])/np.mean(ReusMatrix_N_raw[:,i])
    RelUnc_agg[39, i] = np.std(ReusMatrix_T_raw[:,i])/np.mean(ReusMatrix_T_raw[:,i])
    RelUnc_agg[40, i] = np.std(ReusMatrix_P_raw[:,i])/np.mean(ReusMatrix_P_raw[:,i])
    RelUnc_agg[41, i] = np.std(WIPMatrix_N_raw[:,i])/np.mean(WIPMatrix_N_raw[:,i])
    RelUnc_agg[42, i] = np.std(WIPMatrix_M_raw[:,i])/np.mean(WIPMatrix_M_raw[:,i])
    RelUnc_agg[43, i] = np.std(WIPMatrix_T_raw[:,i])/np.mean(WIPMatrix_T_raw[:,i])
    RelUnc_agg[44, i] = np.std(WIPMatrix_P_raw[:,i])/np.mean(WIPMatrix_P_raw[:,i])
    RelUnc_agg[45, i] = np.std(LandfMatrix_N_raw[:,i])/np.mean(LandfMatrix_N_raw[:,i])
    RelUnc_agg[46, i] = np.std(LandfMatrix_M_raw[:,i])/np.mean(LandfMatrix_M_raw[:,i])
    RelUnc_agg[47, i] = np.std(LandfMatrix_T_raw[:,i])/np.mean(LandfMatrix_T_raw[:,i])
    RelUnc_agg[48, i] = np.std(LandfMatrix_P_raw[:,i])/np.mean(LandfMatrix_P_raw[:,i])
    RelUnc_agg[49, i] = np.std(AirMatrix_N_raw[:,i])/np.mean(AirMatrix_N_raw[:,i])
    RelUnc_agg[50, i] = np.std(AirMatrix_M_raw[:,i])/np.mean(AirMatrix_M_raw[:,i])
    RelUnc_agg[51, i] = np.std(AirMatrix_T_raw[:,i])/np.mean(AirMatrix_T_raw[:,i])
    RelUnc_agg[52, i] = np.std(NUSoilMatrix_N_raw[:,i])/np.mean(NUSoilMatrix_N_raw[:,i])
    RelUnc_agg[53, i] = np.std(NUSoilMatrix_M_raw[:,i])/np.mean(NUSoilMatrix_M_raw[:,i])
    RelUnc_agg[54, i] = np.std(STSoilMatrix_N_raw[:,i])/np.mean(STSoilMatrix_N_raw[:,i])
    RelUnc_agg[55, i] = np.std(STSoilMatrix_M_raw[:,i])/np.mean(STSoilMatrix_M_raw[:,i])
    RelUnc_agg[56, i] = np.std(STSoilMatrix_T_raw[:,i])/np.mean(STSoilMatrix_T_raw[:,i])
    RelUnc_agg[57, i] = np.std(SurfWatMatrix_N_raw[:,i])/np.mean(SurfWatMatrix_N_raw[:,i])
    RelUnc_agg[58, i] = np.std(SurfWatMatrix_M_raw[:,i])/np.mean(SurfWatMatrix_M_raw[:,i])
    RelUnc_agg[59, i] = np.std(SurfWatMatrix_T_raw[:,i])/np.mean(SurfWatMatrix_T_raw[:,i])
    


# In[41]:


Mean_agg


# In[42]:


Mean_agg = pd.DataFrame({'Mean Import':Mean_agg[0,:], 
                            'Mean to Production':Mean_agg[1,:], 
                            'Mean to Manufacturing':Mean_agg[2,:], 
                            'Mean to Consumption':Mean_agg[3,:], 
                            'Mean to Wastewater':Mean_agg[4,:], 
                            'Mean to Sewage system':Mean_agg[5,:], 
                            'Mean to WWTP':Mean_agg[6,:], 
                            'Mean to On-site treatment':Mean_agg[7,:], 
                            'Mean to On-site sludge':Mean_agg[8,:], 
                            'Mean to Subsurface':Mean_agg[9,:],
                            'Mean to Sorting':Mean_agg[10,:], 
                            'Mean to Reprocessing':Mean_agg[11,:], 
                            'Mean to Reuse':Mean_agg[12,:],
                            'Mean to WIP':Mean_agg[13,:], 
                            'Mean to Landfill':Mean_agg[14,:], 
                            'Mean to Export':Mean_agg[15,:], 
                            'Mean to Air':Mean_agg[16,:], 
                            'Mean to NU Soil':Mean_agg[17,:], 
                            'Mean to ST Soil':Mean_agg[18,:], 
                            'Mean to Surface water':Mean_agg[19,:],
                            'Mean Pristine to Wastewater':Mean_agg[20,:],
                            'Mean Matrix-embedded to Wastewater':Mean_agg[21,:],
                            'Mean Transformed to Wastewater':Mean_agg[22,:],
                            'Mean Pristine to Sewer':Mean_agg[23,:],
                            'Mean Matrix-embedded to Sewer':Mean_agg[24,:],
                            'Mean Transformed to Sewer':Mean_agg[25,:],
                            'Mean Pristine to WWTP':Mean_agg[26,:], 
                            'Mean Matrix-embedded to WWTP':Mean_agg[27,:], 
                            'Mean Transformed to WWTP':Mean_agg[28,:], 
                            'Mean Pristine to On-site treatment':Mean_agg[29,:],
                            'Mean Matrix-embedded to On-site treatment':Mean_agg[30,:],
                            'Mean Transformed to On-site treatment':Mean_agg[31,:],
                            'Mean Pristine to On-site sludge':Mean_agg[32,:],
                            'Mean Matrix-embedded to On-site sludge':Mean_agg[33,:],
                            'Mean Transformed to On-site sludge':Mean_agg[34,:],
                            'Mean Pristine to Subsurface':Mean_agg[35,:],
                            'Mean Matrix-embedded to Subsurface':Mean_agg[36,:],
                            'Mean Transformed to Subsurface':Mean_agg[37,:], 
                            'Mean Pristine to Reuse':Mean_agg[38,:],
                            'Mean Transformed to Reuse':Mean_agg[39,:],
                            'Mean Product-embedded to Reuse':Mean_agg[40,:],
                            'Mean Pristine to WIP':Mean_agg[41,:],
                            'Mean Matrix-embedded to WIP':Mean_agg[42,:],
                            'Mean Transformed to WIP':Mean_agg[43,:],
                            'Mean Product-embedded to WIP':Mean_agg[44,:],
                            'Mean Pristine to Landfill':Mean_agg[45,:],
                            'Mean Matrix-embedded to Landfill':Mean_agg[46,:],
                            'Mean Transformed to Landfill':Mean_agg[47,:],
                            'Mean Product-embedded to Landfill':Mean_agg[48,:], 
                            'Mean Pristine to Air':Mean_agg[49,:],
                            'Mean Matrix-embedded to Air':Mean_agg[50,:],
                            'Mean Transformed to Air':Mean_agg[51,:], 
                            'Mean Pristine to NU Soil':Mean_agg[52,:],
                            'Mean Matrix-embedded to NU Soil':Mean_agg[53,:], 
                            'Mean Pristine to ST Soil':Mean_agg[54,:], 
                            'Mean Matrix-embedded to ST Soil':Mean_agg[55,:], 
                            'Mean Transformed to ST Soil':Mean_agg[56,:],
                            'Mean Pristine to Surface water':Mean_agg[57,:],
                            'Mean Matrix-embedded to Surface water':Mean_agg[58,:], 
                            'Mean Transformed to Surface water':Mean_agg[59,:]})
Mean_agg.to_csv('Means of totals to compartments - TiO2 - AUT_2.csv', index = False, sep=' ')

SD_agg = pd.DataFrame({'Std Import':Std_agg[0,:],
                            'Std to Production':Std_agg[1,:],
                            'Std to Manufacturing':Std_agg[2,:],
                            'Std to Consumption':Std_agg[3,:],
                            'Std to Wastewater':Std_agg[4,:],
                            'Std to Sewage system':Std_agg[5,:],
                            'Std to WWTP':Std_agg[6,:],
                            'Std to On-site treatment':Std_agg[7,:],
                            'Std to On-site sludge':Std_agg[8,:],
                            'Std to Subsurface':Std_agg[9,:],
                            'Std to Sorting':Std_agg[10,:],
                            'Std to Reprocessing':Std_agg[11,:],
                            'Std to Reprocessing':Std_agg[12,:],
                            'Std to WIP':Std_agg[13,:],
                            'Std to Landfill':Std_agg[14,:],
                            'Std to Export':Std_agg[15,:],
                            'Std to Air':Std_agg[16,:],
                            'Std to NU Soil':Std_agg[17,:],
                            'Std to ST Soil':Std_agg[18,:],
                            'Std to Surface water':Std_agg[19,:],
                            'Std Pristine to Wastewater':Std_agg[20,:],
                            'Std Matrix-embedded to Wastewater':Std_agg[21,:],
                            'Std Transformed to Wastewater':Std_agg[22,:],
                            'Std Pristine to Sewer':Std_agg[23,:],
                            'Std Matrix-embedded to Sewer':Std_agg[24,:],
                            'Std Transformed to Sewer':Std_agg[25,:],
                            'Std Pristine to WWTP':Std_agg[26,:],
                            'Std Matrix-embedded to WWTP':Std_agg[27,:],
                            'Std Transformed to WWTP':Std_agg[28,:],
                            'Std Pristine to On-site treatment':Std_agg[29,:],
                            'Std Matrix-embedded to On-site treatment':Std_agg[30,:],
                            'Std Transformed to On-site treatment':Std_agg[31,:],
                            'Std Pristine to On-site sludge':Std_agg[32,:],
                            'Std Matrix-embedded to On-site sludge':Std_agg[33,:],
                            'Std Transformed to On-site sludge':Std_agg[34,:],
                            'Std Pristine to Subsurface':Std_agg[35,:],
                            'Std Matrix-embedded to Subsurface':Std_agg[36,:],
                            'Std Transformed to Subsurface':Std_agg[37,:],
                            'Std Pristine to Reuse':Std_agg[38,:],
                            'Std Transformed to Reuse':Std_agg[39,:],
                            'Std Product-embedded to Reuse':Std_agg[40,:],
                            'Std Pristine to WIP':Std_agg[41,:],
                            'Std Matrix-embedded to WIP':Std_agg[42,:],
                            'Std Transformed to WIP':Std_agg[43,:],
                            'Std Product-embedded to WIP':Std_agg[44,:],
                            'Std Pristine to Landfill':Std_agg[45,:],
                            'Std Matrix-embedded to Landfill':Std_agg[46,:],
                            'Std Transformed to Landfill':Std_agg[47,:],
                            'Std Product-embedded to Landfill':Std_agg[48,:],
                            'Std Pristine to Air':Std_agg[49,:],
                            'Std Matrix-embedded to Air':Std_agg[50,:],
                            'Std Transformed to Air':Std_agg[51,:],
                            'Std Pristine to NU Soil':Std_agg[52,:],
                            'Std Matrix-embedded to NU Soil':Std_agg[53,:],
                            'Std Pristine to ST Soil':Std_agg[54,:],
                            'Std Matrix-embedded to ST Soil':Std_agg[55,:],
                            'Std Transformed to ST Soil':Std_agg[56,:],
                            'Std Pristine to Surface water':Std_agg[57,:],
                            'Std Matrix-embedded to Surface water':Std_agg[58,:],
                            'Std Transformed to Surface water':Std_agg[59,:]})
SD_agg.to_csv('Std of totals to compartments - TiO2 - AUT_2.csv', index = False, sep=' ')


RelUnc_agg = pd.DataFrame({'Import':RelUnc_agg[0,:],
                           'Production':RelUnc_agg[1,:],
                           'Manufacturing':RelUnc_agg[2,:],
                           'Consumption':RelUnc_agg[3,:],
                           'Wastewater':RelUnc_agg[4,:],
                           'Sewage system':RelUnc_agg[5,:],
                           'WWTP':RelUnc_agg[6,:],
                           'On-site treatment':RelUnc_agg[7,:],
                           'On-site sludge':RelUnc_agg[8,:],
                           'Subsurface':RelUnc_agg[9,:],
                           'Sorting':RelUnc_agg[10,:],
                           'Reprocessing':RelUnc_agg[11,:],
                           'Reuse':RelUnc_agg[12,:],
                           'WIP':RelUnc_agg[13,:],
                           'Landfill':RelUnc_agg[14,:],
                           'Export':RelUnc_agg[15,:],
                           'Air':RelUnc_agg[16,:],
                           'NU Soil':RelUnc_agg[17,:],
                           'ST Soil':RelUnc_agg[18,:],
                           'Surface water':RelUnc_agg[19,:],
                           'Pristine to Wastewater':RelUnc_agg[20,:],
                           'Matrix-embedded to Wastewater':RelUnc_agg[21,:],
                           'Transformed to Wastewater':RelUnc_agg[22,:],
                           'Pristine to Sewer':RelUnc_agg[23,:],
                           'Matrix-embedded to Sewer':RelUnc_agg[24,:],
                           'Transformed to Sewer':RelUnc_agg[25,:],
                           'Pristine to WWTP':RelUnc_agg[26,:],
                           'Matrix-embedded to WWTP':RelUnc_agg[27,:],
                           'Transformed to WWTP':RelUnc_agg[28,:],
                           'Pristine to On-site treatment':RelUnc_agg[29,:],
                           'Matrix-embedded to On-site treatment':RelUnc_agg[30,:],
                           'Transformed to On-site treatment':RelUnc_agg[31,:],
                           'Pristine to On-site sludge':RelUnc_agg[32,:],
                           'Matrix-embedded to On-site sludge':RelUnc_agg[33,:],
                           'Transformed to On-site sludge':RelUnc_agg[34,:],
                           'Pristine to Subsurface':RelUnc_agg[35,:],
                           'Matrix-embedded to Subsurface':RelUnc_agg[36,:],
                           'Transformed to Subsurface':RelUnc_agg[37,:],
                           'Pristine to Reuse':RelUnc_agg[38,:],
                           'Transformed to Reuse':RelUnc_agg[39,:],
                           'Product-embedded to Reuse':RelUnc_agg[40,:],
                           'Pristine to WIP':RelUnc_agg[41,:],
                           'Matrix-embedded to WIP':RelUnc_agg[42,:],
                           'Transformed to WIP':RelUnc_agg[43,:],
                           'Product-embedded to WIP':RelUnc_agg[44,:],
                           'Pristine to Landfill':RelUnc_agg[45,:],
                           'Matrix-embedded to Landfill':RelUnc_agg[46,:],
                           'Transformed to Landfill':RelUnc_agg[47,:],
                           'Product-embedded to Landfill':RelUnc_agg[48,:],
                           'Pristine to Air':RelUnc_agg[49,:],
                           'Matrix-embedded to Air':RelUnc_agg[50,:],
                           'Transformed to Air':RelUnc_agg[51,:],
                           'Pristine to NU Soil':RelUnc_agg[52,:],
                           'Matrix-embedded to NU Soil':RelUnc_agg[53,:],
                           'Pristine to ST Soil':RelUnc_agg[54,:],
                           'Matrix-embedded to ST Soil':RelUnc_agg[55,:],
                           'Transformed to ST Soil':RelUnc_agg[56,:],
                           'Pristine to Surface water':RelUnc_agg[57,:],
                           'Matrix-embedded to Surface water':RelUnc_agg[58,:],
                           'Transformed to Surface water':RelUnc_agg[59,:]})
RelUnc_agg.to_csv('Relative uncertainties of totals to compartments - TiO2 - AUT_2.csv', index = False, sep=' ')


# In[43]:


# Get fifth percentiles

Q5_agg = np.zeros(shape=(60, Tperiods))
for i in np.arange(0,Tperiods):
    Q5_agg[0, i] = np.percentile(ImpoMatrix_raw[:,i], 5)
    Q5_agg[1, i] = np.percentile(ProdMatrix_raw[:,i], 5)
    Q5_agg[2, i] = np.percentile(ManufMatrix_raw[:,i], 5)
    Q5_agg[3, i] = np.percentile(ConsMatrix_raw[:,i], 5)
    Q5_agg[4, i] = np.percentile(WWMatrix_raw[:,i], 5)
    Q5_agg[5, i] = np.percentile(SewMatrix_raw[:,i], 5)
    Q5_agg[6, i] = np.percentile(WWTPMatrix_raw[:,i], 5)
    Q5_agg[7, i] = np.percentile(OSTreatMatrix_raw[:,i], 5)
    Q5_agg[8, i] = np.percentile(OSSludMatrix_raw[:,i], 5)
    Q5_agg[9, i] = np.percentile(SubsurfMatrix_raw[:,i], 5)
    Q5_agg[10, i] = np.percentile(SortMatrix_raw[:,i], 5)
    Q5_agg[11, i] = np.percentile(ReprMatrix_raw[:,i], 5)
    Q5_agg[12, i] = np.percentile(ReusMatrix_raw[:,i], 5)
    Q5_agg[13, i] = np.percentile(WIPMatrix_raw[:,i], 5)
    Q5_agg[14, i] = np.percentile(LandfMatrix_raw[:,i], 5)
    Q5_agg[15, i] = np.percentile(ExpMatrix_raw[:,i], 5)
    Q5_agg[16, i] = np.percentile(AirMatrix_raw[:,i], 5)
    Q5_agg[17, i] = np.percentile(NUSoilMatrix_raw[:,i], 5)
    Q5_agg[18, i] = np.percentile(STSoilMatrix_raw[:,i], 5)
    Q5_agg[19, i] = np.percentile(SurfWatMatrix_raw[:,i], 5)
    Q5_agg[20, i] = np.percentile(WWMatrix_N_raw[:,i], 5)
    Q5_agg[21, i] = np.percentile(WWMatrix_M_raw[:,i], 5)
    Q5_agg[22, i] = np.percentile(WWMatrix_T_raw[:,i], 5)
    Q5_agg[23, i] = np.percentile(SewMatrix_N_raw[:,i], 5)
    Q5_agg[24, i] = np.percentile(SewMatrix_M_raw[:,i], 5)
    Q5_agg[25, i] = np.percentile(SewMatrix_T_raw[:,i], 5)
    Q5_agg[26, i] = np.percentile(WWTPMatrix_N_raw[:,i], 5)
    Q5_agg[27, i] = np.percentile(WWTPMatrix_M_raw[:,i], 5)
    Q5_agg[28, i] = np.percentile(WWTPMatrix_T_raw[:,i], 5)
    Q5_agg[29, i] = np.percentile(OSTreatMatrix_N_raw[:,i], 5)
    Q5_agg[30, i] = np.percentile(OSTreatMatrix_M_raw[:,i], 5)
    Q5_agg[31, i] = np.percentile(OSTreatMatrix_T_raw[:,i], 5)
    Q5_agg[32, i] = np.percentile(OSSludMatrix_N_raw[:,i], 5)
    Q5_agg[33, i] = np.percentile(OSSludMatrix_M_raw[:,i], 5)
    Q5_agg[34, i] = np.percentile(OSSludMatrix_T_raw[:,i], 5)
    Q5_agg[35, i] = np.percentile(SubsurfMatrix_N_raw[:,i], 5)
    Q5_agg[36, i] = np.percentile(SubsurfMatrix_M_raw[:,i], 5)
    Q5_agg[37, i] = np.percentile(SubsurfMatrix_T_raw[:,i], 5)
    Q5_agg[38, i] = np.percentile(ReusMatrix_N_raw[:,i], 5)
    Q5_agg[39, i] = np.percentile(ReusMatrix_T_raw[:,i], 5)
    Q5_agg[40, i] = np.percentile(ReusMatrix_P_raw[:,i], 5)
    Q5_agg[41, i] = np.percentile(WIPMatrix_N_raw[:,i], 5)
    Q5_agg[42, i] = np.percentile(WIPMatrix_M_raw[:,i], 5)
    Q5_agg[43, i] = np.percentile(WIPMatrix_T_raw[:,i], 5)
    Q5_agg[44, i] = np.percentile(WIPMatrix_P_raw[:,i], 5)
    Q5_agg[45, i] = np.percentile(LandfMatrix_N_raw[:,i], 5)
    Q5_agg[46, i] = np.percentile(LandfMatrix_M_raw[:,i], 5)
    Q5_agg[47, i] = np.percentile(LandfMatrix_T_raw[:,i], 5)
    Q5_agg[48, i] = np.percentile(LandfMatrix_P_raw[:,i], 5)
    Q5_agg[49, i] = np.percentile(AirMatrix_N_raw[:,i], 5)
    Q5_agg[50, i] = np.percentile(AirMatrix_M_raw[:,i], 5)
    Q5_agg[51, i] = np.percentile(AirMatrix_T_raw[:,i], 5)
    Q5_agg[52, i] = np.percentile(NUSoilMatrix_N_raw[:,i], 5)
    Q5_agg[53, i] = np.percentile(NUSoilMatrix_M_raw[:,i], 5)
    Q5_agg[54, i] = np.percentile(STSoilMatrix_N_raw[:,i], 5)
    Q5_agg[55, i] = np.percentile(STSoilMatrix_M_raw[:,i], 5)
    Q5_agg[56, i] = np.percentile(STSoilMatrix_T_raw[:,i], 5)
    Q5_agg[57, i] = np.percentile(SurfWatMatrix_N_raw[:,i], 5)
    Q5_agg[58, i] = np.percentile(SurfWatMatrix_M_raw[:,i], 5)
    Q5_agg[59, i] = np.percentile(SurfWatMatrix_T_raw[:,i], 5)
    
Q5_agg = pd.DataFrame({'Import':Q5_agg[0,:],
                       'Production':Q5_agg[1,:],
                       'Manufacturing':Q5_agg[2,:],
                       'Consumption':Q5_agg[3,:],
                       'Wastewater':Q5_agg[4,:],
                       'Sewage system':Q5_agg[5,:],
                       'WWTP':Q5_agg[6,:],
                       'On-site treatment':Q5_agg[7,:],
                       'On-site sludge':Q5_agg[8,:],
                       'Subsurface':Q5_agg[9,:],
                       'Sorting':Q5_agg[10,:],
                       'Reprocessing':Q5_agg[11,:],
                       'Reuse':Q5_agg[12,:],
                       'WIP':Q5_agg[13,:],
                       'Landfill':Q5_agg[14,:],
                       'Export':Q5_agg[15,:],
                       'Air':Q5_agg[16,:],
                       'NU Soil':Q5_agg[17,:],
                       'ST Soil':Q5_agg[18,:],
                       'Surface water':Q5_agg[19,:],
                       'Pristine to Wastewater':Q5_agg[20,:],
                       'Matrix-embedded to Wastewater':Q5_agg[21,:],
                       'Transformed to Wastewater':Q5_agg[22,:],
                       'Pristine to Sewer':Q5_agg[23,:],
                       'Matrix-embedded to Sewer':Q5_agg[24,:],
                       'Transformed to Sewer':Q5_agg[25,:],
                       'Pristine to WWTP':Q5_agg[26,:], 
                       'Matrix-embedded to WWTP':Q5_agg[27,:],
                       'Transformed to WWTP':Q5_agg[28,:],
                       'Pristine to On-site treatment':Q5_agg[29,:],
                       'Matrix-embedded to On-site treatment':Q5_agg[30,:],
                       'Transformed to On-site treatment':Q5_agg[31,:],
                       'Pristine to On-site sludge':Q5_agg[32,:], 
                       'Matrix-embedded to On-site sludge':Q5_agg[33,:],
                       'Transformed to On-site sludge':Q5_agg[34,:],
                       'Pristine to Subsurface':Q5_agg[35,:],
                       'Matrix-embedded to Subsurface':Q5_agg[36,:],
                       'Transformed to Subsurface':Q5_agg[37,:],
                       'Pristine to Reuse':Q5_agg[38,:],
                       'Transformed to Reuse':Q5_agg[39,:],
                       'Product-embedded to Reuse':Q5_agg[40,:],
                       'Pristine to WIP':Q5_agg[41,:], 
                       'Matrix-embedded to WIP':Q5_agg[42,:],
                       'Transformed to WIP':Q5_agg[43,:],
                       'Product-embedded to WIP':Q5_agg[44,:],
                       'Pristine to Landfill':Q5_agg[45,:],
                       'Matrix-embedded to Landfill':Q5_agg[46,:],
                       'Transformed to Landfill':Q5_agg[47,:],
                       'Product-embedded to Landfill':Q5_agg[48,:],
                       'Pristine to Air':Q5_agg[49,:],
                       'Matrix-embedded to Air':Q5_agg[50,:],
                       'Transformed to Air':Q5_agg[51,:],
                       'Pristine to NU Soil':Q5_agg[52,:],
                       'Matrix-embedded to NU Soil':Q5_agg[53,:],
                       'Pristine to ST Soil':Q5_agg[54,:], 
                       'Matrix-embedded to ST Soil':Q5_agg[55,:],
                       'Transformed to ST Soil':Q5_agg[56,:],
                       'Pristine to Surface water':Q5_agg[57,:],
                       'Matrix-embedded to Surface water':Q5_agg[58,:],
                       'Transformed to Surface water':Q5_agg[59,:]})
Q5_agg.to_csv('Q5 of totals to compartments - TiO2 - AUT_2.csv', index = False, sep=' ')


# In[44]:


# Get twenty-fifth percentiles

Q25_agg = np.zeros(shape=(60, Tperiods))
for i in np.arange(0,Tperiods):
    Q25_agg[0, i] = np.percentile(ImpoMatrix_raw[:,i], 25)
    Q25_agg[1, i] = np.percentile(ProdMatrix_raw[:,i], 25)
    Q25_agg[2, i] = np.percentile(ManufMatrix_raw[:,i], 25)
    Q25_agg[3, i] = np.percentile(ConsMatrix_raw[:,i], 25)
    Q25_agg[4, i] = np.percentile(WWMatrix_raw[:,i], 25)
    Q25_agg[5, i] = np.percentile(SewMatrix_raw[:,i], 25)
    Q25_agg[6, i] = np.percentile(WWTPMatrix_raw[:,i], 25)
    Q25_agg[7, i] = np.percentile(OSTreatMatrix_raw[:,i], 25)
    Q25_agg[8, i] = np.percentile(OSSludMatrix_raw[:,i], 25)
    Q25_agg[9, i] = np.percentile(SubsurfMatrix_raw[:,i], 25)
    Q25_agg[10, i] = np.percentile(SortMatrix_raw[:,i], 25)
    Q25_agg[11, i] = np.percentile(ReprMatrix_raw[:,i], 25)
    Q25_agg[12, i] = np.percentile(ReusMatrix_raw[:,i], 25)
    Q25_agg[13, i] = np.percentile(WIPMatrix_raw[:,i], 25)
    Q25_agg[14, i] = np.percentile(LandfMatrix_raw[:,i], 25)
    Q25_agg[15, i] = np.percentile(ExpMatrix_raw[:,i], 25)
    Q25_agg[16, i] = np.percentile(AirMatrix_raw[:,i], 25)
    Q25_agg[17, i] = np.percentile(NUSoilMatrix_raw[:,i], 25)
    Q25_agg[18, i] = np.percentile(STSoilMatrix_raw[:,i], 25)
    Q25_agg[19, i] = np.percentile(SurfWatMatrix_raw[:,i], 25)
    Q25_agg[20, i] = np.percentile(WWMatrix_N_raw[:,i], 25)
    Q25_agg[21, i] = np.percentile(WWMatrix_M_raw[:,i], 25)
    Q25_agg[22, i] = np.percentile(WWMatrix_T_raw[:,i], 25)
    Q25_agg[23, i] = np.percentile(SewMatrix_N_raw[:,i], 25)
    Q25_agg[24, i] = np.percentile(SewMatrix_M_raw[:,i], 25)
    Q25_agg[25, i] = np.percentile(SewMatrix_T_raw[:,i], 25)
    Q25_agg[26, i] = np.percentile(WWTPMatrix_N_raw[:,i], 25)
    Q25_agg[27, i] = np.percentile(WWTPMatrix_M_raw[:,i], 25)
    Q25_agg[28, i] = np.percentile(WWTPMatrix_T_raw[:,i], 25)
    Q25_agg[29, i] = np.percentile(OSTreatMatrix_N_raw[:,i], 25)
    Q25_agg[30, i] = np.percentile(OSTreatMatrix_M_raw[:,i], 25)
    Q25_agg[31, i] = np.percentile(OSTreatMatrix_T_raw[:,i], 25)
    Q25_agg[32, i] = np.percentile(OSSludMatrix_N_raw[:,i], 25)
    Q25_agg[33, i] = np.percentile(OSSludMatrix_M_raw[:,i], 25)
    Q25_agg[34, i] = np.percentile(OSSludMatrix_T_raw[:,i], 25)
    Q25_agg[35, i] = np.percentile(SubsurfMatrix_N_raw[:,i], 25)
    Q25_agg[36, i] = np.percentile(SubsurfMatrix_M_raw[:,i], 25)
    Q25_agg[37, i] = np.percentile(SubsurfMatrix_T_raw[:,i], 25)
    Q25_agg[38, i] = np.percentile(ReusMatrix_N_raw[:,i], 25)
    Q25_agg[39, i] = np.percentile(ReusMatrix_T_raw[:,i], 25)
    Q25_agg[40, i] = np.percentile(ReusMatrix_P_raw[:,i], 25)
    Q25_agg[41, i] = np.percentile(WIPMatrix_N_raw[:,i], 25)
    Q25_agg[42, i] = np.percentile(WIPMatrix_M_raw[:,i], 25)
    Q25_agg[43, i] = np.percentile(WIPMatrix_T_raw[:,i], 25)
    Q25_agg[44, i] = np.percentile(WIPMatrix_P_raw[:,i], 25)
    Q25_agg[45, i] = np.percentile(LandfMatrix_N_raw[:,i], 25)
    Q25_agg[46, i] = np.percentile(LandfMatrix_M_raw[:,i], 25)
    Q25_agg[47, i] = np.percentile(LandfMatrix_T_raw[:,i], 25)
    Q25_agg[48, i] = np.percentile(LandfMatrix_P_raw[:,i], 25)
    Q25_agg[49, i] = np.percentile(AirMatrix_N_raw[:,i], 25)
    Q25_agg[50, i] = np.percentile(AirMatrix_M_raw[:,i], 25)
    Q25_agg[51, i] = np.percentile(AirMatrix_T_raw[:,i], 25)
    Q25_agg[52, i] = np.percentile(NUSoilMatrix_N_raw[:,i], 25)
    Q25_agg[53, i] = np.percentile(NUSoilMatrix_M_raw[:,i], 25)
    Q25_agg[54, i] = np.percentile(STSoilMatrix_N_raw[:,i], 25)
    Q25_agg[55, i] = np.percentile(STSoilMatrix_M_raw[:,i], 25)
    Q25_agg[56, i] = np.percentile(STSoilMatrix_T_raw[:,i], 25)
    Q25_agg[57, i] = np.percentile(SurfWatMatrix_N_raw[:,i], 25)
    Q25_agg[58, i] = np.percentile(SurfWatMatrix_M_raw[:,i], 25)
    Q25_agg[59, i] = np.percentile(SurfWatMatrix_T_raw[:,i], 25)
    
Q25_agg = pd.DataFrame({'Import':Q25_agg[0,:],
                       'Production':Q25_agg[1,:],
                       'Manufacturing':Q25_agg[2,:],
                       'Consumption':Q25_agg[3,:],
                       'Wastewater':Q25_agg[4,:],
                       'Sewage system':Q25_agg[5,:],
                       'WWTP':Q25_agg[6,:],
                       'On-site treatment':Q25_agg[7,:],
                       'On-site sludge':Q25_agg[8,:],
                       'Subsurface':Q25_agg[9,:],
                       'Sorting':Q25_agg[10,:],
                       'Reprocessing':Q25_agg[11,:],
                       'Reuse':Q25_agg[12,:],
                       'WIP':Q25_agg[13,:],
                       'Landfill':Q25_agg[14,:],
                       'Export':Q25_agg[15,:],
                       'Air':Q25_agg[16,:],
                       'NU Soil':Q25_agg[17,:],
                       'ST Soil':Q25_agg[18,:],
                       'Surface water':Q25_agg[19,:],
                       'Pristine to Wastewater':Q25_agg[20,:],
                       'Matrix-embedded to Wastewater':Q25_agg[21,:],
                       'Transformed to Wastewater':Q25_agg[22,:],
                       'Pristine to Sewer':Q25_agg[23,:],
                       'Matrix-embedded to Sewer':Q25_agg[24,:],
                       'Transformed to Sewer':Q25_agg[25,:],
                       'Pristine to WWTP':Q25_agg[26,:], 
                       'Matrix-embedded to WWTP':Q25_agg[27,:],
                       'Transformed to WWTP':Q25_agg[28,:],
                       'Pristine to On-site treatment':Q25_agg[29,:],
                       'Matrix-embedded to On-site treatment':Q25_agg[30,:],
                       'Transformed to On-site treatment':Q25_agg[31,:],
                       'Pristine to On-site sludge':Q25_agg[32,:], 
                       'Matrix-embedded to On-site sludge':Q25_agg[33,:],
                       'Transformed to On-site sludge':Q25_agg[34,:],
                       'Pristine to Subsurface':Q25_agg[35,:],
                       'Matrix-embedded to Subsurface':Q25_agg[36,:],
                       'Transformed to Subsurface':Q25_agg[37,:],
                       'Pristine to Reuse':Q25_agg[38,:],
                       'Transformed to Reuse':Q25_agg[39,:],
                       'Product-embedded to Reuse':Q25_agg[40,:],
                       'Pristine to WIP':Q25_agg[41,:], 
                       'Matrix-embedded to WIP':Q25_agg[42,:],
                       'Transformed to WIP':Q25_agg[43,:],
                       'Product-embedded to WIP':Q25_agg[44,:],
                       'Pristine to Landfill':Q25_agg[45,:],
                       'Matrix-embedded to Landfill':Q25_agg[46,:],
                       'Transformed to Landfill':Q25_agg[47,:],
                       'Product-embedded to Landfill':Q25_agg[48,:],
                       'Pristine to Air':Q25_agg[49,:],
                       'Matrix-embedded to Air':Q25_agg[50,:],
                       'Transformed to Air':Q25_agg[51,:],
                       'Pristine to NU Soil':Q25_agg[52,:],
                       'Matrix-embedded to NU Soil':Q25_agg[53,:],
                       'Pristine to ST Soil':Q25_agg[54,:], 
                       'Matrix-embedded to ST Soil':Q25_agg[55,:],
                       'Transformed to ST Soil':Q25_agg[56,:],
                       'Pristine to Surface water':Q25_agg[57,:],
                       'Matrix-embedded to Surface water':Q25_agg[58,:],
                       'Transformed to Surface water':Q25_agg[59,:]})
Q25_agg.to_csv('Q25 of totals to compartments - TiO2 - AUT_2.csv', index = False, sep=' ')


# In[45]:


# Get medians

Q50_agg = np.zeros(shape=(60, Tperiods))
for i in np.arange(0,Tperiods):
    Q50_agg[0, i] = np.percentile(ImpoMatrix_raw[:,i], 50)
    Q50_agg[1, i] = np.percentile(ProdMatrix_raw[:,i], 50)
    Q50_agg[2, i] = np.percentile(ManufMatrix_raw[:,i], 50)
    Q50_agg[3, i] = np.percentile(ConsMatrix_raw[:,i], 50)
    Q50_agg[4, i] = np.percentile(WWMatrix_raw[:,i], 50)
    Q50_agg[5, i] = np.percentile(SewMatrix_raw[:,i], 50)
    Q50_agg[6, i] = np.percentile(WWTPMatrix_raw[:,i], 50)
    Q50_agg[7, i] = np.percentile(OSTreatMatrix_raw[:,i], 50)
    Q50_agg[8, i] = np.percentile(OSSludMatrix_raw[:,i], 50)
    Q50_agg[9, i] = np.percentile(SubsurfMatrix_raw[:,i], 50)
    Q50_agg[10, i] = np.percentile(SortMatrix_raw[:,i], 50)
    Q50_agg[11, i] = np.percentile(ReprMatrix_raw[:,i], 50)
    Q50_agg[12, i] = np.percentile(ReusMatrix_raw[:,i], 50)
    Q50_agg[13, i] = np.percentile(WIPMatrix_raw[:,i], 50)
    Q50_agg[14, i] = np.percentile(LandfMatrix_raw[:,i], 50)
    Q50_agg[15, i] = np.percentile(ExpMatrix_raw[:,i], 50)
    Q50_agg[16, i] = np.percentile(AirMatrix_raw[:,i], 50)
    Q50_agg[17, i] = np.percentile(NUSoilMatrix_raw[:,i], 50)
    Q50_agg[18, i] = np.percentile(STSoilMatrix_raw[:,i], 50)
    Q50_agg[19, i] = np.percentile(SurfWatMatrix_raw[:,i], 50)
    Q50_agg[20, i] = np.percentile(WWMatrix_N_raw[:,i], 50)
    Q50_agg[21, i] = np.percentile(WWMatrix_M_raw[:,i], 50)
    Q50_agg[22, i] = np.percentile(WWMatrix_T_raw[:,i], 50)
    Q50_agg[23, i] = np.percentile(SewMatrix_N_raw[:,i], 50)
    Q50_agg[24, i] = np.percentile(SewMatrix_M_raw[:,i], 50)
    Q50_agg[25, i] = np.percentile(SewMatrix_T_raw[:,i], 50)
    Q50_agg[26, i] = np.percentile(WWTPMatrix_N_raw[:,i], 50)
    Q50_agg[27, i] = np.percentile(WWTPMatrix_M_raw[:,i], 50)
    Q50_agg[28, i] = np.percentile(WWTPMatrix_T_raw[:,i], 50)
    Q50_agg[29, i] = np.percentile(OSTreatMatrix_N_raw[:,i], 50)
    Q50_agg[30, i] = np.percentile(OSTreatMatrix_M_raw[:,i], 50)
    Q50_agg[31, i] = np.percentile(OSTreatMatrix_T_raw[:,i], 50)
    Q50_agg[32, i] = np.percentile(OSSludMatrix_N_raw[:,i], 50)
    Q50_agg[33, i] = np.percentile(OSSludMatrix_M_raw[:,i], 50)
    Q50_agg[34, i] = np.percentile(OSSludMatrix_T_raw[:,i], 50)
    Q50_agg[35, i] = np.percentile(SubsurfMatrix_N_raw[:,i], 50)
    Q50_agg[36, i] = np.percentile(SubsurfMatrix_M_raw[:,i], 50)
    Q50_agg[37, i] = np.percentile(SubsurfMatrix_T_raw[:,i], 50)
    Q50_agg[38, i] = np.percentile(ReusMatrix_N_raw[:,i], 50)
    Q50_agg[39, i] = np.percentile(ReusMatrix_T_raw[:,i], 50)
    Q50_agg[40, i] = np.percentile(ReusMatrix_P_raw[:,i], 50)
    Q50_agg[41, i] = np.percentile(WIPMatrix_N_raw[:,i], 50)
    Q50_agg[42, i] = np.percentile(WIPMatrix_M_raw[:,i], 50)
    Q50_agg[43, i] = np.percentile(WIPMatrix_T_raw[:,i], 50)
    Q50_agg[44, i] = np.percentile(WIPMatrix_P_raw[:,i], 50)
    Q50_agg[45, i] = np.percentile(LandfMatrix_N_raw[:,i], 50)
    Q50_agg[46, i] = np.percentile(LandfMatrix_M_raw[:,i], 50)
    Q50_agg[47, i] = np.percentile(LandfMatrix_T_raw[:,i], 50)
    Q50_agg[48, i] = np.percentile(LandfMatrix_P_raw[:,i], 50)
    Q50_agg[49, i] = np.percentile(AirMatrix_N_raw[:,i], 50)
    Q50_agg[50, i] = np.percentile(AirMatrix_M_raw[:,i], 50)
    Q50_agg[51, i] = np.percentile(AirMatrix_T_raw[:,i], 50)
    Q50_agg[52, i] = np.percentile(NUSoilMatrix_N_raw[:,i], 50)
    Q50_agg[53, i] = np.percentile(NUSoilMatrix_M_raw[:,i], 50)
    Q50_agg[54, i] = np.percentile(STSoilMatrix_N_raw[:,i], 50)
    Q50_agg[55, i] = np.percentile(STSoilMatrix_M_raw[:,i], 50)
    Q50_agg[56, i] = np.percentile(STSoilMatrix_T_raw[:,i], 50)
    Q50_agg[57, i] = np.percentile(SurfWatMatrix_N_raw[:,i], 50)
    Q50_agg[58, i] = np.percentile(SurfWatMatrix_M_raw[:,i], 50)
    Q50_agg[59, i] = np.percentile(SurfWatMatrix_T_raw[:,i], 50)
    
Q50_agg = pd.DataFrame({'Import':Q50_agg[0,:],
                       'Production':Q50_agg[1,:],
                       'Manufacturing':Q50_agg[2,:],
                       'Consumption':Q50_agg[3,:],
                       'Wastewater':Q50_agg[4,:],
                       'Sewage system':Q50_agg[5,:],
                       'WWTP':Q50_agg[6,:],
                       'On-site treatment':Q50_agg[7,:],
                       'On-site sludge':Q50_agg[8,:],
                       'Subsurface':Q50_agg[9,:],
                       'Sorting':Q50_agg[10,:],
                       'Reprocessing':Q50_agg[11,:],
                       'Reuse':Q50_agg[12,:],
                       'WIP':Q50_agg[13,:],
                       'Landfill':Q50_agg[14,:],
                       'Export':Q50_agg[15,:],
                       'Air':Q50_agg[16,:],
                       'NU Soil':Q50_agg[17,:],
                       'ST Soil':Q50_agg[18,:],
                       'Surface water':Q50_agg[19,:],
                       'Pristine to Wastewater':Q50_agg[20,:],
                       'Matrix-embedded to Wastewater':Q50_agg[21,:],
                       'Transformed to Wastewater':Q50_agg[22,:],
                       'Pristine to Sewer':Q50_agg[23,:],
                       'Matrix-embedded to Sewer':Q50_agg[24,:],
                       'Transformed to Sewer':Q50_agg[25,:],
                       'Pristine to WWTP':Q50_agg[26,:], 
                       'Matrix-embedded to WWTP':Q50_agg[27,:],
                       'Transformed to WWTP':Q50_agg[28,:],
                       'Pristine to On-site treatment':Q50_agg[29,:],
                       'Matrix-embedded to On-site treatment':Q50_agg[30,:],
                       'Transformed to On-site treatment':Q50_agg[31,:],
                       'Pristine to On-site sludge':Q50_agg[32,:], 
                       'Matrix-embedded to On-site sludge':Q50_agg[33,:],
                       'Transformed to On-site sludge':Q50_agg[34,:],
                       'Pristine to Subsurface':Q50_agg[35,:],
                       'Matrix-embedded to Subsurface':Q50_agg[36,:],
                       'Transformed to Subsurface':Q50_agg[37,:],
                       'Pristine to Reuse':Q50_agg[38,:],
                       'Transformed to Reuse':Q50_agg[39,:],
                       'Product-embedded to Reuse':Q50_agg[40,:],
                       'Pristine to WIP':Q50_agg[41,:], 
                       'Matrix-embedded to WIP':Q50_agg[42,:],
                       'Transformed to WIP':Q50_agg[43,:],
                       'Product-embedded to WIP':Q50_agg[44,:],
                       'Pristine to Landfill':Q50_agg[45,:],
                       'Matrix-embedded to Landfill':Q50_agg[46,:],
                       'Transformed to Landfill':Q50_agg[47,:],
                       'Product-embedded to Landfill':Q50_agg[48,:],
                       'Pristine to Air':Q50_agg[49,:],
                       'Matrix-embedded to Air':Q50_agg[50,:],
                       'Transformed to Air':Q50_agg[51,:],
                       'Pristine to NU Soil':Q50_agg[52,:],
                       'Matrix-embedded to NU Soil':Q50_agg[53,:],
                       'Pristine to ST Soil':Q50_agg[54,:], 
                       'Matrix-embedded to ST Soil':Q50_agg[55,:],
                       'Transformed to ST Soil':Q50_agg[56,:],
                       'Pristine to Surface water':Q50_agg[57,:],
                       'Matrix-embedded to Surface water':Q50_agg[58,:],
                       'Transformed to Surface water':Q50_agg[59,:]})
Q50_agg.to_csv('Q50 of totals to compartments - TiO2 - AUT_2.csv', index = False, sep=' ')


# In[46]:


# Get seventy-fifth percentiles

Q75_agg = np.zeros(shape=(60, Tperiods))
for i in np.arange(0,Tperiods):
    Q75_agg[0, i] = np.percentile(ImpoMatrix_raw[:,i], 75)
    Q75_agg[1, i] = np.percentile(ProdMatrix_raw[:,i], 75)
    Q75_agg[2, i] = np.percentile(ManufMatrix_raw[:,i], 75)
    Q75_agg[3, i] = np.percentile(ConsMatrix_raw[:,i], 75)
    Q75_agg[4, i] = np.percentile(WWMatrix_raw[:,i], 75)
    Q75_agg[5, i] = np.percentile(SewMatrix_raw[:,i], 75)
    Q75_agg[6, i] = np.percentile(WWTPMatrix_raw[:,i], 75)
    Q75_agg[7, i] = np.percentile(OSTreatMatrix_raw[:,i], 75)
    Q75_agg[8, i] = np.percentile(OSSludMatrix_raw[:,i], 75)
    Q75_agg[9, i] = np.percentile(SubsurfMatrix_raw[:,i], 75)
    Q75_agg[10, i] = np.percentile(SortMatrix_raw[:,i], 75)
    Q75_agg[11, i] = np.percentile(ReprMatrix_raw[:,i], 75)
    Q75_agg[12, i] = np.percentile(ReusMatrix_raw[:,i], 75)
    Q75_agg[13, i] = np.percentile(WIPMatrix_raw[:,i], 75)
    Q75_agg[14, i] = np.percentile(LandfMatrix_raw[:,i], 75)
    Q75_agg[15, i] = np.percentile(ExpMatrix_raw[:,i], 75)
    Q75_agg[16, i] = np.percentile(AirMatrix_raw[:,i], 75)
    Q75_agg[17, i] = np.percentile(NUSoilMatrix_raw[:,i], 75)
    Q75_agg[18, i] = np.percentile(STSoilMatrix_raw[:,i], 75)
    Q75_agg[19, i] = np.percentile(SurfWatMatrix_raw[:,i], 75)
    Q75_agg[20, i] = np.percentile(WWMatrix_N_raw[:,i], 75)
    Q75_agg[21, i] = np.percentile(WWMatrix_M_raw[:,i], 75)
    Q75_agg[22, i] = np.percentile(WWMatrix_T_raw[:,i], 75)
    Q75_agg[23, i] = np.percentile(SewMatrix_N_raw[:,i], 75)
    Q75_agg[24, i] = np.percentile(SewMatrix_M_raw[:,i], 75)
    Q75_agg[25, i] = np.percentile(SewMatrix_T_raw[:,i], 75)
    Q75_agg[26, i] = np.percentile(WWTPMatrix_N_raw[:,i], 75)
    Q75_agg[27, i] = np.percentile(WWTPMatrix_M_raw[:,i], 75)
    Q75_agg[28, i] = np.percentile(WWTPMatrix_T_raw[:,i], 75)
    Q75_agg[29, i] = np.percentile(OSTreatMatrix_N_raw[:,i], 75)
    Q75_agg[30, i] = np.percentile(OSTreatMatrix_M_raw[:,i], 75)
    Q75_agg[31, i] = np.percentile(OSTreatMatrix_T_raw[:,i], 75)
    Q75_agg[32, i] = np.percentile(OSSludMatrix_N_raw[:,i], 75)
    Q75_agg[33, i] = np.percentile(OSSludMatrix_M_raw[:,i], 75)
    Q75_agg[34, i] = np.percentile(OSSludMatrix_T_raw[:,i], 75)
    Q75_agg[35, i] = np.percentile(SubsurfMatrix_N_raw[:,i], 75)
    Q75_agg[36, i] = np.percentile(SubsurfMatrix_M_raw[:,i], 75)
    Q75_agg[37, i] = np.percentile(SubsurfMatrix_T_raw[:,i], 75)
    Q75_agg[38, i] = np.percentile(ReusMatrix_N_raw[:,i], 75)
    Q75_agg[39, i] = np.percentile(ReusMatrix_T_raw[:,i], 75)
    Q75_agg[40, i] = np.percentile(ReusMatrix_P_raw[:,i], 75)
    Q75_agg[41, i] = np.percentile(WIPMatrix_N_raw[:,i], 75)
    Q75_agg[42, i] = np.percentile(WIPMatrix_M_raw[:,i], 75)
    Q75_agg[43, i] = np.percentile(WIPMatrix_T_raw[:,i], 75)
    Q75_agg[44, i] = np.percentile(WIPMatrix_P_raw[:,i], 75)
    Q75_agg[45, i] = np.percentile(LandfMatrix_N_raw[:,i], 75)
    Q75_agg[46, i] = np.percentile(LandfMatrix_M_raw[:,i], 75)
    Q75_agg[47, i] = np.percentile(LandfMatrix_T_raw[:,i], 75)
    Q75_agg[48, i] = np.percentile(LandfMatrix_P_raw[:,i], 75)
    Q75_agg[49, i] = np.percentile(AirMatrix_N_raw[:,i], 75)
    Q75_agg[50, i] = np.percentile(AirMatrix_M_raw[:,i], 75)
    Q75_agg[51, i] = np.percentile(AirMatrix_T_raw[:,i], 75)
    Q75_agg[52, i] = np.percentile(NUSoilMatrix_N_raw[:,i], 75)
    Q75_agg[53, i] = np.percentile(NUSoilMatrix_M_raw[:,i], 75)
    Q75_agg[54, i] = np.percentile(STSoilMatrix_N_raw[:,i], 75)
    Q75_agg[55, i] = np.percentile(STSoilMatrix_M_raw[:,i], 75)
    Q75_agg[56, i] = np.percentile(STSoilMatrix_T_raw[:,i], 75)
    Q75_agg[57, i] = np.percentile(SurfWatMatrix_N_raw[:,i], 75)
    Q75_agg[58, i] = np.percentile(SurfWatMatrix_M_raw[:,i], 75)
    Q75_agg[59, i] = np.percentile(SurfWatMatrix_T_raw[:,i], 75)
    
Q75_agg = pd.DataFrame({'Import':Q75_agg[0,:],
                       'Production':Q75_agg[1,:],
                       'Manufacturing':Q75_agg[2,:],
                       'Consumption':Q75_agg[3,:],
                       'Wastewater':Q75_agg[4,:],
                       'Sewage system':Q75_agg[5,:],
                       'WWTP':Q75_agg[6,:],
                       'On-site treatment':Q75_agg[7,:],
                       'On-site sludge':Q75_agg[8,:],
                       'Subsurface':Q75_agg[9,:],
                       'Sorting':Q75_agg[10,:],
                       'Reprocessing':Q75_agg[11,:],
                       'Reuse':Q75_agg[12,:],
                       'WIP':Q75_agg[13,:],
                       'Landfill':Q75_agg[14,:],
                       'Export':Q75_agg[15,:],
                       'Air':Q75_agg[16,:],
                       'NU Soil':Q75_agg[17,:],
                       'ST Soil':Q75_agg[18,:],
                       'Surface water':Q75_agg[19,:],
                       'Pristine to Wastewater':Q75_agg[20,:],
                       'Matrix-embedded to Wastewater':Q75_agg[21,:],
                       'Transformed to Wastewater':Q75_agg[22,:],
                       'Pristine to Sewer':Q75_agg[23,:],
                       'Matrix-embedded to Sewer':Q75_agg[24,:],
                       'Transformed to Sewer':Q75_agg[25,:],
                       'Pristine to WWTP':Q75_agg[26,:], 
                       'Matrix-embedded to WWTP':Q75_agg[27,:],
                       'Transformed to WWTP':Q75_agg[28,:],
                       'Pristine to On-site treatment':Q75_agg[29,:],
                       'Matrix-embedded to On-site treatment':Q75_agg[30,:],
                       'Transformed to On-site treatment':Q75_agg[31,:],
                       'Pristine to On-site sludge':Q75_agg[32,:], 
                       'Matrix-embedded to On-site sludge':Q75_agg[33,:],
                       'Transformed to On-site sludge':Q75_agg[34,:],
                       'Pristine to Subsurface':Q75_agg[35,:],
                       'Matrix-embedded to Subsurface':Q75_agg[36,:],
                       'Transformed to Subsurface':Q75_agg[37,:],
                       'Pristine to Reuse':Q75_agg[38,:],
                       'Transformed to Reuse':Q75_agg[39,:],
                       'Product-embedded to Reuse':Q75_agg[40,:],
                       'Pristine to WIP':Q75_agg[41,:], 
                       'Matrix-embedded to WIP':Q75_agg[42,:],
                       'Transformed to WIP':Q75_agg[43,:],
                       'Product-embedded to WIP':Q75_agg[44,:],
                       'Pristine to Landfill':Q75_agg[45,:],
                       'Matrix-embedded to Landfill':Q75_agg[46,:],
                       'Transformed to Landfill':Q75_agg[47,:],
                       'Product-embedded to Landfill':Q75_agg[48,:],
                       'Pristine to Air':Q75_agg[49,:],
                       'Matrix-embedded to Air':Q75_agg[50,:],
                       'Transformed to Air':Q75_agg[51,:],
                       'Pristine to NU Soil':Q75_agg[52,:],
                       'Matrix-embedded to NU Soil':Q75_agg[53,:],
                       'Pristine to ST Soil':Q75_agg[54,:], 
                       'Matrix-embedded to ST Soil':Q75_agg[55,:],
                       'Transformed to ST Soil':Q75_agg[56,:],
                       'Pristine to Surface water':Q75_agg[57,:],
                       'Matrix-embedded to Surface water':Q75_agg[58,:],
                       'Transformed to Surface water':Q75_agg[59,:]})
Q75_agg.to_csv('Q75 of totals to compartments - TiO2 - AUT_2.csv', index = False, sep=' ')


# In[47]:


# Get ninety-fifth percentiles

Q95_agg = np.zeros(shape=(60, Tperiods))
for i in np.arange(0,Tperiods):
    Q95_agg[0, i] = np.percentile(ImpoMatrix_raw[:,i], 95)
    Q95_agg[1, i] = np.percentile(ProdMatrix_raw[:,i], 95)
    Q95_agg[2, i] = np.percentile(ManufMatrix_raw[:,i], 95)
    Q95_agg[3, i] = np.percentile(ConsMatrix_raw[:,i], 95)
    Q95_agg[4, i] = np.percentile(WWMatrix_raw[:,i], 95)
    Q95_agg[5, i] = np.percentile(SewMatrix_raw[:,i], 95)
    Q95_agg[6, i] = np.percentile(WWTPMatrix_raw[:,i], 95)
    Q95_agg[7, i] = np.percentile(OSTreatMatrix_raw[:,i], 95)
    Q95_agg[8, i] = np.percentile(OSSludMatrix_raw[:,i], 95)
    Q95_agg[9, i] = np.percentile(SubsurfMatrix_raw[:,i], 95)
    Q95_agg[10, i] = np.percentile(SortMatrix_raw[:,i], 95)
    Q95_agg[11, i] = np.percentile(ReprMatrix_raw[:,i], 95)
    Q95_agg[12, i] = np.percentile(ReusMatrix_raw[:,i], 95)
    Q95_agg[13, i] = np.percentile(WIPMatrix_raw[:,i], 95)
    Q95_agg[14, i] = np.percentile(LandfMatrix_raw[:,i], 95)
    Q95_agg[15, i] = np.percentile(ExpMatrix_raw[:,i], 95)
    Q95_agg[16, i] = np.percentile(AirMatrix_raw[:,i], 95)
    Q95_agg[17, i] = np.percentile(NUSoilMatrix_raw[:,i], 95)
    Q95_agg[18, i] = np.percentile(STSoilMatrix_raw[:,i], 95)
    Q95_agg[19, i] = np.percentile(SurfWatMatrix_raw[:,i], 95)
    Q95_agg[20, i] = np.percentile(WWMatrix_N_raw[:,i], 95)
    Q95_agg[21, i] = np.percentile(WWMatrix_M_raw[:,i], 95)
    Q95_agg[22, i] = np.percentile(WWMatrix_T_raw[:,i], 95)
    Q95_agg[23, i] = np.percentile(SewMatrix_N_raw[:,i], 95)
    Q95_agg[24, i] = np.percentile(SewMatrix_M_raw[:,i], 95)
    Q95_agg[25, i] = np.percentile(SewMatrix_T_raw[:,i], 95)
    Q95_agg[26, i] = np.percentile(WWTPMatrix_N_raw[:,i], 95)
    Q95_agg[27, i] = np.percentile(WWTPMatrix_M_raw[:,i], 95)
    Q95_agg[28, i] = np.percentile(WWTPMatrix_T_raw[:,i], 95)
    Q95_agg[29, i] = np.percentile(OSTreatMatrix_N_raw[:,i], 95)
    Q95_agg[30, i] = np.percentile(OSTreatMatrix_M_raw[:,i], 95)
    Q95_agg[31, i] = np.percentile(OSTreatMatrix_T_raw[:,i], 95)
    Q95_agg[32, i] = np.percentile(OSSludMatrix_N_raw[:,i], 95)
    Q95_agg[33, i] = np.percentile(OSSludMatrix_M_raw[:,i], 95)
    Q95_agg[34, i] = np.percentile(OSSludMatrix_T_raw[:,i], 95)
    Q95_agg[35, i] = np.percentile(SubsurfMatrix_N_raw[:,i], 95)
    Q95_agg[36, i] = np.percentile(SubsurfMatrix_M_raw[:,i], 95)
    Q95_agg[37, i] = np.percentile(SubsurfMatrix_T_raw[:,i], 95)
    Q95_agg[38, i] = np.percentile(ReusMatrix_N_raw[:,i], 95)
    Q95_agg[39, i] = np.percentile(ReusMatrix_T_raw[:,i], 95)
    Q95_agg[40, i] = np.percentile(ReusMatrix_P_raw[:,i], 95)
    Q95_agg[41, i] = np.percentile(WIPMatrix_N_raw[:,i], 95)
    Q95_agg[42, i] = np.percentile(WIPMatrix_M_raw[:,i], 95)
    Q95_agg[43, i] = np.percentile(WIPMatrix_T_raw[:,i], 95)
    Q95_agg[44, i] = np.percentile(WIPMatrix_P_raw[:,i], 95)
    Q95_agg[45, i] = np.percentile(LandfMatrix_N_raw[:,i], 95)
    Q95_agg[46, i] = np.percentile(LandfMatrix_M_raw[:,i], 95)
    Q95_agg[47, i] = np.percentile(LandfMatrix_T_raw[:,i], 95)
    Q95_agg[48, i] = np.percentile(LandfMatrix_P_raw[:,i], 95)
    Q95_agg[49, i] = np.percentile(AirMatrix_N_raw[:,i], 95)
    Q95_agg[50, i] = np.percentile(AirMatrix_M_raw[:,i], 95)
    Q95_agg[51, i] = np.percentile(AirMatrix_T_raw[:,i], 95)
    Q95_agg[52, i] = np.percentile(NUSoilMatrix_N_raw[:,i], 95)
    Q95_agg[53, i] = np.percentile(NUSoilMatrix_M_raw[:,i], 95)
    Q95_agg[54, i] = np.percentile(STSoilMatrix_N_raw[:,i], 95)
    Q95_agg[55, i] = np.percentile(STSoilMatrix_M_raw[:,i], 95)
    Q95_agg[56, i] = np.percentile(STSoilMatrix_T_raw[:,i], 95)
    Q95_agg[57, i] = np.percentile(SurfWatMatrix_N_raw[:,i], 95)
    Q95_agg[58, i] = np.percentile(SurfWatMatrix_M_raw[:,i], 95)
    Q95_agg[59, i] = np.percentile(SurfWatMatrix_T_raw[:,i], 95)
    
Q95_agg = pd.DataFrame({'Import':Q95_agg[0,:],
                       'Production':Q95_agg[1,:],
                       'Manufacturing':Q95_agg[2,:],
                       'Consumption':Q95_agg[3,:],
                       'Wastewater':Q95_agg[4,:],
                       'Sewage system':Q95_agg[5,:],
                       'WWTP':Q95_agg[6,:],
                       'On-site treatment':Q95_agg[7,:],
                       'On-site sludge':Q95_agg[8,:],
                       'Subsurface':Q95_agg[9,:],
                       'Sorting':Q95_agg[10,:],
                       'Reprocessing':Q95_agg[11,:],
                       'Reuse':Q95_agg[12,:],
                       'WIP':Q95_agg[13,:],
                       'Landfill':Q95_agg[14,:],
                       'Export':Q95_agg[15,:],
                       'Air':Q95_agg[16,:],
                       'NU Soil':Q95_agg[17,:],
                       'ST Soil':Q95_agg[18,:],
                       'Surface water':Q95_agg[19,:],
                       'Pristine to Wastewater':Q95_agg[20,:],
                       'Matrix-embedded to Wastewater':Q95_agg[21,:],
                       'Transformed to Wastewater':Q95_agg[22,:],
                       'Pristine to Sewer':Q95_agg[23,:],
                       'Matrix-embedded to Sewer':Q95_agg[24,:],
                       'Transformed to Sewer':Q95_agg[25,:],
                       'Pristine to WWTP':Q95_agg[26,:], 
                       'Matrix-embedded to WWTP':Q95_agg[27,:],
                       'Transformed to WWTP':Q95_agg[28,:],
                       'Pristine to On-site treatment':Q95_agg[29,:],
                       'Matrix-embedded to On-site treatment':Q95_agg[30,:],
                       'Transformed to On-site treatment':Q95_agg[31,:],
                       'Pristine to On-site sludge':Q95_agg[32,:], 
                       'Matrix-embedded to On-site sludge':Q95_agg[33,:],
                       'Transformed to On-site sludge':Q95_agg[34,:],
                       'Pristine to Subsurface':Q95_agg[35,:],
                       'Matrix-embedded to Subsurface':Q95_agg[36,:],
                       'Transformed to Subsurface':Q95_agg[37,:],
                       'Pristine to Reuse':Q95_agg[38,:],
                       'Transformed to Reuse':Q95_agg[39,:],
                       'Product-embedded to Reuse':Q95_agg[40,:],
                       'Pristine to WIP':Q95_agg[41,:], 
                       'Matrix-embedded to WIP':Q95_agg[42,:],
                       'Transformed to WIP':Q95_agg[43,:],
                       'Product-embedded to WIP':Q95_agg[44,:],
                       'Pristine to Landfill':Q95_agg[45,:],
                       'Matrix-embedded to Landfill':Q95_agg[46,:],
                       'Transformed to Landfill':Q95_agg[47,:],
                       'Product-embedded to Landfill':Q95_agg[48,:],
                       'Pristine to Air':Q95_agg[49,:],
                       'Matrix-embedded to Air':Q95_agg[50,:],
                       'Transformed to Air':Q95_agg[51,:],
                       'Pristine to NU Soil':Q95_agg[52,:],
                       'Matrix-embedded to NU Soil':Q95_agg[53,:],
                       'Pristine to ST Soil':Q95_agg[54,:], 
                       'Matrix-embedded to ST Soil':Q95_agg[55,:],
                       'Transformed to ST Soil':Q95_agg[56,:],
                       'Pristine to Surface water':Q95_agg[57,:],
                       'Matrix-embedded to Surface water':Q95_agg[58,:],
                       'Transformed to Surface water':Q95_agg[59,:]})
Q95_agg.to_csv('Q95 of totals to compartments - TiO2 - AUT_2.csv', index = False, sep=' ')


# In[48]:


Speriod = 20


# In[49]:


print('PMC flow to technical and environmental compartments Inflows')
compartmentlist = simulator.getCompartments()

PMCrellist = [comp for comp in compartmentlist if ('PMCrel' in comp.categories)]
PMCrel2TE = simulator.getCombinedOutflows(PMCrellist) # PMC2TE is a dictionary


# In[50]:


print('From Use and Waste categories to techn and env compartments')

for key,value in PMCrel2TE.items(): 
    Tinflow_Mean = np.mean(value[:,Speriod])
    Tinflow_Q50 = np.percentile(value[:,Speriod], 50)
    Tinflow_Q25 = np.percentile(value[:,Speriod], 25)
    Tinflow_Q75 = np.percentile(value[:,Speriod], 75)
    Tinflow_min = min(value[:,Speriod])
    Tinflow_max = max(value[:,Speriod])
    print(str(key)+':')
    print('Mean --> ' + str(round(Tinflow_Mean, 4)))
    print('Q50 --> ' + str(round(Tinflow_Q50, 4)))
    print('Q25 --> ' + str(round(Tinflow_Q25, 4)))
    print('Q75 --> ' + str(round(Tinflow_Q75, 4)))
    print('Min --> ' + str(round(Tinflow_min, 4)))
    print('Max --> ' + str(round(Tinflow_max, 4)))


# In[51]:


print('Total release from use and EoL in one period, including stocked from previous years')
# equals to immediate release from consumption and stock release from consumption"

Total_PMCrel = simulator.getLoggedCategoryOutflowSum('PMC')

Total_PMCrel_Mean = np.mean(Total_PMCrel[:,Speriod])
Total_PMCrel_Q50 = np.percentile(Total_PMCrel[:,Speriod], 50)
Total_PMCrel_Q25 = np.percentile(Total_PMCrel[:,Speriod], 25)
Total_PMCrel_Q75 = np.percentile(Total_PMCrel[:,Speriod], 75)
Total_PMCrel_min = min(Total_PMCrel[:,Speriod])
Total_PMCrel_max = max(Total_PMCrel[:,Speriod])

print('From use and EoL immediate total release')
print('Total_PMCrel_Mean --> ' + str(round(Total_PMCrel_Mean, 4)))
print('Total_PMCrel_Q50 --> ' + str(round(Total_PMCrel_Q50, 4)))
print('Total_PMCrel_Q25 --> ' + str(round(Total_PMCrel_Q25, 4)))
print('Total_PMCrel_Q75 --> ' + str(round(Total_PMCrel_Q75, 4)))
print('Total_PMCrel_min --> ' + str(round(Total_PMCrel_min, 4)))
print('Total_PMCrel_max --> ' + str(round(Total_PMCrel_max, 4)))


# In[52]:


print('Current cumulative PMC stock')
Total_PMCstock = simulator.getLoggedCategoryStock('PMC')
Total_PMCstock_Mean = np.mean(Total_PMCstock[:,Speriod])
Total_PMCstock_Q50 = np.percentile(Total_PMCstock[:,Speriod], 50)
Total_PMCstock_Q25 = np.percentile(Total_PMCstock[:,Speriod], 25)
Total_PMCstock_Q75 = np.percentile(Total_PMCstock[:,Speriod], 75)
Total_PMCstock_Min = min(Total_PMCstock[:,Speriod])
Total_PMCstock_Max = max(Total_PMCstock[:,Speriod])

print('Total_PMCstock_Mean --> ' + str(round(Total_PMCstock_Mean, 4)))
print('Total_PMCstock_Q50 --> ' + str(round(Total_PMCstock_Q50, 4)))
print('Total_PMCstock_Q25 --> ' + str(round(Total_PMCstock_Q25, 4)))
print('Total_PMCstock_Q75 --> ' + str(round(Total_PMCstock_Q75, 4)))
print('Total_PMCstock_Min --> ' + str(round(Total_PMCstock_Min, 4)))
print('Total_PMCstock_Max --> ' + str(round(Total_PMCstock_Max, 4)))


# In[53]:


print('Immediate total release from the inflow in current year')
PMC2TE_IM = simulator.getCategoryImmediateFlowFromStockSum('PMC')
PMC2TE_IM_Mean = np.mean(PMC2TE_IM[:,Speriod])
PMC2TE_IM_Q50 = np.percentile(PMC2TE_IM[:,Speriod], 50)
PMC2TE_IM_Q25 = np.percentile(PMC2TE_IM[:,Speriod], 25)
PMC2TE_IM_Q75 = np.percentile(PMC2TE_IM[:,Speriod], 75)
PMC2TE_IM_Min = min(PMC2TE_IM[:,Speriod])
PMC2TE_IM_Max = max(PMC2TE_IM[:,Speriod])

print('PMC2TE_IM_Mean --> ' + str(round(PMC2TE_IM_Mean, 4)))
print('PMC2TE_IM_Q50 --> ' + str(round(PMC2TE_IM_Q50, 4)))
print('PMC2TE_IM_Q25 --> ' + str(round(PMC2TE_IM_Q25, 4)))
print('PMC2TE_IM_Q75 --> ' + str(round(PMC2TE_IM_Q75, 4)))
print('PMC2TE_IM_Min --> ' + str(round(PMC2TE_IM_Min, 4)))
print('PMC2TE_IM_Max --> ' + str(round(PMC2TE_IM_Max, 4)))


# In[54]:


print('From stock to current release')

Stock2CR_Mean = Total_PMCrel_Mean - PMC2TE_IM_Mean
Stock2CR_Q50 = Total_PMCrel_Q50 - PMC2TE_IM_Q50
Stock2CR_Q25 = Total_PMCrel_Q25 - PMC2TE_IM_Q25
Stock2CR_Q75 = Total_PMCrel_Q75 - PMC2TE_IM_Q75

print('From PMC immediate total release')
print('Stock2CR_mean --> ' + str(round(Stock2CR_Mean, 4)))
print('Stock2CR_Q50 --> ' + str(round(Stock2CR_Q50, 4)))
print('Stock2CR_Q25 --> ' + str(round(Stock2CR_Q25, 4)))
print('Stock2CR_Q75 --> ' + str(round(Stock2CR_Q75, 4)))


# In[ ]:




