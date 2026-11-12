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


'''

# Add the search function before main(), and invoke it after displaying the total.
if "def search_student(" not in text:
    text = text.replace("def main():", search_function + "def main():")

if 'search_student(students, "Van")' not in text:
    text = text.replace(
        '    print(f"\\nTotal: {len(students)} students")',
        '    print(f"\\nTotal: {len(students)} students")\n\n'
        '    # Tìm kiếm sinh viên\n'
        '    print("\\n--- Tìm kiếm ---")\n'
        '    search_student(students, "Van")'
    )

output = Path("/mnt/data/main_updated.py")
output.write_text(text, encoding="utf-8")
print(f"Đã tạo: {output}")
print(text)
