"""
Author: Palaniraj I
Date: 27-May-2021
Project: CGPA  calculator for Bharathidasan University Academic programs.
This project is done as a part of the Code in Place 2021 Program conducted by Stanford University Professors
Chris Piech, Mehran Sahami and team.
"""
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename


def main():
    """
    This function has the function calls to all the helper functions
    """
    print("CGPA Calculator\n\n")
    student_details = {}
    get_student_details(student_details)
    program_details = {}
    get_program_details(program_details)
    no_of_semesters = int(program_details['Number of Semesters'])  # saving the number of semesters in a variable
    semester_details = {}
    """
    This dictionary "semester_details={}" has number of the semester as keys and another dictionary as its value.
    The sub dictionary has the course number as its key and has a list as value for the keys.
    This sub list has the course name, course credits, marks scored, grade points as its elements.
    Example: {1: {'CS01': ['DS', 4, 66.0, 7.0]}}
        {semester number : {course_number : [course name, credits, marks scored, grade points]}} 
    """
    print("CGPA Calculator\n\n")
    get_semester_details(semester_details, no_of_semesters)
    cgpa = []
    calculate_cgpa(semester_details, cgpa)
    print_result(cgpa, no_of_semesters)
    response = messagebox.askyesno("Report","Do you want save the result as a file?")
    if response == 1:
        filename = asksaveasfilename( defaultextension='.txt')
        export_file(filename,cgpa,semester_details,no_of_semesters,student_details,program_details)



def get_student_details(student):
    """
    This function asks the student for name, age, gender, Register Number.
    Parameter: The dictionary created in main function is passed here.
    The user inputs are to stored in the dictionary.
    """
    student_name = input("Enter your Name: ")
    student['Name'] = student_name

    # To save only if the input is integer
    student_age = input("Enter Your age: ")
    while student_age.isalpha():
        student_age = input("Enter Your Age in numbers: ")
    student['Age'] = student_age

    student_program_name = input("Enter your Program Name: ")
    student['Program Name'] = student_program_name

    student_program_subject = input("Enter your Specialization: ")
    student['Specialization'] = student_program_subject

    # Register number can be of any combination
    student_regno = input("Enter your Register Number: ")
    student['Register Number'] = student_regno


def get_program_details(program):
    """
    This function asks for the user's course details such as academic year, number of semesters.
    Parameter: The dictionary created in main function is passed to this function.
    The user inputs are to stored in the dictionary.
    """

    # To save only if the input is  an integer
    program_start = input("Enter the year of admission: ")
    while program_start.isalpha():
        program_start = input("Enter the year in numbers: ")
    program['Year of Admission'] = program_start

    # To save only if the input is  an integer
    program_end = input("Enter the passing out year: ")
    while program_end.isalpha():
        program_end = input("Enter the year in numbers: ")
    program['Year of Completion'] = program_end

    # To save only if the input is  an integer
    no_of_semesters = input("Enter the number of semesters: ")
    while no_of_semesters.isalpha():
        no_of_semesters = input("Enter the value in numbers: ")
    program['Number of Semesters'] = no_of_semesters

    return program


def get_semester_details(semester, no_of_sem):
    """
    This unction asks for the user's input such as the Number of courses in Semester,
    Name of the course, credits, marks scored.
    Parameters: semester is a dictionary which is created in the main function and passed here.
    no_of_sem is an integer that holds the value of the number of semesters.
    """
    # creating number of keys as per the number of semesters.
    for i in range(no_of_sem):
        semester[i+1] = {}
    print("Enter the Semester details such as number of courses and their details.")
    for keys in semester:
        print("Semester "+str(keys))
        course_details(semester[keys], keys)
        # calling an helper function to update the subject details of each semester


def course_details(sem, sem_no):
    """
    This function asks for the number of courses in the semester to the user.
    Asks the user for the course name, course credits
    """
    # To save only if the input is  an integer
    no_of_courses = input("Enter the number of courses in Semester "+str(sem_no)+" : ")
    while no_of_courses.isalpha() or no_of_courses == "":
        no_of_courses = input("Enter the value in numbers: ")
    no_of_courses = int(no_of_courses)

    # To ask for the user's input such as course number, name, course credits, marks scored.
    for i in range(no_of_courses):
        print("Enter the course "+str(i+1)+" details below.")
        course_number = input("Enter the Course "+str(i+1)+" number: ")
        sem[course_number] = []
        course_name = input("Enter the name of the "+str(i+1)+" course: ")
        sem[course_number].append(course_name)
        course_credit = input("Enter the course credit points in number: ")
        while course_credit.isalpha():
            course_credit = input("Enter the value in numbers: ")
        course_credit = int(course_credit)
        sem[course_number].append(course_credit)
        marks_scored = input("Enter the marks scored in numbers: ")
        while marks_scored.isalpha():
            marks_scored = input("Enter the value in numbers: ")
        marks_scored = float(marks_scored)
        sem[course_number].append(marks_scored)
        grade_points = convert_marks_to_grade(marks_scored)
        sem[course_number].append(grade_points)


def convert_marks_to_grade(marks):
    """
    This function converts the marks into grade points as per the norms of the Bharathidasan University.
    Parameter: marks
    """

    grade_point = 0.0
    if marks >= 96:
        grade_point = 10.0
    elif 91 <= marks <= 95:
        grade_point = 9.5
    elif 86 <= marks <= 90:
        grade_point = 9.0
    elif 81 <= marks <= 85:
        grade_point = 8.5
    elif 76 <= marks <= 80:
        grade_point = 8.0
    elif 71 <= marks <= 75:
        grade_point = 7.5
    elif 66 <= marks <= 70:
        grade_point = 7.0
    elif 61 <= marks <= 65:
        grade_point = 6.5
    elif 56 <= marks <= 60:
        grade_point = 6.0
    elif 51 <= marks <= 55:
        grade_point = 5.5
    elif marks <= 50:
        grade_point = 0.0
    return grade_point


def calculate_cgpa(semester, cgpa):
    """
    This function calculates the CGPA for each semester as well as the whole CGPA.
    Parameters: semester is a dictionary which the details of all semester courses.
                CGPA is a list, which is supposed to store all the CGPA calculations.
    """

    course_dict = {}
    temp_list = []
    overall_cgpa = 0.0
    grade_x_credit = 0.0
    sum_of_credits = 0.0
    for keys in semester:
        sem_cgpa = 0.0
        sem_grade_x_credit = 0.0
        sem_sum_of_credits = 0.0
        course_dict = semester[keys]
        for course in course_dict:
            temp_list = course_dict[course]
            sem_grade_x_credit += temp_list[1]*temp_list[3]
            sem_sum_of_credits += temp_list[1]
        sem_cgpa = sem_grade_x_credit/sem_sum_of_credits
        cgpa.append(sem_cgpa)
        sum_of_credits += sem_sum_of_credits
        grade_x_credit += sem_grade_x_credit
    overall_cgpa = grade_x_credit/sum_of_credits
    cgpa.append(overall_cgpa)


def print_result(cgpa, no_of_semesters):
    """
    This function prints the CGPA of each semester as well as the overall CGPA.
    Parameters: CGPA is a list which contains the CGPA details.
                no_of_semesters contains the total number of semesters as an integer.
    """
    for i in range(no_of_semesters):
        print("CGPA of Semester "+str(i+1)+": "+str("{:.2f}".format(cgpa[i])))
    print("Overall CGPA: "+str("{:.2f}".format(cgpa[-1])))

def export_file(filename,cgpa,semester_details,no_of_semesters,student_details,program_details):
    """
    This function writes the content to the file chosen in the save as dialog box.
    """
    with open(filename,"w") as f:
        for key in student_details:
            f.write(str(key)+" : "+str(student_details[key])+"\n")
        for item in program_details:
            f.write(str(item)+" : "+str(program_details[item])+"\n\n")
        f.write("Semester    Course Code    Course Name                             Credits    Marks Scored    Grade Points\n")
        for keys in semester_details:
            tempdict = semester_details[keys]
            for items in tempdict:
                templist = tempdict[items]
                f.write("   "+str(keys)+"           "+str(items)+"        "+str(templist[0])+fill_space(templist[0])+"   "+str(templist[1])+"           "+str(templist[2])+"               "+str(templist[3])+"\n")
        for i in range(len(cgpa)-1):
            f.write("\nCGPA of Semester "+str(i+1)+" : "+ str("{:.2f}".format(cgpa[i]))+"\n")
        f.write("\nOverall CGPA " + str(i + 1)+" : "+ str("{:.2f}".format(cgpa[-1])))

def fill_space(word):
    """
    This is a helper function for the export_file function,
    """
    max = 40 - len(word)
    space = ""
    for i in range(max):
        space += " "
    return space



if __name__ == '__main__':
    main()
