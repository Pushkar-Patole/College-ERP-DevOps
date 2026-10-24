from app import students, display_student


def test_students_exist():
    assert len(students) == 2


def test_student_data():
    assert students[101]["name"] == "Rahul"


def test_display_student_not_found(capsys):
    display_student(999)
    assert "Student not found" in capsys.readouterr().out