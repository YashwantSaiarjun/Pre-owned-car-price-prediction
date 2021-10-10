#=============================================================================
# PREDICTING THE PRICE OF PREOWNED CARS
#=============================================================================

import pandas as pd
import numpy as np
import seaborn as sns

# IMPORTING OS
import os
os.chdir("C:\\Users\\indra\\Documents\\DataScience_ML\\github_linkedin")

# READ CSV
data=pd.read_csv("cars_sampled.csv");

# CREATING A COPY FOR THE DATA

df=data.copy(deep=True)
 
df.info()

# CHECKING MEAN MEDION MODE OF EACH COLUMNS OF THE DATA
# SUMMARIZING

df.describe()
pd.set_option('display.float_format',lambda x:'%.3f' %x)
pd.set_option('display.max_columns',500)
df.describe()

# ==========================================================================
# DROPPING UNWANTED COLUMNS
# ==========================================================================

cols=['name','dateCrawled','dateCreated','lastSeen']
df=df.drop(columns=cols,axis=1)

print(df.head())

#============================================================================
# DROPPING DUPLICATES
#============================================================================
df.drop_duplicates(keep='first',inplace=True)
print(df.head())
print(df.shape)

# ===========================================================================
# DATA CLEANING
# ============================================================================

# NO OF MISSING VALUES IN EACH COLUMN
print(df.isnull().sum())

# VARIABLE YEAR OF REGESTRATION
yearwise_counts=df['yearOfRegistration'].value_counts().sort_index()

sum(df['yearOfRegistration']>2018)
sum(df['yearOfRegistration']<1950)

sns.regplot(x='yearOfRegistration',y='price',scatter=True,fit_reg=False,data=df)


# VARIABLE PRICE
price_counts=df['price'].value_counts().sort_index()
sns.distplot(df['price'])
sns.boxplot(y=df['price'])
df['price'].describe()



sum(df['price']>150000)
sum(df['price']<100)

#VARIABLE POWER PS

power_count=df['powerPS'].value_counts().sort_index()
sns.distplot(df['powerPS'])
sns.boxplot(y=df['powerPS'])
df['powerPS'].describe()

sns.regplot(x='powerPS',y='price',scatter=True,fit_reg=False,data=df)

sum(df['powerPS']>500)
sum(df['powerPS']<10)

#==========================================================================
# DATA CLEANING
#==========================================================================

#KEEPING INLY THE CERTAIN COLUMNS

df=df[(df.yearOfRegistration<=2018)
          & (df.yearOfRegistration>=1950) 
          & (df.powerPS<=500)
          & (df.powerPS>=10)
          & (df.price>=100)
          & (df.price<=150000)]

df['monthOfRegistration']/=12

# CREATING NEW COLUMNS AGE 
df['Age']=(2018-df['yearOfRegistration'])+df['monthOfRegistration']
df['Age']=round(df['Age'],2)
df['Age'].describe()

# DROPPING YEAR AND MONTH OF REGISTRATION
df=df.drop(columns=['yearOfRegistration','monthOfRegistration'],axis=1)

print(df.shape)

#========================================================================
# VISUALISING PARAMETERS USING PLOTS
#========================================================================

# AGE
sns.distplot(df['Age'])
sns.boxplot(y=df['Age'])

# PRICE
sns.distplot(df['price'],bins=30)
sns.boxplot(y=df['powerPS'])

# POWERPS
sns.distplot(df['powerPS'])
sns.boxplot(y=df['powerPS'])

#PLOTTING TWO DIFFERENT VARIBLE

# POWERPS VS PRICE

sns.regplot(x=df['powerPS'],y=df['price'],fit_reg=True,scatter=True)

#===========================================================================
# DATA VISUALIZATION
#===========================================================================

# VARIABLE SELLER

df['seller'].value_counts()
pd.crosstab(df['seller'],columns='count',normalize=True)
sns.countplot(x=df['seller'])

# VARIABLE OFFERTYPE

pd.crosstab(df['offerType'],columns='count',normalize=False)
sns.countplot(x=df['offerType'])

# VARIABLE ABTEST

df['abtest'].value_counts()
sns.countplot(x=df['abtest'])

# VARIABLE VEHICLE

df['vehicleType'].value_counts()
sns.countplot(x=df['vehicleType'])
sns.boxplot(x=df['vehicleType'],y=df['price'])

# VARAIBLE GEARBOX

df['gearbox'].value_counts()
sns.countplot(x=df['gearbox'])
sns.boxplot(x=df['gearbox'],y=df['price'])

# VARIABLE MODEL

df['model'].value_counts()


# VARIABLE KILOMETER

df['kilometer'].value_counts()
sns.countplot(x=df['kilometer'])
sns.boxplot(x=df['kilometer'],y=df['price'])

# VARIABLE FUELTYPE

df['fuelType'].value_counts()
sns.countplot(x=df['fuelType'])
sns.boxplot(x=df['fuelType'],y=df['price'])

# VARIABLE BRAND

df['brand'].value_counts()
sns.countplot(x=df['brand'])
sns.boxplot(x=df['brand'],y=df['price'])

# VARIABLE NOT REPAIRED DAMAGE

df['notRepairedDamage'].value_counts()
sns.countplot(x=df['notRepairedDamage'])
sns.boxplot(x=df['notRepairedDamage'],y=df['price'])

#===========================================================================
# REMOVING INSIGNIFICANT VARIABLES
#===========================================================================

cols=['seller','offerType','abtest']
df=df.drop(columns=cols,axis=1)



