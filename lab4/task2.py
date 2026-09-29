# # import matplotlib.pyplot as plt
# # # Data
# # x = [1, 2, 3, 4, 5]
# # y = [10, 25, 35, 42, 50]
# # fig, ax = plt.subplots()
# # ax.plot(x, y, marker='o', label='Growth Trajectory')
# # # Customizing plot for clarity
# # ax.set_title('Product Adoption Rate Over Time')
# # ax.set_xlabel('Time (Months)')
# # ax.set_ylabel('Users (in Thousands)')
# # ax.legend()

# # plt.show()



# import matplotlib.pyplot as plt
# weeks = [1, 2, 3, 4, 5]
# series_a = [50, 55, 65, 70, 85]
# series_b = [40, 48, 52, 60, 68]

# fig, ax = plt.subplots()
# # Distinguish series using BOTH colors AND line styles/markers
# ax.plot(weeks, series_a, color='tab:blue', linestyle='-', marker='o', label='Group A')
# ax.plot(weeks, series_b, color='tab:orange', linestyle='--', marker='s', label='Group B')

# ax.set_title('Group Performance (Accessible View)')
# ax.set_xlabel('Week')
# ax.set_ylabel('Score (%)')
# ax.legend()

# plt.show()





# import matplotlib.pyplot as plt

# categories = ['Product A', 'Product B', 'Product C']
# sales = [98, 100, 99]

# fig, ax = plt.subplots()
# ax.bar(categories, sales, color='skyblue')

# # Specific command to prevent misleading axis truncation
# ax.set_ylim(bottom=0)

# ax.set_title('Honest Sales Comparison Across Products')
# ax.set_xlabel('Products')
# ax.set_ylabel('Units Sold')

# plt.show()



# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5, 6, 7]
# y = [12, 15, 14, 45, 18, 16, 13]  # Spike at x = 4

# fig, ax = plt.subplots()
# ax.scatter(x, y, color='tab:purple', s=50)

# # Direct annotation pointing to the point of interest
# ax.annotate('Traffic Spike', xy=(4, 45), xytext=(2.5, 40),
#             arrowprops=dict(arrowstyle='->', color='black', lw=1.5))

# ax.set_title('Network Request Monitoring')
# ax.set_xlabel('Hour')
# ax.set_ylabel('Requests per Second')

# plt.show()





import matplotlib.pyplot as plt

categories = ['Dept 1', 'Dept 2', 'Dept 3', 'Dept 4']
values = [45, 60, 52, 70]

fig, ax = plt.subplots()

# Data-ink principle: Use a single, consistent color for a single series
ax.bar(categories, values, color='steelblue')

ax.set_title('Departmental Resource Allocation')
ax.set_xlabel('Department')
ax.set_ylabel('Budget Allocated ($k)')

plt.show()