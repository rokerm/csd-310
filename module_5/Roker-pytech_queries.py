from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.arleilq.mongodb.net/"
client = MongoClient(url)
db = client.pytech
students = db.students

# Query All Students
print("--DISPLAYING ALL NEW STUDENTS FROM find() QUERY--")
docs = students.find ({})
for doc in docs:
    print(doc)

# Query One Student
print("--DISPLAYING ONE STUDENT FROM find_one() QUERY--")
doc = students.find_one({"student_id": "1007"})
print(doc)

