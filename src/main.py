from pathlib import Path

source = Path("/mnt/data/main.py")
text = source.read_text(encoding="utf-8")

search_function = '''def search_student(students: list, keyword: str) -> list:
    """Tìm kiếm sinh viên theo tên hoặc mã.

    Args:
        students: Danh sách sinh viên
        keyword: Từ khóa tìm kiếm

    Returns:
        Danh sách sinh viên khớp với từ khóa
    """
    results = []
    keyword_lower = keyword.lower()

    for s in students:
        if keyword_lower in s.name.lower() or keyword_lower in s.student_id.lower():
            results.append(s)

    if results:
        print(f"🔍 Tìm thấy {len(results)} sinh viên với từ khóa '{keyword}':")
        for s in results:
            print(f"  {s}")
    else:
        print(f"❌ Không tìm thấy sinh viên nào với từ khóa '{keyword}'")

    return results


<<<<<<< HEAD
'''
=======
def add_student(students: list, student_id: str, name: str, age: int, grade: str) -> list:
    """Thêm sinh viên mới vào danh sách.
    Args:
        students: Danh sách sinh viên hiện tại
        student_id: Mã sinh viên
        name: Họ tên
        age: Tuổi
        grade: Khóa
    Returns:
        Danh sách sinh viên đã được cập nhật
    """
    # Kiểm tra trùng mã sinh viên
    for s in students:
        if s.student_id == student_id:
            print(f"❌ Mã sinh viên {student_id} đã tồn tại!")
            return students

    new_student = Student(student_id, name, age, grade)
    students.append(new_student)
    print(f"Đã thêm sinh viên: {new_student}")
    return students


def main():
    """Hàm chính của ứng dụng."""
    print("=" * 50)
    print("STUDENT MANAGER — DevOps Lab 5")
    print("=" * 50)
>>>>>>> origin/develop

# Add the search function before main(), and invoke it after displaying the total.
if "def search_student(" not in text:
    text = text.replace("def main():", search_function + "def main():")

<<<<<<< HEAD
if 'search_student(students, "Van")' not in text:
    text = text.replace(
        '    print(f"\\nTotal: {len(students)} students")',
        '    print(f"\\nTotal: {len(students)} students")\n\n'
        '    # Tìm kiếm sinh viên\n'
        '    print("\\n--- Tìm kiếm ---")\n'
        '    search_student(students, "Van")'
    )
=======
    # Thêm sinh viên mới
    students = add_student(students, "SV004", "Pham Thi D", 22, "K19")

    # Hiển thị danh sách
    for student in students:
        print(f"  {student}")
>>>>>>> origin/develop

output = Path("/mnt/data/main_updated.py")
output.write_text(text, encoding="utf-8")
print(f"Đã tạo: {output}")
print(text)
