def merge_sort(string):
    if len(string) <= 1:
        return string.lower()

    middle = len(string) // 2
    left_half = string[:middle]
    right_half = string[middle:]

    ordered_left_half = merge_sort(left_half)
    ordered_right_half = merge_sort(right_half)

    return merge(ordered_left_half, ordered_right_half)


def merge(left_half, right_half):
    outcome = []
    index_left = index_right = 0

    while index_left < len(left_half) and index_right < len(right_half):
        if left_half[index_left] < right_half[index_right]:
            outcome.append(left_half[index_left])
            index_left += 1
        else:
            outcome.append(right_half[index_right])
            index_right += 1

    outcome.extend(left_half[index_left:])
    outcome.extend(right_half[index_right:])
    sorted_string = "".join(outcome)
    return sorted_string.lower()


def is_anagram(first_string, second_string):
    ordered_first_string = merge_sort(first_string)
    ordered_second_string = merge_sort(second_string)

    if not first_string or not second_string:
        return (ordered_first_string, ordered_second_string, False)

    if len(first_string) != len(second_string):
        return (ordered_first_string, ordered_second_string, False)

    return (
        ordered_first_string,
        ordered_second_string,
        ordered_first_string == ordered_second_string,
    )
