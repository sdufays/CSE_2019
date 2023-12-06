import os
from consolemenu import ConsoleMenu, SelectionMenu
from consolemenu.items import FunctionItem, SubmenuItem

week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

def list_to_string(lst):
    return ''.join(lst)

def update_roster(file_name):
    with open(file_name, "r") as file:
        lines = [line for line in file if line.strip()]
    with open("class_roster.txt", "w") as file:
        file.writelines(lines)

def print_roster():
    update_roster("class_attendance.txt")
    with open("class_roster.txt", "r") as file:
        students = file.readlines()
    print("Current students in class:\n" + list_to_string(students))

def add_student():
    student_name = input("Name of student to add: ")
    with open("class_attendance.txt", "a") as file:
        file.write(student_name + "\n")
    print_roster()

def remove_student():
    student_name = input("Name of student to remove: ")
    if not student_name:
        print("Not Valid Input!")
    else:
        with open("class_attendance.txt", "r") as file:
            lines = file.readlines()
        with open("class_attendance.txt", "w") as file:
            file.writelines(line for line in lines if line.strip("\n") != student_name)
        print(f"{student_name} removed from list" if student_name + "\n" in lines else "Student does not exist")
    input("Press Enter to go back to menu. ")

def take_attendance():
    day_of_week = input("What day of the week is it? ")
    while day_of_week not in week_days:
        print("That is not a valid day of the week!")
        day_of_week = input("What day of the week is it? ")

    with open("Class Report.txt", "a") as report_file, open("class_attendance.txt", "r") as attendance_file:
        print("Attendance Options: Present: 1, Tardy: 2, Tardy Unexcused: 3, Absent Excused: 4, Absent Unexcused: 5, Unknown: 6")
        for name in attendance_file:
            name = name.strip()
            if name:
                attendance_status = int(input(f"{name}'s attendance status on {day_of_week}: "))
                while attendance_status not in range(1, 7):
                    print("Integer not in range!")
                    attendance_status = int(input(f"{name}'s attendance status on {day_of_week}: "))

                status_dict = {1: "Present", 2: "Tardy", 3: "Absent Excused", 4: "Absent Unexcused", 5: "Unknown"}
                status = status_dict.get(attendance_status, "Unknown")
                report_file.write(f"{name}: {status} on {day_of_week}\n")
                print(f"Attendance updated for {name}")

def generate_week_report():
    with open("Class Report.txt", "r") as file:
        report = file.readlines()
    print("Weekly Report:\n" + list_to_string(report))
    input("Press Enter to continue ")

def view_class_roster():
    print_roster()
    input("Press Enter to go back to menu! ")

# Create the menu
menu = ConsoleMenu("Class Management System", "Welcome!")

# Add menu items
menu.append_item(FunctionItem("Add Students to Class", add_student))
menu.append_item(FunctionItem("Remove Students from Class", remove_student))
menu.append_item(FunctionItem("Take Attendance", take_attendance))
menu.append_item(FunctionItem("Generate Weekly Report", generate_week_report))
menu.append_item(FunctionItem("View Class Roster", view_class_roster))

# Submenu for days of the week
days_of_week_menu = SelectionMenu(week_days, "Days of the Week")
menu.append_item(SubmenuItem("Days of the Week", days_of_week_menu, menu))

# Display the menu
menu.show()
