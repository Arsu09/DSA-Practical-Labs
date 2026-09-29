# import pandas as pd
# df = pd.DataFrame({
#     'region': ['North', 'South', 'North', 'East', 'South', 'East'],
#     'sales': [100, 200, 150, 300, 250, 400]
# })
# total_sales_per_region = df.groupby('region')['sales'].sum()

# print("Total Sales Per Region:")
# print(total_sales_per_region)



# import pandas as pd
# df = pd.DataFrame({
#     'batch': ['A', 'B', 'A', 'B', 'A', 'B'],
#     'score': [88, 72, 90, 60, 55, 95]
# })
# summary_table = df.groupby('batch')['score'].agg(['mean', 'max', 'count'])

# print("Aggregated Summary Table:")
# print(summary_table)




# import pandas as pd

# df = pd.DataFrame({
#     'batch':   ['A', 'A', 'B', 'B', 'A', 'B'],
#     'subject': ['math', 'cs', 'math', 'cs', 'math', 'cs'],
#     'score':   [88, 90, 60, 72, 55, 95]
# })
# pivot_grid = df.pivot_table(index='batch', columns='subject', values='score', aggfunc='mean')
# print("Reshaped Pivot Table Grid:")
# print(pivot_grid)



# import pandas as pd
# df1 = pd.DataFrame({'key': [1, 2, 3, 4], 'val1': ['A', 'B', 'C', 'D']})
# df2 = pd.DataFrame({'key': [1, 2, 3], 'val2': ['X', 'Y', 'Z']})

# inner_merged = pd.merge(df1, df2, on='key', how='inner')
# left_merged = pd.merge(df1, df2, on='key', how='left')

# print("Inner Merge Result Count:", len(inner_merged))
# print("Left Merge Result Count :", len(left_merged))



import pandas as pd

df_a = pd.DataFrame({'key': [1, 2, 3], 'val_a': ['A1', 'A2', 'A3']})
df_b = pd.DataFrame({'key': [2, 3, 4], 'val_b': ['B2', 'B3', 'B4']})

outer_merged = pd.merge(df_a, df_b, on='key', how='outer')

print("Outer Merge Result (Missing values filled with NaN):")
print(outer_merged)