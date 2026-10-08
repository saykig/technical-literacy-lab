# Working glossary

Consult the relevant section during a lesson. These are short orientation definitions, not exhaustive specifications. Write your own example beside a term once you have used it. References are collected in [SOURCES.md](SOURCES.md).

## Unit 0 — A map of the basics

Use this section alongside [the foundation lesson](lessons/00-foundations.md). Learn the relationships through its examples; consult later sections only when their units need them.

### Computer and execution

**Hardware / software:** Hardware is physical equipment, such as a processor or drive. Software is programs that direct its work. A laptop is hardware; its word processor is software.

**CPU:** Central processing unit: hardware that executes machine instructions. Language tools make human-written code executable; the CPU does not understand ordinary English requests.

**Operating system (OS):** Software managing resources such as memory, files, and devices. macOS, Windows, and Linux let applications use the computer's hardware.

**Memory (RAM) / storage:** RAM is temporary working space for running programs. Storage, such as an SSD or hard drive, keeps saved files when power is off. Changing a working copy is different from saving it.

**Source code / program:** Source code is text written in a programming language. A program organizes instructions to perform a task. Source code can be saved without being executed.

**Interpreter / compiler:** An interpreter executes code; a compiler translates it into another form. Python has an interpreter; Rust normally compiles to a runnable program. Systems can use both translation and execution steps.

**Input / output:** Information supplied to a program and information it produces. Calculator numbers are input; its displayed answer is output, not source code.

**Error / bug:** An error may stop code from being understood or an operation from finishing. A bug causes behavior that differs from what was intended; it can produce wrong output without stopping execution. Later lessons teach how to distinguish these cases.

### Tools and project files

**Editor / IDE:** An editor changes text. An IDE (integrated development environment) combines an editor with other tools, such as running and debugging. A Run control and a text-editing area have different jobs even in one app.

**Terminal / shell / CLI:** A terminal provides a text interface; a shell reads commands and starts programs. A CLI (command-line interface) is a way of using a tool by typing commands. The terminal window is not the Python interpreter.

**File / directory / path:** A file stores information; a directory is a folder organizing files or other directories; a path identifies a location. `lessons/00-foundations.md` locates a file from this repository's root folder.

**Repository / Git / GitHub:** A repository holds project files and recorded history. Git records versions and changes; GitHub hosts repositories online. Git works locally without GitHub. Saving, recording, and uploading are separate actions.

**Library / dependency:** A library provides reusable code. A dependency is a component a project needs; a required library is one example. Python's standard library comes with Python, while other libraries may need installing. The starter exercises need no additional libraries.

### Connected systems

**Local / cloud:** Local means on your own computer; cloud means using other computers over a network. A browser can do local work while also asking remote software for information.

**Server:** Software handling requests, or the computer hosting it. A server can run locally or remotely; the role does not require a special kind of physical machine.

**API:** Application programming interface: agreed ways for software to interact, such as requesting a forecast. An API can be local or network-accessible and need not involve AI.

**Frontend / backend:** The user-facing part of an app and its supporting logic or data handling. A search box belongs to the frontend; finding records may happen in a backend on a server. The exact boundary depends on the app.

### Kinds of technical text

**Programming language:** Rules for expressing computations. Python and Rust serve many purposes; R emphasizes statistical computing. Learn Python first, then compare other languages through their own rules.

**DSL:** Domain-specific language: a language focused on a narrower task. SQL expresses database work. A DSL can perform computations; its scope distinguishes it from a general-purpose language.

**Markup:** Text notation describing document structure, such as Markdown headings or HTML paragraphs. It is useful alongside programming languages without being another general-purpose programming language.

**Data format:** Rules for representing information. JSON holds structured values and CSV holds tabular text data. A program reads these formats; the data alone does not specify the program's behavior or prove its claims.

References: [S0 foundation resources](SOURCES.md#s0--unit-0-foundations), Python documentation, and the language/software references in SOURCES.md. Units 5, 7, and 8 deepen this map when you use the tools.

## Units 1–4: Python code and execution

**Variable:** A name associated with a value or object. In Python, assignment can bind the name to a different object later.

**Assignment:** Setting a name to refer to a value, such as `count = 3`. This is not a test of whether two values are equal.

**Type:** A category that determines which operations a value supports. Text `"3"` and number `3` have different types.

**String:** Text represented as a value, such as `"pending"`. The quotation marks distinguish literal text from a variable name.

**Boolean:** A true-or-false value. Python spells these values `True` and `False`.

**Expression:** Code evaluated to produce a value, such as `count + 1` or `status == "pending"`.

**Function:** A reusable operation that can take inputs and return an output. It may also have effects, such as printing or writing a file.

**Parameter / argument:** A parameter is the input name in a function definition; an argument is the actual value supplied when calling it.

**Return value:** The result handed back to the caller. Printing a value displays it; it does not by itself return that value.

**Control flow:** The order in which instructions execute, including decisions, repetitions, function calls, and early returns.

**Conditional:** A choice about whether to execute some code, usually based on a Boolean expression.

**Loop:** Repeated execution of a block. A Python `for` loop can visit each item in a collection.

**List:** An ordered collection. Python lists can be modified. The first item has index 0, not 1.

**Dictionary:** A collection of key–value associations, such as `{"status": "pending"}`. Looking up a missing key directly can raise an error.

**Scope:** The region in which a name is available. A variable inside a function is not automatically available everywhere else.

**Mutability:** Whether an object can change after creation. Changing a list is different from rebinding a variable to a new list.

**Bug:** A defect causing behavior that does not match the intended specification. A program may contain a bug even when it runs without crashing.

**Exception / traceback:** An exception signals a problem during execution; a traceback reports the call path leading to it. Some exceptions can be handled deliberately.

**Test:** A check of a specified behavior. Passing selected tests does not establish correctness for every input or the validity of the underlying research.

**Edge case:** An input at a boundary or unusual condition, such as an empty list, a missing field, or a value exactly at a threshold.

Reference: Python's tutorial and control-flow documentation, CS50P, and Software Carpentry (S2–S3).

## Units 5 and 8: tools and repositories in practice

**Working directory / relative path:** The working directory is the folder a running program uses as its current location. A relative path is interpreted from a starting location, often that directory. For example, `exercises/check_03.py` finds the checker when the working directory is the repository root.

**Process:** A running instance of a program, with its own execution state and resources.

**Package / package manager:** A distributable unit of software, and a tool for installing or managing such units. The precise meaning of “package” varies by ecosystem.

**Environment:** The software and settings available when a program runs: interpreter, packages, operating-system details, and configuration.

**Commit / diff / branch:** A commit records a version in history; a diff shows changes; a branch names a line of development.

**Clone / fork:** A clone is a local copy of a repository with Git history. On GitHub, a fork is a separate hosted repository related to an upstream repository. Neither is a required first step for learning from a course website.

**Pull request:** A proposal to review and merge a set of changes. It is not the same as downloading or running code.

**Continuous integration (CI):** Automated checks triggered by changes to a project. What a passing result means depends on which checks actually ran.

**Computational complexity:** How resource requirements change as an input grows. It is not simply how many lines the program contains.

Reference: Software Carpentry and Missing Semester (S3–S4).

## Units 6–7: data and connected systems in practice

**CSV / JSON:** CSV represents tabular text data; JSON represents structured values such as objects and arrays. Neither format establishes that its contents are accurate.

**Schema:** A specification of expected structure, fields, and types. A valid structure can still contain incorrect facts.

**DataFrame:** A table-like data structure used by data-analysis tools. Column types and missing values affect operations.

**SQL / query / join:** SQL is a language for working with relational databases; a query requests an operation or result; a join combines rows according to a relationship. Joins can duplicate rows when several matches exist.

**Client / server:** Roles in an interaction: a client requests something; a server handles requests. One machine or program can participate in both roles.

**Endpoint / HTTP / status code:** An endpoint is an addressable interface; HTTP is a web communication protocol; a status code reports a category of response. A successful response is not a guarantee that its content answers your question correctly.

**Authentication / authorization:** Establishing who or what is making a request versus deciding what that identity may do.

**Rate limit / latency:** A constraint on how much activity is allowed over an interval versus the delay associated with an operation. These are different from the term “latent.”

**Serialization:** Converting data into a representation suitable for storage or exchange; deserialization reconstructs usable data from it.

Reference: Software Carpentry, Missing Semester, and MDN's JSON reference. Treat these as orientation terms and consult the actual API documentation when using a service.

## Later: mathematics and AI

**Vector / matrix:** For these lessons, an ordered collection of numbers and a rectangular arrangement of numbers. These computational descriptions are an introduction to the more general mathematical objects.

**Feature / parameter:** A feature represents an input property; a parameter is part of a model's fitted configuration. A column in a dataset and a learned model weight are not the same thing.

**Training / inference:** Adjusting a model using data versus using the model to produce an output. A chat message does not necessarily retrain a model's parameters.

**Loss:** A numerical measure used to evaluate a model's predictions during optimization. A lower value matters only relative to the chosen loss and data.

**Overfitting:** Adapting too closely to the training examples in ways that do not generalize to new examples.

**Embedding:** A numerical representation of an item, such as text, constructed so useful structure can be represented. What counts as useful depends on the method and objective.

**Latent space:** A space of underlying, unobserved representations. In many ML settings these are learned numerical coordinates. It is not necessarily two-dimensional, and individual coordinates need not have simple meanings. Usage varies across models; not every use of “latent” is identical to a text-embedding API.

**Token:** A unit into which input is divided for a model, often a word fragment, punctuation, or another symbol. One token is not necessarily one word.

**Retrieval / RAG:** Finding stored material; retrieval-augmented generation uses retrieved material as context for generation. It does not automatically verify that material or retrain the model.

**Fine-tuning:** Further training an existing model on additional data or objectives. It changes model parameters; merely supplying documents as context generally does not.

**Evaluation / benchmark:** Measuring behavior against specified criteria; a benchmark is a standardized evaluation task or dataset. Neither implies coverage of every real-world situation.

**Red teaming:** Deliberately probing a system for failures or harmful behavior within an authorized scope. It can discover unexpected problems; selected findings alone do not measure how common the problems are.

**Prompt injection:** Untrusted content attempting to redirect an AI system's behavior, for example when retrieved text contains instructions masquerading as something the system should obey.

**False positive / false negative:** A test reports a condition that is absent versus missing a condition that is present. Define the condition clearly before counting errors.

Reference: Google's ML glossary and prerequisites (S7), Hugging Face (S8), and Microsoft's red-teaming guidance (S9). These entries intentionally avoid a promise that similarity, model confidence, or a passing test establishes truth.

## Language transfer

**Static / dynamic typing:** Type checks can happen before execution or during execution, with details varying by language and tools. Python type annotations alone do not enforce runtime types.

**Ownership / borrowing in Rust:** Rules governing which binding owns a value and how references can access it. These rules help manage resources and memory safety; they are not just alternate variable names.

**Option / Result in Rust:** Types making “a value or no value” and “success or error” explicit. Their use is a good entry point for reading Rust control flow.

Reference: the Rust Book (S6) and the language references in SOURCES.md.
