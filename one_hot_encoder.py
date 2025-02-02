import pandas as pd
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler

data = {
    'Age': [25, 30, 35, 40, 45],
    'Income': [50000, 60000, 80000, 90000, 120000],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Male'],
    'City': ['Tehran', 'Shiraz', 'Tehran', 'Isfahan', 'Shiraz']
}
df = pd.DataFrame(data)

print("دیتاست اصل:")
print(df)

encoder = OneHotEncoder(sparse_output=False)
encoded_data = encoder.fit_transform(df[['Gender', 'City']])

encoded_df = pd.DataFrame(encoded_data, columns=encoder.get_feature_names_out(['Gender', 'City']))


scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(df[['Age', 'Income']])

scaled_df = pd.DataFrame(scaled_data, columns=['Age', 'Income'])

final_df = pd.concat([scaled_df, encoded_df], axis=1)

print("\nدیتاست نهایی (آماده برای مدل‌سازی):")
print(final_df)

