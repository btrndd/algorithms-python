def study_schedule(permanence_period, target_time):
    if (target_time is None):
        return None
    total_students = 0
    for index in range(0, len(permanence_period)):
        if (
            type(permanence_period[index][0]) is not int
            or type(permanence_period[index][1]) is not int
        ):
            return None
        if (
            target_time >= permanence_period[index][0]
            and target_time <= permanence_period[index][1]
        ):
            total_students += 1
    return total_students
