def study_schedule(permanence_period, target_time):
    if not target_time:
        return None
    number_of_students = 0
    for period in permanence_period:
        if not isinstance(period[0], int) or not isinstance(period[1], int):
            return None
        if period[0] <= target_time <= period[1]:
            number_of_students += 1
    return number_of_students
