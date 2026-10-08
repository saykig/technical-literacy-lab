# Practice exercises

Start with [Unit 0's no-code worksheet](00_foundations.md). Python practice follows the browser orientation. Predict, attempt, explain, and ask for a hint before looking at a solution.

| Unit | Practice file | What to do |
|---|---|---|
| 0 | [00_foundations.md](00_foundations.md) | Explain relationships without coding |
| 2 | [01_follow_a_program.py](01_follow_a_program.py) | Predict output, then change one assignment |
| 3 | [02_count_labels.py](02_count_labels.py) | Trace a loop, then change the condition and input |
| 4 | [03_count_status.py](03_count_status.py) | Repair the intentional bug yourself |

Units and original lesson numbers differ: the new Unit 0 comes before the original orientation, and that orientation is Unit 1. Existing Python filenames are preserved.

## Running Python later

The first two scripts can be pasted into Futurecoder or Python Tutor. For the function exercise in a browser, paste the function and call it with your chosen inputs; a definition alone does not print a result. Local files become the focus in Unit 5, though you can use them earlier once you understand the setup.

From the repository's root directory, after Python is installed:

```sh
python3 exercises/01_follow_a_program.py
python3 exercises/02_count_labels.py
python3 exercises/check_03.py
```

Each line is a separate shell command, not Python source. On Windows with the Python launcher, replace `python3` with `py`. The starter scripts need no extra libraries. The supplied checker uses Python 3.9+ syntax; for a new installation, use a currently supported Python 3 version.

The first two scripts display results for you to compare with your predictions. Running `03_count_status.py` directly only defines a function, so it normally produces no output. Run `check_03.py` to call the function on several inputs. Before your repair, some checks must fail and the checker exits with status 1. After a correct repair, those checks pass and it exits with status 0. This expected failure is part of the lesson.

`count_status_cases.py` is shared checker support, not a learner assignment. Do not study its extra syntax before functions make sense. A passing checker is evidence about behavior; an independent explanation and a new example are evidence about learning.

After an attempt, use [the existing checks](../solutions/checks.md) or [reference repair](../solutions/03_count_status.py) to compare. Ask ChatGPT to review your reasoning rather than rewrite the exercise.
