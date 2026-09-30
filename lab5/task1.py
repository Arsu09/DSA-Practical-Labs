# import pandas as pd
# import seaborn as sns

# # Load dataset
# df = sns.load_dataset('tips')

# print("--- DATASET INFO ---")
# df.info()
# print("\n--- DESCRIPTIVE STATISTICS ---")
# print(df.describe())


# import pandas as pd
# import seaborn as sns

# df = sns.load_dataset('tips')

# # Analyze category counts and proportions
# print("--- VALUE COUNTS FOR 'day' ---")
# print(df['day'].value_counts())

# print("\n--- PROPORTIONS ---")
# print(df['day'].value_counts(normalize=True).round(2))




# import pandas as pd
# import seaborn as sns

# df = sns.load_dataset('tips')
# mean_val = df['total_bill'].mean()
# median_val = df['total_bill'].median()
# skew_val = df['total_bill'].skew()

# print(f"Mean: {mean_val:.2f}")
# print(f"Median: {median_val:.2f}")
# print(f"Skewness: {skew_val:.2f}")



# import pandas as pd
# import seaborn as sns

# df = sns.load_dataset('tips')

# # Standard deviation and Percentiles
# std_dev = df['total_bill'].std()
# quantiles = df['total_bill'].quantile([0.25, 0.75])
# q25 = quantiles[0.25]
# q75 = quantiles[0.75]
# iqr = q75 - q25

# print(f"Standard Deviation: {std_dev:.2f}")
# print(f"25th Percentile (Q1): {q25:.2f}")
# print(f"75th Percentile (Q3): {q75:.2f}")
# print(f"Interquartile Range (IQR): {iqr:.2f}")


# import pandas as pd
# import seaborn as sns

# df = sns.load_dataset('tips')

# # Grouped descriptive summary
# grouped_summary = df.groupby('day')['total_bill'].describe().round(2)
# print(grouped_summary)



import pandas as pd
import seaborn as sns

# Load the dataset
df = sns.load_dataset('tips')

# Calculate mean, median, and skewness for total_bill
mean_val = df['total_bill'].mean()
median_val = df['total_bill'].median()
skew_val = df['total_bill'].skew()

print(f"Mean: {mean_val:.2f}")
print(f"Median: {median_val:.2f}")
print(f"Skewness: {skew_val:.2f}")