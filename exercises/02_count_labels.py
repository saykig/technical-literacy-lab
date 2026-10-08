# These labels are invented practice data, not scientific findings.
statuses = ["accepted", "pending", "accepted"]
count = 0
for status in statuses:
    if status == "accepted":
        count = count + 1
print(count)
