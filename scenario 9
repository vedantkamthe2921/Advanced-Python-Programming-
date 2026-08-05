#9 Course Management System, Develop a Python application to maintain course information.
# Course Management System

class Course:
    def __init__(self, name, duration, fee):
        self.name = name
        self.duration = duration      # Duration in months
        self.fee = fee

    # Categorize Course
    def category(self):
        if self.duration <= 6:
            return "Short-Term"
        else:
            return "Long-Term"


class Institute:
    def __init__(self):
        self.courses = []

    # Add Course
    def add_course(self, course):
        self.courses.append(course)

    # Display Courses
    def display_courses(self):
        print("\nCourse Details")
        print("-" * 40)
        for course in self.courses:
            print("Course Name :", course.name)
            print("Duration    :", course.duration, "Months")
            print("Fee         : Rs.", course.fee)
            print("Category    :", course.category())
            print("-" * 40)


# Main Program
institute = Institute()

# Add Courses
institute.add_course(Course("Python Programming", 3, 15000))
institute.add_course(Course("Data Science", 12, 60000))
institute.add_course(Course("Web Development", 6, 25000))

# Display All Courses
institute.display_courses()
