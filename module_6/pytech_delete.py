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
    
# test document
test_doc = {
    "student_id": "1010",
    "first_name": "Stan",
    "last_name": "Marsh"
}

# insert the test document into MongoDB atlas
test_doc_id = students.insert_one(test_doc).inserted_id

# insert statements with output
print("\n -- INSERT STATEMENTS --")
print(" Inserted student record into the students collection with document_id "
+ str(test_doc_id))

# call the find_one() method by student_id 1010
student_test_doc = students.find_one({"student_id": "1010"})

# display the results
print("\n -- DISPLAYING STUDENT TEST DOC -- ")
print(" Student ID: " + student_test_doc["student_id"] + "\n First Name: " +
student_test_doc["first_name"] + "\n Last Name: " +
student_test_doc["last_name"] + "\n")

# call the delete_one method to remove the student_test_doc
deleted_student_test_doc = students.delete_one({"student_id": "1010"})

# find all students in the collection
new_student_list = students.find({})

# display message
print("\n -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results
for doc in new_student_list:
    print(" Student ID: " + doc["student_id"] + "\n First Name: " +
doc["first_name"] + "\n Last Name: " + doc["last_name"] + "\n")
    
# exit message
input("\n\n End of program, press any key to continue...")