# Lesson 2 — Lists, loops, and decisions

## Aim

Read a small decision repeated over several values.

Square brackets create a list. Quotation marks mark text values. `for` visits each item in the list. `if` runs its indented block only when its condition holds. `==` compares two values; it does not assign one. Indentation is part of Python's syntax, not just visual decoration.

```python
statuses = ["accepted", "pending", "accepted"]
count = 0
for status in statuses:
    if status == "accepted":
        count = count + 1
print(count)
```

These are invented administrative labels. The program counts labels; it does not establish that any scientific claim is true.

## Predict, then run

Write the value of `status` and `count` after each iteration. Predict the final output. Run [the exercise](../exercises/02_count_labels.py) or use a browser environment.

Change the condition to count `"pending"`. Then replace the input with `[]`, an empty list. Predict again before running each change.

## Two important boundaries

The list contains strings, not records of evidence. A status label is not a verification procedure. Also, comparing text is exact: `"Accepted"` is different from `"accepted"`.

## Small independent task

Write a similar program that counts numbers greater than 3 in `[1, 4, 3, 7]`. The symbol `>` means “greater than.” Explain what happens to the value exactly equal to 3. Do not use a library or ask an assistant to write the whole solution first.

## Readiness check

Explain the roles of the list, loop variable, condition, counter, and indentation. Explain what changes when the final `print` is placed inside the loop.

Reference: [Python control flow](https://docs.python.org/3/tutorial/controlflow.html).

Next: [Lesson 3](03-functions-and-bugs.md).
