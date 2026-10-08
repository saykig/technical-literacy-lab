# Compare with your own repair only after an independent attempt.
def count_status(statuses, wanted):
    count = 0
    for status in statuses:
        if status == wanted:
            count = count + 1
    return count
