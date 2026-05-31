import pandas as pd

df = pd.read_csv("data/Dataset for Data Analytics.csv")

print(df.head())

df['CouponCode'] = df['CouponCode'].fillna('NA')
print(df.isnull().sum())

df.drop_duplicates(inplace=True)
print(df.duplicated().sum())

print(df.dtypes)

df.to_csv("data/cleaned_Dataset for Data Analytics.csv", index=False)
print("Data Cleaning Completed Successfully!")