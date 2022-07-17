def study_schedule(permanence_period, target_time):
    if (target_time is None):
        return None
    total_students = 0
    for student in permanence_period:
        if (student[0] is None or student[1] is None):
            return None
        if (type(student[0]) is not int or type(student[1]) is not int):
            return None
        if (target_time >= student[0] and target_time <= student[1]):
            total_students += 1
    return total_students
