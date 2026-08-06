def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "F"
def topper(marks_dict):
    if not marks_dict:
        return None
    return max(marks_dict, key=marks_dict.get)

def average(marks_list):
    return sum(marks_list) / len(marks_list)

if __name__ == "__main__":
    marks = 82
    print("Marks:", marks)
    print("Grade:", calculate_grade(marks))
    student_marks = {"Alice": 85, "Bob": 92, "Charlie": 78}
    print("Topper:", topper(student_marks))
    print("Average of [82, 76, 90]:", average([82, 76, 90]))
    
