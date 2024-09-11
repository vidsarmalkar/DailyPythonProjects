import sys

grades = {}


def menu() -> None:
    print("""
    Menu:
    1. Add a student and their grade
    2. View all students and their grades
    3. Exit
    """)


def add_student() -> None:
    student_name = input("Enter the student's name: ")
    student_grade = input(f"Enter {student_name}'s grade: ")
    grades[student_name] = student_grade
    print(f"{student_name}'s grade has been added.")


def show_students() -> None:
    print(grades)


def exit() -> None:
    sys.exit()


def get_input() -> None:
    selection = input("Choose an option (1-3): ")
    if selection == '1':
        add_student()
    elif selection == '2':
        show_students()
    elif selection == '3':
        exit()
    else:
        print("User selection is not correct")


def main() -> None:
    while True:
        menu()
        get_input()


if __name__ == '__main__':
    main()
