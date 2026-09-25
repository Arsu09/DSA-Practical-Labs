# student = {
#     'name': 'Ali',
#     'score': 88,
#     'coordinates': (25.3960, 68.3578)
# }

# # Print dictionary and individual elements
# print("Dictionary record:")
# print(student)

# print("\nAccessed fields:")
# print("Name:", student['name'])
# print("Score:", student['score'])
# print("Coordinates:", student['coordinates'])# Create dictionary with required keys and types



# raw_readings = [12.5, 45.0, 102.1, 8.2, 150.3, 33.7]

# # Filter list comprehension for values > 40.0
# filtered_readings = [r for r in raw_readings if r > 40.0]

# print("Filtered Readings (> 40.0):")
# print(filtered_readings)



# user_ids = [101, 102, 103]

# # Dictionary comprehension mapping ID to 'User_{id}'
# user_map = {uid: f"User_{uid}" for uid in user_ids}

# print("User ID Mapping:")
# print(user_map)



# def safe_convert(val):
#     """Convert value to int or return 'Invalid' if conversion fails."""
#     try:
#         return int(val)
#     except (ValueError, TypeError):
#         return 'Invalid'

# # Test calls with required inputs
# res_valid = safe_convert('10')
# res_invalid = safe_convert('N/A')

# print("Result for '10':", res_valid)
# print("Result for 'N/A':", res_invalid)



# def safe_convert(val):
#     """Convert value to int or return 'Invalid' if conversion fails."""
#     try:
#         return int(val)
#     except (ValueError, TypeError):
#         return 'Invalid'

# # Table represented as a list of dicts
# data = [{'val': '10'}, {'val': '20'}, {'val': 'error'}, {'val': '30'}]

# # Process each record using list comprehension
# results = [safe_convert(item['val']) for item in data]

# print("Processed Table Results:")
# print(results)