import json

# Specify the path to your JSON file
json_file_path = "./Tester.json"

# Read the JSON file
with open(json_file_path, 'r') as file:
    # Load the JSON content
    data = json.load(file)

# Access and print specific values from the loaded data
print("Name:", data["name"])
print("Age:", data["age"])
print("City:", data["city"])
print("Is Student:", data["isStudent"])
print("Skills:", data["skills"])
