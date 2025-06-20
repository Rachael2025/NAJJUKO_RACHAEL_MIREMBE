import pandas as pd
import numpy as np
import matplotlib as mt

from datetime import datetime

df = pd.read_csv("climate_action_data.csv")
df.head(10)
df.info()
print (df.describe())
print(df.isnull().sum(),'\n\n')


non_numeric_cols=['Sensor_ID','Date','Soil_Moisture(%)','Soil_pH','Temperature(C)','Humidity(%)','Crop_Type','Fertilizer_Recommended(kg/ha)','Irrigation_Recommended(mm)','Drone_Image_ID']
for col in non_numeric_cols:
   if col in df.columns:
    df[col] = df[col].fillna(df[col].mode()[0])

print('Missing values\n')
print(df.isnull().sum(),'\n\n')

df[col] = pd.to_numeric(df[col], errors='coerce')
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
print(df.describe())

print(df.isnull().sum(),'\n\n')

#check for duplicates
print('Numbers of duplicated rows:', df.duplicated().sum())

duplicates= df.duplicated().sum()
#Remove duplicates if any
if duplicates > 0:
 df.drop_duplicates(inplace=True)
 print('Duplicates removed')
else:
  print('No duplicates found')

  #Histograms
  import matplotlib.pyplot as plt
  import seaborn as sns 
  plt.figure(figsize=(10,8))

plt
sns.heatmap(corr_matrix, annot=True, cmap= '')

