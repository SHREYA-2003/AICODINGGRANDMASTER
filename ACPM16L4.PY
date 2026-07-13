import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Load dataset (update path if needed)
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

# 3. Frequency of categories for Genre
genre_counts = df['Genre'].value_counts()
print("\nGenre Frequency:\n", genre_counts)

# 4. Median of Genre (convert to numeric first)
df['Genre_numeric'] = df['Genre'].astype('category').cat.codes
median_genre = df['Genre_numeric'].median()
print("\nMedian of Genre (numeric form):", median_genre)

# 5. Bar Chart for Genre
plt.figure()
genre_counts.plot(kind='bar')
plt.title("Bar Chart of Genre")
plt.xlabel("Genre")
plt.ylabel("Count")
plt.show()

# 6. Pie Chart for Genre
plt.figure()
genre_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title("Pie Chart of Genre")
plt.ylabel("")
plt.show()

# 7. Create dataframe with numerical features only
numeric_df = df.select_dtypes(include=['int64', 'float64'])
print("\nNumerical Features:\n", numeric_df.head())

# 8. Boxplot to check spread
plt.figure()
numeric_df.boxplot()
plt.title("Boxplot of Numerical Features")
plt.xticks(rotation=45)
plt.show()

# 9. Data Transformation (choose based on spread)

# Standardization (good if data has outliers)
scaler = StandardScaler()
standardized_data = scaler.fit_transform(numeric_df)
standardized_df = pd.DataFrame(standardized_data, columns=numeric_df.columns)

print("\nStandardized Data Sample:\n", standardized_df.head())

# OR Normalization (uncomment if needed)
# normalizer = MinMaxScaler()
# normalized_data = normalizer.fit_transform(numeric_df)
# normalized_df = pd.DataFrame(normalized_data, columns=numeric_df.columns)
# print("\nNormalized Data Sample:\n", normalized_df.head())
