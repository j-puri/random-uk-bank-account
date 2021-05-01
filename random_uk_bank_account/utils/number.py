def get_indices_of_min_even_integer(array: [], level=1):
    return _get_indices_of_even_or_odd_integers(type="EVEN", array=array, level=level)


def get_indices_of_min_odd_integer(array: [], level=1):
    return _get_indices_of_even_or_odd_integers(type="ODD", array=array, level=level)


def _get_indices_of_even_or_odd_integers(type, array: [], level=1):
    mod = 0
    if type == "EVEN":
        mod = 0
    elif type == "ODD":
        mod = 1

    selected_integers = [number for number in array if (number % 2) == mod]

    if selected_integers:
        return array.index(sorted(selected_integers)[level - 1])
    else:
        return None
