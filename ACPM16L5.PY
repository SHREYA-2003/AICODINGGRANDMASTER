import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, chi2_contingency

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

# 3. Check if combining categories is required
print("\nUnique values in Genre:\n", df['Genre'].unique())
# Example: If too many categories, we could combine them (not needed here usually)

# 4. Bin User Rating into categories
df['Rating_Category'] = pd.cut(
    df['User Rating'],
    bins=[0, 4.5, 5],
    labels=['Good', 'Excellent']
)

print("\nBinned User Ratings:\n", df[['User Rating', 'Rating_Category']].head())

# 5. Check skewness of numerical features
print("\nSkewness of numerical features:\n")
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_cols:
    print(f"{col}: {skew(df[col])}")

# 6. Association between User Rating and Genre (Chi-Square Test)
contingency1 = pd.crosstab(df['Genre'], df['Rating_Category'])
chi2, p, dof, expected = chi2_contingency(contingency1)

print("\nAssociation between User Rating and Genre:")
print("Chi-square value:", chi2)
print("p-value:", p)

# 7. Association between User Rating and Price (Correlation)
correlation = df['User Rating'].corr(df['Price'])
print("\nCorrelation between User Rating and Price:", correlation)

# Visualization (optional but helpful)

# Boxplot: Rating vs Genre
plt.figure()
sns.boxplot(x='Genre', y='User Rating', data=df)
plt.title("User Rating vs Genre")
plt.show()

# Scatter plot: Rating vs Price
plt.figure()
sns.scatterplot(x='Price', y='User Rating', data=df)
plt.title("User Rating vs Price")
plt.show()
