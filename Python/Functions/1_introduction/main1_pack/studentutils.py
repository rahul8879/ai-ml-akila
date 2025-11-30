def get_average_marks(student, subjects,):
    average = sum(subjects.values()) / len(subjects)
    print("Average marks: {0} -> {1:.2f}".format(student, average))
    return [student, average]

def top_student_name(average_marks_list):
    top_student = max(average_marks_list)
    print(f"Top Student: {top_student[0]}")
