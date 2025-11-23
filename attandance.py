import json
import os
from datetime import datetime


DATA_FILE = "attendance_data.json"

def load_data():
    """Loads data from the JSON file. Returns default structure if file doesn't exist."""
    if not os.path.exists(DATA_FILE):
        return {"students": [], "attendance": {}}
    
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError):
        return {"students": [], "attendance": {}}

def save_data(data):
    """Saves the current data dictionary to the JSON file."""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"Error saving data: {e}")


def add_student(data):
    print("\n--- Add New Student ---")
    roll_no = input("Enter Roll Number: ").strip()
    
    
    for s in data["students"]:
        if s["roll_no"] == roll_no:
            print("Error: Student with this Roll Number already exists.")
            return

    name = input("Enter Student Name: ").strip()
    if not name or not roll_no:
        print("Error: Name and Roll Number cannot be empty.")
        return

    data["students"].append({"roll_no": roll_no, "name": name})
    save_data(data)
    print(f"Success: {name} (Roll: {roll_no}) added!")

def view_students(data):
    print("\n--- Student List ---")
    if not data["students"]:
        print("No students registered yet.")
        return
    
    print(f"{'Roll No':<15} | {'Name':<20}")
    print("-" * 40)
    for s in data["students"]:
        print(f"{s['roll_no']:<15} | {s['name']:<20}")

def delete_student(data):
    print("\n--- Delete Student ---")
    roll_no = input("Enter Roll Number to delete: ").strip()
    
    
    student_found = False
    student_index = -1
    student_name = ""
    
    for i, s in enumerate(data["students"]):
        if s["roll_no"] == roll_no:
            student_index = i
            student_name = s["name"]
            student_found = True
            break
    
    if not student_found:
        print("Error: Student with that Roll Number not found.")
        return

    
    confirm = input(f"Are you sure you want to PERMANENTLY delete {student_name}? (y/n): ").lower()
    if confirm == 'y':
        
        del data["students"][student_index]
        
        
        for date in data["attendance"]:
            if roll_no in data["attendance"][date]:
                data["attendance"][date].remove(roll_no)
        
        save_data(data)
        print(f"Success: Student {student_name} and their attendance history deleted.")
    else:
        print("Deletion cancelled.")


def mark_attendance(data):
    print("\n--- Mark Attendance ---")
    if not data["students"]:
        print("No students to mark. Add students first.")
        return

    date = input("Enter Date (YYYY-MM-DD) [Press Enter for Today]: ").strip()
    if not date:
        date = datetime.now().strftime("%Y-%m-%d")
    
    print(f"Marking attendance for: {date}")
    print("Type 'P' for Present, 'A' for Absent (default is Absent)")

    
    if date not in data["attendance"]:
        data["attendance"][date] = []

    present_count = 0
    for student in data["students"]:
        
        if student["roll_no"] in data["attendance"][date]:
            print(f"{student['name']} is already marked PRESENT.")
            continue

        status = input(f"Is {student['name']} ({student['roll_no']}) present? [y/n]: ").lower()
        if status == 'y':
            data["attendance"][date].append(student["roll_no"])
            present_count += 1
    
    save_data(data)
    print(f"\nAttendance saved! {present_count}/{len(data['students'])} present on {date}.")


def view_report(data):
    print("\n--- Attendance Report ---")
    if not data["attendance"]:
        print("No attendance records found.")
        return

    total_sessions = len(data["attendance"])
    print(f"Total Sessions Conducted: {total_sessions}")
    print("-" * 65)
    print(f"{'Roll No':<10} | {'Name':<20} | {'Present':<8} | {'%':<6} | {'Status'}")
    print("-" * 65)

    for student in data["students"]:
        present_days = 0
        for date, present_list in data["attendance"].items():
            if student["roll_no"] in present_list:
                present_days += 1
        
        percentage = (present_days / total_sessions) * 100 if total_sessions > 0 else 0.0
        status = "Low" if percentage < 75 else "Good"
        
        print(f"{student['roll_no']:<10} | {student['name']:<20} | {present_days:<8} | {percentage:.1f}%  | {status}")


def main():
    data = load_data()
    
    while True:
        print("\n" + "="*30)
        print(" SMART TRACK (CLI Version)")
        print("="*30)
        print("1. Add Student")
        print("2. View Students")
        print("3. Mark Attendance")
        print("4. View Report")
        print("5. Delete Student")  
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            add_student(data)
        elif choice == '2':
            view_students(data)
        elif choice == '3':
            mark_attendance(data)
        elif choice == '4':
            view_report(data)
        elif choice == '5':
            delete_student(data) 
        elif choice == '6':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()   