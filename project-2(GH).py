# ==========================================
# ======= STUDENT MANAGEMENT SYSTEM =======
# ==========================================

students = {
"ali": {"marks": 85, "city": "Lahore", "fee": 25000},
"sara": {"marks": 92, "city": "Karachi", "fee": 30000},
"ahmad": {"marks": 78, "city": "Lahore", "fee": 25000},
"zara": {"marks": 65, "city": "Islamabad", "fee": 20000}
}

present_today = {"ali", "sara", "zara"}
science_class = {"sara", "ahmad", "zara"}

# Finding highest marks

ali_marks = students["ali"]["marks"]
sara_marks = students["sara"]["marks"]
ahmad_marks = students["ahmad"]["marks"]
zara_marks = students["zara"]["marks"]

marks_list = [ali_marks, sara_marks, ahmad_marks, zara_marks]

highest_marks = max(marks_list)

if(ali_marks == highest_marks):
    print("Ali has the highest marks")

if(sara_marks == highest_marks):
    print("Sara has the highest marks")

if(ahmad_marks == highest_marks):
    print("Ahmad has the highest marks")

if(zara_marks == highest_marks):
    print("Zara has the highest marks")

# Finding lowest marks

ali_low = students["ali"]["marks"]
sara_low = students["sara"]["marks"]
ahmad_low = students["ahmad"]["marks"]
zara_low = students["zara"]["marks"]

lowest_marks_list = [ali_low, sara_low, ahmad_low, zara_low]

lowest_marks = min(lowest_marks_list)

if(ali_low == lowest_marks):
    print("Ali has the lowest marks")

if(sara_low == lowest_marks):
    print("Sara has the lowest marks")

if(ahmad_low == lowest_marks):
    print("Ahmad has the lowest marks")

if(zara_low == lowest_marks):
    print("Zara has the lowest marks")

print("Students present and also in science class:",present_today.intersection(science_class))

print("Students only present today:",present_today - science_class)

# Student search system

name = input("Please enter the student name: ").lower()

if(name in students):
    print("marks:",students[name]["marks"])
    print("city:",students[name]["city"])

else:
    print("Student not found!!")

# Calculating total fee

ali_fee = students["ali"]["fee"]
sara_fee = students["sara"]["fee"]
ahmad_fee = students["ahmad"]["fee"]
zara_fee = students["zara"]["fee"]

fee_list = [ali_fee, sara_fee, ahmad_fee, zara_fee]

total_fee = sum(fee_list)

print("Total fee of all students is:", total_fee)

# Students with marks greater than or equal to 70
print("Students with marks greater than or equal to 70")
if(students["ali"]["marks"] >= 70):
    print("ali")

if(students["sara"]["marks"] >= 70):
    print("sara")

if(students["ahmad"]["marks"] >= 70):
    print("ahmad")

if(students["zara"]["marks"] >= 70):
    print("zara")

