import pandas as pd
from sklearn.impute import SimpleImputer

data = {
    'Name': ['Ali', 'Amir', 'Javad', 'Hamid', 'Hamed', 'Farzad'],
    'Age': [25, 30, None, 35, 40, 43],
    'Salary': [50000, None, 60000, None, 70000, 75000]
}

df = pd.DataFrame(data)

imputer = SimpleImputer(strategy='mean')
df[['Age', 'Salary']] = imputer.fit_transform(df[['Age', 'Salary']])

df['Age'] = df['Age'].astype('int')
df['Salary'] = df['Salary'].astype('int')

df.to_excel('Salary.xlsx', index=False)

print(df)
