# # import seaborn as sns
# # import pandas as pd
# # import numpy as np

# # # Load tips dataset
# # df = sns.load_dataset('tips')

# # # Compute correlation matrix for numeric columns
# # numeric_df = df.select_dtypes(include=[np.number])
# # corr_matrix = numeric_df.corr().round(2)

# # print(corr_matrix)





# # import seaborn as sns
# # import pandas as pd
# # import numpy as np

# # # Load dataset and calculate correlation matrix
# # df = sns.load_dataset('tips')
# # corr_matrix = df.select_dtypes(include=[np.number]).corr().round(2)

# # print("Correlation Matrix:")
# # print(corr_matrix)



# # import pandas as pd
# # import seaborn as sns
# # import numpy as np

# # # Load tips dataset and select numeric columns
# # df = sns.load_dataset('tips')
# # numeric_df = df.select_dtypes(include=[np.number])

# # # Compute correlation matrix
# # corr_matrix = numeric_df.corr().round(2)
# # print("--- CORRELATION MATRIX ---")
# # print(corr_matrix)



# # import matplotlib
# # matplotlib.use('Agg')
# # import matplotlib.pyplot as plt
# # import numpy as np

# # # Create a perfect U-shaped non-linear relationship
# # np.random.seed(42)
# # x = np.linspace(-5, 5, 100)
# # y = x**2  # Fully determined quadratic relationship

# # # Compute the correlation coefficient
# # r = np.corrcoef(x, y)[0, 1]
# # print(f"Correlation coefficient r: {r:.4f}")

# # # Plot the scatter plot
# # fig, ax = plt.subplots(figsize=(6, 4))
# # ax.scatter(x, y, color='purple', alpha=0.7)
# # ax.set_title('U-Shaped Non-Linear Relationship (r ≈ 0)')
# # ax.set_xlabel('x')
# # ax.set_ylabel('y = x²')

# # # Save the plot
# # fig.savefig('task3_nonlinear.png', dpi=120, bbox_inches='tight')
# # plt.close(fig)






# # import pandas as pd
# # import seaborn as sns
# # import numpy as np

# # # Load dataset and isolate numeric columns
# # df = sns.load_dataset('tips')
# # numeric_df = df.select_dtypes(include=[np.number])

# # # Generate and print the correlation matrix
# # corr_matrix = numeric_df.corr().round(2)
# # print("Correlation Matrix:")
# # print(corr_matrix)


# # import matplotlib
# # matplotlib.use('Agg')
# # import matplotlib.pyplot as plt
# # import seaborn as sns

# # # Load dataset
# # df = sns.load_dataset('tips')

# # # Create a box plot comparing tip (numeric) across smoker status (categorical)
# # fig, ax = plt.subplots(figsize=(6, 4))
# # sns.boxplot(data=df, x='smoker', y='tip', ax=ax, palette='Set2')
# # ax.set_title('Tip Amount Distribution Across Smoker Categories')
# # ax.set_xlabel('Smoker Status')
# # ax.set_ylabel('Tip ($)')

# # # Save the plot
# # fig.savefig('task4_boxplot.png', dpi=120, bbox_inches='tight')
# # plt.close(fig)




# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load dataset
# df = sns.load_dataset('tips')

# # Create a box plot checking the confounder (total_bill) across the category (smoker)
# fig, ax = plt.subplots(figsize=(6, 4))
# sns.boxplot(data=df, x='smoker', y='total_bill', ax=ax, palette='Set3')
# ax.set_title('Total Bill by Smoker Status (Checking the Confounder)')
# ax.set_xlabel('Smoker Status')
# ax.set_ylabel('Total Bill ($)')

# # Save the plot
# fig.savefig('task5_confounder.png', dpi=120, bbox_inches='tight')
# plt.close(fig)




# import matplotlib
# matplotlib.use('Agg')
# import matplotlib.pyplot as plt
# import seaborn as sns

# # Load the tips dataset
# df = sns.load_dataset('tips')

# # Generate box plot to visualize the categorical difference
# fig, ax = plt.subplots(figsize=(6, 4))
# sns.boxplot(data=df, x='smoker', y='total_bill', ax=ax, palette='Set3')
# ax.set_title('Total Bill by Smoker Status')
# ax.set_xlabel('Smoker Status')
# ax.set_ylabel('Total Bill ($)')

# # Save the plot
# fig.savefig('task5_confounder.png', dpi=120, bbox_inches='tight')
# plt.close(fig)








import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('Agg')

fig, ax = plt.subplots()

ax.plot([1, 2, 3, 4, 5], [50, 50, 63, 71, 80], marker='o')

ax.set_title("Score over sessions")
ax.set_xlabel("Sessions")
ax.set_ylabel("Scores")

fig.savefig("line.png", dpi=150, bbox_inches='tight')

print("Check your line.png file")