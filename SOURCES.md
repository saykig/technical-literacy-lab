# Sources and resource decisions

Reviewed 7 October 2026. This is a selected curriculum, not an exhaustive repository survey. Course pages and selected repository READMEs were inspected; full deployments and every exercise were not audited. Prices, interfaces, and account entitlements can change.

## The learning core

### S1 — Futurecoder: initial practice environment
[Course](https://futurecoder.io/) · [Repository](https://github.com/alexmojaki/futurecoder)

A free, open-source, browser-based Python course for complete beginners. It requires code execution and includes visual debugging and staged hints. Use the hosted course; do not fork and maintain its full application to learn Python. Its README's local setup requires a Python and frontend toolchain. The repository identifies its license as MIT; inspect the relevant files before reusing material.

### S2 — CS50P: selected structured programming material
[Course and syllabus](https://cs50.harvard.edu/python/)

Free OpenCourseWare for learners with or without prior programming experience. Follow the relevant topics, not a second full beginner course in parallel. This plan uses original practice exercises; anyone submitting CS50 work must follow that course's academic-honesty rules. A paid credential is not needed to study the OpenCourseWare.

### S3 — Software Carpentry: practical research computing
[Python course](https://swcarpentry.github.io/python-novice-gapminder/) · [Python repository](https://github.com/swcarpentry/python-novice-gapminder)

[Shell course](https://swcarpentry.github.io/shell-novice/) · [Shell repository](https://github.com/swcarpentry/shell-novice)

[Git course](https://swcarpentry.github.io/git-novice/) · [Git repository](https://github.com/swcarpentry/git-novice)

[SQL course](https://swcarpentry.github.io/sql-novice-survey/) · [SQL repository](https://github.com/swcarpentry/sql-novice-survey)

Use these for the transition from isolated snippets to files, datasets, and reproducible work. The Python lesson expects knowledge of files, working directories, and launching an interpreter. The lesson pages identify their teaching materials as CC BY 4.0. Preserve attribution for any adaptations and inspect file-level terms before redistribution.

### S4 — MIT Missing Semester: software-tool literacy
[Course](https://missing.csail.mit.edu/) · [Repository](https://github.com/missing-semester/missing-semester)

The 2026 syllabus covers shells, development environments, debugging, Git, packaging, and code quality. Use selected sections after initial programming practice; it is not the first Python course. Its README identifies course content and website source as CC BY-NC-SA 4.0. Linking is simpler than combining its material into a differently licensed course.

### S5 — Python Tutor: visual execution
[Tool](https://pythontutor.com/)

A free browser tool for stepping through short programs and inspecting variables and objects. Use it to test your mental model of execution, not merely to obtain an answer. Do not paste private or sensitive code into an external service.

## Later material, not required on day one

### S6 — Rust Book and Rustlings
[Book](https://doc.rust-lang.org/book/) · [Ownership chapter](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html)

[Rustlings](https://rustlings.rust-lang.org/) · [Repository](https://github.com/rust-lang/rustlings)

Rustlings supplies small reading-and-writing exercises and recommends using the Rust Book alongside it. For this plan, choose a small subset only after Python foundations. The Book introduces ownership and borrowing, which require new concepts rather than merely translated Python syntax.

### S7 — Google ML material
[Prerequisites](https://developers.google.com/machine-learning/crash-course/prereqs-and-prework) · [Glossary](https://developers.google.com/machine-learning/glossary)

Use the glossary selectively. The full Crash Course expects programming ability and mathematical preparation; its prerequisites include algebra, basic linear algebra, and statistics, with calculus optional for advanced topics. The original short explanations in this learning folder are an orientation, not a substitute for the relevant technical definition in context.

### S8 — Hugging Face LLM Course
[Introduction and prerequisites](https://huggingface.co/learn/llm-course/en/chapter1/1)

Free material, but not a first programming course. It explicitly requires good Python knowledge and recommends introductory deep-learning preparation. Defer its substantial coding exercises until those prerequisites are met. Free course content does not guarantee that every optional model-training workload is free to run.

### S9 — Microsoft: AI red-teaming concepts
[Planning red teaming](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/red-teaming)

Use the conceptual guidance on scope, testing, recording findings, and distinguishing failure discovery from measurement. Reading the guide does not require deploying Azure infrastructure. Our introductory exercise uses toy data or saved outputs, not a cloud lab.

## Language and software references

[Python tutorial](https://docs.python.org/3/tutorial/) — explicitly aimed at programmers new to Python, not absolute beginners.

[Python control flow and functions](https://docs.python.org/3/tutorial/controlflow.html) — reference for the introductory exercises.

[R: What is R?](https://www.r-project.org/about.html) — R's statistical and programming orientation.

[Domain-specific languages](https://learn.microsoft.com/en-us/visualstudio/modeling/about-domain-specific-languages?view=vs-2022) — scope distinction and examples such as SQL and regular expressions.

[JSON](https://developer.mozilla.org/en-US/docs/Glossary/JSON) — data-interchange format and supported value types.

[Mermaid](https://mermaid.js.org/intro/index.html) — text-based diagram definitions; optional documentation skill, not a first coding language.

## AI assistance: current capabilities, not course dependencies

[ChatGPT Voice](https://help.openai.com/en/articles/20001274-chatgpt-voice)

At review, the official page described limited Free access to Live voice, with text and supported images in the same chat. Live did not support screen sharing; supported mobile screen sharing required Advanced and an eligible subscription. Availability and limits depend on account and app. Do not assume a voice chat automatically sees your editor.

[Study mode](https://help.openai.com/en/articles/11780217-study-mode)

At review, available across plans in regular chats, but the Study selector was not available in Projects, GPTs, or Temporary Chats. You can still request the tutoring method in an ordinary project conversation; that is not the same as enabling the product's Study mode.

[Codex access](https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan)

At review, Codex was included across plans, including Free, with varying limits; Codex Cloud was not included with Free or Go. The official guide also described voice in the refreshed CLI. Check the installed client's actual controls. Neither Codex nor a paid API is necessary for the lessons in this folder.

## Reuse policy for this learning folder

Keep source courses linked and create your own notes and exercises. If external material is copied or adapted later, record its exact URL or commit, relevant file, author, license, and changes. Do not treat a public GitHub repository as permission to relicense its contents. No external course text, lesson dataset, application source, or private project documents are bundled here.
