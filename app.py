students = {
    101: {"name": "Rahul", "attendance": 85, "marks": 78},
    102: {"name": "Priya", "attendance": 90, "marks": 82},
}

def get_student(sid):
    return students.get(sid)

def main():
    print("College ERP System")
    try:
        sid = int(input("Enter Student ID: "))
    except (EOFError, ValueError):
        sid = None
    s = get_student(sid)
    print()
    if s:
        print(f"Student ID: {sid}")
        print(f"Name: {s['name']}")
        print(f"Attendance: {s['attendance']} %")
        print(f"Marks: {s['marks']}")
    else:
        print("Student not found")
    print("\nAll Students")
    for k, v in students.items():
        print(f"{k} - {v['name']}")

if __name__ == "__main__":
    main()