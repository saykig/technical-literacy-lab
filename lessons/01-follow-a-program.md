# Lesson 1 — Follow the state of a small program

Syllabus Unit 2. Previous: [Unit 1 — browser orientation](00-orientation.md). If saving, running, and output still blur together, revisit [Unit 0](00-foundations.md).

## Aim

Understand assignment and execution order before trying to write a large program.

In Python, `=` assigns a value to a name. `+` adds these numbers. `print(...)` displays a value. A name such as `papers_read` is a variable; it is not special Python vocabulary.

Read the program:

```python
papers_read = 3
new_papers = 2
total = papers_read + new_papers
new_papers = 5
print(total)
```

The important question is whether `total` is a stored result or an automatically updating formula. Predict the output before running it. The answer and explanation are in [the checks](../solutions/checks.md), not here.

## Trace it

Write the values after each line:

| Line executed | papers_read | new_papers | total |
|---|---|---|---|
| 1 | | | not assigned |
| 2 | | | not assigned |
| 3 | | | |
| 4 | | | |

Run [the exercise](../exercises/01_follow_a_program.py), or paste its code into the browser environment. Compare the output with your prediction.

## Change one thing

Make the final printed value use the newer value of `new_papers`. Do this by placing one assignment at the appropriate point, not by replacing `print(total)` with a fixed answer.

Then put quotation marks around one of the numbers, such as `new_papers = "2"`, and predict what will happen when Python tries to add it to a number. An error message is evidence about what the program attempted, not a reason to abandon the exercise.

## Teach it back

Explain assignment, a variable, and output in your own words. Then explain why changing a variable later does or does not change an earlier computed value.

Reference: [Python tutorial](https://docs.python.org/3/tutorial/), especially its introductory arithmetic and assignment examples. Our exercise is original.

Next: [Lesson 2](02-collections-and-decisions.md).
