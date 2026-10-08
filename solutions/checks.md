# Checks — open after an attempt

## Lesson 1

The program prints `5`. The assignment to `total` computed `3 + 2` at that point in execution. Reassigning `new_papers` afterward does not recalculate `total`. Assign `total = papers_read + new_papers` again after `new_papers = 5` to make the final output `8`.

With a string value `"2"`, directly adding it to the integer 3 raises a TypeError. Text and numbers are not interchangeable. Converting with `int("2")` would produce an integer, but arbitrary text cannot always be converted into a number.

## Lesson 2

The initial output is `2`. The counter progresses through 1, 1, and 2. Counting `"pending"` instead gives 1. An empty list gives 0 because no iteration changes the initial counter.

Putting `print(count)` inside the loop can display intermediate counts, depending on its exact indentation. It is a different program, not merely a different style.

For the independent numbers exercise, exactly 4 and 7 are greater than 3. The number 3 is not greater than itself, so the result is 2.

## Lesson 3

The buggy function returns after its first iteration. For the three-element example it returns 1 rather than 2. For an empty list the loop never runs, and the function returns `None` implicitly.

Move `return count` outside the loop while keeping it inside the function. This preserves the accumulator until every item has been examined and also returns 0 for an empty list. See [the reference repair](03_count_status.py).

The checks cover an empty input, a single match, no match, multiple matches, a match later in the list, case-sensitive matching, a different target, and lack of input mutation on those cases. They do not prove correctness for every possible object or validate the meaning of the labels.
