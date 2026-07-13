import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (update file path if needed)
df = pd.read_csv("bestsellers.csv")

# 1. Check for null values
print("Null Values in Dataset:\n")
print(df.isnull().sum())

# 2. Handle missing values
# Fill numerical columns with mean, categorical with mode
for col in df.columns:
    if df[col].dtype in ['int64', 'float64']:
        df[col].fillna(df[col].mean(), inplace=True)
    else:
        df[col].fillna(df[col].mode()[0], inplace=True)

print("\nMissing values handled.\n")

# 3. Variance and Standard Deviation - User Rating
print("User Rating Statistics:")
print("Variance:", df['User Rating'].var())
print("Standard Deviation:", df['User Rating'].std())

# 4. Variance and Standard Deviation - Price
print("\nPrice Statistics:")
print("Variance:", df['Price'].var())
print("Standard Deviation:", df['Price'].std())

# 5. Histogram for User Rating
plt.figure()
plt.hist(df['User Rating'], bins=10)  # custom bin range
plt.title("Distribution of User Rating")
plt.xlabel("User Rating")
plt.ylabel("Frequency")
plt.show()

# 6. Histogram for Price
plt.figure()
plt.hist(df['Price'], bins=15)  # custom bin range
plt.title("Distribution of Price")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()
