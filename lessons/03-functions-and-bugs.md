# Lesson 3 — Functions and a bug that does not need a crash

## Aim

Turn a repeated operation into a function and understand early return.

A function definition begins with `def`. The names inside its parentheses are parameters. When a function is called, the supplied values are arguments. `return` sends a result back to the caller and ends that function call immediately. It does not merely display a value.

Open [the debugging exercise](../exercises/03_count_status.py). It is deliberately wrong:

```python
def count_status(statuses, wanted):
    count = 0
    for status in statuses:
        if status == wanted:
            count = count + 1
        return count
```

The intended contract is: given a list of status strings and one target string, return the number of exact matches. For an empty list, return 0. The function must not change the input list. Input validation for other types is outside this first exercise's scope.

## Before editing

Predict the result for `count_status(["accepted", "pending", "accepted"], "accepted")`. Then trace the first iteration and ask whether the second iteration ever starts.

Predict the result for an empty list. Remember that a Python function reaching its end without executing `return` returns `None`, which is not the number 0.

## Repair

Change as little as possible. Do not replace the loop with a different technique. Explain why your edit changes which instructions execute.

Once you know how to run local files, the provided checker can be run from the root folder with:

```sh
python3 exercises/check_03.py
```

On Windows with the Python launcher, the equivalent is `py exercises/check_03.py`. In a browser, call the function with the example inputs manually instead.

The checker intentionally reports failures before the repair. Afterward, inspect the individual checks and explain what each one establishes. The checker itself introduces more syntax; you do not need to read its complete implementation yet.

## Readiness check

Explain why one passing example is insufficient. Distinguish an incorrect result, an exception, and a bad assumption about what a status means. Write one additional input that could expose the early-return bug.

Reference: [Python functions and control flow](https://docs.python.org/3/tutorial/controlflow.html).

After an independent attempt, compare with [the solution](../solutions/03_count_status.py).
