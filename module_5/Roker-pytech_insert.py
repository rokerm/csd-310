from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.arleilq.mongodb.net/"
client = MongoClient(url)
db = client.pytech
students = db.students

# Document for New Students
huey = {
    "first_name" : "Huey",
    "last_name" : "Freeman",
    "student_id" : "1007"
}
huey_student_id = students.insert_one(huey).inserted_id
print(huey_student_id)

finn = {
    "first_name" : "Finn",
    "last_name" : "Mertins",
    "student_id" : "1008"
}
finn_student_id = students.insert_one(finn).inserted_id
print(finn_student_id)

catherine = {
    "first_name" : "Cathrine",
    "last_name" : "Higgens",
    "student_id" : "1009"
}
catherine_student_id = students.insert_one(catherine).inserted_id
print(catherine_student_id)
