import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew, chi2_contingency

# Load dataset (update file path)
df = pd.read_csv("students.csv")

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

# 3. Statistical measures of numerical features
print("\nStatistical Summary:\n")
print(df.describe())

# 4. Count plots for categorical variables
categorical_cols = df.select_dtypes(include=['object']).columns

for col in categorical_cols:
    plt.figure()
    sns.countplot(x=col, data=df)
    plt.title(f"Count Plot of {col}")
    plt.xticks(rotation=45)
    plt.show()

# 5. Pie charts
# Race/Ethnicity
race_counts = df['race/ethnicity'].value_counts()
plt.figure()
race_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title("Race/Ethnicity Distribution")
plt.ylabel("")
plt.show()

# Parental Level of Education
parent_counts = df['parental level of education'].value_counts()
plt.figure()
parent_counts.plot(kind='pie', autopct='%1.1f%%')
plt.title("Parental Level of Education")
plt.ylabel("")
plt.show()

# 6. Males and females in different race groups
gender_race = pd.crosstab(df['gender'], df['race/ethnicity'])
print("\nGender vs Race:\n", gender_race)

# 7. Lunch type vs Gender
gender_lunch = pd.crosstab(df['gender'], df['lunch'])
print("\nGender vs Lunch:\n", gender_lunch)

# 8. Distribution & skewness of numerical features
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in numeric_cols:
    plt.figure()
    sns.histplot(df[col], bins=10, kde=True)
    plt.title(f"Distribution of {col}")
    plt.show()
    
    print(f"Skewness of {col}: {skew(df[col])}")

# 9. Association between Gender and Math Score (Chi-square test)
# Convert math score into categories
df['math_category'] = pd.cut(df['math score'], bins=[0,50,75,100], labels=['Low','Medium','High'])

contingency = pd.crosstab(df['gender'], df['math_category'])
chi2, p, dof, expected = chi2_contingency(contingency)

print("\nAssociation between Gender and Math Score:")
print("Chi-square value:", chi2)
print("p-value:", p)

# 10. Correlation Heatmap
plt.figure()
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()
