import pandas as pd
from sklearn.model_selection import train_test_split


df = pd.read_csv("aparts.csv")
df = df.dropna()

df = pd.get_dummies(df, columns=["metro", "way", "provider"])
print(df.head())

# correlations = df.corr()['price'].sort_values(ascending=False)
# print(correlations)

X = df.drop(columns=['price', 'fee_percent'])
Y = df['price']


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
print(X.shape[1])

model.predict(X_test)