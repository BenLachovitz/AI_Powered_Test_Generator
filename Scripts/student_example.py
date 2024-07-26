from my_profile import insert_details_to_my_profile


name: str
grade: str
email: str
gender: str
dob: str
password: str


def set_the_login_or_signup_details(list_of_details):
    global name, grade, email, gender, dob, password
    name = list_of_details[0]
    grade = list_of_details[1]
    email = list_of_details[2]
    gender = list_of_details[3]
    dob = list_of_details[4]
    password = list_of_details[5]
    insert_details_to_my_profile(name, grade, email, gender, dob)

