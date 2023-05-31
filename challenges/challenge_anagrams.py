def ordered_string(string):
    characters = list(string.lower())
    characters_length = len(characters)

    for i in range(characters_length):
        min_index = i
        for j in range(i + 1, characters_length):
            if characters[j] < characters[min_index]:
                min_index = j
        characters[i], characters[min_index] = (
            characters[min_index],
            characters[i],
        )
    sorted_string = "".join(characters)
    return sorted_string


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    if len(first_string) != len(second_string):
        return False
    return ordered_string(first_string) == ordered_string(second_string)
