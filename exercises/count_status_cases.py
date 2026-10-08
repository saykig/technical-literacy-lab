"""Test support: read after learning functions; not a first-lesson exercise."""
from collections.abc import Callable


def run_checks(function: Callable[[list[str], str], object]) -> int:
    """Return zero when the specified examples and no-mutation check pass."""
    cases = [
        ([], "accepted", 0),
        (["accepted"], "accepted", 1),
        (["pending"], "accepted", 0),
        (["accepted", "pending", "accepted"], "accepted", 2),
        (["pending", "accepted"], "accepted", 1),
        (["Accepted", "accepted"], "accepted", 1),
        (["accepted", "pending", "pending"], "pending", 2),
    ]
    failures = 0
    for values, wanted, expected in cases:
        original = values.copy()
        try:
            actual = function(values, wanted)
            passed = type(actual) is int and actual == expected and values == original
        except Exception as error:
            actual = f"{type(error).__name__}: {error}"
            passed = False
        label = "PASS" if passed else "FAIL"
        print(f"{label}: {original!r}, target={wanted!r}: expected {expected}, got {actual!r}")
        failures += int(not passed)
    if failures:
        print(f"{failures} check(s) failed. Trace the function before rewriting it.")
    else:
        print("These checks passed. Explain the repair and add one new test.")
    return int(failures > 0)
