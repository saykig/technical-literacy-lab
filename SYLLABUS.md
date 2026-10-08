# Learning sequence

## Aim and boundaries

This learning plan is for anyone starting without a computer science background. It begins with familiar examples and short exercises, then increases the challenge through independent debugging, working with data, reading repositories, evaluating AI behavior, and a small tested capstone. The aim is to understand each action well enough to explain it and eventually choose the next step independently.

The aim is practical technical literacy: read small programs accurately, write short useful scripts, inspect a repository without getting lost, and ask informed questions about AI and software. It is not the ability to understand every unfamiliar codebase without documentation.

The language sequence is **Python first; SQL after basic data handling; Rust reading later; R when your actual research or coursework calls for it**. Learn Markdown and JSON along the way. Shell commands are another small skill, not a prerequisite to months of programming.

Python and Rust are general-purpose programming languages. R is a programming language and environment oriented toward statistical computing. A domain-specific language (DSL) addresses a narrower problem: SQL queries databases, and regular expressions describe text patterns. Mermaid provides notation for diagrams. JSON is a data-interchange format, not another general-purpose programming language. See the language references in [SOURCES.md](SOURCES.md).

Begin with a short, no-code Unit 0. Then keep the original Python-first sequence in Units 1–12. Units 0–4 have starter lessons; Units 5–12 describe later work rather than promising complete lesson files. No advanced mathematics is needed for Units 0–8 as designed here. Units 9–10 introduce the mathematical ideas needed for basic ML literacy. Mathematical derivations of training algorithms are a separate, later goal.

## How to judge progress

For each unit, distinguish four abilities: recognizing a term, explaining it, using it with help, and using it independently. A useful graduation check is a new example you have not memorized. Reading someone else's explanation is not itself evidence of mastery.

Use one main resource at a time. Futurecoder is the initial practice environment; selected CS50P material supplies a structured programming sequence. Other resources enter only when their topic is needed. You are not expected to complete several introductory courses in parallel.

## Unit 0 — Foundations before Python

**Aim:** Understand how instructions, tools, files, and computers relate, assuming no computer science background. One 45–60-minute session, or two short sessions; no installation or coding.

**Concepts, in six small groups:**

1. Hardware and software; CPU; operating system; temporary memory (RAM) and persistent storage.
2. Source code and programming languages; interpreter and compiler; input, output, and errors.
3. Editor and IDE; terminal, shell, and CLI; files, directories, and paths.
4. Repository; Git versus GitHub; libraries and dependencies.
5. Local versus cloud; servers and APIs; frontend and backend.
6. General-purpose languages, DSLs, markup, and data formats, using Python, SQL, Markdown, and JSON as examples.

**Work:** Read [the foundations lesson](lessons/00-foundations.md), answer its short comprehension questions, and complete [the no-code worksheet](exercises/00_foundations.md). Trace opening and saving a note, distinguish instructions from results, locate a file in a folder tree, and sketch a request to a weather service. Explain the relationships rather than reciting definitions.

**Resource:** The original lesson is sufficient to begin. Optional: selected [Code.org How Computers Work videos](https://code.org/en-US/resources/videos) or MDN's [clients-and-servers explanation](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works). See [S0](SOURCES.md#s0--unit-0-foundations) for the limited reading scope.

**Ready to move on:** You can explain how a saved instruction becomes an action, distinguish saving from running, describe the separate roles of an editor and execution tool, and distinguish local files from an online repository. Apply this to one new familiar example without a full answer from a tutor. Any uncertain terms remain questions in [PROGRESS.md](PROGRESS.md); do not delay Python until every definition is memorized.

**Defer:** CPU internals, binary arithmetic, compiler stages, detailed networking, package managers, and deployments. Units 5, 7, and 8 return to these systems as practical tasks make them relevant.

## Unit 1 — Where code lives and what runs it

**Concepts:** source code, file, folder, path, editor, interpreter, terminal, shell, browser, local and remote execution.

**Work:** After Unit 0, follow [the original orientation lesson](lessons/00-orientation.md). Identify the code editor, the Run control, and the output area in a browser environment. Explain which text is an instruction and which is output. Inspect a folder without running anything in it. This turns Unit 0's map into your first small Python experience.

**Resource:** [Futurecoder](https://futurecoder.io/); Software Carpentry's [Unix Shell introduction](https://swcarpentry.github.io/shell-novice/) for the later local setup.

**Ready to move on:** You can explain why a Python file, a terminal command, and a printed result are different things. You do not need to install anything yet.

## Unit 2 — Variables, types, expressions, and execution order

**Concepts:** assignment, integer, floating-point number, string, Boolean, expression, function call, output, syntax error.

**Work:** Follow [Lesson 1](lessons/01-follow-a-program.md). Predict a 5–10-line program's output, then change a value and predict again. Compare `3`, `"3"`, and `True` without treating them as interchangeable.

**Resource:** [Futurecoder](https://futurecoder.io/); [CS50P “Functions, Variables”](https://cs50.harvard.edu/python/weeks/0/). Use the official Python tutorial as a reference later, not the first textbook.

**Ready to move on:** You can trace reassignment correctly and explain why a previously computed result does not automatically update when an input variable changes.

## Unit 3 — Collections and decisions

**Concepts:** list, index, dictionary, key, value, comparison, conditional, Boolean expression, loop, indentation.

**Work:** Follow [Lesson 2](lessons/02-collections-and-decisions.md). Count records matching a condition. Change the condition. Test a collection with no matches and an empty collection. Introduce a dictionary only after a list makes sense.

**Resource:** [Futurecoder](https://futurecoder.io/); [CS50P “Conditionals”](https://cs50.harvard.edu/python/weeks/1/) and [“Loops”](https://cs50.harvard.edu/python/weeks/2/).

**Ready to move on:** You can say what happens on every loop iteration, distinguish `=` from `==`, and explain why indentation changes behavior.

## Unit 4 — Functions, failures, and tests

**Concepts:** function definition, parameter, argument, return value, scope, traceback, exception, test, edge case, input contract.

**Work:** Follow [Lesson 3](lessons/03-functions-and-bugs.md). Repair a function that returns too early. Write a small check with expected inputs and outputs. Separate a crash from an incorrect result and from a bad assumption.

**Resource:** [CS50P](https://cs50.harvard.edu/python/) “Exceptions,” “Libraries,” and “Unit Tests,” with short tutor explanations connecting the pieces.

**Ready to move on:** You can explain the difference between printing and returning; repair one bug without replacing the whole program; test an empty input and an input that could expose the bug.

## Unit 5 — Files, the shell, Git, and GitHub

**Concepts:** working directory, relative path, command, option, repository, commit, diff, branch, clone, fork, pull request, issue.

**Work:** Save and run one `.py` file locally. Learn how to list files and change directory. Inspect this public GitHub repository, then learn to keep your own copy and read a diff before recording or uploading a change. Learn what a branch is; practice creating one only when you explicitly request it. First learn the concepts in the browser where possible; terminal Git comes afterward.

**Resource:** Software Carpentry “The Unix Shell” episodes 1–3 and “Version Control with Git” episodes 1–7. MIT Missing Semester's overview and Git lecture are optional reinforcement, not additional compulsory courses.

**Ready to move on:** You know which machine and folder a command affects, can inspect your changes, and can explain clone versus fork. You do not paste commands whose effects you cannot describe.

**Safety:** Keep `.env` files, passwords, API keys, and sensitive documents out of commits. Do not run downloaded installation scripts blindly.

## Unit 6 — Small datasets and SQL

**Concepts:** CSV, JSON, row, column, missing value, data type, DataFrame, schema, database, query, filter, aggregate, join.

**Work:** Use a small invented list of research records. Read it from a file, filter it, count categories, and explain missing or duplicate records. Then express one equivalent question in SQL with `SELECT` and `WHERE`; add `GROUP BY` and a simple join later. Compare the row counts before and after the join.

**Resource:** Software Carpentry “Plotting and Programming in Python,” especially libraries, reading tabular data, DataFrames, and plotting. Its “Databases and SQL” lesson supplies query practice. Use the lesson setup instructions only when ready for local packages.

**Ready to move on:** You can explain the transformation from input to output, identify a silent missing-data problem, and recognize that a successful query does not prove a substantive claim.

## Unit 7 — APIs, the web, and interfaces

**Concepts:** client, server, frontend, backend, API, HTTP, request, response, endpoint, status code, authentication, rate limit, serialization.

**Work:** Trace a toy request and a saved JSON response before calling any live service. Identify required fields and possible failures. Explain the distinction between a button the user sees and the computation behind it. Introduce a read-only public API only when there is a clear learning purpose and no required payment.

**Resource:** Selected Missing Semester material on development and packaging; official documentation for whichever API is eventually chosen. Do not begin with an agent framework.

**Ready to move on:** You can locate where data enters, changes, and leaves the system. You know that an API is an interface, not necessarily an AI model or an internet service.

## Unit 8 — Reading a real repository and understanding its environment

**Concepts:** README, source directory, tests, dependency, package manager, environment, manifest, lockfile, process, RAM versus disk, compiler, runtime, continuous integration, computational complexity.

**Work:** Read a small repository in this order: purpose; example input/output; entry point; one function; its tests; required packages. Inspect one manifest such as `pyproject.toml` without trying to understand every field. Explain why a program that works in one environment might fail in another. Introduce “one pass through n records” versus “compare every pair” as a first complexity example.

**Resource:** Missing Semester “Development Environment and Tools,” “Debugging and Profiling,” and selected “Packaging and Shipping Code.”

**Ready to move on:** You can describe one complete path through the code, identify what remains uncertain, and use documentation rather than guessing at unfamiliar syntax.

## Unit 9 — The mathematics needed for basic machine-learning literacy

**Concepts:** function as input/output rule, coordinate, vector, matrix, mean, probability, feature, label, model parameter, loss, training, inference, training/validation/test split, overfitting.

**Work:** Represent three invented observations as lists of numbers. Compute a mean and a simple distance. Compare a fixed rule with a model whose parameters are fitted to examples. Explain why evaluating on training examples can mislead.

**Resource:** Google's introductory ML material and the prerequisites page for its Machine Learning Crash Course. Its full course has real programming and mathematics prerequisites; it is not an absolute-beginner coding course.

**Ready to move on:** You can distinguish raw observations from numerical representations and distinguish fitting a model from using it. Add algebra, probability, and linear algebra in small pieces as needed; defer calculus derivations.

## Unit 10 — Embeddings, latent spaces, and language models

**Concepts:** token, embedding, latent representation, similarity, nearest neighbor, retrieval, context window, generation, retrieval-augmented generation (RAG), fine-tuning, latency.

**Work:** Begin with clearly labeled, hand-made 2D vectors to understand coordinates and distance. These are teaching examples, not learned embeddings. Later inspect a small real embedding example and explain what the model was trained to make similar. Separate “retrieve similar text” from “verify a claim.”

**Resource:** Google's ML glossary and embeddings material. Hugging Face's LLM Course is an optional later extension; it explicitly expects good Python knowledge and recommends introductory deep-learning preparation.

**Ready to move on:** You can explain an embedding as a representation rather than a fact, describe a latent space without treating its axes as necessarily human-interpretable, and distinguish retrieval from training.

## Unit 11 — Evaluation and red teaming

**Concepts:** evaluation dataset, benchmark, failure mode, threat model, adversarial test, prompt injection, false positive, false negative, reproducibility, mitigation, regression test.

**Work:** Define one narrowly scoped failure in a toy research assistant: for example, treating “passed one check” as “scientifically established.” Make a small test table with input, expected behavior, observed behavior, and limitation. Start with saved outputs or an authorized toy system; no live attack infrastructure or paid API is required. Try ordinary cases as well as difficult ones.

**Resource:** Microsoft's “Planning red teaming for large language models and their applications.” Read the conceptual guide before considering automation tools or infrastructure-heavy labs.

**Ready to move on:** You can report a reproducible failure without claiming its frequency is known, distinguish open-ended red teaming from systematic evaluation, and state which systems you are authorized to test.

## Unit 12 — Transfer across languages and a small capstone

**Concepts:** shared programming ideas versus language-specific semantics; static versus dynamic typing; Rust ownership and borrowing; `Option` and `Result`; language and library boundaries.

**Work:** Read the same small filtering task in Python, SQL, and either R or Rust. In Rust, prioritize `fn`, `let`, type annotations, `struct`, `enum`, references, `match`, `Option`, and `Result`; recognize `?` as error-propagation syntax when you encounter it. Do not try to infer all Rust behavior from Python. Use a few Rustlings exercises after the relevant book section, not the whole track.

**Resource:** The official Rust Book, initially chapters 3–4, then selected material on structs, enums, and error handling; Rustlings for small practice. R's official introduction and Software Carpentry R material become relevant when a real R task arises.

**Capstone:** A small research-record register. It reads invented records, filters them, counts categories, handles missing fields according to an explicit rule, and has a few tests. Explain every line you wrote and one limitation in the data model. Keep the first version as a script. A CLI or small website can be a later extension only when the script is understood.

**Ready to finish the foundation:** You can write a short script without AI, explain a 30–50-line example using documentation where needed, make a controlled edit, test it, and describe what you still do not understand.

## What not to do yet

Do not start several languages at once. Do not start with interview puzzles, a full computer-science degree curriculum, advanced model training, a framework-heavy agent project, or deploying your own learning platform. These are possible later routes, not entrance requirements.

## The recurring lesson format

Use this as a flexible 45–60-minute session: recall one previous idea; introduce one concept; trace a small example; predict and run it; modify it; explain the result; try a new problem without assistance. For Unit 0, sketch and explain a familiar action instead of running code. Give each unfamiliar technical term an example and a non-example. Keep a list of unresolved questions, but do not let that list expand the current lesson indefinitely. Ask ChatGPT for one hint at a time; the learner makes exercise edits and demonstrates understanding before progress is recorded.
