# Technical Literacy Lab
## Read code. Write small programs. Understand technical claims.

Prepared for Sara • 7 October 2026 • Draft 1

This is a personal learning folder, not a software engineering degree or a custom teaching app. It contains a 12-unit roadmap, four starter lessons (orientation plus three coding lessons), small Python exercises, a glossary, source links, and tutor instructions. The later units are a syllabus, not fully authored lessons.

Nothing in this folder requires a paid API, a GPU, a subscription, or a deployed website. The introductory Python exercises use built-in Python features. External learning sites require internet access; AI assistance is optional and subject to the provider's limits.

## Start here

Open [Lesson 0: where code lives](lessons/00-orientation.md). Then open [Lesson 1: following a program](lessons/01-follow-a-program.md).

Use [Futurecoder](https://futurecoder.io/) for the first browser-based practice. Its homepage has a “Just code” option for experimenting with your own snippets. [Python Tutor](https://pythontutor.com/) is an alternative for stepping through short programs visually. Use only toy or public code in external tools.

Do not install Rust, Docker, an AI framework, or a web-development toolchain to begin. Do not try to complete every linked course. The [syllabus](SYLLABUS.md) specifies which parts to use and when.

## How the folder works

- [SYLLABUS.md](SYLLABUS.md): the order, exercises, and readiness checks.
- [GLOSSARY.md](GLOSSARY.md): vocabulary grouped by topic; consult it rather than memorizing it all.
- [PROGRESS.md](PROGRESS.md): evidence of what you can do independently.
- [SOURCES.md](SOURCES.md): reviewed courses, repositories, and official references.
- [AGENTS.md](AGENTS.md): instructions for a coding assistant acting as a tutor.

The `exercises` folder contains practice code. The `solutions` folder is for checking after an attempt. The debugging exercise deliberately contains a bug; its checker is supposed to fail until that bug is fixed.

## Suggested session

Start with an explanation of one concept, predict what a short program will do, run it, change one thing, and explain the result in plain English. End with one unfamiliar example without AI help. Record the example and any hints in PROGRESS.md.

A planning starting point is three sessions of 45–60 minutes per week. This is a suggested study rhythm, not a completion guarantee. Move by demonstrated understanding rather than calendar weeks.

## Local use, later

After installing Python 3 and learning what a terminal and working directory are, open a terminal in this folder. A common macOS/Linux command is:

```sh
python3 exercises/01_follow_a_program.py
```

On Windows, when the Python launcher is installed, use:

```powershell
py exercises/01_follow_a_program.py
```

The exact launcher depends on the installation. Browser practice does not require either command.

## GitHub, later

This folder has not been published or connected to a remote repository. It can become a new repository named `technical-literacy-lab` when you reach Unit 5. Prefer a private repository initially. Keep personal notes and credentials out of any public version. Fork an upstream project only when intentionally modifying that project; use this new folder to organize your own learning instead.

## Scope and attribution

Examples and exercises here were written for this learning plan. They use invented data, not real research findings or an implementation of Vela. External courses are linked rather than copied. Before redistributing any adapted external material, check its applicable license and attribution requirements. This folder does not assign a new license to third-party work.
