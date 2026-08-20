# Student Grade Calculator
# Week 2 Project - Control Flow & Data Structures
# Name: Pratiksha Navnath Gajare

# ANSI color codes
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"


# --------------------------------------------------
# Calculate grade and personalized comment
# --------------------------------------------------
def calculate_grade(average):
    if average >= 90:
        return "A", "Excellent! Keep up the great work!"
    elif average >= 80:
        return "B", "Very Good! You're doing well."
    elif average >= 70:
        return "C", "Good. Room for improvement."
    elif average >= 60:
        return "D", "Needs Improvement. Please study more."
    else:
        return "F", "Failed. Please seek help from your teacher."


# --------------------------------------------------
# Get a valid mark between 0 and 100
# --------------------------------------------------
def get_valid_mark(subject):
    while True:
        try:
            mark = float(input(f"{subject}: "))

            if 0 <= mark <= 100:
                return mark
            else:
                print("Please enter a mark between 0 and 100.")

        except ValueError:
            print("Invalid input! Please enter a number.")


# --------------------------------------------------
# Get number of students
# --------------------------------------------------
def get_number_of_students():
    while True:
        try:
            number = int(input("Enter number of students: "))

            if number > 0:
                return number
            else:
                print("Please enter a positive number.")

        except ValueError:
            print("Invalid input! Please enter a whole number.")


# --------------------------------------------------
# Get student name
# --------------------------------------------------
def get_student_name():
    while True:
        name = input("Student name: ").strip()

        if name:
            return name

        print("Name cannot be empty!")


# --------------------------------------------------
# Get grade color
# --------------------------------------------------
def get_grade_color(grade):
    if grade == "A":
        return GREEN
    elif grade == "B":
        return BLUE
    elif grade == "C":
        return YELLOW
    elif grade == "D":
        return YELLOW
    else:
        return RED


# --------------------------------------------------
# Add students
# --------------------------------------------------
def add_students(names, marks, results):

    number = get_number_of_students()

    for i in range(number):

        print("\n" + "=" * 50)
        print(f"STUDENT {i + 1}")
        print("=" * 50)

        name = get_student_name()

        print("\nEnter marks from 0 to 100:")

        math = get_valid_mark("Math")
        science = get_valid_mark("Science")
        english = get_valid_mark("English")

        student_marks = [math, science, english]

        average = sum(student_marks) / len(student_marks)

        grade, comment = calculate_grade(average)

        names.append(name)
        marks.append(student_marks)

        results.append({
            "name": name,
            "marks": student_marks,
            "average": average,
            "grade": grade,
            "comment": comment
        })

        print(f"\n{GREEN}Student added successfully!{RESET}")


# --------------------------------------------------
# Display results
# --------------------------------------------------
def display_results(results):

    if not results:
        print("\nNo student data available.")
        return

    print("\n" + "=" * 100)
    print("                         RESULTS SUMMARY")
    print("=" * 100)

    print(
        f"{'Name':<20}"
        f"{'Math':>8}"
        f"{'Science':>10}"
        f"{'English':>10}"
        f"{'Average':>10}"
        f"{'Grade':>8}"
    )

    print("-" * 100)

    for student in results:

        color = get_grade_color(student["grade"])

        print(
            f"{student['name']:<20}"
            f"{student['marks'][0]:>8.1f}"
            f"{student['marks'][1]:>10.1f}"
            f"{student['marks'][2]:>10.1f}"
            f"{student['average']:>10.1f}"
            f"{color}{student['grade']:>8}{RESET}"
        )

        print(f"   Comment: {student['comment']}")

    print("=" * 100)


# --------------------------------------------------
# Display statistics
# --------------------------------------------------
def display_statistics(results):

    if not results:
        print("\nNo student data available.")
        return

    averages = []

    for student in results:
        averages.append(student["average"])

    class_average = sum(averages) / len(averages)

    highest = max(averages)
    lowest = min(averages)

    highest_index = averages.index(highest)
    lowest_index = averages.index(lowest)

    print("\n" + "=" * 60)
    print("                    CLASS STATISTICS")
    print("=" * 60)

    print(f"Total Students : {len(results)}")
    print(f"Class Average  : {class_average:.2f}")
    print(
        f"Highest Average: {highest:.2f} "
        f"({results[highest_index]['name']})"
    )
    print(
        f"Lowest Average : {lowest:.2f} "
        f"({results[lowest_index]['name']})"
    )

    print("=" * 60)


# --------------------------------------------------
# Search for a student
# --------------------------------------------------
def search_student(results):

    if not results:
        print("\nNo student data available.")
        return

    search_name = input("\nEnter student name to search: ").strip().lower()

    found = False

    for student in results:

        if search_name in student["name"].lower():

            found = True

            color = get_grade_color(student["grade"])

            print("\n" + "=" * 60)
            print("                  STUDENT FOUND")
            print("=" * 60)

            print(f"Name    : {student['name']}")
            print(f"Math    : {student['marks'][0]:.1f}")
            print(f"Science : {student['marks'][1]:.1f}")
            print(f"English : {student['marks'][2]:.1f}")
            print(f"Average : {student['average']:.2f}")
            print(f"Grade   : {color}{student['grade']}{RESET}")
            print(f"Comment : {student['comment']}")

            print("=" * 60)

    if not found:
        print(f"\nNo student found with name '{search_name}'.")


# --------------------------------------------------
# Save results to a file
# --------------------------------------------------
def save_results(results):

    if not results:
        print("\nNo results available to save.")
        return

    try:

        with open("results.txt", "w") as file:

            file.write("=" * 80 + "\n")
            file.write("              STUDENT GRADE CALCULATOR RESULTS\n")
            file.write("=" * 80 + "\n\n")

            for student in results:

                file.write(f"Name: {student['name']}\n")
                file.write(f"Math: {student['marks'][0]:.1f}\n")
                file.write(f"Science: {student['marks'][1]:.1f}\n")
                file.write(f"English: {student['marks'][2]:.1f}\n")
                file.write(f"Average: {student['average']:.2f}\n")
                file.write(f"Grade: {student['grade']}\n")
                file.write(f"Comment: {student['comment']}\n")
                file.write("-" * 80 + "\n")

            averages = []

            for student in results:
                averages.append(student["average"])

            class_average = sum(averages) / len(averages)

            file.write("\nCLASS STATISTICS\n")
            file.write("=" * 80 + "\n")
            file.write(f"Total Students: {len(results)}\n")
            file.write(f"Class Average: {class_average:.2f}\n")
            file.write(f"Highest Average: {max(averages):.2f}\n")
            file.write(f"Lowest Average: {min(averages):.2f}\n")

        print(f"\n{GREEN}Results saved successfully to results.txt{RESET}")

    except IOError:
        print("Error! Could not save the results file.")


# --------------------------------------------------
# Main menu
# --------------------------------------------------
def main():

    student_names = []
    student_marks = []
    student_results = []

    while True:

        print("\n")
        print("=" * 60)
        print("              STUDENT GRADE CALCULATOR")
        print("=" * 60)

        print("1. Add Students")
        print("2. Display Results")
        print("3. Show Class Statistics")
        print("4. Search Student")
        print("5. Save Results")
        print("6. Exit")

        print("=" * 60)

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":

            add_students(
                student_names,
                student_marks,
                student_results
            )

        elif choice == "2":

            display_results(student_results)

        elif choice == "3":

            display_statistics(student_results)

        elif choice == "4":

            search_student(student_results)

        elif choice == "5":

            save_results(student_results)

        elif choice == "6":

            print("\n" + "=" * 60)
            print("Thank you for using the Student Grade Calculator!")
            print("=" * 60)

            break

        else:

            print(
                f"{RED}Invalid choice! "
                f"Please enter a number between 1 and 6.{RESET}"
            )


# --------------------------------------------------
# Program starts here
# --------------------------------------------------
if __name__ == "__main__":
    main()