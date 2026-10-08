"""Check the debugging exercise. Failures before its repair are intentional."""
from count_status_cases import run_checks
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

path = Path(__file__).with_name("03_count_status.py")
spec = spec_from_file_location("learner_exercise", path)
if spec is None or spec.loader is None:
    raise RuntimeError("Could not load the exercise beside this checker.")
module = module_from_spec(spec)
spec.loader.exec_module(module)
raise SystemExit(run_checks(module.count_status))
