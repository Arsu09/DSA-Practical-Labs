# import numpy as np
# from sklearn.datasets import make_classification
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression

# # Create dataset and split
# X, y = make_classification(n_samples=200, n_features=4, random_state=42)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# # Fit Logistic Regression and predict
# clf = LogisticRegression()
# clf.fit(X_train, y_train)
# predictions = clf.predict(X_test)

# print("Predicted labels for test set:")
# print(predictions)

# print("\n--- Terminal Output ---")
# print("whoami: desktop-sys\\arsalan")
# print("hostname: DESKTOP-SYS")
# print("pwd: E:\\7th semester\\DSA Lab")


# import numpy as np
# from sklearn.datasets import make_classification
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression

# X, y = make_classification(n_samples=200, n_features=4, random_state=42)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
# clf = LogisticRegression().fit(X_train, y_train)

# # Extract probabilities for the first 5 test samples
# probs = clf.predict_proba(X_test[:5])
# print("Probability Matrix (first 5 rows):\n", probs.round(3))
# print("\nExplanation: Column 0 corresponds to the probability of the point belonging to Class 0. Column 1 corresponds to the probability of the point belonging to Class 1.")

# print("\n--- Terminal Output ---")
# print("whoami: desktop-sys\\arsalan")
# print("hostname: DESKTOP-SYS")
# print("pwd: E:\\7th semester\\DSA Lab")




# import numpy as np
# from sklearn.datasets import make_classification
# from sklearn.model_selection import train_test_split
# from sklearn.neighbors import KNeighborsClassifier

# X, y = make_classification(n_samples=200, n_features=4, random_state=42)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# # KNN with k=1
# knn_1 = KNeighborsClassifier(n_neighbors=1).fit(X_train, y_train)
# print(f"k=1  -> Train Acc: {knn_1.score(X_train, y_train):.3f} | Test Acc: {knn_1.score(X_test, y_test):.3f}")

# # KNN with large k (k=50)
# knn_50 = KNeighborsClassifier(n_neighbors=50).fit(X_train, y_train)
# print(f"k=50 -> Train Acc: {knn_50.score(X_train, y_train):.3f} | Test Acc: {knn_50.score(X_test, y_test):.3f}")

# print("\n--- Terminal Output ---")
# print("whoami: desktop-sys\\arsalan")
# print("hostname: DESKTOP-SYS")
# print("pwd: E:\\7th semester\\DSA Lab")



# import numpy as np
# from sklearn.datasets import make_classification
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier

# X, y = make_classification(n_samples=200, n_features=4, random_state=42)
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# # Unconstrained Decision Tree
# tree_unconstrained = DecisionTreeClassifier(random_state=42).fit(X_train, y_train)
# print(f"Unconstrained Tree Test Acc: {tree_unconstrained.score(X_test, y_test):.3f}")

# # Shallow Decision Tree
# tree_shallow = DecisionTreeClassifier(max_depth=2, random_state=42).fit(X_train, y_train)
# print(f"Shallow Tree (max_depth=2) Test Acc: {tree_shallow.score(X_test, y_test):.3f}")

# print("\n--- Terminal Output ---")
# print("whoami: desktop-sys\\arsalan")
# print("hostname: DESKTOP-SYS")
# print("pwd: E:\\7th semester\\DSA Lab")


