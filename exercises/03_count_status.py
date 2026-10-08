# Intentional debugging exercise: return is in the wrong place.
# Inputs: a list of strings and a target string. Output: match count.
def count_status(statuses, wanted):
    count = 0
    for status in statuses:
        if status == wanted:
            count = count + 1
        return count
