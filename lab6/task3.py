# from sklearn.metrics import classification_report

# # Small set of 10 true and predicted labels
# y_true = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1]
# y_pred = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0]

# print("--- Classification Report ---")
# print(classification_report(y_true, y_pred))

# print("\n--- Terminal Output ---")
# print("whoami: desktop-sys\\arsalan")
# print("hostname: DESKTOP-SYS")
# print("pwd: E:\\7th semester\\DSA Lab")


# from sklearn.metrics import confusion_matrix

# # 15 actual negatives (0): 13 predicted correctly (0), 2 predicted wrongly (1)
# # 5 actual positives (1): 2 predicted correctly (1), 3 predicted wrongly (0)
# y_true = [0]*15 + [1]*5
# y_pred = [0]*13 + [1]*2 + [0]*3 + [1]*2

# cm = confusion_matrix(y_true, y_pred)
# print("--- Confusion Matrix ---")
# print(cm)

# print("\n--- Terminal Output ---")
# print("whoami: desktop-sys\\arsalan")
# print("hostname: DESKTOP-SYS")
# print("pwd: E:\\7th semester\\DSA Lab")


# from sklearn.datasets import make_classification
# from sklearn.model_selection import cross_val_score
# from sklearn.linear_model import LogisticRegression

# # Generate dummy dataset
# X, y = make_classification(n_samples=100, n_features=4, random_state=42)
# clf = LogisticRegression()

# # Cross validation with f1 scoring
# f1_scores = cross_val_score(clf, X, y, cv=5, scoring='f1')

# print("--- F1 Scores per fold ---")
# print(f1_scores)

# print("\n--- Terminal Output ---")
# print("whoami: desktop-sys\\arsalan")
# print("hostname: DESKTOP-SYS")
# print("pwd: E:\\7th semester\\DSA Lab")


# from sklearn.datasets import make_classification
# from sklearn.model_selection import cross_val_score
# from sklearn.pipeline import make_pipeline
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LogisticRegression

# # Generate dataset
# X, y = make_classification(n_samples=100, n_features=4, random_state=42)

# # Create a leak-free pipeline
# pipe = make_pipeline(StandardScaler(), LogisticRegression())

# # Evaluate the pipeline safely
# scores = cross_val_score(pipe, X, y, cv=5, scoring='accuracy')

# print("--- Leak-Free Pipeline CV Scores ---")
# print(scores)

# print("\n--- Terminal Output ---")
# print("whoami: desktop-sys\\arsalan")
# print("hostname: DESKTOP-SYS")
# print("pwd: E:\\7th semester\\DSA Lab")


