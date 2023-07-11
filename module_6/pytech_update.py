#import statements
from pymongo import MongoClient

#mongodb connection
url = "mongodb+srv://admin:admin@cluster0.arleilq.mongodb.net/"

#connects mongodb cluster
client = MongoClient(url)

#specifies pytech database
db = client.pytech

#retrieves the student collection
students = db.students

# find all students in the collection
student_list = students.find({})

# display message
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results
for doc in student_list:
    print("Student ID: " + doc["student_id"] + "\n First Name: " + 
doc["first_name"] + "\n Last Name: " + doc ["last_name"] + "\n")
    
# update student_id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name":
"Newton"}})

# find the updated student document
huey = students.find_one({"student_id": "1007"})

# display message
print("\n -- DISPLAYING STUDENT DOCUMENT 1007 --")

# output the updated document to the terminal window
print(" Student ID: " + huey["student_id"] + "\n First Name: " +
huey["first_name"] + "\n Last Name: " + huey["last_name"] + "\n")

# exit message
input("\n\n End of program, press any key to continue...")