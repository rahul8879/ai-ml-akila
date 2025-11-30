def get_average_marks1(student, subjects):
    print("Average marks: {0} -> {1:.2f}".format(student, sum(subjects.values())/len(subjects)))