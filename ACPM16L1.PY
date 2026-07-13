import pandas as pd

# Load dataset (update path if needed)
df = pd.read_csv("bestsellers.csv")

# 1. Check quantitative and categorical features
print("Quantitative Features:")
print(df.select_dtypes(include=['int64', 'float64']).columns)

print("\nCategorical Features:")
print(df.select_dtypes(include=['object']).columns)

# 2. Check for null values
print("\nNull Values in Dataset:")
print(df.isnull().sum())

# 3. Handle missing values (if any)
# Example: Fill numeric with mean, categorical with mode
for col in df.columns:
    if df[col].dtype in ['int64', 'float64']:
        df[col].fillna(df[col].mean(), inplace=True)
    else:
        df[col].fillna(df[col].mode()[0], inplace=True)

# 4. Mean, Median, Mode of User Rating
print("\nUser Rating Statistics:")
print("Mean:", df['User Rating'].mean())
print("Median:", df['User Rating'].median())
print("Mode:", df['User Rating'].mode()[0])

# 5. Mean, Median, Mode of Price
print("\nPrice Statistics:")
print("Mean:", df['Price'].mean())
print("Median:", df['Price'].median())
print("Mode:", df['Price'].mode()[0])

# 6. Mean, Median, Mode of Reviews
print("\nReviews Statistics:")
print("Mean:", df['Reviews'].mean())
print("Median:", df['Reviews'].median())
print("Mode:", df['Reviews'].mode()[0])
