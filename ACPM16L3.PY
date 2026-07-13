import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (update file path if needed)
df = pd.read_csv("bestsellers.csv")

# 1. Check for null values
print("Null Values:\n")
print(df.isnull().sum())

# 2. Handle missing values
for col in df.columns:
    if df[col].dtype in ['int64', 'float64']:
        df[col].fillna(df[col].mean(), inplace=True)
    else:
        df[col].fillna(df[col].mode()[0], inplace=True)

print("\nMissing values handled.\n")

# 3. 10% quantile (0.10) for Price
q10_price = df['Price'].quantile(0.10)
print("10% Quantile (Price):", q10_price)

# 4. Quartiles & IQR for Price
q1_price = df['Price'].quantile(0.25)
q2_price = df['Price'].quantile(0.50)  # median
q3_price = df['Price'].quantile(0.75)
iqr_price = q3_price - q1_price

print("\nPrice Quartiles:")
print("Q1:", q1_price)
print("Q2 (Median):", q2_price)
print("Q3:", q3_price)
print("IQR:", iqr_price)

# 5. Quartiles & IQR for User Rating
q1_rating = df['User Rating'].quantile(0.25)
q2_rating = df['User Rating'].quantile(0.50)
q3_rating = df['User Rating'].quantile(0.75)
iqr_rating = q3_rating - q1_rating

print("\nUser Rating Quartiles:")
print("Q1:", q1_rating)
print("Q2 (Median):", q2_rating)
print("Q3:", q3_rating)
print("IQR:", iqr_rating)

# 6. Boxplots
plt.figure()
plt.boxplot(df['Price'])
plt.title("Boxplot of Price")
plt.ylabel("Price")
plt.show()

plt.figure()
plt.boxplot(df['User Rating'])
plt.title("Boxplot of User Rating")
plt.ylabel("User Rating")
plt.show()
