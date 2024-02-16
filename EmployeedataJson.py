import json

# JSON data as a string
json_data = '''
{
  "employees": {
    "employee": [
      {
        "name": "John Doe",
        "age": 20,
        "city": "New York",
        "isStudent": true,
        "skills": ["Java", "C#", "Python", "JavaScript"]
      },
      {
        "name": "John Smith",
        "age": 30,
        "city": "Raleigh",
        "isStudent": false,
        "skills": ["Java", "Python", "JavaScript", "Ruby"]
      },
      {
        "name": "Kattie Josh",
        "age": 23,
        "city": "Ellicott City",
        "isStudent": true,
        "skills": ["Java", "Python", "JavaScript"]
      }
    ]
  }
}
'''

# Load the JSON data
data = json.loads(json_data)

# Retrieve and print employee information
employees = data["employees"]["employee"]
for employee in employees:
    print("\nName:", employee["name"])
    print("Age:", employee["age"])
    print("City:", employee["city"])
    print("Is Student:", employee["isStudent"])
    print("Skills:", ", ".join(employee["skills"]))
