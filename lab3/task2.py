# import pandas as pd

# df = pd.DataFrame({
#     'id': [1, 2, 1, 3],
#     'name': ['Ali', 'Sara', 'Ali', 'Omar']
# })

# duplicate_count = df.duplicated().sum()

# df_clean = df.drop_duplicates()

# print("Duplicate rows count:", duplicate_count)
# print("\nFinal Cleaned DataFrame:")
# print(df_clean)



# import pandas as pd
# df = pd.DataFrame({'price': ['10.5', '20.0', 'missing', '15.2']})

# df['price'] = pd.to_numeric(df['price'], errors='coerce')

# print("Column Data Types:")
# print(df.dtypes)

# print("\nConverted DataFrame:")
# print(df)



# import pandas as pd
# df = pd.DataFrame({'name': [' Ali ', 'ali', 'ALI', 'Sara']})

# df['name'] = df['name'].str.strip().str.lower()

# print("Cleaned DataFrame:")
# print(df)




# import pandas as pd
# import numpy as np

# train = pd.DataFrame({'age': [22, np.nan, 35, 19, 40]})
# test = pd.DataFrame({'age': [np.nan, 28, 30]})

# train_median = train['age'].median()
# train['age'] = train['age'].fillna(train_median)
# test['age'] = test['age'].fillna(train_median)

# print("Calculated Training Median:", train_median)
# print("\nImputed Train DataFrame:")
# print(train)
# print("\nImputed Test DataFrame:")
# print(test)


import pandas as pd
import numpy as np

df = pd.DataFrame({
    'ID': [101, np.nan, 103, 104, 105],
    'Score': [88, 72, np.nan, 91, 60]
})

df_clean = df.dropna(subset=['ID']).copy()
df_clean['Score'] = df_clean['Score'].fillna(df_clean['Score'].mean())

print("Final DataFrame with mixed missing data strategy:")
print(df_clean)