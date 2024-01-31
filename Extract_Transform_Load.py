import pandas as pd

'''
df = pd.read_csv('country_data_index.csv')

#print (df)

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")



column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data",header=None, names= column_names)

'''

#print (df)
########################################
#######  Inconsistent Data Types & Names
########################################
'''
df2 = pd.read_excel('residentdoctors.xlsx')

#print (df2)

df2['LOWER_AGE'] = df2['AGEDIST'].str.extract('(\d+)-') #Extracts 1st decimal #
df2['LOWER_AGE'] = df2['LOWER_AGE'].astype(int)

#print (df2)
#print(df2['AGEDIST'])
#print(df2['LOWER_AGE'])

df3 = pd.read_csv('time_series_data.csv')

df3['Date'] = pd.to_datetime(df3['Date'])

#print (df3)

df3['Year'] = df3['Date'].dt.year
df3['Month'] = df3['Date'].dt.month
df3['Day'] = df3['Date'].dt.day

#print (df3)

#print(df3['Year'])

df4 = pd.read_csv('patient_data_dates.csv')



df4.drop(['Index'],inplace=True,axis=1)

x = df4["Calories"].mean()


df4["Calories"].fillna(x, inplace = True) 

df4['Date'] = pd.to_datetime(df4['Date'])



df4.dropna(inplace = True)

#print (df4)
df5 = df4.reset_index(drop=True)

#print (df5)
df5.loc[7, 'Duration'] = 45

df5.drop_duplicates(inplace = True)

df6 = df5.reset_index(drop=True)

#print (df6)
'''

###################################
##### Applying Data Transformations
###################################

################### 1. Aggregation

df7 = pd.read_csv('iris.csv')

df7['sepal_length_sq']= df7['sepal_length']**2


#print(df7)

#df7['sepal_length_sq']= df7['sepal_length_sq'].apply(lambda x: x**2) #for multiple data sets

grouped = df7.groupby('class')

# Calculate mean, sum, and count for the squared values
mean_squared_values = grouped['sepal_length_sq'].mean()

'''
print(mean_squared_values)
sum_squared_values = grouped['sepal_length_sq'].sum()
count_squared_values = grouped['sepal_length_sq'].count()

# Display the results
print("Mean of Sepal Length Squared:")
print(mean_squared_values)

print("\nSum of Sepal Length Squared:")
print(sum_squared_values)

print("\nCount of Sepal Length Squared:")
print(count_squared_values)

'''

################### 2. Append and merge

df8 = pd.read_csv('person_split1.csv')
df9 = pd.read_csv('person_split2.csv')

df10 = pd.concat([df8,df9], ignore_index = True)


df11 = pd.read_csv('person_education.csv')
df12 = pd.read_csv('person_work.csv')


df13_merge_inner = pd.merge(df11,df12,on='id')

#print(df13_merge_inner)

df13_merge = pd.merge(df11, df12, on='id', how='outer')

#print(df13_merge)

################### 3. Filtering

df7['class'] = df7['class'].str.replace('Iris-', '')


df13 = df7[df7['sepal_length']>5]

df13 = df7[df7['sepal_length']=='DJ']

print(df13)






