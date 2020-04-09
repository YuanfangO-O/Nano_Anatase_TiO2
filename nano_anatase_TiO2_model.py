#!/usr/bin/env python
# coding: utf-8

# Original Authur: Adam Veronique
# Modified by Yuanfang Zheng


# In[2]:


import components as cp
import numpy.random as nr
import numpy as np
import Model 
import pandas as pd

import TruncatingFunctions as tf


# In[5]:


model = Model.Model('nano-TiO2 anatase from 2000 to 2020')


# In[6]:


# split of the total inflow to different compartments
totalInflow = cp.FlowCompartment('Total Inflow', logInflows=True, logOutflows=True)
#Import_Manuf = cp.FlowCompartment('Import to Manufacturing', logInflows=True, logOutflows=True, categories=['Import'])
#Import_Cons = cp.FlowCompartment('Import to Consumption', logInflows=True, logOutflows=True, categories=['Import'])


# In[7]:


# Production of the nano-material and Manufacturing of the products it is used in   
Production  = cp.Stock('Production',  logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['Production'])
Manufacture = cp.Stock('Manufacture', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['Manufacture'])
Consumption = cp.FlowCompartment('Consumption', logInflows=True, logOutflows=True, categories=['Consumption'])


# In[8]:


Prod_Air_N = cp.Sink('Pristine from Production to Air', logInflows=True, categories=['Air', 'Air_N', 'Pristine'])
Manuf_Air_N = cp.Sink('Pristine from Manufacturing to Air', logInflows=True, categories=['Air', 'Air_N', 'Pristine'])


# In[9]:


# Manufacturing and waste
#Manuf_Text = cp.FlowCompartment('Manuf Textiles', logInflows=True, logOutflows=True, categories=['Manufacture'])
#Manuf_Plas = cp.FlowCompartment('Manuf Plastics', logInflows=True, logOutflows=True, categories=['Manufacture'])
Manuf_Solids = cp.FlowCompartment('Manuf Solids', logInflows=True, logOutflows=True, categories=['Manufacture'])
Manuf_Liquids = cp.FlowCompartment('Manuf Liquids', logInflows=True, logOutflows=True, categories=['Manufacture'])

#manuf_textiles_waste = cp.FlowCompartment('Waste from manuf Textiles', logInflows=True, logOutflows=True, categories=['Manufacture', 'Solid Waste'])
#manuf_plastics_waste = cp.FlowCompartment('Waste from manuf Plastics', logInflows=True, logOutflows=True, categories=['Manufacture', 'Solid Waste'])

#ManufTextW_Reuse_P = cp.Sink('Product-embedded from Textile manufacturing to reprocessing and reuse', logInflows=True, categories=['Reprocessing', 'Reuse', 'Reuse_P'])
#ManufPlasW_Reuse_P = cp.Sink('Product-embedded from Plastic manufacturing to reprocessing and reuse', logInflows=True, categories=['Reprocessing', 'Reuse', 'Reuse_P'])
ManufSolidW_Reuse_P = cp.Sink('Product-embedded from Other solids manufacturing to reprocessing and reuse', logInflows=True, categories=['Reprocessing', 'Reuse', 'Reuse_P'])


# In[10]:


# Definition of Products categories (compartments)
#PersCare = cp.FlowCompartment('PersCare', logInflows=True, logOutflows=True, categories=['Products'])
#PersCare_Use = cp.Stock('PersCare_Use', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','Use','PMCrel'])
#PersCare_EoL = cp.Stock('PersCare_EoL', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','EoL'])

OutPaints = cp.FlowCompartment('OutPaints', logInflows=True, logOutflows=True, categories='Products')
OutPaints_Use = cp.Stock('OutPaints_Use', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','Use','PMCrel'])
OutPaints_EoL = cp.Stock('OutPaints_EoL', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','EoL'])

InPaints = cp.FlowCompartment('InPaints', logInflows=True, logOutflows=True, categories='Products')
InPaints_Use = cp.Stock('InPaints_Use', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','Use','PMCrel'])
InPaints_EoL = cp.Stock('InPaints_EoL', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','EoL'])

Cement= cp.FlowCompartment('Cement', logInflows=True, logOutflows=True, categories='Products')
Cement_Use =cp.Stock('Cement_Use', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','Use','PMCrel'])
Cement_EoL =cp.Stock('Cement_EoL', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','EoL'])

Glass = cp.FlowCompartment('Glass', logInflows=True, logOutflows=True, categories='Products')
Glass_Use = cp.Stock('Glass_Use', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','Use','PMCrel'])
Glass_EoL = cp.Stock('Glass_EoL', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','EoL'])

Ceramics = cp.FlowCompartment('Ceramics', logInflows=True, logOutflows=True, categories='Products')
Ceramics_Use = cp.Stock('Ceramics_Use', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','Use','PMCrel'])
Ceramics_EoL = cp.Stock('Ceramics_EoL', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','EoL'])

#RubPlas = cp.FlowCompartment('RubPlas', logInflows=True, logOutflows=True, categories='Products')
#RubPlas_Use = cp.Stock('RubPlas_Use', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','Use','PMCrel'])
#RubPlas_EoL = cp.Stock('RubPlas_EoL', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','EoL'])

Solar = cp.FlowCompartment('Solar', logInflows=True, logOutflows=True, categories='Products')
Solar_EoL = cp.Stock('Solar_EoL', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','EoL'])

#Electronics= cp.FlowCompartment('Electronics', logInflows=True, logOutflows=True, categories='Products')
#Electronics_Use = cp.Stock('Electronics_Use', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','Use','PMCrel'])
#Electronics_EoL = cp.Stock('Electronics_EoL', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','EoL'])

#CleanAgents= cp.FlowCompartment('CleanAgents', logInflows=True, logOutflows=True, categories='Products')
#CleanAgents_Use = cp.Stock('CleanAgents_Use', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','Use','PMCrel'])
#CleanAgents_EoL = cp.Stock('CleanAgents_EoL', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','EoL'])

#Food = cp.FlowCompartment('Food', logInflows=True, logOutflows=True, categories='Products')
#Food_Use = cp.Stock('Food_Use', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','Use','PMCrel'])
#Food_EoL = cp.Stock('Food_EoL', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','EoL'])

#Textiles = cp.FlowCompartment('Textiles', logInflows=True, logOutflows=True, categories='Products')
#Textiles_Use = cp.Stock('Textiles_Use', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','Use','PMCrel'])
#Textiles_EoL = cp.Stock('Textiles_EoL', logInflows=True, logOutflows=True, logImmediateFlows=True, categories=['PMC','EoL'])


# In[11]:


# Definition of forms of release after use
#PersCare_WW = cp.FlowCompartment('From PersCare to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater'])
#PersCare_WW_N = cp.FlowCompartment('Pristine in Wastewater from PersCare', logInflows=True, logOutflows=True, categories=['Wastewater_N', 'Pristine'])
#PersCare_SW = cp.FlowCompartment('From PersCare to Surfacewater', logInflows=True, logOutflows=True, categories=['Surfacewater'])
#PersCare_SW_N = cp.Sink('Pristine in Surfacewater from PersCare', logInflows=True, categories=['Surfacewater_N', 'Pristine'])

OutPaints_Air = cp.FlowCompartment('From OutPaints to Air', logInflows=True, logOutflows=True, categories=['Air'])
OutPaints_Air_N = cp.Sink('Pristine in Air from OutPaints', logInflows=True, categories=['Air_N', 'Pristine'])
OutPaints_Air_M = cp.Sink('Matrix-embedded in Air from OutPaints', logInflows=True, categories=['Air_M', 'Matrix-embedded'])
OutPaints_WW = cp.FlowCompartment('From OutPaints to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater'])
OutPaints_WW_N = cp.FlowCompartment('Pristine in Wastewater from OutPaints', logInflows=True, logOutflows=True, categories=['Wastewater_N', 'Pristine'])
OutPaints_WW_M = cp.FlowCompartment('Matrix-embedded in Wastewater from OutPaints', logInflows=True, logOutflows=True, categories=['Wastewater_M', 'Matrix-embedded'])
OutPaints_NUsoil = cp.FlowCompartment('From OutPaints to Soil', logInflows=True, logOutflows=True, categories=['Soil', 'NU Soil'])
OutPaints_NUsoil_N = cp.Sink('Pristine in Soil from OutPaints', logInflows=True, categories=['Soil_N', 'NU Soil_N', 'Pristine'])
OutPaints_NUsoil_M = cp.Sink('Matrix-embedded in Soil from OutPaints', logInflows=True, categories=['Soil_M', 'NU Soil_M', 'Matrix-embedded'])

InPaints_Air = cp.FlowCompartment('From InPaints to Air', logInflows=True, logOutflows=True, categories=['Air'])
InPaints_Air_N = cp.Sink('Pristine in Air from InPaints', logInflows=True, categories=['Air_N', 'Pristine'])
InPaints_Air_M = cp.Sink('Matrix-embedded in Air from InPaints', logInflows=True, categories=['Air_M', 'Matrix-embedded'])
InPaints_WW = cp.FlowCompartment('From InPaints to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater'])
InPaints_WW_N = cp.FlowCompartment('Pristine in Wastewater from InPaints', logInflows=True, logOutflows=True, categories=['Wastewater_N', 'Pristine'])
InPaints_WW_M = cp.FlowCompartment('Matrix-embedded in Wastewater from InPaints', logInflows=True, logOutflows=True, categories=['Wastewater_M', 'Matrix-embedded'])
InPaints_NUsoil = cp.FlowCompartment('From InPaints to Soil', logInflows=True, logOutflows=True, categories=['Soil', 'NU Soil'])
InPaints_NUsoil_N = cp.Sink('Pristine in Soil from InPaints', logInflows=True, categories=['Soil_N', 'NU Soil_N', 'Pristine'])
InPaints_NUsoil_M = cp.Sink('Matrix-embedded in Soil from InPaints', logInflows=True, categories=['Soil_M', 'NU Soil_M', 'Matrix-embedded'])

Cement_WW = cp.FlowCompartment('From Cement to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater'])
Cement_WW_N = cp.FlowCompartment('Pristine from Cement to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater_N', 'Pristine'])
Cement_WW_M = cp.FlowCompartment('Matrix-embedded from Cement to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater_M', 'Matrix-embedded'])

Glass_WW = cp.FlowCompartment('From Glass coating to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater'])
Glass_WW_N = cp.FlowCompartment('Pristine from Glass coating to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater_N', 'Pristine'])
Glass_WW_M = cp.FlowCompartment('Matrix-embedded from Glass coating to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater_M', 'Matrix-embedded'])
Glass_Air = cp.FlowCompartment('From Glass coating to Air', logInflows=True, logOutflows=True, categories=['Air'])
Glass_Air_N = cp.Sink('Pristine from Glass coating to Air', logInflows=True, categories=['Air_N', 'Pristine'])
Glass_Air_M = cp.Sink('Matrix-embedded from Glass coating to Air', logInflows=True, categories=['Air_M', 'Matrix-embedded'])
Glass_NUsoil = cp.FlowCompartment('From Glass coating to Soil', logInflows=True, logOutflows=True, categories=['Soil', 'NU Soil'])
Glass_NUsoil_N = cp.Sink('Pristine from Glass coating to NU Soil', logInflows=True, categories=['Soil_N', 'NU Soil_N', 'Pristine'])
Glass_NUsoil_M = cp.Sink('Matrix-embedded from Glass coating to NU Soil', logInflows=True, categories=['Soil_M', 'NU Soil_M', 'Matrix-embedded'])

Ceramics_WW = cp.FlowCompartment('From Ceramics coating to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater'])
Ceramics_WW_N = cp.FlowCompartment('Pristine from Ceramics coating to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater_N', 'Pristine'])
Ceramics_WW_M = cp.FlowCompartment('Matrix-embedded from Ceramics coating to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater_M', 'Matrix-embedded'])
Ceramics_Air = cp.FlowCompartment('From Ceramics coating to Air', logInflows=True, logOutflows=True, categories=['Air'])
Ceramics_Air_N = cp.Sink('Pristine from Ceramics coating to Air', logInflows=True, categories=['Air_N', 'Pristine'])
Ceramics_Air_M = cp.Sink('Matrix-embedded from Ceramics coating to Air', logInflows=True, categories=['Air_M', 'Matrix-embedded'])
Ceramics_NUsoil = cp.FlowCompartment('From Ceramics coating to Soil', logInflows=True, logOutflows=True, categories=['Soil', 'NU Soil'])
Ceramics_NUsoil_N = cp.Sink('Pristine from Ceramics coating to NU Soil', logInflows=True, categories=['Soil_N', 'NU Soil_N', 'Pristine'])
Ceramics_NUsoil_M = cp.Sink('Matrix-embedded from Ceramics coating to NU Soil', logInflows=True, categories=['Soil_M', 'NU Soil_M', 'Matrix-embedded'])

#RubPlas_Air = cp.FlowCompartment('From RubPlas to Air', logInflows=True, logOutflows=True, categories=['Air'])
#RubPlas_Air_N = cp.Sink('Pristine from RubPlas to Air', logInflows=True, categories=['Air_N', 'Pristine'])
#RubPlas_Air_M = cp.Sink('Matrix-embedded from RubPlas to Air', logInflows=True, categories=['Air_M', 'Matrix-embedded'])
#RubPlas_WW = cp.FlowCompartment('From RubPlas to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater'])
#RubPlas_WW_N = cp.FlowCompartment('Pristine from RubPlas to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater_N', 'Pristine'])
#RubPlas_WW_M = cp.FlowCompartment('Matrix-embedded from RubPlas to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater_M', 'Matrix-embedded'])

#Electronics_WW = cp.FlowCompartment('From Electronics to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater'])
#Electronics_WW_N = cp.FlowCompartment('Pristine from Electronics to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater_N', 'Pristine'])
#Electronics_WW_M = cp.FlowCompartment('Matrix-embedded from Electronics to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater_M', 'Matrix-embedded'])

#CleanAgents_WW = cp.FlowCompartment('From Cleaning agents to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater'])
#CleanAgents_WW_N = cp.FlowCompartment('Pristine from Cleaning agents to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater_N', 'Pristine'])

#Food_WW = cp.FlowCompartment('From Food to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater'])
#Food_WW_N = cp.FlowCompartment('Pristine from Food to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater_N', 'Pristine'])

#Textiles_Air = cp.FlowCompartment('From Textiles to Air', logInflows=True, logOutflows=True, categories=['Air'])
#Textiles_Air_N = cp.Sink('Pristine from Textiles to Air', logInflows=True, categories=['Air_N', 'Pristine'])
#Textiles_Air_M = cp.Sink('Matrix-embedded from Textiles to Air', logInflows=True, categories=['Air_M', 'Matrix-embedded'])
#Textiles_WW = cp.FlowCompartment('From Textiles to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater'])
#Textiles_WW_N = cp.FlowCompartment('Pristine from Textiles to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater_N', 'Pristine'])
#Textiles_WW_M = cp.FlowCompartment('Matrix-embedded from Textiles to Wastewater', logInflows=True, logOutflows=True, categories=['Wastewater_M', 'Matrix-embedded'])


# In[12]:


# Definition of WIP compartments 
WIP_P = cp.FlowCompartment('Product-embedded to Waste Incineration Plant', logInflows=True, logOutflows=True, categories=['WIP', 'WIP_P', 'Product-embedded'])
WIP_N = cp.FlowCompartment('Pristine to Waste Incineration Plant', logInflows=True, logOutflows=True, categories=['WIP', 'WIP_N', 'Pristine'])
WIP_M = cp.FlowCompartment('Matrix-embedded to Waste Incineration Plant', logInflows=True, logOutflows=True, categories=['WIP_M','Matrix-embedded'])
WIP_T = cp.FlowCompartment('Transformed to Waste Incineration Plant', logInflows=True, logOutflows=True, categories=['WIP_T','Transformed'])

Burning_N = cp.FlowCompartment('Pristine to Burning', logInflows=True, logOutflows=True, categories=['Burning', 'Burning_N', 'Pristine'])
Burning_T = cp.FlowCompartment('Transformed to Burning', logInflows=True, logOutflows=True, categories=['Burning', 'Burning_T', 'Transformed'])

Bottomash_N = cp.FlowCompartment('Pristine in Bottom ash', logInflows=True, logOutflows=True, categories=['Bottomash', 'Bottomash_N', 'Pristine'])
Bottomash_T = cp.FlowCompartment('Transformed in Bottom ash', logInflows=True, logOutflows=True, categories=['Bottomash', 'Bottomash_M', 'Matrix-embedded'])

Flyash_N = cp.FlowCompartment('Pristine in Flyash', logInflows=True, logOutflows=True, categories=['Flyash', 'Flyash_N', 'Pristine'])
Flyash_T = cp.FlowCompartment('Transformed in Flyash', logInflows=True, logOutflows=True, categories=['Flyash', 'Flyash_T', 'Transformed'])

Filterash_N = cp.FlowCompartment('Pristine in Filterash', logInflows=True, logOutflows=True, categories=['Filterash', 'Filterash_N', 'Pristine'])
Filterash_T = cp.FlowCompartment('Transformed in Filterash', logInflows=True, logOutflows=True, categories=['Filterash', 'Filterash_T', 'Transformed'])

WIP_Air_N = cp.Sink('From WIP to Air as Pristine', logInflows=True, categories=['Air', 'Air_N', 'Pristine'])
WIP_Air_T = cp.Sink('From WIP to Air as Transformed', logInflows=True, categories=['Air', 'Air_T', 'Transformed'])

# Definition of STP
WW_N = cp.FlowCompartment('Pristine in Wastewater', logInflows=True, logOutflows=True, categories=['AllWastewater', 'AllWastewater_N', 'Pristine'])
WW_M = cp.FlowCompartment('Matrix-embedded in Wastewater', logInflows=True, logOutflows=True, categories=['AllWastewater', 'AllWastewater_M', 'Matrix-embedded'])
WW_T = cp.FlowCompartment('Transformed in Wastewater', logInflows=True, logOutflows=True, categories=['AllWastewater', 'AllWastewater_T', 'Transformed'])

NoSewageSystem_N = cp.FlowCompartment('Pristine in NoSewageSystem', logInflows=True, logOutflows=True, categories=['NoSewageSystem', 'NoSewageSystem_N', 'Pristine'])
NoSewageSystem_M = cp.FlowCompartment('Matrix-embedded in NoSewageSystem', logInflows=True, logOutflows=True, categories=['NoSewageSystem', 'NoSewageSystem_M', 'Matrix-embedded'])
NoSewageSystem_T = cp.FlowCompartment('Transformed in NoSewageSystem', logInflows=True, logOutflows=True, categories=['NoSewageSystem', 'NoSewageSystem_T', 'Transformed'])

NoSew_SW_N = cp.Sink('Pristine from no sewer to surface water', logInflows=True, categories=['Surfacewater', 'Surfacewater_N', 'Pristine'])
NoSew_SW_M = cp.Sink('Matrix-embedded from no sewer to surface water', logInflows=True, categories=['Surfacewater', 'Surfacewater_M', 'Matrix-embedded'])
NoSew_SW_T = cp.Sink('Transformed from no sewer to surface water', logInflows=True, categories=['Surfacewater', 'Surfacewater_T', 'Transformed'])

SewageSystem_N = cp.FlowCompartment('Pristine in SewageSystem', logInflows=True, logOutflows=True, categories=['SewageSystem', 'SewageSystem_N', 'Pristine'])
SewageSystem_M = cp.FlowCompartment('Matrix-embedded in SewageSystem', logInflows=True, logOutflows=True, categories=['SewageSystem', 'SewageSystem_M', 'Matrix-embedded'])
SewageSystem_T = cp.FlowCompartment('Transformed in SewageSystem', logInflows=True, logOutflows=True, categories=['SewageSystem', 'SewageSystem_T', 'Transformed'])

Sew_SW_N = cp.Sink('Pristine from sewer to surface water', logInflows=True, categories=['Surfacewater', 'Surfacewater_N', 'Pristine'])
Sew_SW_M = cp.Sink('Matrix-embedded from sewer to surface water', logInflows=True, categories=['Surfacewater', 'Surfacewater_M', 'Matrix-embedded'])
Sew_SW_T = cp.Sink('Transformed from sewer to surface water', logInflows=True, categories=['Surfacewater', 'Surfacewater_T', 'Transformed'])

OnSiteTreat_N = cp.FlowCompartment('Pristine in OnsiteTreat', logInflows=True, logOutflows=True, categories = ['OnsiteTreat', 'OnsiteTreat_N', 'Pristine'])
OnSiteTreat_M = cp.FlowCompartment('Matrix-embedded in OnsiteTreat', logInflows=True, logOutflows=True, categories = ['OnsiteTreat', 'OnsiteTreat_M', 'Matrix-embedded'])
OnSiteTreat_T = cp.FlowCompartment('Transformed in OnsiteTreat', logInflows=True, logOutflows=True, categories = ['OnsiteTreat', 'OnsiteTreat_T', 'Transformed'])

WWTP_N  = cp.FlowCompartment('Pristine to WWTP', logInflows=True, logOutflows=True, categories=['WWTP', 'WWTP_N', 'Pristine']) 
WWTP_M  = cp.FlowCompartment('Matrix-embedded to WWTP', logInflows=True, logOutflows=True, categories=['WWTP', 'WWTP_M', 'Matrix-embedded'])
WWTP_T  = cp.FlowCompartment('Transformed to WWTP', logInflows=True, logOutflows=True, categories=['WWTP', 'WWTP_T', 'Transformed'])

TreatIOnSite_N = cp.FlowCompartment('Pristine in TreatIOnsite', logInflows=True, logOutflows=True, categories=['Treat', 'Treat_N', 'TreatIOnsite', 'TreatIOnsite_N', 'Pristine'])
TreatIOnSite_M = cp.FlowCompartment('Matrix-embedded in TreatIOnSite', logInflows=True, logOutflows=True, categories=['Treat', 'Treat_M', 'TreatIOnsite', 'TreatIOnsite_M', 'Matrix-embedded'])
TreatIOnSite_T = cp.FlowCompartment('Transformed in TreatIOnSite', logInflows=True, logOutflows=True, categories=['Treat', 'Treat_T', 'TreatIOnsite', 'TreatIOnsite_T', 'Transformed'])

TreatI_N = cp.FlowCompartment('Pristine in TreatI', logInflows=True, logOutflows=True, categories=['STP', 'STP_N', 'Treat', 'Treat_N', 'TreatI', 'TreatI_N', 'Pristine'])
TreatI_M = cp.FlowCompartment('Matrix-embedded in TreatI', logInflows=True, logOutflows=True, categories=['STP', 'STP_M', 'Treat', 'Treat_M', 'TreatI', 'TreatI_M', 'Matrix-embedded'])
TreatI_T = cp.FlowCompartment('Transformed in TreatI', logInflows=True, logOutflows=True, categories=['STP', 'STP_T', 'Treat', 'Treat_T', 'TreatI', 'TreatI_T', 'Transformed'])

TreatII_N = cp.FlowCompartment('Pristine in TreatII', logInflows=True, logOutflows=True, categories=['STP', 'STP_N', 'Treat', 'Treat_N', 'TreatII', 'TreatII_N', 'Pristine'])
TreatII_M = cp.FlowCompartment('Matrix-embedded in TreatII', logInflows=True, logOutflows=True, categories=['STP', 'STP_M', 'Treat', 'Treat_M', 'TreatII', 'TreatII_M', 'Matrix-embedded'])
TreatII_T = cp.FlowCompartment('Transformed in TreatII', logInflows=True, logOutflows=True, categories=['STP', 'STP_T', 'Treat', 'Treat_T', 'TreatII', 'TreatII_T,' 'Transformed'])

TreatIII_N = cp.FlowCompartment('Pristine in TreatIII', logInflows=True, logOutflows=True, categories=['STP', 'STP_N', 'Treat', 'Treat_N', 'TreatIII', 'TreatIII_N', 'Pristine'])
TreatIII_M = cp.FlowCompartment('Matrix-embedded in TreatIII', logInflows=True, logOutflows=True, categories=['STP', 'STP_M', 'Treat', 'Treat_M', 'TreatIII', 'TreatIII_M', 'Matrix-embedded'])
TreatIII_T = cp.FlowCompartment('Transformed in TreatIII', logInflows=True, logOutflows=True, categories=['STP', 'STP_T', 'Treat', 'Treat_T', 'TreatIII', 'TreatIII_T', 'Transformed'])

STPoverflow_N = cp.Sink('Pristine to STPoverflow and Surface water', logInflows=True, categories=['Overflow', 'Overflow_N', 'Surfacewater', 'Surfacewater_N' 'Pristine'])
STPoverflow_M = cp.Sink('Matrix-embedded to STPoverflow and Surface water', logInflows=True, categories=['Overflow', 'Overflow_M', 'Surfacewater', 'Surfacewater_M', 'Matrix-embedded'])
STPoverflow_T = cp.Sink('Transformed to STPoverflow and Surface water', logInflows=True, categories=['Overflow', 'Overflow_T', 'Surfacewater', 'Surfacewater_T', 'Transformed'])

STPeffluent_N = cp.Sink('Pristine to STPeffluent and Surface water', logInflows=True, categories=['STPeffluent', 'STPeffluent_N', 'Surfacewater', 'Surfacewater_N', 'Pristine'])
STPeffluent_M = cp.Sink('Matrix-embedded to STPeffluent and Surface water', logInflows=True, categories=['STPeffluent', 'STPeffluent_M', 'Surfacewater', 'Surfacewater_M', 'Matrix-embedded'])
STPeffluent_T = cp.Sink('Transformed to STPeffluent and Surface water', logInflows=True, categories=['STPeffluent', 'STPeffluent_T', 'Surfacewater', 'Surfacewater_T', 'Transformed'])

STPsludge_N = cp.FlowCompartment('Pristine in STPsludge', logInflows=True, logOutflows=True, categories=['STPSludge', 'STPSludge_N', 'Pristine'])
STPsludge_M = cp.FlowCompartment('Matrix-embedded in STPsludge', logInflows=True, logOutflows=True, categories=['STPSludge', 'STPSludge_M', 'Matrix-embedded'])
STPsludge_T = cp.FlowCompartment('Transformed in STPsludge', logInflows=True, logOutflows=True, categories=['STPSludge', 'STPSludge_T', 'Transformed'])


# In[13]:


#Definition of MMSW
MMSW = cp.FlowCompartment('MMSW', logInflows=True, logOutflows=True, categories=['SolidWaste','PMCrel'])

#Definition of CDW
CDW = cp.FlowCompartment('CDW', logInflows=True, logOutflows=True, categories=['SolidWaste', 'PMCrel'])

#Definition of solar waste
SolarWaste = cp.FlowCompartment('SolarWaste', logInflows=True, logOutflows=True, categories=['SolidWaste', 'PMCrel'])


# In[14]:


# Definition of Sorting_CDW
Sorting_CDW = cp.FlowCompartment('Sorting_CDW', logInflows=True, logOutflows=True, categories=['Sorting', 'Sorting1'])

#Definition of CDW sorting subcompartments
Sorting_CDW_Mineral=cp.FlowCompartment('Sorting_CDW_Mineral', logInflows=True, logOutflows=True, categories=['Sorting', 'Sorting2'])
Sorting_CDW_Glass=cp.FlowCompartment('Sorting_CDW_Glass', logInflows=True, logOutflows=True, categories=['Sorting', 'Sorting2'])

# Disposal compartment with the same disposal rates as MMSW 
# - but actually it should be called 'Disposal' because it doesn't specifically needs to be disposed from sorting
Sorting_Disposal = cp.FlowCompartment('Sorting_Disposal', logInflows=True, logOutflows=True, categories =['Sorting','Sorting_Disposal'])


# In[15]:


# Definition of Landfill
#ManufTextW_Landfill_P = cp.Sink('Product-embedded from Textile manufacturing waste to Landfill', logInflows=True, categories=['Landfill', 'Landfill_P', 'Product-embedded'])
#ManufPlasW_Landfill_P = cp.Sink('Product-embedded from Plastics manufacturing waste to Landfill', logInflows=True, categories=['Landfill', 'Landfill_P', 'Product-embedded'])
STPSlud_Landfill_N = cp.Sink('Pristine from STP Sludge to Landfill', logInflows=True, categories=['Landfill', 'Landfill_N', 'Pristine'])
STPSlud_Landfill_M = cp.Sink('Matrix-embedded from STP Sludge to Landfill', logInflows=True, categories=['Landfill', 'Landfill_M', 'Matrix-embedded'])
STPSlud_Landfill_T = cp.Sink('Transformed from STP Sludge to Landfill', logInflows=True, categories=['Landfill', 'Landfill_T', 'Transformed'])
MMSW_Landfill_P = cp.Sink('Product-embedded from MMSW to Landfill', logInflows=True, categories=['Landfill', 'Landfill_P', 'Product-embedded'])
CDW_Landfill_P = cp.Sink('Product-embedded from CDW to Landfill', logInflows=True, categories=['Landfill', 'Landfill_P', 'Product-embedded'])
SortCDWGlass_Landfill_P = cp.Sink('Product-embedded from Sorted CDW glass to Landfill', logInflows=True, categories=['Landfill', 'Landfill_P', 'Product-embedded'])
SortCDWMiner_Landfill_P = cp.Sink('Product-embedded from Sorted CDW minerals to Landfill', logInflows=True, categories=['Landfill', 'Landfill_P', 'Product-embedded'])
SortDisp_Landfill_P = cp.Sink('Product-embedded from other sorting to Landfill', logInflows=True, categories=['Landfill', 'Landfill_P', 'Product-embedded'])
#GranuPlas_Landfill_P = cp.Sink('Product-embedded from Plastic granulation to Landfill', logInflows=True, categories=['Landfill', 'Landfill_P', 'Product-embedded'])
#BaliText_Landfill_P = cp.Sink('Product-embedded from Textile baling to Landfill', logInflows=True, categories=['Landfill', 'Landfill_P', 'Product-embedded'])
PuriSlag_Landfill_T = cp.Sink('Transformed from Purification slag to Landfill', logInflows=True, categories=['Landfill', 'Landfill_T', 'Transformed'])
PuriSlag_Landfill_P = cp.Sink('Product-embedded from Purification slag to Landfill', logInflows=True, categories=['Landfill', 'Landfill_P', 'Product-embedded'])
SortMiner_Landfill_P = cp.Sink('Product-embedded from Sorted minerals to Landfill', logInflows=True, categories=['Landfill', 'Landfill_P', 'Product-embedded'])
Filterash_Landfill_N = cp.Sink('Pristine from Filter ash to Landfill', logInflows=True, categories=['Landfill', 'Landfill_N', 'Pristine'])
Filterash_Landfill_T = cp.Sink('Transformed from Filter ash to Landfill', logInflows=True, categories=['Landfill', 'Landfill_T', 'Transformed'])
Bottomash_Landfill_N = cp.Sink('Pristine from Bottom ash to Landfill', logInflows=True, categories=['Landfill', 'Landfill_N', 'Pristine'])
Bottomash_Landfill_T = cp.Sink('Transformed from Bottom ash to Landfill', logInflows=True, categories=['Landfill', 'Landfill_T', 'Transformed'])


# In[16]:


# Definition of Sludge treated soil
STsoil_N = cp.Sink('Pristine in Sludge treated soil', logInflows=True, categories=['Soil', 'Soil_N', 'ST Soil', 'ST Soil_N', 'Pristine'])
STsoil_M = cp.Sink('Matrix-embedded in Sludge treated soil', logInflows=True, categories=['Soil', 'Soil_M','ST Soil', 'ST Soil_M', 'Matrix-embedded'])
STsoil_T = cp.Sink('Transformed in Sludge treated soil', logInflows=True, categories=['Soil', 'Soil_T', 'ST Soil', 'ST Soil_T', 'Transformed'])

#Definition of Subsurface
Sew_Subsurface_N = cp.Sink('Pristine from Sewer to Subsurface', logInflows=True, categories=['Subsurface', 'Subsurface_N', 'Pristine'])
Sew_Subsurface_M = cp.Sink('Matrix-embedded from Sewer to Subsurface', logInflows=True, categories=['Subsurface', 'Subsurface_M', 'Matrix-embedded'])
Sew_Subsurface_T = cp.Sink('Transformed from Sewer to Subsurface', logInflows=True, categories=['Subsurface', 'Subsurface_T', 'Transformed'])

OnSiteTreat_Subsurface_N = cp.Sink('Pristine from On-site treatment to Subsurface', logInflows=True, categories=['Subsurface', 'Subsurface_N', 'Pristine'])
OnSiteTreat_Subsurface_M = cp.Sink('Matrix-embedded from On-site treatment to Subsurface', logInflows=True, categories=['Subsurface', 'Subsurface_M', 'Matrix-embedded'])
OnSiteTreat_Subsurface_T = cp.Sink('Transformed from On-site treatment to Subsurface', logInflows=True, categories=['Subsurface', 'Subsurface_T', 'Transformed'])

#Definition of the sludge that stays on site
OnSiteSludge_N = cp.Sink('Pristine in OnsiteSludge', logInflows=True, categories=['OnsiteSludge', 'OnsiteSludge_N', 'Pristine'])
OnSiteSludge_M = cp.Sink('Matrix-embedded in OnsiteSludge', logInflows=True, categories=['OnsiteSludge', 'OnsiteSludge_M', 'Matrix-embedded'])
OnSiteSludge_T = cp.Sink('Transformed in OnsiteSludge', logInflows=True, categories=['OnsiteSludge', 'OnsiteSludge_T', 'Transformed'])


# In[17]:



''' -----------------Define necessary commpartments for recycling systems--------------------------'''

# Definition of Reprocessing
#define the waste categories in reprocesseing systems as product-embedded forms
Reprocess_Glass_P=cp.FlowCompartment('Glass waste to reprocess as product-embedded forms',logInflows=True, logOutflows=True, categories=['Reprocessing','Reprocess_P','Reprocessed Glass'])
Reprocess_Mineral_P=cp.FlowCompartment('Mineral waste to reprocess as product-embedded forms',logInflows=True, logOutflows=True, categories=['Reprocessing','Reprocess_P','Reprocessed Minerals'])
#Reprocess_Text_P=cp.FlowCompartment('Textile waste to reprocess as product-embedded forms',logInflows=True, logOutflows=True, categories=['Reprocessing','Reprocess_P','Reprocessed Textiles'])

Reprocess_Solar_P=cp.Sink('Solar waste to reprocess as product-embedded forms',logInflows=True, categories=['Reprocessing','Reprocess_P','Reprocessed Solar waste'])


# define glass recycling system
Melting_Glass=cp.FlowCompartment('Melting of glass',logInflows=True, logOutflows=True, categories=['ReprMeltGlas'])
#Moulding_Glass_T=cp.FlowCompartment('Moulding of glass',logInflows=True, logOutflows=True, categories=['Procedures in reprocessing system'])
Air_Glass= cp.FlowCompartment('ENM particles in Air from crushing glass', logInflows=True,logOutflows=True, categories=['Air'])
#Landfill_Glass_P = cp.Sink('ENM partciles in Landfill as product-embedded forms with glass', logInflows=True, categories=['Landfill'])

# define mineral recycling system
Sorting_Mineral=cp.FlowCompartment('Sorting/Sieving of mineral',logInflows=True, logOutflows=True, categories=['ReprSortMine'])
Air_Mineral= cp.FlowCompartment('ENM particles in Air from crushing minerals', logInflows=True,logOutflows=True, categories=['Air'])

# define air NM
# Air_NM_Plas = cp.FlowCompartment('N and M particles in air from plastics',logInflows=True,logOutflows=True, categories=['Air_NM'])
Air_NM = cp.FlowCompartment('N and M particles in air from metal/textile/mineral/glass',logInflows=True,logOutflows=True, categories=['Air_NM'])


# defined RPAir here in order to sum up flows to air from reprocessing
RPAir_N= cp.Sink('Pristine particles in air from reprocessing systems',logInflows=True, categories=['Air_N', 'Pristine'])
RPAir_M= cp.Sink('Matrix-embedded particles in air from reprocessing systems',logInflows=True, categories=['Air_M','Matrix-embedded'])

RPWIP_P = cp.FlowCompartment('Product-embedded to Waste Incineration Plant from reprocessing', logInflows=True, logOutflows=True, categories=['WIP','WIP_P', 'Product_embedded'])
RPWW_N = cp.FlowCompartment('Pristine in Wastewater from reprocessing', logInflows=True, logOutflows=True, categories=['Wastewater', 'Wastewater_N', 'Pristine'])
RPWW_M = cp.FlowCompartment('Matrix-embedded in Wastewater from reprocessing', logInflows=True, logOutflows=True, categories=['Wastewater', 'Wastewater_M', 'Matrix-embedded'])

# define reuse compartment to store all final products from recycling factories
MeltGlass_Reuse_T = cp.Sink('Transformed from Glass melting to Reuse', logInflows=True, categories=['Reuse', 'Reuse_T', 'Transformed'])
SortMiner_Reuse_P = cp.Sink('Product-embedded from Sorted minerals to Reuse', logInflows=True, categories=['Reuse', 'Reuse_P', 'Product-embedded'])
Filterash_Reuse_N = cp.Sink('Pristine from Filter ash to Reuse', logInflows=True, categories=['Reuse', 'Reuse_N', 'Pristine'])
Filterash_Reuse_T = cp.Sink('Transformed from Filter ash to Reuse', logInflows=True, categories=['Reuse', 'Reuse_T', 'Transformed'])
Bottomash_Reuse_N = cp.Sink('Pristine from Bottom ash to Reuse', logInflows=True, categories=['Reuse', 'Reuse_N', 'Pristine'])
Bottomash_Reuse_T = cp.Sink('Transformed from Bottom ash to Reuse', logInflows=True, categories=['Reuse', 'Reuse_T', 'Transformed'])


# In[19]:


compartmentList=[totalInflow,
                 Production, 
                 Prod_Air_N, Manuf_Air_N, 
                 Manufacture, 
                 Manuf_Solids, Manuf_Liquids,
                 ManufSolidW_Reuse_P,
                 Consumption,
                 OutPaints, OutPaints_Use, OutPaints_EoL,
                 InPaints, InPaints_Use, InPaints_EoL,
                 Cement, Cement_Use, Cement_EoL,
                 Glass, Glass_Use, Glass_EoL,
                 Ceramics, Ceramics_Use, Ceramics_EoL,
                 Solar, Solar_EoL,

                 

                 OutPaints_Air, OutPaints_Air_N, OutPaints_Air_M, OutPaints_WW, OutPaints_WW_N, OutPaints_WW_M, 
                 OutPaints_NUsoil, OutPaints_NUsoil_N, OutPaints_NUsoil_M,
                 InPaints_Air, InPaints_Air_N, InPaints_Air_M, InPaints_WW, InPaints_WW_N, InPaints_WW_M, 
                 InPaints_NUsoil, InPaints_NUsoil_N, InPaints_NUsoil_M,
                 Cement_WW, Cement_WW_N, Cement_WW_M,
                 Glass_WW, Glass_WW_N, Glass_WW_M, Glass_Air, Glass_Air_N, Glass_Air_M, 
                 Glass_NUsoil, Glass_NUsoil_N, Glass_NUsoil_M,
                 Ceramics_WW, Ceramics_WW_N, Ceramics_WW_M, Ceramics_Air, Ceramics_Air_N, Ceramics_Air_M, 
                 Ceramics_NUsoil, Ceramics_NUsoil_N, Ceramics_NUsoil_M,

                 
                 WW_N, WW_M, WW_T,
                 OnSiteTreat_N, OnSiteTreat_M, OnSiteTreat_T,
                 SewageSystem_N, SewageSystem_M, SewageSystem_T,
                 NoSewageSystem_N, NoSewageSystem_M, NoSewageSystem_T,
                 TreatIOnSite_N, TreatIOnSite_M, TreatIOnSite_T,
                 WWTP_N, WWTP_M, WWTP_T,
                 STPoverflow_N, STPoverflow_M, STPoverflow_T,
                 STPeffluent_N, STPeffluent_M, STPeffluent_T,
                 STPsludge_N, STPsludge_M, STPsludge_T,
                 OnSiteSludge_N, OnSiteSludge_M, OnSiteSludge_T,
                 TreatI_N, TreatII_N, TreatIII_N, TreatI_M, TreatII_M, TreatIII_M, TreatI_T, TreatII_T, TreatIII_T,
                 
                 NoSew_SW_N, NoSew_SW_T, NoSew_SW_M,
                 Sew_SW_N, Sew_SW_T, Sew_SW_M,
                                  
                 MMSW, CDW, SolarWaste,
                 
                 Sorting_CDW,
                 
                
                 Sorting_CDW_Mineral, Sorting_CDW_Glass,
                 Sorting_Disposal,
                 
                 MeltGlass_Reuse_T, SortMiner_Reuse_P,
                 Filterash_Reuse_N, Filterash_Reuse_T, Bottomash_Reuse_N, Bottomash_Reuse_T,
                 
                 Air_NM, RPAir_N, RPAir_M,
                 RPWIP_P, RPWW_N, RPWW_M,
                 Melting_Glass, Air_Glass, 
                 Sorting_Mineral, Air_Mineral, 
                 
                 Reprocess_Glass_P, Reprocess_Mineral_P, Reprocess_Solar_P,
                 
                 WIP_N, WIP_M, WIP_P, WIP_T, Burning_N, Burning_T, 
                 Bottomash_N, Bottomash_T, Flyash_N, Flyash_T, Filterash_N, Filterash_T,
                 WIP_Air_N, WIP_Air_T,
                 
                 
                STPSlud_Landfill_N, STPSlud_Landfill_M, STPSlud_Landfill_T,
                 MMSW_Landfill_P, CDW_Landfill_P, SortCDWGlass_Landfill_P, SortCDWMiner_Landfill_P, SortDisp_Landfill_P,
                 SortMiner_Landfill_P, Filterash_Landfill_N, Filterash_Landfill_T, Bottomash_Landfill_N, Bottomash_Landfill_T,
                 
                 STsoil_N, STsoil_M, STsoil_T,
                 
                 Sew_Subsurface_N, Sew_Subsurface_M, Sew_Subsurface_T,
                 OnSiteTreat_Subsurface_N, OnSiteTreat_Subsurface_M, OnSiteTreat_Subsurface_T]
          

model.setCompartments(compartmentList)


# In[20]:


Productiondata = pd.read_csv('nano_TiO2production2000-2030.csv', header=None)
Productiondata.shape


# In[21]:


# Production for the whole Europe:
Productiondata_EU = Productiondata.values #in earlier code as " Productiondata = Productiondata.as_matrix(Productiondata)
# Scaling production for the UK only:
Productiondata_anatase = Productiondata_EU*0.238   #nano-anatase fraction 
# Putting the numbers in the model:
Productionvolume_EU = []
Productionvolume_anatase = []
for i in np.arange(0,21):
    Productionvolume_EU.append(Productiondata_EU[:,i])
    Productionvolume_anatase.append(Productiondata_anatase[:,i])
#model.addInflow(cp.ExternalListInflow(totalInflow, inflowList=Productionvolume))   
periodRange = np.arange(0,21)

# Setting inflow to production
model.addInflow(cp.ExternalListInflow(totalInflow, [cp.RandomChoiceInflow(Productionvolume_anatase[x]) for x in periodRange]))


# In[22]:


totalInflow.transfers = [cp.ConstTransfer(1, Production)]


# In[23]:


## Production and Manufacture
Production.localRelease = cp.ListRelease([1.0])

Manufacture.localRelease = cp.ListRelease([1.0])  

Production.transfers = [cp.StochasticTransfer(nr.triangular, [0.0002, 0.0125, 0.0467], WW_N, priority=2),
                        cp.StochasticTransfer(nr.triangular, [0.0000008, 0.0000016, 0.0000024], Prod_Air_N, priority=2),
                        cp.ConstTransfer(1, Manufacture, priority=1)]

# Allocate manufactured products to different categories:
#Solids: cement, solar
Tot_Manuf_Solids = nr.triangular(0.06, 0.067, 0.08, 10000) + nr.triangular(0.00, 0.084, 0.17, 10000) 
#Liquids: Outpaints, Inpaintes, Glass, Ceramics
Tot_Manuf_Liquids = nr.triangular(0.18, 0.214, 0.44, 10000) + nr.triangular(0.32, 0.391, 0.46, 10000) + 2*(nr.triangular(0.10, 0.122, 0.14, 10000)) 


Manufacture.transfers = [cp.RandomChoiceTransfer(Tot_Manuf_Solids, Manuf_Solids, priority=2),
                        cp.RandomChoiceTransfer(Tot_Manuf_Liquids, Manuf_Liquids, priority=2)]

Manuf_Solids.transfers = [cp.StochasticTransfer(nr.triangular, [0.00000085, 0.0000017, 0.00000255], Manuf_Air_N, priority=2),
                           cp.StochasticTransfer(nr.uniform, [0.001, 0.0016], WW_N, priority=2),
                           cp.StochasticTransfer(nr.triangular, [0.005, 0.01, 0.015], ManufSolidW_Reuse_P, priority=2),
                           cp.ConstTransfer(1, Consumption, priority=1)]
Manuf_Liquids.transfers = [cp.StochasticTransfer(nr.triangular, [0.00000085, 0.0000017, 0.00000255], Manuf_Air_N, priority=2),
                           cp.StochasticTransfer(nr.uniform, [0.001, 0.0016], WW_N, priority=2),
                           cp.ConstTransfer(1, Consumption, priority=1)]


# In[24]:


# ENM allocation to product categories
Consumption.transfers = [cp.StochasticTransfer(nr.triangular, [0.18, 0.214, 0.44], OutPaints),
                         cp.StochasticTransfer(nr.triangular, [0.32, 0.391, 0.46], InPaints),
                         cp.StochasticTransfer(nr.triangular, [0.06, 0.067, 0.08], Cement),
                         cp.StochasticTransfer(nr.triangular, [0.10, 0.122, 0.14], Glass),
                         cp.StochasticTransfer(nr.triangular, [0.10, 0.122, 0.14], Ceramics),
                         cp.StochasticTransfer(nr.triangular, [0.00, 0.084, 0.17], Solar)]


# In[25]:


# Products categories to their USE and EoL compartments

#For pigment TiO2
#PersCare.transfers = [cp.ConstTransfer(1, PersCare_Use, priority=1),
#                      cp.StochasticTransfer(nr.triangular, [0.069, 0.11, 0.151], PersCare_EoL, priority=2)] 

OutPaints.transfers = [cp.ConstTransfer(1, OutPaints_EoL, priority=1),
                    cp.StochasticTransfer(nr.triangular, [0.005, 0.01, 0.015], OutPaints_Use, priority=2)]

InPaints.transfers = [cp.ConstTransfer(1, InPaints_EoL, priority=1),
                    cp.StochasticTransfer(tf.TriangTrunc, [0.001, 3.22, 1, 0, 1], InPaints_Use, priority=2)],

Cement.transfers = [cp.ConstTransfer(1, Cement_EoL, priority=1),
                    cp.StochasticTransfer(nr.triangular, [0.005, 0.01, 0.015], Cement_Use, priority=2)]

Glass.transfers = [cp.ConstTransfer(1, Glass_EoL, priority=1),
                   cp.StochasticTransfer(nr.triangular, [0.175, 0.35, 0.525], Glass_Use, priority=2)] 

Ceramics.transfers = [cp.ConstTransfer(1, Ceramics_EoL, priority=1),
                      cp.StochasticTransfer(nr.triangular, [0.175, 0.35, 0.525], Ceramics_Use, priority=2)] 

Solar.transfers = [cp.ConstTransfer(1, Solar_EoL, priority=1)]


# In[27]:


# OutPaints                           
OutPaints_Use.localRelease = cp.ListRelease([0.9,0.01666667,0.01666667,0.01666667,0.01666667,
                                          0.01666667,0.01666667])

OutPaints_EoL.localRelease = cp.ListRelease([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                                         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                                         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.001722281,
                                         0.001037804,0.001572363,0.00232936,0.003374171,0.004779078,
                                         0.006618624,0.00896268,0.01186737,0.01536449,0.01945038,
                                         0.02407602,0.0291399,0.03448561,0.03990567,0.04515209,
                                         0.04995371,0.05403864,0.0571594,0.05911772,0.05978529, 
                                         0.05911772,0.0571594,0.05403864,0.04995371,0.04515209,
                                         0.03990567,0.03448561,0.0291399,0.02407602,0.01945038,
                                         0.01536449,0.01186737,0.00896268,0.006618624,0.004779078,
                                         0.003374171,0.00232936,0.001572363,0.001037804,0.001722281]) 

OutPaints_Use.transfers = [cp.StochasticTransfer(nr.triangular, [0.25, 0.50, 0.75], OutPaints_WW, priority=1),
                        cp.StochasticTransfer(nr.triangular, [0.125, 0.25,0.375], OutPaints_Air, priority=1),
                        cp.StochasticTransfer(nr.triangular, [0.125, 0.25,0.375], OutPaints_NUsoil, priority=1)]

OutPaints_WW.transfers = [cp.StochasticTransfer(nr.triangular, [0.15, 0.30, 0.45], OutPaints_WW_N, priority=1),
                      cp.StochasticTransfer(tf.TriangTruncDet, [0.35, 0.7, 1.05, 1, 0, 1], OutPaints_WW_M, priority=1)]

OutPaints_Air.transfers = [cp.StochasticTransfer(nr.uniform, [1e-6, 1], OutPaints_Air_N, priority=1),
                       cp.StochasticTransfer(nr.uniform, [1e-6, 1], OutPaints_Air_M, priority=1)]

OutPaints_NUsoil.transfers = [cp.StochasticTransfer(nr.triangular, [0.15, 0.30, 0.45], OutPaints_NUsoil_N, priority=1),
                           cp.StochasticTransfer(tf.TriangTruncDet, [0.35, 0.70, 1.05, 1, 0, 1], OutPaints_NUsoil_M, priority=1)]

OutPaints_EoL.transfers = [cp.StochasticTransfer(tf.TriangTruncDet, [0.475, 0.95, 1.9, 1, 0, 1], CDW, priority=1),
                        cp.StochasticTransfer(nr.triangular, [0.025, 0.05, 0.075], MMSW, priority=1)]


# In[27.5]:

# InPaints                           

InPaints_Use.localRelease = cp.FixedRateRelease(0.1)

InPaints_EoL.localRelease = cp.ListRelease([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                                         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                                         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.001722281,
                                         0.001037804,0.001572363,0.00232936,0.003374171,0.004779078,
                                         0.006618624,0.00896268,0.01186737,0.01536449,0.01945038,
                                         0.02407602,0.0291399,0.03448561,0.03990567,0.04515209,
                                         0.04995371,0.05403864,0.0571594,0.05911772,0.05978529, 
                                         0.05911772,0.0571594,0.05403864,0.04995371,0.04515209,
                                         0.03990567,0.03448561,0.0291399,0.02407602,0.01945038,
                                         0.01536449,0.01186737,0.00896268,0.006618624,0.004779078,
                                         0.003374171,0.00232936,0.001572363,0.001037804,0.001722281]) 

InPaints_Use.transfers = [cp.StochasticTransfer(nr.triangular, [0.09, 0.11, 0.136], InPaints_WW, priority=1),
                        cp.StochasticTransfer(nr.triangular, [0.125, 0.25,0.375], InPaints_Air, priority=1),
                        cp.StochasticTransfer(nr.triangular, [0.512, 0.64,0.768], InPaints_NUsoil, priority=1)]

InPaints_WW.transfers = [cp.StochasticTransfer(nr.triangular, [0.15, 0.30, 0.45], InPaints_WW_N, priority=1),
                      cp.StochasticTransfer(tf.TriangTruncDet, [0.35, 0.7, 1.05, 1, 0, 1], InPaints_WW_M, priority=1)]

InPaints_Air.transfers = [cp.StochasticTransfer(nr.uniform, [1e-6, 1], InPaints_Air_N, priority=1),
                       cp.StochasticTransfer(nr.uniform, [1e-6, 1], InPaints_Air_M, priority=1)]

InPaints_NUsoil.transfers = [cp.StochasticTransfer(nr.triangular, [0.15, 0.30, 0.45], InPaints_NUsoil_N, priority=1),
                           cp.StochasticTransfer(tf.TriangTruncDet, [0.35, 0.70, 1.05, 1, 0, 1], InPaints_NUsoil_M, priority=1)]

InPaints_EoL.transfers = [cp.StochasticTransfer(tf.TriangTruncDet, [0.475, 0.95, 1.9, 1, 0, 1], CDW, priority=1),
                        cp.StochasticTransfer(nr.triangular, [0.025, 0.05, 0.075], MMSW, priority=1)]



# In[28]:


# Cement
Cement_Use.localRelease = cp.ListRelease([0.9,0.01666667,0.01666667,0.01666667,0.01666667,
                                          0.01666667,0.01666667,0.01666667])

Cement_EoL.localRelease = cp.ListRelease([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                                          0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.001722281,
                                          0.001037804,0.001572363,0.00232936,0.003374171,0.004779078,
                                          0.006618624,0.00896268,0.01186737,0.01536449,0.01945038,
                                          0.02407602,0.0291399,0.03448561,0.03990567,0.04515209,
                                          0.04995371,0.05403864,0.0571594,0.05911772,0.05978529,
                                          0.05911772,0.0571594,0.05403864,0.04995371,0.04515209,
                                          0.03990567,0.03448561,0.0291399,0.02407602,0.01945038,
                                          0.01536449,0.01186737,0.00896268,0.006618624,0.004779078,
                                          0.003374171,0.00232936,0.001572363,0.001037804,0.001722281]) 

Cement_Use.transfers = [cp.ConstTransfer(1, Cement_WW, priority=1)]
Cement_WW.transfers = [cp.StochasticTransfer(nr.uniform, [1e-6, 0.01], Cement_WW_N, priority=1),
                      cp.StochasticTransfer(nr.uniform, [0.99, 1], Cement_WW_M, priority=1)]

Cement_EoL.transfers = [cp.ConstTransfer(1, CDW, priority=1)]


# In[29]:


# Glass coatings
Glass_Use.localRelease = cp.ListRelease([0.9,0.01111111,0.01111111,0.01111111,0.01111111,
                                       0.01111111,0.01111111,0.01111111,0.01111111,0.01111111])

Glass_EoL.localRelease = cp.ListRelease([0,0,0,0,0.003466974,
                                       0.01439745,0.04894278,0.1172529,0.1980285,0.2358228,
                                       0.1980285,0.1172529,0.04894278,0.01439745,0.003466974]) 

Glass_Use.transfers = [cp.ConstTransfer(1, Glass_WW, priority=1),
                      cp.StochasticTransfer(nr.triangular, [0.05,0.10,0.15], Glass_Air, priority=2),
                      cp.StochasticTransfer(nr.triangular, [0.05,0.10,0.15], Glass_NUsoil, priority=2)]

Glass_WW.transfers = [cp.StochasticTransfer(nr.triangular, [0.1, 0.3, 0.5], Glass_WW_N, priority=1),
                     cp.StochasticTransfer(nr.triangular, [0.5, 0.7, 0.9], Glass_WW_M, priority=1)]

Glass_Air.transfers = [cp.StochasticTransfer(nr.uniform, [1e-6, 1], Glass_Air_N, priority=1),
                      cp.StochasticTransfer(nr.uniform, [1e-6, 1], Glass_Air_M, priority=1)]

Glass_NUsoil.transfers = [cp.StochasticTransfer(nr.triangular, [0.1, 0.3, 0.5], Glass_NUsoil_N, priority=1),
                         cp.StochasticTransfer(nr.triangular, [0.5, 0.7, 0.9], Glass_NUsoil_M, priority=1)]

Glass_EoL.transfers = [cp.ConstTransfer(1, CDW, priority=1)]


# In[30]:


# Ceramic coatings
Ceramics_Use.localRelease = cp.ListRelease([0.9,0.01111111,0.01111111,0.01111111,0.01111111, 
                                            0.01111111,0.01111111,0.01111111,0.01111111,0.01111111])

Ceramics_EoL.localRelease = cp.ListRelease([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                                         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
                                         0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0.001722281,
                                         0.001037804,0.001572363,0.00232936,0.003374171,0.004779078,
                                         0.006618624,0.00896268,0.01186737,0.01536449,0.01945038,
                                         0.02407602,0.0291399,0.03448561,0.03990567,0.04515209,
                                         0.04995371,0.05403864,0.0571594,0.05911772,0.05978529, 
                                         0.05911772,0.0571594,0.05403864,0.04995371,0.04515209,
                                         0.03990567,0.03448561,0.0291399,0.02407602,0.01945038,
                                         0.01536449,0.01186737,0.00896268,0.006618624,0.004779078,
                                         0.003374171,0.00232936,0.001572363,0.001037804,0.001722281]) 

Ceramics_Use.transfers = [cp.ConstTransfer(1, Ceramics_WW, priority=1),
                          cp.StochasticTransfer(nr.triangular, [0.05,0.10,0.15], Ceramics_Air, priority=2),
                          cp.StochasticTransfer(nr.triangular, [0.05,0.10,0.15], Ceramics_NUsoil, priority=2)]

Ceramics_WW.transfers = [cp.StochasticTransfer(nr.triangular, [0.1, 0.3, 0.5], Ceramics_WW_N, priority=1),
                         cp.StochasticTransfer(nr.triangular, [0.5, 0.7, 0.9], Ceramics_WW_M, priority=1)]

Ceramics_Air.transfers = [cp.StochasticTransfer(nr.uniform, [1e-6, 1], Ceramics_Air_N, priority=1),
                          cp.StochasticTransfer(nr.uniform, [1e-6, 1], Ceramics_Air_M, priority=1)]

Ceramics_NUsoil.transfers = [cp.StochasticTransfer(nr.triangular, [0.1, 0.3, 0.5], Ceramics_NUsoil_N, priority=1),
                             cp.StochasticTransfer(nr.triangular, [0.5, 0.7, 0.9], Ceramics_NUsoil_M, priority=1)]

Ceramics_EoL.transfers = [cp.ConstTransfer(1, CDW, priority=1)]



# In[32]:


# Solar 
# IRENA, 2016, End-of-life management - Solar Photovoltaic Panels Report: Average lifetime of a solar panel is 30 years.
# Since our model covers only 20 years and we assume no TiO2 was included in solar panels before 2000, we don't need to 
# look at what happens to waste, since the nano will still be in stock in 2020/2030.
# So I assume everything goes to waste at 21 years, and everything is reprocessed, only to give the model transfers.
Solar_EoL.localRelease = cp.ListRelease([0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                         0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])

Solar_EoL.transfers = [cp.ConstTransfer(1, SolarWaste, priority=1)]

# To change if the model goes further than 2030.
SolarWaste.transfers = [cp.ConstTransfer(1, Reprocess_Solar_P, priority=1)]


# In[37]:


##############################################################################
########################## WASTE MANAGEMENT ##################################
##############################################################################


################## sampling of the removal data from different sources ########
s = 10000 #sampling size used for sampling in uncertainty ranges of several sources/values


# In[38]:


#################################   WWTP   ####################################  


# In[39]:


# Gather all pristine flows to wastewater
OutPaints_WW_N.transfers = [cp.ConstTransfer(1, WW_N, priority=1)]
InPaints_WW_N.transfers = [cp.ConstTransfer(1, WW_N, priority=1)]
Cement_WW_N.transfers = [cp.ConstTransfer(1, WW_N, priority=1)]
Glass_WW_N.transfers = [cp.ConstTransfer(1, WW_N, priority=1)]
Ceramics_WW_N.transfers = [cp.ConstTransfer(1, WW_N, priority=1)]

# Gather all matrix-embedded flows to wastewater
OutPaints_WW_M.transfers = [cp.ConstTransfer(1, WW_M, priority=1)]
InPaints_WW_M.transfers = [cp.ConstTransfer(1, WW_M, priority=1)]
Cement_WW_M.transfers = [cp.ConstTransfer(1, WW_M, priority=1)]
Glass_WW_M.transfers = [cp.ConstTransfer(1, WW_M, priority=1)]
Ceramics_WW_M.transfers = [cp.ConstTransfer(1, WW_M, priority=1)]


# In[40]:


# From wastewater to non-sewer      
WW_NS_y0 = cp.TransferDistribution(nr.triangular, [0.0815, 0.163, 0.2445])
WW_NS_y1 = cp.TransferDistribution(nr.triangular, [0.075, 0.15, 0.225])
WW_NS_y2 = cp.TransferDistribution(nr.triangular, [0.0775, 0.155, 0.2325])
WW_NS_y3 = cp.TransferDistribution(nr.triangular, [0.0765, 0.153, 0.2295])
WW_NS_y4 = cp.TransferDistribution(nr.triangular, [0.076, 0.152, 0.228])
WW_NS_y5 = cp.TransferDistribution(nr.triangular, [0.0785, 0.157, 0.2355])
WW_NS_y6 = cp.TransferDistribution(nr.triangular, [0.067, 0.134, 0.201])
WW_NS_y7 = cp.TransferDistribution(nr.triangular, [0.0715, 0.143, 0.2145])
WW_NS_y8 = cp.TransferDistribution(nr.triangular, [0.071, 0.142, 0.213])
WW_NS_y9 = cp.TransferDistribution(nr.triangular, [0.072, 0.144, 0.216])
WW_NS_y10 = cp.TransferDistribution(nr.triangular, [0.0715, 0.143, 0.2145])
WW_NS_y11 = cp.TransferDistribution(nr.triangular, [0.074, 0.148, 0.222])
WW_NS_y12 = cp.TransferDistribution(nr.triangular, [0.0725, 0.145, 0.2175])
WW_NS_y13 = cp.TransferDistribution(nr.triangular, [0.072, 0.144, 0.216])
WW_NS_y14 = cp.TransferDistribution(nr.triangular, [0.071, 0.142, 0.213])
WW_NS_y15 = cp.TransferDistribution(nr.triangular, [0.0715, 0.143, 0.2145])
WW_NS_y16 = cp.TransferDistribution(nr.triangular, [0.0715, 0.143, 0.2145])
WW_NS_y17 = cp.TransferDistribution(nr.triangular, [0.0715, 0.143, 0.2145])
WW_NS_y18 = cp.TransferDistribution(nr.triangular, [0.0715, 0.143, 0.2145])
WW_NS_y19 = cp.TransferDistribution(nr.triangular, [0.0715, 0.143, 0.2145])
WW_NS_y20 = cp.TransferDistribution(nr.triangular, [0.072, 0.144, 0.216])

WW_N.transfers = [cp.TimeDependendDistributionTransfer([WW_NS_y0,
                                                        WW_NS_y1,WW_NS_y2,WW_NS_y3,WW_NS_y4,WW_NS_y5,
                                                        WW_NS_y6,WW_NS_y7,WW_NS_y8,WW_NS_y9,WW_NS_y10,
                                                        WW_NS_y11,WW_NS_y12,WW_NS_y13,WW_NS_y14,WW_NS_y15,
                                                        WW_NS_y16,WW_NS_y17,WW_NS_y18,WW_NS_y19,WW_NS_y20],
                                                       NoSewageSystem_N, WW_N, priority=2), 
                        cp.ConstTransfer(1, SewageSystem_N, priority=1)]

WW_M.transfers = [cp.TimeDependendDistributionTransfer([WW_NS_y0,
                                                        WW_NS_y1,WW_NS_y2,WW_NS_y3,WW_NS_y4,WW_NS_y5,
                                                        WW_NS_y6,WW_NS_y7,WW_NS_y8,WW_NS_y9,WW_NS_y10,
                                                        WW_NS_y11,WW_NS_y12,WW_NS_y13,WW_NS_y14,WW_NS_y15,
                                                        WW_NS_y16,WW_NS_y17,WW_NS_y18,WW_NS_y19,WW_NS_y20],
                                                       NoSewageSystem_M, WW_M, priority=2), 
                        cp.ConstTransfer(1, SewageSystem_M, priority=1)]

WW_T.transfers = [cp.TimeDependendDistributionTransfer([WW_NS_y0,
                                                        WW_NS_y1,WW_NS_y2,WW_NS_y3,WW_NS_y4,WW_NS_y5,
                                                        WW_NS_y6,WW_NS_y7,WW_NS_y8,WW_NS_y9,WW_NS_y10,
                                                        WW_NS_y11,WW_NS_y12,WW_NS_y13,WW_NS_y14,WW_NS_y15,
                                                        WW_NS_y16,WW_NS_y17,WW_NS_y18,WW_NS_y19,WW_NS_y20],
                                                       NoSewageSystem_T, WW_T, priority=2), 
                        cp.ConstTransfer(1, SewageSystem_T, priority=1)]

NoSewageSystem_N.transfers = [cp.ConstTransfer(0.03, NoSew_SW_N, priority=1),   
                            cp.ConstTransfer(0.11, OnSiteTreat_N, priority=1)]

NoSewageSystem_M.transfers = [cp.ConstTransfer(0.03, NoSew_SW_M, priority=1),   
                            cp.ConstTransfer(0.11, OnSiteTreat_M, priority=1)]

NoSewageSystem_T.transfers = [cp.ConstTransfer(0.03, NoSew_SW_T, priority=1),   
                            cp.ConstTransfer(0.11, OnSiteTreat_T, priority=1)]
                       
OnSiteTreat_N.transfers = [cp.ConstTransfer(1, TreatIOnSite_N, priority=1)]

OnSiteTreat_M.transfers = [cp.ConstTransfer(1, TreatIOnSite_M, priority=1)]

OnSiteTreat_T.transfers = [cp.ConstTransfer(1, TreatIOnSite_T, priority=1)]


# In[41]:


# From sewer system to surface water (non-treated, NT)

SS_NT_y0 = cp.TransferDistribution(nr.triangular, [0.0325, 0.065, 0.0975])
SS_NT_y1 = cp.TransferDistribution(nr.triangular, [0.034, 0.068, 0.102])
SS_NT_y2 = cp.TransferDistribution(nr.triangular, [0.028, 0.056, 0.084])
SS_NT_y3 = cp.TransferDistribution(nr.triangular, [0.0245, 0.049, 0.0735])
SS_NT_y4 = cp.TransferDistribution(nr.triangular, [0.0225, 0.045, 0.0675])
SS_NT_y5 = cp.TransferDistribution(nr.triangular, [0.018, 0.036, 0.054])
SS_NT_y6 = cp.TransferDistribution(nr.triangular, [0.0285, 0.057, 0.0855])
SS_NT_y7 = cp.TransferDistribution(nr.triangular, [0.024, 0.048, 0.072])
SS_NT_y8 = cp.TransferDistribution(nr.triangular, [0.0235, 0.047, 0.0705])
SS_NT_y9 = cp.TransferDistribution(nr.triangular, [0.0205, 0.041, 0.0615])
SS_NT_y10 = cp.TransferDistribution(nr.triangular, [0.0185, 0.037, 0.0555])
SS_NT_y11 = cp.TransferDistribution(nr.triangular, [0.016, 0.032, 0.048])
SS_NT_y12 = cp.TransferDistribution(nr.triangular, [0.014, 0.028, 0.042])
SS_NT_y13 = cp.TransferDistribution(nr.triangular, [0.0125, 0.025, 0.0375])
SS_NT_y14 = cp.TransferDistribution(nr.triangular, [0.0105, 0.021, 0.0315])
SS_NT_y15 = cp.TransferDistribution(nr.triangular, [0.0085, 0.017, 0.0255])
SS_NT_y16 = cp.TransferDistribution(nr.triangular, [0.007, 0.014, 0.021])
SS_NT_y17 = cp.TransferDistribution(nr.triangular, [0.005, 0.01, 0.015])
SS_NT_y18 = cp.TransferDistribution(nr.triangular, [0.0035, 0.007, 0.0105])
SS_NT_y19 = cp.TransferDistribution(nr.triangular, [0.0015, 0.003, 0.0045])
SS_NT_y20 = cp.TransferDistribution(nr.triangular, [0, 0, 0.0001]) # changed by hand to be different from 0
                           
SewageSystem_N.transfers= [cp.StochasticTransfer(nr.triangular,[0.016, 0.032, 0.048], STPoverflow_N, priority=2),  # overflow rate
                         cp.StochasticTransfer(nr.triangular, [0.0325, 0.065, 0.0975], Sew_Subsurface_N, priority=2), #Exfiltration
                         cp.TimeDependendDistributionTransfer([SS_NT_y0,
                                                               SS_NT_y1,SS_NT_y2,SS_NT_y3,SS_NT_y4,SS_NT_y5,
                                                               SS_NT_y6,SS_NT_y7,SS_NT_y8,SS_NT_y9,SS_NT_y10,
                                                               SS_NT_y11,SS_NT_y12,SS_NT_y13,SS_NT_y14,SS_NT_y15,
                                                               SS_NT_y16,SS_NT_y17,SS_NT_y18,SS_NT_y19,SS_NT_y20],
                                                       Sew_SW_N, SewageSystem_N, priority=2), #discharges of sewer to nature (when no wwtp is installed)
                         cp.ConstTransfer(1, WWTP_N, priority=1)]

SewageSystem_M.transfers= [cp.StochasticTransfer(nr.triangular,[0.016, 0.032, 0.048], STPoverflow_M, priority=2),  # overflow rate
                         cp.StochasticTransfer(nr.triangular, [0.0325, 0.065, 0.0975], Sew_Subsurface_M, priority=2), #Exfiltration
                         cp.TimeDependendDistributionTransfer([SS_NT_y0,
                                                               SS_NT_y1,SS_NT_y2,SS_NT_y3,SS_NT_y4,SS_NT_y5,
                                                               SS_NT_y6,SS_NT_y7,SS_NT_y8,SS_NT_y9,SS_NT_y10,
                                                               SS_NT_y11,SS_NT_y12,SS_NT_y13,SS_NT_y14,SS_NT_y15,
                                                               SS_NT_y16,SS_NT_y17,SS_NT_y18,SS_NT_y19,SS_NT_y20],
                                                       Sew_SW_M, SewageSystem_M, priority=2), #discharges of sewer to nature (when no wwtp is installed)
                         cp.ConstTransfer(1, WWTP_M, priority=1)]

SewageSystem_T.transfers= [cp.StochasticTransfer(nr.triangular,[0.016, 0.032, 0.048], STPoverflow_T, priority=2),  # overflow rate
                         cp.StochasticTransfer(nr.triangular, [0.0325, 0.065, 0.0975], Sew_Subsurface_T, priority=2), #Exfiltration
                         cp.TimeDependendDistributionTransfer([SS_NT_y0,
                                                               SS_NT_y1,SS_NT_y2,SS_NT_y3,SS_NT_y4,SS_NT_y5,
                                                               SS_NT_y6,SS_NT_y7,SS_NT_y8,SS_NT_y9,SS_NT_y10,
                                                               SS_NT_y11,SS_NT_y12,SS_NT_y13,SS_NT_y14,SS_NT_y15,
                                                               SS_NT_y16,SS_NT_y17,SS_NT_y18,SS_NT_y19,SS_NT_y20],
                                                      Sew_SW_T, SewageSystem_T, priority=2), #discharges of sewer to nature (when no wwtp is installed)
                         cp.ConstTransfer(1, WWTP_T, priority=1)]


# In[42]:


# Levels of treatment in WWTP

WWTP_TI_y0 = cp.TransferDistribution(nr.triangular, [0.0295, 0.059, 0.0885])
WWTP_TI_y1 = cp.TransferDistribution(nr.triangular, [0.0255, 0.051, 0.0765])
WWTP_TI_y2 = cp.TransferDistribution(nr.triangular, [0.021, 0.042, 0.063])
WWTP_TI_y3 = cp.TransferDistribution(nr.triangular, [0.0175, 0.035, 0.0525])
WWTP_TI_y4 = cp.TransferDistribution(nr.triangular, [0.014, 0.028, 0.042])
WWTP_TI_y5 = cp.TransferDistribution(nr.triangular, [0.011, 0.022, 0.033])
WWTP_TI_y6 = cp.TransferDistribution(nr.triangular, [0.012, 0.024, 0.036])
WWTP_TI_y7 = cp.TransferDistribution(nr.triangular, [0.0105, 0.021, 0.0315])
WWTP_TI_y8 = cp.TransferDistribution(nr.triangular, [0.011, 0.022, 0.033])
WWTP_TI_y9 = cp.TransferDistribution(nr.triangular, [0.008, 0.016, 0.024])
WWTP_TI_y10 = cp.TransferDistribution(nr.triangular, [0.0075, 0.015, 0.0225])
WWTP_TI_y11 = cp.TransferDistribution(nr.triangular, [0.0065, 0.013, 0.0195])
WWTP_TI_y12 = cp.TransferDistribution(nr.triangular, [0.0055, 0.011, 0.0165])
WWTP_TI_y13 = cp.TransferDistribution(nr.triangular, [0.005, 0.01, 0.015])
WWTP_TI_y14 = cp.TransferDistribution(nr.triangular, [0.004, 0.008, 0.012])
WWTP_TI_y15 = cp.TransferDistribution(nr.triangular, [0.0035, 0.007, 0.0105])
WWTP_TI_y16 = cp.TransferDistribution(nr.triangular, [0.0025, 0.005, 0.0075])
WWTP_TI_y17 = cp.TransferDistribution(nr.triangular, [0.002, 0.004, 0.006])
WWTP_TI_y18 = cp.TransferDistribution(nr.triangular, [0.0015, 0.003, 0.0045])
WWTP_TI_y19 = cp.TransferDistribution(nr.triangular, [0.0005, 0.001, 0.0015])
WWTP_TI_y20 = cp.TransferDistribution(nr.triangular, [0, 0, 0.00001]) # adapted by hand to be not equal 0

WWTP_TII_y0 = cp.TransferDistribution(nr.triangular, [0.1725, 0.345, 0.5175])
WWTP_TII_y1 = cp.TransferDistribution(nr.triangular, [0.1615, 0.323, 0.4845])
WWTP_TII_y2 = cp.TransferDistribution(nr.triangular, [0.161, 0.322, 0.483])
WWTP_TII_y3 = cp.TransferDistribution(nr.triangular, [0.1535, 0.307, 0.4605])
WWTP_TII_y4 = cp.TransferDistribution(nr.triangular, [0.145, 0.29, 0.435])
WWTP_TII_y5 = cp.TransferDistribution(nr.triangular, [0.123, 0.246, 0.369])
WWTP_TII_y6 = cp.TransferDistribution(nr.triangular, [0.1305, 0.261, 0.3915])
WWTP_TII_y7 = cp.TransferDistribution(nr.triangular, [0.124, 0.248, 0.372])
WWTP_TII_y8 = cp.TransferDistribution(nr.triangular, [0.118, 0.236, 0.354])
WWTP_TII_y9 = cp.TransferDistribution(nr.triangular, [0.1125, 0.225, 0.3375])
WWTP_TII_y10 = cp.TransferDistribution(nr.triangular, [0.108, 0.216, 0.324])
WWTP_TII_y11 = cp.TransferDistribution(nr.triangular, [0.105, 0.21, 0.315])
WWTP_TII_y12 = cp.TransferDistribution(nr.triangular, [0.1025, 0.205, 0.3075])
WWTP_TII_y13 = cp.TransferDistribution(nr.triangular, [0.0975, 0.195, 0.2925])
WWTP_TII_y14 = cp.TransferDistribution(nr.triangular, [0.0925, 0.185, 0.2775])
WWTP_TII_y15 = cp.TransferDistribution(nr.triangular, [0.0875, 0.175, 0.2625])
WWTP_TII_y16 = cp.TransferDistribution(nr.triangular, [0.083, 0.166, 0.249])
WWTP_TII_y17 = cp.TransferDistribution(nr.triangular, [0.0785, 0.157, 0.2355])
WWTP_TII_y18 = cp.TransferDistribution(nr.triangular, [0.074, 0.148, 0.222])
WWTP_TII_y19 = cp.TransferDistribution(nr.triangular, [0.0706, 0.139, 0.2074])
WWTP_TII_y20 = cp.TransferDistribution(nr.triangular, [0.0609, 0.109, 0.1571])

WWTP_N.transfers = [cp.TimeDependendDistributionTransfer([WWTP_TI_y0,
                                                        WWTP_TI_y1,WWTP_TI_y2,WWTP_TI_y3,WWTP_TI_y4,WWTP_TI_y5,
                                                        WWTP_TI_y6,WWTP_TI_y7,WWTP_TI_y8,WWTP_TI_y9,WWTP_TI_y10,
                                                        WWTP_TI_y11,WWTP_TI_y12,WWTP_TI_y13,WWTP_TI_y14,WWTP_TI_y15,
                                                        WWTP_TI_y16,WWTP_TI_y17,WWTP_TI_y18,WWTP_TI_y19,WWTP_TI_y20],
                                                        TreatI_N, WWTP_N, priority=2),
                  cp.TimeDependendDistributionTransfer([WWTP_TII_y0,
                                                        WWTP_TII_y1,WWTP_TII_y2,WWTP_TII_y3,WWTP_TII_y4,WWTP_TII_y5,
                                                        WWTP_TII_y6,WWTP_TII_y7,WWTP_TII_y8,WWTP_TII_y9,WWTP_TII_y10,
                                                        WWTP_TII_y11,WWTP_TII_y12,WWTP_TII_y13,WWTP_TII_y14,WWTP_TII_y15,
                                                        WWTP_TII_y16,WWTP_TII_y17,WWTP_TII_y18,WWTP_TII_y19,WWTP_TII_y20],
                                                        TreatII_N, WWTP_N, priority=2),
                  cp.ConstTransfer(1, TreatIII_N, priority=1)]

WWTP_M.transfers = [cp.TimeDependendDistributionTransfer([WWTP_TI_y0,
                                                        WWTP_TI_y1,WWTP_TI_y2,WWTP_TI_y3,WWTP_TI_y4,WWTP_TI_y5,
                                                        WWTP_TI_y6,WWTP_TI_y7,WWTP_TI_y8,WWTP_TI_y9,WWTP_TI_y10,
                                                        WWTP_TI_y11,WWTP_TI_y12,WWTP_TI_y13,WWTP_TI_y14,WWTP_TI_y15,
                                                        WWTP_TI_y16,WWTP_TI_y17,WWTP_TI_y18,WWTP_TI_y19,WWTP_TI_y20],
                                                        TreatI_M, WWTP_M, priority=2),
                  cp.TimeDependendDistributionTransfer([WWTP_TII_y0,
                                                        WWTP_TII_y1,WWTP_TII_y2,WWTP_TII_y3,WWTP_TII_y4,WWTP_TII_y5,
                                                        WWTP_TII_y6,WWTP_TII_y7,WWTP_TII_y8,WWTP_TII_y9,WWTP_TII_y10,
                                                        WWTP_TII_y11,WWTP_TII_y12,WWTP_TII_y13,WWTP_TII_y14,WWTP_TII_y15,
                                                        WWTP_TII_y16,WWTP_TII_y17,WWTP_TII_y18,WWTP_TII_y19,WWTP_TII_y20],
                                                        TreatII_M, WWTP_M, priority=2),
                  cp.ConstTransfer(1, TreatIII_M, priority=1)]

WWTP_T.transfers = [cp.TimeDependendDistributionTransfer([WWTP_TI_y0,
                                                        WWTP_TI_y1,WWTP_TI_y2,WWTP_TI_y3,WWTP_TI_y4,WWTP_TI_y5,
                                                        WWTP_TI_y6,WWTP_TI_y7,WWTP_TI_y8,WWTP_TI_y9,WWTP_TI_y10,
                                                        WWTP_TI_y11,WWTP_TI_y12,WWTP_TI_y13,WWTP_TI_y14,WWTP_TI_y15,
                                                        WWTP_TI_y16,WWTP_TI_y17,WWTP_TI_y18,WWTP_TI_y19,WWTP_TI_y20],
                                                        TreatI_T, WWTP_T, priority=2),
                  cp.TimeDependendDistributionTransfer([WWTP_TII_y0,
                                                        WWTP_TII_y1,WWTP_TII_y2,WWTP_TII_y3,WWTP_TII_y4,WWTP_TII_y5,
                                                        WWTP_TII_y6,WWTP_TII_y7,WWTP_TII_y8,WWTP_TII_y9,WWTP_TII_y10,
                                                        WWTP_TII_y11,WWTP_TII_y12,WWTP_TII_y13,WWTP_TII_y14,WWTP_TII_y15,
                                                        WWTP_TII_y16,WWTP_TII_y17,WWTP_TII_y18,WWTP_TII_y19,WWTP_TII_y20],
                                                        TreatII_T, WWTP_T, priority=2),
                  cp.ConstTransfer(1, TreatIII_T, priority=1)]


# In[43]:


RemovalData_TreatI = np.concatenate([
        nr.triangular(0, 0, 0.000001, s*0), nr.uniform( 0, 0.1, int(s*0.91)), nr.triangular(0.1, 0.1, 0.12, int(s*0.09))]) # Johnson et al., 2011

TreatI_N.transfers = [cp.RandomChoiceTransfer(RemovalData_TreatI, STPsludge_N, priority=2),
                      cp.ConstTransfer(1, STPeffluent_N, priority=1)]

TreatI_T.transfers = [cp.RandomChoiceTransfer(RemovalData_TreatI, STPsludge_T, priority=2),
                      cp.ConstTransfer(1, STPeffluent_T, priority=1)]



TreatIOnSite_N.transfers = [cp.RandomChoiceTransfer(RemovalData_TreatI, OnSiteSludge_N, priority=2),
                          cp.ConstTransfer(1, OnSiteTreat_Subsurface_N, priority=1)]

TreatIOnSite_T.transfers = [cp.RandomChoiceTransfer(RemovalData_TreatI, OnSiteSludge_T, priority=2),
                          cp.ConstTransfer(1, OnSiteTreat_Subsurface_T, priority=1)]

# We make the assumption that matrix-embedded ENMs behave as microplastics in WWTP, since they have about the same size.
# Three sources are available that studied the removal of MPs after primary treatment in Europe:
# Murphy et al. 2016: 78.34% go to sludge, with a coefficient of variation of 8%.
# Talvitie et al. 2015: from their data, we build a triangular distribution with min of 25.8%, mode of 50% and max of 92.5%.
# Lares et al. 2018: from their data, we build a triangular distribution with min of 91.9%, mode of 99% and max of 99%.
Removal_Murphy = nr.triangular(0.7834*(1-0.08), 0.7834, 0.7834*(1+0.08), 3333)
Removal_Talvitie = nr.triangular(0.258, 0.5, 0.925, 3333)
Removal_Lares = nr.triangular(0.919, 0.99, 0.99, 3333)
RemovalData_TreatI_M = np.concatenate([Removal_Murphy, Removal_Talvitie, Removal_Lares])

TreatI_M.transfers = [cp.RandomChoiceTransfer(RemovalData_TreatI_M, STPsludge_M, priority=2),
                      cp.ConstTransfer(1, STPeffluent_M, priority=1)]

TreatIOnSite_M.transfers = [cp.RandomChoiceTransfer(RemovalData_TreatI_M, OnSiteSludge_M, priority=2),
                          cp.ConstTransfer(1, OnSiteTreat_Subsurface_M, priority=1)]


# In[44]:


NonRemovalData_TreatII = np.concatenate([ #inversed from removal data
        nr.triangular(0.084, 0.105, 0.126, s), # Johnson et al., 2011
        nr.triangular(0.376, 0.47, 0.564, s), # Shi et al., 2016
        nr.triangular(0.208, 0.26, 0.312, s), # Shi et al., 2016
        nr.triangular(0.008, 0.01, 0.01, int(s*0.08)), nr.uniform(0.01, 0.02, int(s*0.77)), nr.triangular( 0.02, 0.02, 0.024, int(s*0.15)), # Westerhoff et al., 2011
        nr.uniform(0, 0.04, int(s*0.91)), nr.triangular(0.04, 0.04, 0.048, int(s*0.09)), # Westerhoff et al., 2011
        nr.triangular(0.016, 0.02, 0.02, int(s*0.05)), nr.uniform(0.02, 0.05, int(s*0.81)), nr.triangular(0.05, 0.05, 0.06, int(s*0.14)), # Westerhoff et al., 2011
        nr.uniform(0, 0.02, int(s*0.91)), nr.triangular(0.02, 0.02, 0.024, int(s*0.09)), # Westerhoff et al., 2011
        nr.triangular(0.016, 0.02, 0.02, int(s*0.13)), nr.uniform(0.02, 0.03, int(s*0.67)), nr.triangular(0.03, 0.03, 0.036, int(s*0.2)), # Westerhoff et al., 2011
         ]) 

TreatII_N.transfers = [cp.RandomChoiceTransfer(NonRemovalData_TreatII, STPeffluent_N, priority=2),
                      cp.ConstTransfer(1, STPsludge_N, priority=1)]

TreatII_T.transfers = [cp.RandomChoiceTransfer(NonRemovalData_TreatII, STPeffluent_T, priority=2),
                      cp.ConstTransfer(1, STPsludge_T, priority=1)]

# We make the assumption that matrix-embedded ENMs behave as microplastics in WWTP, since they have about the same size.
# Four sources are available that studied the removal of MPs after secondary treatment in Europe:
# Murphy et al. 2016: 98.41% go to sludge, with a coefficient of variation of 16%.
# Talvitie et al. 2015: from their data, we build a triangular distribution with min of 96.5%, mode of 97.8% and max of 98.1%.
# Magnusson and Norén 2014: uniform distribution within 99.94% and 99.95%.
# Lares et al. 2018: from their data, we build a triangular distribution with min of 81.1%, mode of 98.3% and max of 98.3%.
Removal_Murphy = nr.triangular(0.9841*(1-0.16), 0.9841, 0.9841*(1+0.16), 2500)
Removal_Talvitie = nr.triangular(0.965, 0.978, 0.981, 2500)
Removal_Magnusson = nr.uniform(0.9994, 0.9995, 2500)
Removal_Lares = nr.triangular(0.811, 0.983, 0.983, 2500)
RemovalData_TreatII_M = np.concatenate([Removal_Murphy, Removal_Talvitie, Removal_Magnusson])

TreatII_M.transfers = [cp.RandomChoiceTransfer(RemovalData_TreatII_M, STPsludge_M, priority=2),
                      cp.ConstTransfer(1, STPeffluent_M, priority=1)]


# In[45]:


NonRemovalData_TreatIII = np.concatenate([ # 1-removal data 
        nr.triangular(0.208, 0.26, 0.312, s), # Shi et al., 2016
        nr.triangular(0.12, 0.15, 0.18, s),   # Shi et al., 2016     
        nr.uniform(0, 0.03, int(s*0.91)), nr.triangular(0.03, 0.03, 0.036, int(s*0.09)), # Westerhoff et al., 2011
        nr.uniform(0, 0.1, int(s*0.91)), nr.triangular(0.1, 0.1, 0.12, int(s*0.09)), # Westerhoff et al., 2011
        nr.uniform(0, 0.01, int(s*0.91)), nr.triangular(0.01, 0.01, 0.012, int(s*0.09)), # Westerhoff et al., 2011
        nr.uniform(0, 0.02, int(s*0.91)), nr.triangular(0.02, 0.02, 0.024, int(s*0.09)), # Westerhoff et al., 2011
        nr.triangular(0.008, 0.01, 0.01, int(s*0.01)), nr.uniform(0.01, 0.08, int(s*0.89)), nr.triangular(0.08, 0.08, 0.096, int(s*0.1)), # Zhang et al., 2008
          ]) 
         
TreatIII_N.transfers = [cp.RandomChoiceTransfer(NonRemovalData_TreatIII, STPeffluent_N, priority=2),
                      cp.ConstTransfer(1, STPsludge_N, priority=1)]

TreatIII_T.transfers = [cp.RandomChoiceTransfer(NonRemovalData_TreatIII, STPeffluent_T, priority=2),
                      cp.ConstTransfer(1, STPsludge_T, priority=1)]

# We make the assumption that matrix-embedded ENMs behave as microplastics in WWTP, since they have about the same size.
# Two sources are available that studied the removal of MPs after secondary treatment in Europe:
# Magni et al. 2019: from their data, we build a triangular distribution with min of 67.5%, mode of 84% and max of 91%.
# Lares et al. 2018: from their data, we build a triangular distribution with min of 94.6%, mode of 99.3% and max of 99.8%.
Removal_Magni = nr.triangular(0.675, 0.84, 0.91, 5000)
Removal_Lares = nr.triangular(0.946, 0.993, 0.998, 5000)
RemovalData_TreatIII_M = np.concatenate([Removal_Magni, Removal_Lares])

TreatIII_M.transfers = [cp.RandomChoiceTransfer(RemovalData_TreatIII_M, STPsludge_M, priority=2),
                      cp.ConstTransfer(1, STPeffluent_M, priority=1)]


# In[46]:


# Transfers from sludge

# To incineration
# Eurostat, for year 2014: 73.45% incinerated in Austria.
# Mean of this value for Europe for year 2014: 30.1% (this model).
# It results a scaling factor of 2.416. 
# Before multiplication by 2.416, distributions must not exceed 0.414.


SG_WIIP_y0_data = (nr.triangular(0.1887, 0.209, 0.2293, s))
SG_WIIP_y1_data = (nr.triangular(0.1822, 0.213, 0.2438, s))
SG_WIIP_y2_data = (nr.triangular(0.1754, 0.217, 0.2586, s))
SG_WIIP_y3_data = (nr.triangular(0.1792, 0.221, 0.2628, s))
SG_WIIP_y4_data = (nr.triangular(0.1943, 0.225, 0.2557, s))
SG_WIIP_y5_data = (nr.triangular(0.2098, 0.229, 0.2482, s))
SG_WIIP_y6_data = (nr.triangular(0.2170, 0.256, 0.2950, s))
SG_WIIP_y7_data = (nr.triangular(0.2228, 0.286, 0.3492, s))
SG_WIIP_y8_data = (nr.triangular(0.2411, 0.317, 0.3929, s))
SG_WIIP_y9_data = (nr.triangular(0.2526, 0.319, 0.3854, s))
SG_WIIP_y10_data = (nr.triangular(0.2643, 0.321, 0.3777, s))
SG_WIIP_y11_data = (nr.triangular(0.2231, 0.315, 0.4069, s))
SG_WIIP_y12_data = (tf.TriangTruncDet(0.1868, 0.315, 0.4432, s, 0, 0.414))
SG_WIIP_y13_data = (tf.TriangTruncDet(0.1780, 0.308, 0.4381, s, 0, 0.414))
SG_WIIP_y14_data = (tf.TriangTruncDet(0.1693, 0.301, 0.4327, s, 0, 0.414))
SG_WIIP_y15_data = (tf.TriangTruncDet(0.1614, 0.315, 0.4686, s, 0, 0.414))
SG_WIIP_y16_data = (tf.TriangTruncDet(0.1645, 0.329, 0.4935, s, 0, 0.414))
SG_WIIP_y17_data = (tf.TriangTruncDet(0.1715, 0.343, 0.5145, s, 0, 0.414))
SG_WIIP_y18_data = (tf.TriangTruncDet(0.1785, 0.357, 0.5355, s, 0, 0.414))
SG_WIIP_y19_data = (tf.TriangTruncDet(0.1901, 0.371, 0.5519, s, 0, 0.414))
SG_WIIP_y20_data = (tf.TriangTruncDet(0.2171, 0.386, 0.5549, s, 0, 0.414))

SG_WIIP_y0 = cp.TransferDistribution(nr.choice, [SG_WIIP_y0_data])
SG_WIIP_y1 = cp.TransferDistribution(nr.choice, [SG_WIIP_y1_data])
SG_WIIP_y2 = cp.TransferDistribution(nr.choice, [SG_WIIP_y2_data])
SG_WIIP_y3 = cp.TransferDistribution(nr.choice, [SG_WIIP_y3_data])
SG_WIIP_y4 = cp.TransferDistribution(nr.choice, [SG_WIIP_y4_data])
SG_WIIP_y5 = cp.TransferDistribution(nr.choice, [SG_WIIP_y5_data])
SG_WIIP_y6 = cp.TransferDistribution(nr.choice, [SG_WIIP_y6_data])
SG_WIIP_y7 = cp.TransferDistribution(nr.choice, [SG_WIIP_y7_data])
SG_WIIP_y8 = cp.TransferDistribution(nr.choice, [SG_WIIP_y8_data])
SG_WIIP_y9 = cp.TransferDistribution(nr.choice, [SG_WIIP_y9_data])
SG_WIIP_y10 = cp.TransferDistribution(nr.choice, [SG_WIIP_y10_data])
SG_WIIP_y11 = cp.TransferDistribution(nr.choice, [SG_WIIP_y11_data])
SG_WIIP_y12 = cp.TransferDistribution(nr.choice, [SG_WIIP_y12_data])
SG_WIIP_y13 = cp.TransferDistribution(nr.choice, [SG_WIIP_y13_data])
SG_WIIP_y14 = cp.TransferDistribution(nr.choice, [SG_WIIP_y14_data])
SG_WIIP_y15 = cp.TransferDistribution(nr.choice, [SG_WIIP_y15_data])
SG_WIIP_y16 = cp.TransferDistribution(nr.choice, [SG_WIIP_y16_data])
SG_WIIP_y17 = cp.TransferDistribution(nr.choice, [SG_WIIP_y17_data])
SG_WIIP_y18 = cp.TransferDistribution(nr.choice, [SG_WIIP_y18_data])
SG_WIIP_y19 = cp.TransferDistribution(nr.choice, [SG_WIIP_y19_data])
SG_WIIP_y20 = cp.TransferDistribution(nr.choice, [SG_WIIP_y20_data])

# Sludge to landfill
# Eurostat, for year 2014: 1.99% landfilled in Austria.
# Mean of this value for Europe for year 2014: 10.5% (this model).
# It results a scaling factor of 0.189.


SG_LF_y0_data = (nr.triangular(0.1887, 0.209, 0.2293, s))
SG_LF_y1_data = (nr.triangular(0.1780, 0.208, 0.2380, s))
SG_LF_y2_data = (nr.triangular(0.1681, 0.208, 0.2479, s))
SG_LF_y3_data = (nr.triangular(0.1678, 0.207, 0.2462, s))
SG_LF_y4_data = (nr.triangular(0.1779, 0.206, 0.2341, s))
SG_LF_y5_data = (nr.triangular(0.1878, 0.205, 0.2222, s))
SG_LF_y6_data = (nr.triangular(0.1729, 0.204, 0.2351, s))
SG_LF_y7_data = (nr.triangular(0.1581, 0.203, 0.2479, s))
SG_LF_y8_data = (nr.triangular(0.1544, 0.203, 0.2516, s))
SG_LF_y9_data = (nr.triangular(0.1457, 0.184, 0.2223, s))
SG_LF_y10_data = (nr.triangular(0.1375, 0.167, 0.1965, s))
SG_LF_y11_data = (nr.triangular(0.1069, 0.151, 0.1951, s))
SG_LF_y12_data = (nr.triangular(0.0818, 0.138, 0.1942, s))
SG_LF_y13_data = (nr.triangular(0.0699, 0.121, 0.1721, s))
SG_LF_y14_data = (nr.triangular(0.0591, 0.105, 0.1509, s))
SG_LF_y15_data = (nr.triangular(0.0567, 0.102, 0.1473, s))
SG_LF_y16_data = (nr.triangular(0.0539, 0.098, 0.1421, s))
SG_LF_y17_data = (nr.triangular(0.0516, 0.095, 0.1384, s))
SG_LF_y18_data = (nr.triangular(0.0579, 0.091, 0.1241, s))
SG_LF_y19_data = (nr.triangular(0.0642, 0.088, 0.1118, s))
SG_LF_y20_data = (nr.triangular(0.0692, 0.084, 0.0988, s))

SG_LF_y0 = cp.TransferDistribution(nr.choice, [SG_LF_y0_data])
SG_LF_y1 = cp.TransferDistribution(nr.choice, [SG_LF_y1_data])
SG_LF_y2 = cp.TransferDistribution(nr.choice, [SG_LF_y2_data])
SG_LF_y3 = cp.TransferDistribution(nr.choice, [SG_LF_y3_data])
SG_LF_y4 = cp.TransferDistribution(nr.choice, [SG_LF_y4_data])
SG_LF_y5 = cp.TransferDistribution(nr.choice, [SG_LF_y5_data])
SG_LF_y6 = cp.TransferDistribution(nr.choice, [SG_LF_y6_data])
SG_LF_y7 = cp.TransferDistribution(nr.choice, [SG_LF_y7_data])
SG_LF_y8 = cp.TransferDistribution(nr.choice, [SG_LF_y8_data])
SG_LF_y9 = cp.TransferDistribution(nr.choice, [SG_LF_y9_data])
SG_LF_y10 = cp.TransferDistribution(nr.choice, [SG_LF_y10_data])
SG_LF_y11 = cp.TransferDistribution(nr.choice, [SG_LF_y11_data])
SG_LF_y12 = cp.TransferDistribution(nr.choice, [SG_LF_y12_data])
SG_LF_y13 = cp.TransferDistribution(nr.choice, [SG_LF_y13_data])
SG_LF_y14 = cp.TransferDistribution(nr.choice, [SG_LF_y14_data])
SG_LF_y15 = cp.TransferDistribution(nr.choice, [SG_LF_y15_data])
SG_LF_y16 = cp.TransferDistribution(nr.choice, [SG_LF_y16_data])
SG_LF_y17 = cp.TransferDistribution(nr.choice, [SG_LF_y17_data])
SG_LF_y18 = cp.TransferDistribution(nr.choice, [SG_LF_y18_data])
SG_LF_y19 = cp.TransferDistribution(nr.choice, [SG_LF_y19_data])
SG_LF_y20 = cp.TransferDistribution(nr.choice, [SG_LF_y20_data])

STPsludge_N.transfers =[cp.TimeDependendDistributionTransfer([SG_WIIP_y0,
                                                            SG_WIIP_y1,SG_WIIP_y2,SG_WIIP_y3,SG_WIIP_y4,SG_WIIP_y5,
                                                            SG_WIIP_y6,SG_WIIP_y7,SG_WIIP_y8,SG_WIIP_y9,SG_WIIP_y10,
                                                            SG_WIIP_y11,SG_WIIP_y12,SG_WIIP_y13,SG_WIIP_y14,SG_WIIP_y15,
                                                            SG_WIIP_y16,SG_WIIP_y17,SG_WIIP_y18,SG_WIIP_y19,SG_WIIP_y20], 
                                                            WIP_N, STPsludge_N, priority=2),
                      cp.TimeDependendDistributionTransfer([SG_LF_y0,
                                                            SG_LF_y1,SG_LF_y2,SG_LF_y3,SG_LF_y4,SG_LF_y5,
                                                            SG_LF_y6,SG_LF_y7,SG_LF_y8,SG_LF_y9,SG_LF_y10,
                                                            SG_LF_y11,SG_LF_y12,SG_LF_y13,SG_LF_y14,SG_LF_y15,
                                                            SG_LF_y16,SG_LF_y17,SG_LF_y18,SG_LF_y19,SG_LF_y20],
                                                            STPSlud_Landfill_N, STPsludge_N, priority=2),
                      cp.ConstTransfer(1, STsoil_N, priority=1)]

STPsludge_M.transfers =[cp.TimeDependendDistributionTransfer([SG_WIIP_y0,
                                                            SG_WIIP_y1,SG_WIIP_y2,SG_WIIP_y3,SG_WIIP_y4,SG_WIIP_y5,
                                                            SG_WIIP_y6,SG_WIIP_y7,SG_WIIP_y8,SG_WIIP_y9,SG_WIIP_y10,
                                                            SG_WIIP_y11,SG_WIIP_y12,SG_WIIP_y13,SG_WIIP_y14,SG_WIIP_y15,
                                                            SG_WIIP_y16,SG_WIIP_y17,SG_WIIP_y18,SG_WIIP_y19,SG_WIIP_y20], 
                                                            WIP_M, STPsludge_M, priority=2),
                      cp.TimeDependendDistributionTransfer([SG_LF_y0,
                                                            SG_LF_y1,SG_LF_y2,SG_LF_y3,SG_LF_y4,SG_LF_y5,
                                                            SG_LF_y6,SG_LF_y7,SG_LF_y8,SG_LF_y9,SG_LF_y10,
                                                            SG_LF_y11,SG_LF_y12,SG_LF_y13,SG_LF_y14,SG_LF_y15,
                                                            SG_LF_y16,SG_LF_y17,SG_LF_y18,SG_LF_y19,SG_LF_y20],
                                                            STPSlud_Landfill_M, STPsludge_M, priority=2),
                      cp.ConstTransfer(1, STsoil_M, priority=1)]

STPsludge_T.transfers =[cp.TimeDependendDistributionTransfer([SG_WIIP_y0,
                                                            SG_WIIP_y1,SG_WIIP_y2,SG_WIIP_y3,SG_WIIP_y4,SG_WIIP_y5,
                                                            SG_WIIP_y6,SG_WIIP_y7,SG_WIIP_y8,SG_WIIP_y9,SG_WIIP_y10,
                                                            SG_WIIP_y11,SG_WIIP_y12,SG_WIIP_y13,SG_WIIP_y14,SG_WIIP_y15,
                                                            SG_WIIP_y16,SG_WIIP_y17,SG_WIIP_y18,SG_WIIP_y19,SG_WIIP_y20], 
                                                            WIP_T, STPsludge_T, priority=2),
                      cp.TimeDependendDistributionTransfer([SG_LF_y0,
                                                            SG_LF_y1,SG_LF_y2,SG_LF_y3,SG_LF_y4,SG_LF_y5,
                                                            SG_LF_y6,SG_LF_y7,SG_LF_y8,SG_LF_y9,SG_LF_y10,
                                                            SG_LF_y11,SG_LF_y12,SG_LF_y13,SG_LF_y14,SG_LF_y15,
                                                            SG_LF_y16,SG_LF_y17,SG_LF_y18,SG_LF_y19,SG_LF_y20],
                                                            STPSlud_Landfill_T, STPsludge_T, priority=2),
                      cp.ConstTransfer(1, STsoil_T, priority=1)]


# In[47]:


###########################  COLLECTION RATE  #################################


# In[48]:


# Mixed Municipal Solid Waste

# for MSW there is first an array built with 's' sampled values from each distribution of the different sources
# In a second step from this sampled data, one value is selected and multiplied by the scaling factor for the UK.
# Eurostat, for year 2014: 11.25% landfilled in Austria.
# Mean of this value for Europe for year 2014: 47.87% (this model).
# It results a scaling factor of 0.235.

MSW_LF_Data_y0 = (np.concatenate([nr.triangular(0.461, 0.922, 1.383, s), nr.triangular(0.411, 0.822, 1.233, s), nr.triangular(0.3978, 0.765, 1.1628, s)] ))
MSW_LF_Data_y1 = (np.concatenate([nr.triangular(0.4495, 0.899, 1.3485, s), nr.triangular(0.4035, 0.807, 1.2105, s), nr.triangular(0.38948, 0.749, 1.1385, s)] ))
MSW_LF_Data_y2 = (np.concatenate([nr.triangular(0.4708, 0.877, 1.3478, s), nr.triangular(0.3955, 0.791, 1.1865, s), nr.triangular(0.3817, 0.734, 1.11568, s)] ))
MSW_LF_Data_y3 = (np.concatenate([nr.triangular(0.5231, 0.855, 1.2056, s), nr.triangular(0.4035, 0.773, 1.1765, s), nr.triangular(0.3760, 0.723, 1.099, s)] ))
MSW_LF_Data_y4 = (np.concatenate([nr.triangular(0.5713, 0.832, 1.1149, s), nr.triangular(0.4347, 0.76, 1.1947, s), nr.triangular(0.3645, 0.701, 1.0655, s)] ))
MSW_LF_Data_y5 = (np.concatenate([nr.triangular(0.6169, 0.81, 1.0287, s), nr.triangular(0.3826, 0.733, 1.0629, s), nr.triangular(0.3484, 0.67, 0.9916, s)] ))
MSW_LF_Data_y6 = (np.concatenate([nr.triangular(0.7637, 0.913, 1.0956, s), nr.triangular(0.4021, 0.703, 1.1051, s), nr.triangular(0.3406, 0.655, 0.9694, s)] ))
MSW_LF_Data_y7 = (np.concatenate([nr.triangular(0.6412, 0.822, 1.0357, s), nr.triangular(0.3581, 0.686, 0.9947, s), nr.triangular(0.33488, 0.644, 0.95312, s)] ))
MSW_LF_Data_y8 = (np.concatenate([nr.triangular(0.5995, 0.728, 0.8565, s), nr.triangular(0.3815, 0.667, 0.9525, s), nr.triangular(0.31772, 0.611, 0.90428, s)] ))
MSW_LF_Data_y9 = (np.concatenate([nr.triangular(0.5175, 0.658, 0.7985, s), nr.triangular(0.3377, 0.647, 0.9563, s), nr.triangular(0.312, 0.6, 0.888, s)] ))
MSW_LF_Data_y10 = (np.concatenate([nr.triangular(0.5072, 0.597, 0.6868, s), nr.triangular(0.3586, 0.627, 0.8954, s), nr.triangular(0.3042, 0.585, 0.8658, s)] ))
MSW_LF_Data_y11 = (np.concatenate([nr.triangular(0.4582, 0.57, 0.6818, s), nr.triangular(0.3054, 0.585, 0.8646, s), nr.triangular(0.28652, 0.551, 0.81548, s)] ))
MSW_LF_Data_y12 = (np.concatenate([nr.triangular(0.4193, 0.553, 0.6867, s), nr.triangular(0.3077, 0.538, 0.7683, s), nr.triangular(0.27456, 0.528, 0.78144, s)] ))
MSW_LF_Data_y13 = (np.concatenate([nr.triangular(0.4355, 0.536, 0.6365, s), nr.triangular(0.2662, 0.51, 0.7538, s), nr.triangular(0.25792, 0.496, 0.73408, s)] ))
MSW_LF_Data_y14 = (np.concatenate([nr.triangular(0.4200, 0.487, 0.5540, s), nr.triangular(0.2740, 0.479, 0.6840, s), nr.triangular(0.24596, 0.473, 0.70004, s)] ))
MSW_LF_Data_y15 = (np.concatenate([nr.triangular(0.3831, 0.474, 0.5649, s), nr.triangular(0.2219, 0.425, 0.6282, s), nr.triangular(0.23296, 0.448, 0.66304, s)] ))
MSW_LF_Data_y16 = (np.concatenate([nr.triangular(0.3468, 0.46, 0.5732, s), nr.triangular(0.1875, 0.375, 0.5625, s), nr.triangular(0.206, 0.412, 0.618, s)] ))
MSW_LF_Data_y17 = (np.concatenate([nr.triangular(0.3113, 0.445, 0.5787, s), nr.triangular(0.1595, 0.319, 0.4785, s), nr.triangular(0.1895, 0.379, 0.5685, s)] ))
MSW_LF_Data_y18 = (np.concatenate([nr.triangular(0.3197, 0.429, 0.5383, s), nr.triangular(0.128, 0.256, 0.384, s), nr.triangular(0.1725, 0.345, 0.5175, s)] ))
MSW_LF_Data_y19 = (np.concatenate([nr.triangular(0.3250, 0.411, 0.4970, s), nr.triangular(0.0925, 0.185, 0.2775, s), nr.triangular(0.154, 0.308, 0.462, s)] ))
MSW_LF_Data_y20 = (np.concatenate([nr.triangular(0.3271, 0.391, 0.4549, s), nr.triangular(0.0515, 0.103, 0.1545, s), nr.triangular(0.1345, 0.269, 0.4035, s)] ))


MSW_LF_y0 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y0])
MSW_LF_y1 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y1])
MSW_LF_y2 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y2])
MSW_LF_y3 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y3])
MSW_LF_y4 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y4])
MSW_LF_y5 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y5])
MSW_LF_y6 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y6])
MSW_LF_y7 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y7])
MSW_LF_y8 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y8])
MSW_LF_y9 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y9])
MSW_LF_y10 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y10])
MSW_LF_y11 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y11])
MSW_LF_y12 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y12])
MSW_LF_y13 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y13])
MSW_LF_y14 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y14])
MSW_LF_y15 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y15])
MSW_LF_y16 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y16])
MSW_LF_y17 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y17])
MSW_LF_y18 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y18])
MSW_LF_y19 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y19])
MSW_LF_y20 = cp.TransferDistribution(nr.choice, [MSW_LF_Data_y20])

# if changes are made here, don't forget to update the transfers for sorting (same same TCs)
MMSW.transfers = [cp.TimeDependendDistributionTransfer([MSW_LF_y0,
                                                        MSW_LF_y1,MSW_LF_y2,MSW_LF_y3,MSW_LF_y4,MSW_LF_y5,
                                                        MSW_LF_y6,MSW_LF_y7,MSW_LF_y8,MSW_LF_y9,MSW_LF_y10,
                                                        MSW_LF_y11,MSW_LF_y12,MSW_LF_y13,MSW_LF_y14,MSW_LF_y15,
                                                        MSW_LF_y16,MSW_LF_y17,MSW_LF_y18,MSW_LF_y19,MSW_LF_y20],
                                                        MMSW_Landfill_P, MMSW, priority=2), # From MMSW to Landfill
                  cp.ConstTransfer(1, WIP_P, priority=1)]


# In[52]:


### SAME AS FOR EUROPE ###

# CDW
CDW_LF_y0 = cp.TransferDistribution(nr.triangular, [0.4028, 0.646, 0.8892])
CDW_LF_y1 = cp.TransferDistribution(nr.triangular, [0.4155, 0.617, 0.8185])
CDW_LF_y2 = cp.TransferDistribution(nr.triangular, [0.4254, 0.588, 0.7506])
CDW_LF_y3 = cp.TransferDistribution(nr.triangular, [0.4324, 0.559, 0.6856])
CDW_LF_y4 = cp.TransferDistribution(nr.triangular, [0.4447, 0.54, 0.6353])
CDW_LF_y5 = cp.TransferDistribution(nr.triangular, [0.3709, 0.507, 0.6431])
CDW_LF_y6 = cp.TransferDistribution(nr.triangular, [0.3032, 0.474, 0.6448])
CDW_LF_y7 = cp.TransferDistribution(nr.triangular, [0.2416, 0.441, 0.6404])
CDW_LF_y8 = cp.TransferDistribution(nr.triangular, [0.2268, 0.408, 0.5892])
CDW_LF_y9 = cp.TransferDistribution(nr.triangular, [0.2115, 0.375, 0.5385])
CDW_LF_y10 = cp.TransferDistribution(nr.triangular, [0.1956, 0.342, 0.4884])
CDW_LF_y11 = cp.TransferDistribution(nr.triangular, [0.1650, 0.316, 0.4670])
CDW_LF_y12 = cp.TransferDistribution(nr.triangular, [0.1665, 0.291, 0.4155])
CDW_LF_y13 = cp.TransferDistribution(nr.triangular, [0.1436, 0.275, 0.4065])
CDW_LF_y14 = cp.TransferDistribution(nr.triangular, [0.1481, 0.259, 0.3699])
CDW_LF_y15 = cp.TransferDistribution(nr.triangular, [0.1096, 0.21, 0.3104])
CDW_LF_y16 = cp.TransferDistribution(nr.triangular, [0.0905, 0.181, 0.2715])
CDW_LF_y17 = cp.TransferDistribution(nr.triangular, [0.076, 0.152, 0.228])
CDW_LF_y18 = cp.TransferDistribution(nr.triangular, [0.0615, 0.123, 0.1845])
CDW_LF_y19 = cp.TransferDistribution(nr.triangular, [0.0465, 0.093, 0.1395])
CDW_LF_y20 = cp.TransferDistribution(nr.triangular, [0.032, 0.0640, 0.0960])

CDW.transfers = [cp.TimeDependendDistributionTransfer([CDW_LF_y0,
                                                       CDW_LF_y1,CDW_LF_y2,CDW_LF_y3,CDW_LF_y4,CDW_LF_y5,
                                                       CDW_LF_y6,CDW_LF_y7,CDW_LF_y8,CDW_LF_y9,CDW_LF_y10,
                                                       CDW_LF_y11,CDW_LF_y12,CDW_LF_y13,CDW_LF_y14,CDW_LF_y15,
                                                       CDW_LF_y16,CDW_LF_y17,CDW_LF_y18,CDW_LF_y19,CDW_LF_y20],
                                                       CDW_Landfill_P, CDW, priority=2),
                 cp.ConstTransfer(1, Sorting_CDW, priority=1)]


# In[53]:


############################  SORTING  ########################################  

# all these processes were kept static, so there are no time-dependent transfers
# thus the coefficient of variance is kept to 50%            


# In[55]:


### SAME AS FOR EUROPE

# CDW   
## The categories (materials) of CDW are distributed here.
# For TiO2, we have:
Total_mineral_CDW = nr.triangular(0, 0.0508, 0.10, s) + nr.triangular(0, 0.0286, 0.05, s) + nr.triangular(0, 0.0286, 0.05, s)
Total_glass_CDW = nr.triangular(0, 0.0286, 0.05, s)
Total_CDW = Total_mineral_CDW + Total_glass_CDW
# Proportion of mineral and glass waste:
Prop_Mine = Total_mineral_CDW/Total_CDW
Prop_Glass = Total_glass_CDW/Total_CDW


Sorting_CDW.transfers = [cp.StochasticTransfer(nr.choice, [Prop_Mine], Sorting_CDW_Mineral, priority=2),
                         cp.ConstTransfer(1, Sorting_CDW_Glass, priority=1)] 
    
Glass_LF = np.concatenate([nr.uniform(0, 0.5, int(s*0.8)), nr.triangular(0.5, 0.5, 0.75, int(s*0.2))])
Sorting_CDW_Glass.transfers = [cp.RandomChoiceTransfer(Glass_LF, SortCDWGlass_Landfill_P, priority=2),
                               cp.ConstTransfer(1, Reprocess_Glass_P, priority=1)]

Reprocessing_Mineral = np.concatenate([nr.uniform( 0, 0.28, int(s*0.8)), nr.triangular(0.28, 0.28, 0.294, int(s*0.2))])
Sorting_CDW_Mineral.transfers= [cp.RandomChoiceTransfer(Reprocessing_Mineral, Reprocess_Mineral_P, priority=2),
                                cp.ConstTransfer(1, SortCDWMiner_Landfill_P, priority=1)]


# Sorting_Disposal, is a transfer to disposal with the same TCs as MMSW
Sorting_Disposal.transfers = [cp.TimeDependendDistributionTransfer([MSW_LF_y0,
                                                                    MSW_LF_y1,MSW_LF_y2,MSW_LF_y3,MSW_LF_y4,MSW_LF_y5,
                                                                    MSW_LF_y6,MSW_LF_y7,MSW_LF_y8,MSW_LF_y9,MSW_LF_y10,
                                                                    MSW_LF_y11,MSW_LF_y12,MSW_LF_y13,MSW_LF_y14,MSW_LF_y15,
                                                                    MSW_LF_y16,MSW_LF_y17,MSW_LF_y18,MSW_LF_y19,MSW_LF_y20],
                                                        SortDisp_Landfill_P, Sorting_Disposal, priority=2),
                              cp.ConstTransfer(1, WIP_P, priority=1)]


# In[56]:


###############################Transfers form technical compartments ##########
###############################################################################


# In[57]:


'''########################################################################################################################
   ####---------------------------------------------Recycling System---------------------------------------------------####
   ########################################################################################################################
   '''
# all these processes were kept static, so there are no time-dependent transfers
# thus the coefficient of variance is kept to 50%  


# In[62]:


'''Reprocess_Glass_P'''
# from crushing galss to air

Reprocess_Glass_P.transfers =[cp.StochasticTransfer(tf.TrapezTrunc, [0.07, 0.47, 0.49, 0.49, 1, 0, 1], Air_Glass,  priority=2), # since Tc from moulding to reuse is 1, here we skip moulding to reuse to simplify the code
                              cp.ConstTransfer(1, Melting_Glass, priority=1)]

Melting_Glass.transfers=[cp.ConstTransfer(1, MeltGlass_Reuse_T, priority=1)]

# Release form
Air_Glass.transfers=[cp.StochasticTransfer(tf.TriangTrunc, [0.2, 1.47, 1, 0, 1], Air_NM,priority=2),
                     cp.ConstTransfer(1, RPAir_M, priority=1)]  



# In[63]:


'''#7. Reprocess_Mineral_P'''   
# from crushing minerals to air

Reprocess_Mineral_P.transfers =[cp.StochasticTransfer(tf.TrapezTrunc, [0.05, 0.16, 0.48, 0.48, 1, 0, 1], Air_Mineral, priority=2), # since Tc from moulding to reuse is 1, here we skip moulding to reuse to simplify the code
                                cp.ConstTransfer(1, Sorting_Mineral, priority=1)]


Sorting_Mineral.transfers =[cp.StochasticTransfer(tf.TriangTrunc, [0.7944, 1.02, 1, 0, 1], SortMiner_Landfill_P, priority=2),
                            cp.StochasticTransfer(tf.TriangTrunc, [0.05, 1.01, 1, 0, 1], Air_Mineral, priority=2),
                            cp.ConstTransfer(1, SortMiner_Reuse_P, priority=1)]

                           
# release form
Air_Mineral.transfers=[cp.StochasticTransfer(tf.TriangTrunc, [0.2, 1.47, 1, 0, 1], Air_NM, priority=2),
                       cp.ConstTransfer(1, RPAir_M, priority=1)]

# In[62]:   
# Allocate all release to air with mixed N and M
# allocation of Air_NM for the fraction of 0.2
Air_NM.transfers=[cp.StochasticTransfer(tf.TriangTrunc, [0.1535, 1.07, 1, 0, 1], RPAir_N, priority=2),
                  cp.ConstTransfer(1, RPAir_M,priority=1)]


# In[64]:


RPWIP_P.transfers=[cp.ConstTransfer(1, WIP_P, priority=1)]

RPWW_N.transfers=[cp.ConstTransfer(1, WW_N, priority=1)]
RPWW_M.transfers=[cp.ConstTransfer(1, WW_M, priority=1)]


# In[65]:


##################################  WIP ######################################


# In[66]:


# Elimination while burning
WIP_P.transfers =[cp.StochasticTransfer(nr.uniform, [1e-6, 1], Burning_T, priority=2),
                  cp.ConstTransfer(1, Burning_N, priority=1)]

WIP_M.transfers =[cp.StochasticTransfer(nr.uniform,[1e-6 , 1], Burning_T, priority=2),
                  cp.ConstTransfer(1, Burning_N, priority=1)]

WIP_N.transfers =[cp.StochasticTransfer(nr.uniform,[1e-6 , 1], Burning_T, priority=2),
                  cp.ConstTransfer(1, Burning_N, priority=1)]

WIP_T.transfers = [cp.ConstTransfer(1, Burning_T, priority=1)]
               
# transfer to bottom / fly ash
ToFlyash = np.concatenate([ 
        nr.triangular(0.095, 0.19, 0.285, s),
        nr.triangular(0.0276, 0.029, 0.029, int(0.1759*s)), nr.uniform(0.029, 0.197, int(0.63241*s)), nr.triangular(0.197, 0.197, 0.2069, int(0.1917*s))
        ]) 

Burning_N.transfers =[cp.RandomChoiceTransfer(ToFlyash, Flyash_N, priority=2),
                            cp.ConstTransfer(1, Bottomash_N, priority=1)]

Burning_T.transfers =[cp.RandomChoiceTransfer(ToFlyash, Flyash_T, priority=2),
                            cp.ConstTransfer(1, Bottomash_T, priority=1)]


Flyash_N.transfers =[cp.StochasticTransfer(nr.triangular, [0.000025, 0.00005, 0.000075], WIP_Air_N, priority=2), # 1- 0.99995 (filter efficiency)
                   cp.StochasticTransfer(nr.triangular, [0, 0.0001, 0.00015], WW_N, priority=2), # flow to Wastewater during the acid washing
                   cp.ConstTransfer(1, Filterash_N, priority=1)]

Flyash_T.transfers =[cp.StochasticTransfer(nr.triangular, [0.000025, 0.00005, 0.000075], WIP_Air_T, priority=2), # 1- 0.99995 (filter efficiency)
                   cp.StochasticTransfer(nr.triangular, [0, 0.0001, 0.00015], WW_T, priority=2), # flow to Wastewater during the acid washing
                   cp.ConstTransfer(1, Filterash_T, priority=1)]


# In[67]:


# From filter ash
FA_LF_y0 = cp.TransferConstant(1)
FA_LF_y1 = cp.TransferConstant(1)
FA_LF_y2 = cp.TransferConstant(1)
FA_LF_y3 = cp.TransferConstant(1)
FA_LF_y4 = cp.TransferConstant(1)
FA_LF_y5 = cp.TransferConstant(1)
FA_LF_y6 = cp.TransferConstant(1)
FA_LF_y7 = cp.TransferConstant(1)
FA_LF_y8 = cp.TransferConstant(1)
FA_LF_y9 = cp.TransferConstant(1)
FA_LF_y10 = cp.TransferConstant(1)
FA_LF_y11 = cp.TransferConstant(1)
FA_LF_y12 = cp.TransferConstant(1)
FA_LF_y13 = cp.TransferConstant(1)
FA_LF_y14 = cp.TransferConstant(1)
FA_LF_y15 = cp.TransferConstant(1)
FA_LF_y16 = cp.TransferConstant(1)
FA_LF_y17 = cp.TransferConstant(1)
FA_LF_y18 = cp.TransferConstant(1)
FA_LF_y19 = cp.TransferConstant(1)
FA_LF_y20 = cp.TransferConstant(1)

Filterash_N.transfers =[cp.TimeDependendDistributionTransfer([FA_LF_y0,
                                                            FA_LF_y1,FA_LF_y2,FA_LF_y3,FA_LF_y4,FA_LF_y5,
                                                            FA_LF_y6,FA_LF_y7,FA_LF_y8,FA_LF_y9,FA_LF_y10,
                                                            FA_LF_y11,FA_LF_y12,FA_LF_y13,FA_LF_y14,FA_LF_y15,
                                                            FA_LF_y16,FA_LF_y17,FA_LF_y18,FA_LF_y19,FA_LF_y20],
                                                            Filterash_Landfill_N, Filterash_N, priority=2),
                      cp.ConstTransfer(1, Filterash_Reuse_N, priority=1)]

Filterash_T.transfers =[cp.TimeDependendDistributionTransfer([FA_LF_y0,
                                                            FA_LF_y1,FA_LF_y2,FA_LF_y3,FA_LF_y4,FA_LF_y5,
                                                            FA_LF_y6,FA_LF_y7,FA_LF_y8,FA_LF_y9,FA_LF_y10,
                                                            FA_LF_y11,FA_LF_y12,FA_LF_y13,FA_LF_y14,FA_LF_y15,
                                                            FA_LF_y16,FA_LF_y17,FA_LF_y18,FA_LF_y19,FA_LF_y20],
                                                            Filterash_Landfill_T, Filterash_T, priority=2),
                      cp.ConstTransfer(1, Filterash_Reuse_T, priority=1)]


# In[68]:


### SAME AS EUROPE ###

# From bottom ash
BA_R_y0 = cp.TransferDistribution(nr.triangular, [0.2445, 0.489, 0.7335])
BA_R_y1 = cp.TransferDistribution(nr.triangular, [0.243, 0.486, 0.729])
BA_R_y2 = cp.TransferDistribution(nr.triangular, [0.2470, 0.482, 0.7170])
BA_R_y3 = cp.TransferDistribution(nr.triangular, [0.2531, 0.45, 0.6469])
BA_R_y4 = cp.TransferDistribution(nr.triangular, [0.2531, 0.45, 0.6469])
BA_R_y5 = cp.TransferDistribution(nr.triangular, [0.2365, 0.46, 0.6835])
BA_R_y6 = cp.TransferDistribution(nr.triangular, [0.235, 0.47, 0.705])
BA_R_y7 = cp.TransferDistribution(nr.triangular, [0.24, 0.48, 0.72])
BA_R_y8 = cp.TransferDistribution(nr.triangular, [0.245, 0.49, 0.735])
BA_R_y9 = cp.TransferDistribution(nr.triangular, [0.2602, 0.5, 0.7398])
BA_R_y10 = cp.TransferDistribution(nr.triangular, [0.2917, 0.51, 0.7283])
BA_R_y11 = cp.TransferDistribution(nr.triangular, [0.2401, 0.46, 0.6799])
BA_R_y12 = cp.TransferDistribution(nr.triangular, [0.2345, 0.41, 0.5855])
BA_R_y13 = cp.TransferDistribution(nr.triangular, [0.2156, 0.413, 0.6104])
BA_R_y14 = cp.TransferDistribution(nr.triangular, [0.2380, 0.416, 0.5940])
BA_R_y15 = cp.TransferDistribution(nr.triangular, [0.2276, 0.436, 0.6444])
BA_R_y16 = cp.TransferDistribution(nr.triangular, [0.2165, 0.433, 0.6495])
BA_R_y17 = cp.TransferDistribution(nr.triangular, [0.2145, 0.429, 0.6435])
BA_R_y18 = cp.TransferDistribution(nr.triangular, [0.2125, 0.425, 0.6375])
BA_R_y19 = cp.TransferDistribution(nr.triangular, [0.211, 0.422, 0.633])
BA_R_y20 = cp.TransferDistribution(nr.triangular, [0.209, 0.418, 0.627])

Bottomash_N.transfers =[cp.TimeDependendDistributionTransfer([BA_R_y0,
                                                            BA_R_y1,BA_R_y2,BA_R_y3,BA_R_y4,BA_R_y5,
                                                            BA_R_y6,BA_R_y7,BA_R_y8,BA_R_y9,BA_R_y10,
                                                            BA_R_y11,BA_R_y12,BA_R_y13,BA_R_y14,BA_R_y15,
                                                            BA_R_y16,BA_R_y17,BA_R_y18,BA_R_y19,BA_R_y20],
                                                            Bottomash_Reuse_N, Bottomash_N, priority=2),
                      cp.ConstTransfer(1, Bottomash_Landfill_N, priority=1)]

Bottomash_T.transfers =[cp.TimeDependendDistributionTransfer([BA_R_y0,
                                                            BA_R_y1,BA_R_y2,BA_R_y3,BA_R_y4,BA_R_y5,
                                                            BA_R_y6,BA_R_y7,BA_R_y8,BA_R_y9,BA_R_y10,
                                                            BA_R_y11,BA_R_y12,BA_R_y13,BA_R_y14,BA_R_y15,
                                                            BA_R_y16,BA_R_y17,BA_R_y18,BA_R_y19,BA_R_y20],
                                                            Bottomash_Reuse_T, Bottomash_T, priority=2),
                      cp.ConstTransfer(1, Bottomash_Landfill_T, priority=1)]


# In[ ]:




