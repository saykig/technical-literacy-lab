# Unit 0 — What happens when a computer does something?

Begin here. No coding, installation, or computer science background is needed. Allow about 45–60 minutes including the [no-code worksheet](../exercises/00_foundations.md), or split the work into two short sessions. Read each section, answer its question in your own words, and ask for a hint when needed.

The aim is to connect the tools you will use. You do not need to memorize every term before beginning Python.

## 1. Instructions need a machine

**Hardware** is the physical equipment: a keyboard, screen, processor, and storage drive. **Software** is the programs that tell this equipment what to do. The **CPU** (central processing unit) executes small machine instructions, such as calculations and comparisons. A word processor and a browser are software; both ultimately run on hardware.

The **operating system** (OS), such as macOS, Windows, or Linux, is software that manages the machine's resources. It helps programs use the processor, memory, files, and devices. Clicking Save involves the application, the OS, and the storage device working together.

**Memory**, usually called RAM, is the temporary workspace holding information while programs run. **Storage**, such as an SSD, keeps saved files when the power is off. Think of a desk and a filing cabinet: working on a page at the desk and putting it in the cabinet are different actions. Some apps save automatically, but information in RAM alone is not a saved file.

```text
Saved file on storage --open--> working copy in RAM
Working copy in RAM  --save--> saved file on storage

The CPU executes instructions that work with this information.
The operating system manages access to these resources.
```

**Check:** You change a note but it has not been saved. Why might the change disappear after a power failure, while yesterday's saved version remains?

## 2. Code becomes actions

**Source code** is the text people write in a **programming language**, with rules a computer's language tools can process. A **program** is instructions organized to do a task. The computer does not infer what you meant: an instruction must follow the language's rules.

An **interpreter** executes code; a **compiler** translates code into another form before that form is executed. Python provides an interpreter; Rust normally uses a compiler to produce a runnable program. Systems can combine translation and execution steps. You only need the broad roles now.

```text
You write source code
        |
        v
Language tools translate and/or execute it
        |
        v
Actions on hardware, with OS support --> output
```

**Input** is information supplied to a program; **output** is information it produces. A calculator receives two numbers and an operation, then displays a result. Code describes the operation; the displayed result is output.

An **error** can prevent an instruction from being understood or an operation from finishing. A program can also run and produce the wrong result. Counting only the first page of a ten-page document may finish successfully while answering the wrong question. An error message and an incorrect answer need different investigation.

**Check:** If you edit a saved program but do not run it again, should its earlier output change? Explain the missing action.

## 3. Tools have different jobs

An **editor** changes text, including source code. An **IDE** (integrated development environment) combines an editor with tools for running code and investigating problems. A Run button asks an execution tool to act on code; the editor itself need not understand how to execute it.

A **terminal** provides a text interface. A **shell** is the program that reads commands there and starts the requested programs. A **CLI** (command-line interface) is a way of using a tool by typing commands. Git and Python can be started through a shell; they are different programs. An IDE may include a terminal panel, so several roles can appear in one window.

```text
Editor --save--> source file
Terminal contains your conversation with the shell
Shell --starts--> Python --runs--> source file --produces--> output
```

A **file** holds saved information. A **directory** is a folder containing files or other folders. A **path** describes a location, such as `lessons/00-foundations.md` inside this repository. The starting folder matters when using a path that does not begin at the computer's top-level location. You will practice that in Unit 5.

**Check:** A terminal appears inside an IDE. Does this make the terminal, shell, editor, and Python interpreter the same tool? Describe two different jobs.

## 4. Projects have structure and history

A **repository** holds a project's files and, when tracked with Git, its recorded history. In this repository, `lessons/` contains explanations and `exercises/` contains practice. The README helps you find your starting point.

**Git** records changes to files. **GitHub** hosts repositories online so they can be stored, viewed, and shared with permitted people. Git can work on your computer without GitHub. Saving a file changes its current contents; recording a version in Git and sending it to GitHub are separate actions. Viewing a Python file on GitHub does not execute it.

A **library** provides reusable code, such as tools for reading a spreadsheet. A **dependency** is something a project needs in order to work. If your program needs that library, the library is a dependency. Python includes a standard library; additional libraries may need installing later. Our starter exercises need no extra libraries.

**Check:** A project folder is on your laptop. What would Git add, and what would GitHub add? Why might someone else's program need a library yours does not?

## 5. Work can happen on different computers

**Local** means on your own computer. **Cloud** means using resources on other computers reached over a network. Cloud files still live on physical machines. A browser runs locally, but a site may do some work in the browser and some on a remote machine; the visible window does not tell you where every computation happens.

A **server** is a program, and often the computer hosting it, that handles requests. An **API** (application programming interface) defines how software asks other software to do something or provide information. A weather app can request a forecast through an API and receive data to display. APIs also exist between programs on the same computer.

For a web app, the **frontend** is the part you interact with, such as a search box. The **backend** handles supporting work, such as looking up matching records, often on a server.

```text
Your browser: frontend           Remote server: backend
       | -- request via API -->        |
       | <-- response data ----        |
       v
Display the result
```

This is one common arrangement. A server can also run locally. Opening this learning repository in GitHub is different from running its exercises; no server or web app needs building for these lessons.

**Check:** You open a weather site on your laptop. Does that prove the forecast was calculated on your laptop? What would you need to find out?

## 6. Different kinds of text do different jobs

Python comes first because it is a general-purpose programming language: it can describe many kinds of computation. Later languages build on that understanding, while adding their own rules.

| Kind | Example | Main job |
|---|---|---|
| General-purpose programming language | Python, Rust | Describe computations and behavior across many tasks |
| Programming language with a specialist focus | R | Support tasks such as statistical analysis; it can do more than statistics |
| Domain-specific language (DSL) | SQL | Express work in a narrower domain, such as database queries |
| Markup | Markdown, HTML | Describe document structure, such as headings and links |
| Data format | JSON, CSV | Represent information for storage or exchange |

These categories describe roles rather than a ranking. SQL can express computations, though it focuses on databases. Markdown headings organize this lesson. A JSON weather record contains information for a program to read; it does not itself instruct the program to fetch a forecast. A file extension is a clue to its intended format, not proof of what its contents mean.

**Check:** Why could one project contain Python, Markdown, and JSON without requiring you to learn three general-purpose programming languages?

## Try the relationships yourself

Complete the [no-code worksheet](../exercises/00_foundations.md) without asking a tutor to fill it in. Use the [Unit 0 glossary](../GLOSSARY.md#unit-0--a-map-of-the-basics) for unfamiliar terms. Record what you can explain and what still needs a hint in [PROGRESS.md](../PROGRESS.md).

You are ready for Unit 1 when you can describe how a saved instruction becomes an action, separate a tool from its job, and say where work or files might be located. Definitions need not be word-perfect. Defer detailed CPU design, binary arithmetic, networking protocols, package installation, and language theory until there is a reason to learn them.

Optional reinforcement: choose the short hardware/software or CPU/memory videos in [Code.org's How Computers Work series](https://code.org/en-US/resources/videos). For the web example, read only the clients-and-servers introduction in [MDN's How the web works](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works). These are supporting explanations, not extra courses to complete.

Next: [Unit 1 — browser orientation](00-orientation.md), then the existing Python lessons.
