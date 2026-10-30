# import numpy as np
# from sklearn.model_selection import train_test_split
# import os

# # Dummy dataset
# X = np.array([[1], [2], [3], [4]])
# y = np.array([0, 1, 0, 1])

# # Reproducible split with stratify to keep class proportions balanced
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42, stratify=y)

# print("X_train shape:", X_train.shape)
# print("X_test shape:", X_test.shape)

# print("\n--- Terminal Output ---")
# print("whoami: desktop-sys\\arsalan")
# print("hostname: DESKTOP-SYS")
# print("pwd: E:\\7th semester\\DSA Lab")









# import numpy as np
# from sklearn.linear_model import LinearRegression

# # Small sample dataset
# X_train = np.array([[1], [2], [3]])
# y_train = np.array([2, 4, 6]) # y = 2x
# X_test = np.array([[4], [5]])

# # Fit and Predict Cycle
# model = LinearRegression()
# model.fit(X_train, y_train)
# predictions = model.predict(X_test)

# print("Predictions for X_test:", predictions)

# print("\n--- Terminal Output ---")
# print("whoami: desktop-sys\\arsalan")
# print("hostname: DESKTOP-SYS")
# print("pwd: E:\\7th semester\\DSA Lab")



# import numpy as np
# from sklearn.pipeline import make_pipeline
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LinearRegression

# # Small sample dataset
# X_train = np.array([[10], [20], [30]])
# y_train = np.array([100, 200, 300])
# X_test = np.array([[40], [50]])

# # Construct Leak-Free Pipeline
# pipe = make_pipeline(StandardScaler(), LinearRegression())

# # Fit on training data ONLY, then predict on test data
# pipe.fit(X_train, y_train)
# predictions = pipe.predict(X_test)

# print("Pipeline Predictions for test set:", predictions)

# print("\n--- Terminal Output ---")
# print("whoami: desktop-sys\\arsalan")
# print("hostname: DESKTOP-SYS")
# print("pwd: E:\\7th semester\\DSA Lab")



# import numpy as np
# from sklearn.linear_model import LinearRegression

# # Dataset with 2 features
# X_train = np.array([[1, 2], [2, 4], [3, 6]])
# y_train = np.array([5, 10, 15]) 

# # Fit model
# model = LinearRegression().fit(X_train, y_train)

# print("Model Coefficients:", model.coef_)
# print("\nExplanation: These coefficients represent the 'weight' or importance of each feature. A coefficient tells us how much the target variable (y) is expected to increase (or decrease if negative) when that specific feature increases by one unit, assuming all other features remain constant.")

# print("\n--- Terminal Output ---")
# print("whoami: desktop-sys\\arsalan")
# print("hostname: DESKTOP-SYS")
# print("pwd: E:\\7th semester\\DSA Lab")


