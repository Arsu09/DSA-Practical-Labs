# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load dataset
# df = sns.load_dataset('tips')

# # Generate Histogram with KDE
# fig, ax = plt.subplots(figsize=(6, 4))
# sns.histplot(df['total_bill'], kde=True, bins=25, ax=ax)
# ax.set_title('Distribution of Total Bill', fontsize=12, fontweight='bold')
# ax.set_xlabel('Total Bill ($)')
# ax.set_ylabel('Count')

# # Save image directly in root directory
# fig.savefig('task1_distribution.png', dpi=120, bbox_inches='tight')
# plt.close(fig)



# import seaborn as sns
# import matplotlib.pyplot as plt

# # Load dataset
# df = sns.load_dataset('tips')

# # Generate Histogram with KDE
# ax = sns.histplot(df['total_bill'], kde=True, bins=25)
# ax.set_title('Distribution of Total Bill', fontsize=12, fontweight='bold')
# ax.set_xlabel('Total Bill ($)')
# ax.set_ylabel('Count')

# plt.show()



# import pandas as pd
# import seaborn as sns

# df = sns.load_dataset('tips')
# col = df['total_bill']

# q1 = col.quantile(0.25)
# q3 = col.quantile(0.75)
# iqr = q3 - q1
# lower_bound = q1 - 1.5 * iqr
# upper_bound = q3 + 1.5 * iqr

# outliers = df[(col < lower_bound) | (col > upper_bound)]

# print(f"Q1: {q1:.2f}, Q3: {q3:.2f}, IQR: {iqr:.2f}")
# print(f"IQR Bounds: [{lower_bound:.2f}, {upper_bound:.2f}]")
# print(f"Flagged Outliers Count: {len(outliers)}\n")
# print(outliers[['total_bill', 'tip', 'day', 'size']])



# import pandas as pd
# import numpy as np
# import seaborn as sns

# df = sns.load_dataset('tips')
# col = df['total_bill']
# z_scores = (col - col.mean()) / col.std()

# z_outliers = df[np.abs(z_scores) > 3]

# print(f"Z-Score Outliers Count (|z| > 3): {len(z_outliers)}\n")
# print(z_outliers[['total_bill', 'tip', 'day', 'size']])





# import pandas as pd
# import numpy as np
# import seaborn as sns

# df = sns.load_dataset('tips')
# col = df['total_bill']

# # 1. IQR Rule
# q1, q3 = col.quantile(0.25), col.quantile(0.75)
# iqr = q3 - q1
# iqr_outliers = df[(col < (q1 - 1.5 * iqr)) | (col > (q3 + 1.5 * iqr))]

# # 2. Z-Score Rule
# z_scores = (col - col.mean()) / col.std()
# z_outliers = df[np.abs(z_scores) > 3]

# print(f"IQR Outliers Count: {len(iqr_outliers)}")
# print(f"Z-Score Outliers Count: {len(z_outliers)}")






# import pandas as pd
# import numpy as np
# import seaborn as sns

# df = sns.load_dataset('tips')
# col = df['total_bill']

# q1 = col.quantile(0.25)
# q3 = col.quantile(0.75)
# iqr = q3 - q1
# lower_iqr = q1 - 1.5 * iqr
# upper_iqr = q3 + 1.5 * iqr
# iqr_outliers = df[(col < lower_iqr) | (col > upper_iqr)]

# z_scores = (col - col.mean()) / col.std()
# z_outliers = df[np.abs(z_scores) > 3]

# print(f"IQR Outliers Count: {len(iqr_outliers)}")
# print(f"Z-Score Outliers Count (|z| > 3): {len(z_outliers)}")





import pandas as pd
import numpy as np
import seaborn as sns

# Load a highly skewed dataset variable
df = sns.load_dataset('tips')
col = df['total_bill']

# 1. IQR Rule Implementation
q1 = col.quantile(0.25)
q3 = col.quantile(0.75)
iqr = q3 - q1
lower_iqr = q1 - 1.5 * iqr
upper_iqr = q3 + 1.5 * iqr
iqr_outliers = df[(col < lower_iqr) | (col > upper_iqr)]

# 2. Z-Score Rule Implementation
z_scores = (col - col.mean()) / col.std()
z_outliers = df[np.abs(z_scores) > 3]

# Output Counts
print(f"IQR Outliers Count: {len(iqr_outliers)}")
print(f"Z-Score Outliers Count (|z| > 3): {len(z_outliers)}")