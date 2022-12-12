'''
CS2410_Capstone
Group: AJ
Names: Anandita Prakash, Julia Ybanez
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('diabetes.csv')

#BASIC STATS TABLE
df.describe().transpose()

#HEAT MAP CORRELATION
corr = df.corr()
sns.heatmap(corr, annot = True)
plt.show()

#INSULIN VS GLUCOSE
sns.lmplot(x = 'Insulin', y = 'Glucose', data = df, hue = 'Outcome')
plt.title('Insulin vs. Glucose')


#SUBPLOTS FOR ALL HISTOGRAMS
fig, ax = plt.subplots(4,2, figsize=(16,16))
sns.histplot(data=df, x="Age", hue="Outcome", kde=True, color="skyblue", bins = 20, ax=ax[0,0])
sns.histplot(data=df, x="Pregnancies", hue="Outcome", kde=True, color="skyblue", bins = 20, ax=ax[0,1])
sns.histplot(data=df, x="Glucose", hue="Outcome", kde=True, color="skyblue", bins = 20, ax=ax[1,0])
sns.histplot(data=df, x="BloodPressure", hue="Outcome", kde=True, color="skyblue", bins = 20, ax=ax[1,1])
sns.histplot(data=df, x="SkinThickness", hue="Outcome", kde=True, color="skyblue", bins = 20, ax=ax[2,0])
sns.histplot(data=df, x="Insulin", hue="Outcome", kde=True, color="skyblue", bins = 20, ax=ax[2,1])
sns.histplot(data=df, x="DiabetesPedigreeFunction", hue="Outcome", kde=True, color="skyblue", bins = 20, ax=ax[3,0])
sns.histplot(data=df, x="BMI", hue="Outcome", kde=True, color="skyblue", bins = 20, ax=ax[3,1])


#SCATTER PLOT - GLUCOSE VS. BLOODPRESSUE
plt.scatter(x = df['Glucose'],y = df['BloodPressure'],color='orange',marker='+')
plt.xlabel('Glucose')
plt.ylabel('Bloodpressure')


# DIABETES PEDIGREE FUNCTION - PIE CHART
dpf = df['DiabetesPedigreeFunction'].to_numpy()

LessEqual0 = 0
Between11_20 = 0
Between21_30 = 0
Between31_40 = 0
Between41_50 = 0
Between51_60 = 0
Between61_70 = 0
Between71_80 = 0
Between81_90 = 0
Between91_100 = 0
GreaterThan100 = 0

for i in dpf:
  if i <= .10:
    LessEqual0 += 1
  elif i > .10 and i <= .20:
    Between11_20 += 1
  elif i > .20 and i <= .30:
    Between21_30 += 1
  elif i > .30 and i <= .40:
    Between31_40 += 1
  elif i > .40 and i <= .50:
    Between41_50 += 1
  elif i > .50 and i <= .60:
    Between51_60 += 1
  elif i > .60 and i <= .70:
    Between61_70 += 1
  elif i > .70 and i <= .80:
    Between71_80 += 1
  elif i > .80 and i <= .90:
    Between81_90 += 1
  elif i > .90 and i <= 1:
    Between91_100 += 1
  else:
    GreaterThan100 += 1

labels = ['<= 10%', '11-20 %', '21-30 %','31-40 %','41-50 %', '51-60 %','61-70 %','71-80 %','81-90 %', '91-100 %','>100%']
pieChart2 = [LessEqual0, Between11_20, Between21_30, Between31_40, Between41_50, Between51_60, Between61_70, Between71_80, Between81_90, Between91_100, GreaterThan100]
explode = (0, 0 ,0, 0, 0, 0, 0, 0, 0, 0 ,0)
fig1, ax1 = plt.subplots()
plt.title("Diabetes Pedigree Function Percentages")
ax1.pie(pieChart2, explode=explode, labels= labels, autopct='%1.1f%%', shadow=True,
startangle=90, counterclock=False, wedgeprops={'linewidth': 4.0, 'edgecolor': 'white'},
    textprops={'size': 'small'})
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
