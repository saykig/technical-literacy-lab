# Curriculum review and setup checks

Reviewed 8 October 2026 before creating the private GitHub repository.

The separate supplied syllabus matched the ZIP's syllabus. The original plan moves from browser-based Python practice to local files and Git, then datasets/SQL, APIs, repository reading, AI literacy, and later language transfer. That order has been retained. The ZIP included four starter lessons; the later units were a roadmap, not complete lessons.

The main gap was the assumption that the learner already understood computers and tool roles. Unit 0 now supplies a short conceptual introduction, familiar examples, diagrams, comprehension questions, and a no-code worksheet. Detailed systems theory and installations remain deferred. The README, syllabus, glossary, tutor instructions, lesson navigation, and progress record now use the same starting point.

The initial import is preserved in Git history. All six supplied Python files are unchanged from that import, including the deliberate debugging bug and the existing reference repair. The learner still makes the exercise edits.

## Verification

Checks ran locally with Python 3.9.6 and no third-party packages:

- All six Python files parsed successfully.
- The first two practice scripts produced their expected outputs.
- Running the function-definition exercise directly completed without output, as expected.
- The debugging checker reported two passing and five failing cases, with exit status 1, before a learner repair. That is the intended starting behavior.
- The existing reference repair passed all seven supplied cases, with exit status 0.
- The checker resolved its practice file correctly when launched from another working directory.
- Local Markdown links and linked heading anchors were checked; syllabus and progress both contain Unit 0 followed by Units 1–12.

Free-course starting links and foundation references were rechecked as recorded in [SOURCES.md](SOURCES.md). No website, custom CLI, package setup, or automated deployment infrastructure was added. These checks verify the supplied starting materials; they do not assess the learner or prove correctness for every possible input.
