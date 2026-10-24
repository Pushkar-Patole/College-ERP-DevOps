from app import get_student

def test_existing_student():
    assert get_student(101)["name"] == "Rahul"

def test_missing_student():
    assert get_student(999) is None