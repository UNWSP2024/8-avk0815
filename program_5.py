# Program #5: Course Info
# Write a program that has the user input a bunch of course ID and course name pairs.  
# For example a course ID could be "COS 2005" and the course name could be "Python Programming."   
# Then ask the user for a subject (like "COS"). 
# Finally, the program will display the ID and name of all the courses having that subject.

def course_info():
    courses = {}

    print("Enter course ID and course name pairs (Example, COS 2005: Python Programming). Type 'done' when finished.")
    while True:
        user_input = input("Course ID and Name: ")
        if user_input.lower() == 'done':
            break
        try:
            course_id, course_name = user_input.split(":")
            courses[course_id.strip()] = course_name.strip()
        except ValueError:
            print("Invalid format. Please enter in the format 'Course ID: Course Name'.")
            
    subject = input("Enter a subject (Example: COS): ")
    print(f"\nCourses in subject '{subject}':")
    for course_id, course_name in courses.items():
        if course_id.startswith(subject):
            print(f"  {course_id}: {course_name}")
if __name__ == "__main__":
    course_info()