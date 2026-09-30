# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# # 1. Define the dataset first
# np.random.seed(42)
# df = pd.DataFrame({
#     'batch': ['A']*25 + ['B']*25,
#     'score': list(np.random.normal(78, 7, 25)) + list(np.random.normal(68, 10, 25))
# })

# # 2. Call Seaborn on the defined DataFrame
# sns.boxplot(data=df, x='batch', y='score')
# plt.show()



# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
# import numpy as np

# # Sample Data
# np.random.seed(2)
# hours = np.random.uniform(1, 10, 80)
# df = pd.DataFrame({
#     'hours': hours,
#     'score': hours * 6 + np.random.normal(0, 6, 80),
#     'batch': np.random.choice(['Batch A', 'Batch B'], 80)
# })

# # Plot
# g = sns.pairplot(df, hue='batch')

# g.savefig('task3_pairplot.png', dpi=100)
# plt.show()





# import matplotlib
# matplotlib.use('Agg')  # Prevents Tkinter GUI popup / terminal loop
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
# import numpy as np

# # Sample Data Definition
# np.random.seed(3)
# df = pd.DataFrame({
#     'batch': ['Group 1']*25 + ['Group 2']*25,
#     'score': list(np.random.normal(70, 10, 25)) + list(np.random.normal(82, 6, 25))
# })

# # 1. Create plot using Seaborn convenience
# fig, ax = plt.subplots(figsize=(6, 4))
# sns.boxplot(data=df, x='batch', y='score', ax=ax)

# # 2. Refine using Matplotlib precision control
# ax.set_title('Performance Analysis (Refined View)', fontsize=14, fontweight='bold')
# ax.set_xlabel('Student Group', fontsize=11)
# ax.set_ylabel('Test Score (out of 100)', fontsize=11)
# ax.axhline(75, color='red', linestyle='--', label='Passing Benchmark')
# ax.legend()

# # Save image file directly
# fig.savefig('lab4/task4_hybrid.png', dpi=120, bbox_inches='tight')
# plt.close(fig)

# print("Task 4 saved successfully as 'lab4/task4_hybrid.png'!")




# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
# import seaborn as sns
# import pandas as pd
# import numpy as np

# # Set seed for reproducible results
# np.random.seed(4)

# # Sample dataset for EDA
# df = pd.DataFrame({
#     'study_hours': np.random.uniform(2, 10, 50),
#     'exam_score': np.random.uniform(50, 100, 50),
#     'sleep_hours': np.random.uniform(5, 9, 50)
# })

# # Calculate correlation matrix
# corr_matrix = df.corr(numeric_only=True)

# # Generate Heatmap
# fig, ax = plt.subplots(figsize=(6, 5))
# sns.heatmap(corr_matrix, annot=True, cmap='viridis', fmt=".2f", linewidths=0.5, ax=ax)
# ax.set_title('EDA Correlation Heatmap', fontsize=12, fontweight='bold')

# # Save image file directly
# fig.savefig('task5_eda_heatmap.png', dpi=120, bbox_inches='tight')
# plt.close(fig)
# print("Task 3 pairplot saved successfully!")



import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Set seed for reproducible output
np.random.seed(4)

# Sample dataset setup for EDA
df = pd.DataFrame({
    'study_hours': np.random.uniform(2, 10, 50),
    'exam_score': np.random.uniform(50, 100, 50),
    'sleep_hours': np.random.uniform(5, 9, 50)
})

# Generate correlation matrix and heatmap
fig, ax = plt.subplots(figsize=(6, 5))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='viridis', fmt=".2f", linewidths=0.5, ax=ax)
ax.set_title('EDA Correlation Heatmap', fontsize=12, fontweight='bold')

# Save directly to root directory
fig.savefig('task5_eda_heatmap.png', dpi=120, bbox_inches='tight')
plt.close(fig)