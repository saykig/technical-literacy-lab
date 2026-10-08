# Technical Literacy Lab
## Read code. Write small programs. Understand technical claims.

Prepared for Sara • Updated 8 October 2026

This is a personal learning repository for building technical intuition from zero. It contains a foundational Unit 0 followed by the original Units 1–12, five starter lessons (foundations, browser orientation, and three Python lessons), small exercises, a glossary, source links, and tutor instructions. Units 5–12 remain a roadmap; their full lessons have not been authored yet.

Nothing in this folder requires a paid API, a GPU, a subscription, or a deployed website. The introductory Python exercises use built-in Python features. External learning sites require internet access; AI assistance is optional and subject to the provider's limits.

## Start here

Open [Unit 0: what happens when a computer does something?](lessons/00-foundations.md). It connects computers, code, development tools, repositories, connected systems, and kinds of technical text. Complete the [no-code worksheet](exercises/00_foundations.md); no installation or coding is needed. Allow one 45–60-minute session or two shorter sessions.

Then follow the original sequence:

| Unit | Lesson | Practice |
|---|---|---|
| 0 | [Foundations](lessons/00-foundations.md) | [No-code worksheet](exercises/00_foundations.md) |
| 1 | [Browser orientation](lessons/00-orientation.md) | Identify instructions, Run, and output |
| 2 | [Follow a program](lessons/01-follow-a-program.md) | Predict and change an assignment |
| 3 | [Collections and decisions](lessons/02-collections-and-decisions.md) | Trace and modify a loop |
| 4 | [Functions and bugs](lessons/03-functions-and-bugs.md) | Repair one intentional bug |

Original lesson filenames are preserved, so a filename's number is not always its syllabus unit. Python remains the first programming language; SQL, Rust reading, and task-specific R come later.

Use [Futurecoder](https://futurecoder.io/) for the first browser-based practice. Its homepage has a “Just code” option for experimenting with your own snippets. [Python Tutor](https://pythontutor.com/) is an alternative for stepping through short programs visually. Use only toy or public code in external tools.

Do not install Rust, Docker, an AI framework, or a web-development toolchain to begin. Do not try to complete every linked course. The [syllabus](SYLLABUS.md) specifies which parts to use and when.

## How the folder works

- [SYLLABUS.md](SYLLABUS.md): the order, exercises, and readiness checks.
- [GLOSSARY.md](GLOSSARY.md): vocabulary grouped by topic; consult it rather than memorizing it all.
- [PROGRESS.md](PROGRESS.md): evidence of what you can do independently.
- [SOURCES.md](SOURCES.md): reviewed courses, repositories, and official references.
- [AGENTS.md](AGENTS.md): instructions for a coding assistant acting as a tutor.
- [REVIEW.md](REVIEW.md): curriculum review and setup verification, separate from your learning progress.

The `exercises` folder contains practice code. The `solutions` folder is for checking after an attempt. The debugging exercise deliberately contains a bug; its checker is supposed to fail until that bug is fixed.

See the [exercise guide](exercises/README.md) for how to run each file and interpret the debugging checker.

## Use this with ChatGPT

Start a learning chat with this request, adding the current lesson and relevant progress entry:

> Act as my tutor for technical-literacy-lab. Teach one concept at a time. Ask me to explain or predict before revealing an answer. Give one hint at a time and wait for my response. Do not complete exercises or edit my practice files unless I explicitly ask. Help me record what I demonstrated and which hints I used.

If ChatGPT can access the repository, ask it to read README.md, AGENTS.md, and PROGRESS.md first. Otherwise paste the tutor guidance and the relevant lesson or snippet. A repository on GitHub does not automatically become visible to a chat. Keep the solution folder closed until you have made your own attempt.

Record progress yourself or ask for a proposed entry after the session. Running code during repository setup does not establish your understanding; all learning skills begin unassessed.

## Suggested session

In Unit 0, explain one relationship, sketch it, and apply it to a familiar action. In the Python lessons, predict what a short program will do, run it, change one thing, and explain the result in plain English. End with one unfamiliar example without AI help. Record the example and any hints in PROGRESS.md.

A planning starting point is three sessions of 45–60 minutes per week. This is a suggested study rhythm, not a completion guarantee. Move by demonstrated understanding rather than calendar weeks.

## Local use, later

After installing a currently supported Python 3 version and learning what a terminal and working directory are, open a terminal in this folder. The supplied checker requires Python 3.9 or newer. A common macOS/Linux command is:

```sh
python3 exercises/01_follow_a_program.py
```

On Windows, when the Python launcher is installed, use:

```powershell
py exercises/01_follow_a_program.py
```

The exact launcher depends on the installation. Browser practice does not require either command.

## This private GitHub repository

The learning repository is [saykig/technical-literacy-lab](https://github.com/saykig/technical-literacy-lab) on GitHub, with private visibility. You can read its lessons there before learning Git commands. The repository stores files and version history; it does not provide a hosted lesson app or execute exercises for you. Unit 5 will teach you how to inspect changes and keep a local copy in sync.

The ignored `personal/` folder can hold local notes you do not want to commit. Keep credentials out of commits even in a private repository. Learn branches conceptually when relevant; create one only when you choose to request that practice.

## Scope and attribution

Examples and exercises here were written for this learning plan. They use invented data, not real research findings or an implementation of Vela. External courses are linked rather than copied. Before redistributing any adapted external material, check its applicable license and attribution requirements. This folder does not assign a new license to third-party work.
