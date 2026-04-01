# AGENTSETUP.md — Agent-executed Project Repository Configuration

> **This file is intended to be processed by an AI agent** (e.g., Claude Code, Codex, or another agentic framework). It defines every configurable placeholder found in the project's Markdown template files and provides structured instructions for collecting values from the user and performing substitutions. It is invoked by the user with the 'execute AGENTSETUP.md' command in the base directory of OpenMVG.

---

## Instructions for the AI Agent

1. **Read this file in full** before prompting the user.
2. **Prompt the user** for every variable listed in the [Variable Registry](#variable-registry) below. Present them in the order shown, grouped by section. For variables marked `(optional)`, let the user know when they can skip with an empty response. Prompt the user for input after every section, not all at once.
3. **Perform substitutions** across every Markdown file listed in the [Files to Process](#files-to-process) section. Follow the substitution rules in [How to Substitute](#how-to-substitute).
4. **Verify** that no unresolved placeholders remain. See [Verification](#verification).
5. **Output** the updated files — either overwrite in place or produce them for download, depending on the environment.

---

## Files to Process

The following files in the project root directory must be processed, by default it is named `project-repo/`. Process them in this order:

| # | File | Notes |
|---|------|-------|
| 1 | `README.md` | Main project landing page |
| 2 | `CONTRIBUTING.md` | Contribution guidelines |
| 3 | `GOVERNANCE.md` | Governance model |
| 4 | `MAINTAINERS.md` | Maintainer roster |
| 5 | `STEERING_COMMITTEE.md` | TSC roster and processes |
| 6 | `SECURITY.md` | Security policy |
| 7 | `AGENTS.md` | AI agent contribution guidelines |
| 8 | `CODE_OF_CONDUCT.md` | No user-configurable placeholders (standard LF Projects policy) |
| 9 | `ANTITRUST.md` | No user-configurable placeholders (standard LF Projects policy) |
| 10 | `TRADEMARKS.md` | No user-configurable placeholders (standard LF Projects policy) |
| 11 | `LICENSE` | User should supply or select a license file; not templated |
| 12 | `DCO` | Standard Developer Certificate of Origin; not templated |

---

## How to Substitute

### Global string replacements

For `project_name` and `project_repo`, perform a **global find-and-replace** across all files:

- Replace every literal occurrence of `project_name` (as a standalone token, not inside other words) with the user-supplied project name.
- Replace every literal occurrence of `project_repo` (used as the full URL of the project repository, e.g., `https://github.com/org/repo`) with the user-supplied repository URL.

### Bracketed placeholders

All other placeholders appear as text enclosed in square brackets, e.g., `[description]`, `[number]`, `[calendar link]`. Replace each **entire bracket expression** (including the brackets) with the user-supplied value.

### Table-row placeholders

Some files contain template table rows with bracketed cells (e.g., maintainer or TSC member entries). For each entry the user provides, duplicate the template row and fill in the values. Remove any unfilled template rows.

### Comment blocks

Some placeholders appear inside HTML comments `<!-- ... -->` as instructional text. After substitution, **remove the comment delimiters** so the text becomes visible, or replace the entire comment block with the user-supplied content.

---

## Variable Registry

Each variable below lists:
- **ID**: A short unique identifier
- **Prompt**: What to ask the user
- **Default/Example**: Suggested default or example value
- **Files affected**: Which files contain this placeholder
- **Placeholder text**: The exact text pattern to find and replace

---

### Section 1 — Global Identifiers

These two values are substituted everywhere across all files.

| ID | Prompt | Example | Files |
|----|--------|---------|-------|
| `PROJECT_NAME` | What is the name of your project? | `MyProject` | All `.md` files — replace every occurrence of the literal string `project_name` |
| `PROJECT_REPO` | What is the full URL of the project repository? (e.g., `https://github.com/org/repo`) | `https://github.com/example/myproject` | All `.md` files — replace every occurrence of the literal string `project_repo` |

---

### Section 2 — Project Overview (README.md, AGENTS.md)

| ID | Prompt | Example | Files → Placeholder |
|----|--------|---------|---------------------|
| `PROJECT_DESCRIPTION` | Provide a short description of what this project does, its purpose, and the problem it solves. | `A high-performance API gateway for microservices` | **README.md** → `[Provide a clear explanation of what the project does, its purpose, and the problem it solves.]` and the HTML comment `<!-- Brief description of what this project does ... -->` ; **AGENTS.md** → `[description of what the project does, its goals, and its importance]` and `[Provide a brief description of the project's purpose that helps AI agents understand the context for their contributions.]` |
| `CURRENT_VERSION` | What is the current release version? | `1.0.0` | **README.md** → `[version number]` |
| `RELEASE_DATE` | What is the release date for the current version? | `2026-03-22` | **README.md** → `[date]` (in the Latest Release section) |
| `LICENSE_NAME` | What is the name of the project license? (e.g., Apache-2.0, MIT) | `Apache-2.0` | **README.md** → `[LICENSE NAME]` and the badge text `[LICENSE]` |

---

### Section 3 — Prerequisites, Installation & Usage (README.md)

| ID | Prompt | Example | Files → Placeholder |
|----|--------|---------|---------------------|
| `PREREQUISITES` | List any prerequisites, dependencies, or system requirements. | `Python 3.10+, pip, Docker (optional)` | **README.md** → `[List any prerequisites, dependencies, or system requirements needed to use this project.]` |
| `INSTALLATION_INSTRUCTIONS` | Provide step-by-step installation instructions (or note if a separate INSTALL.md exists). | `pip install myproject` | **README.md** → `[Provide step-by-step installation instructions. If instructions exceed 30 words, consider creating a separate INSTALL.md file.]` and the `# Additional setup steps` comment |
| `USAGE_INSTRUCTIONS` | Explain basic usage with example commands or code snippets. | `myproject serve --port 8080` | **README.md** → `[Explain how to use the code in this repository. Include basic examples.]` and `# Example usage commands or code snippets` |

---

### Section 4 — Communication Channels (README.md, CONTRIBUTING.md)

| ID | Prompt | Example | Files → Placeholder |
|----|--------|---------|---------------------|
| `MAILING_LIST_LINK` | What is the URL for the project mailing list? | `https://lists.example.org/myproject` | **README.md** → `[mailing list link]` ; **CONTRIBUTING.md** → `[mailing list link]` (Getting Help section) |
| `CHAT_CHANNEL_LINK` | What is the URL for the project's chat/Slack/Discord? | `https://discord.gg/myproject` | **README.md** → `[communication channel link]` ; **CONTRIBUTING.md** → `[chat platform and link]` |
| `FORUM_LINK` | What is the URL for the discussion forum? (optional) | `https://github.com/org/repo/discussions` | **README.md** → `[forum link]` |
| `CONDUCT_EMAIL` | What email address should Code of Conduct violations be reported to? | `conduct@myproject.org` | **CONTRIBUTING.md** → `[conduct email address]` |

---

### Section 5 — TSC Meetings (README.md, GOVERNANCE.md, STEERING_COMMITTEE.md)

These values are shared across multiple files. Substitute into every location listed.

| ID | Prompt | Example | Files → Placeholder |
|----|--------|---------|---------------------|
| `TSC_MEETING_FREQUENCY` | How often does the TSC meet? | `Bi-weekly on Wednesdays at 10:00 AM PT` | **README.md** → `[frequency, e.g., "Every other Tuesday at 10:00 AM PT"]` ; **GOVERNANCE.md** → `[frequency, e.g., "Bi-weekly on Wednesdays at 10:00 AM PT"]` ; **STEERING_COMMITTEE.md** → `[frequency, e.g., "Bi-weekly on Wednesdays at 10:00 AM PT"]` |
| `TSC_CALENDAR_LINK` | What is the URL for the TSC meeting calendar? | `https://calendar.google.com/calendar/...` | **README.md** → `[calendar link]` (TSC section) ; **GOVERNANCE.md** → `[calendar link]` ; **STEERING_COMMITTEE.md** → `[calendar link]` |
| `TSC_VIDEO_LINK` | What is the video conference URL for TSC meetings? | `https://zoom.us/j/123456789` | **README.md** → `[meeting link]` (TSC section) ; **GOVERNANCE.md** → `[meeting link]` ; **STEERING_COMMITTEE.md** → `[meeting link]` |
| `TSC_MEETING_NOTES_LINK` | Where are TSC meeting notes published? | `https://wiki.example.org/myproject/tsc-notes` | **README.md** → `[link to meeting notes]` ; **GOVERNANCE.md** → `[link to meeting notes repository or document]` ; **STEERING_COMMITTEE.md** → `[link to meeting notes]` |
| `TSC_AGENDA_LINK` | Where are TSC meeting agendas published? (if different from notes) | `https://wiki.example.org/myproject/tsc-agendas` | **STEERING_COMMITTEE.md** → `[link to agenda document or repository]` |

---

### Section 6 — Office Hours (README.md)

| ID | Prompt | Example | Files → Placeholder |
|----|--------|---------|---------------------|
| `OFFICE_HOURS_FREQUENCY` | How often are office hours held? | `Every Thursday at 2:00 PM PT` | **README.md** → `[frequency, e.g., "Every Thursday at 2:00 PM PT"]` |
| `OFFICE_HOURS_CALENDAR_LINK` | What is the URL for the office hours calendar? | `https://calendar.google.com/calendar/...` | **README.md** → `[calendar link]` (Office Hours section) |
| `OFFICE_HOURS_VIDEO_LINK` | What is the video conference URL for office hours? | `https://zoom.us/j/987654321` | **README.md** → `[meeting link]` (Office Hours section) |
| `OFFICE_HOURS_NOTES_LINK` | Where are office hours notes or recordings published? (optional) | `https://youtube.com/@myproject` | **README.md** → `[link to notes or recordings, if applicable]` |

---

### Section 7 — Governance Policies (GOVERNANCE.md, STEERING_COMMITTEE.md)

| ID | Prompt | Example | Files → Placeholder |
|----|--------|---------|---------------------|
| `CHARTER_LINK` | What is the URL of the project's Technical Charter? | `https://example.org/charter.pdf` | **GOVERNANCE.md** → `[Link to Technical Charter - do NOT copy the Technical Charter into this repository]` (the value assigned to `[charter-link]`) ; **STEERING_COMMITTEE.md** → `[Link to Technical Charter]` (the value assigned to `[charter-link]`) |
| `VOTING_PERIOD_DAYS` | How many business days is the minimum voting period? | `5` | **GOVERNANCE.md** → `[number]` in "minimum of [number] business days" (voting process) |
| `LAZY_CONSENSUS_DAYS` | How many business days is the lazy consensus waiting period? | `3` | **GOVERNANCE.md** → `[number]` in "waiting period of [number] business days" |
| `AGENDA_LEAD_HOURS` | How many hours before a meeting must the agenda be published? | `24` | **GOVERNANCE.md** → `[number]` in "at least [number] hours before each meeting" ; **STEERING_COMMITTEE.md** → `[number]` in "at least [number] hours before each meeting" |
| `NOTES_PUBLISH_DAYS` | Within how many business days must meeting notes be published? | `3` | **GOVERNANCE.md** → `[number]` in "within [number] business days after each meeting" ; **STEERING_COMMITTEE.md** → `[number]` in "within [number] business days" |
| `AMENDMENT_DISCUSSION_DAYS` | How many business days must governance amendments be discussed before voting? | `7` | **GOVERNANCE.md** → `[number]` in "minimum of [number] business days before voting" (Amendments section) |
| `RELEASE_PROCESS_DESCRIPTION` | Describe the release process (or reference a RELEASE.md file). (optional) | `See RELEASE.md for details.` | **GOVERNANCE.md** → `[Describe the release process or reference a RELEASE.md file]` |

---

### Section 8 — TSC-Specific Governance (STEERING_COMMITTEE.md)

| ID | Prompt | Example | Files → Placeholder |
|----|--------|---------|---------------------|
| `TSC_NOMINATION_PERIOD_DAYS` | How many business days are nominations open for TSC elections? | `10` | **STEERING_COMMITTEE.md** → `[number]` in "Nominations are open for [number] business days" |
| `TSC_APPROVAL_THRESHOLD` | What vote threshold is required to approve new TSC members? (`majority` or `two-thirds majority`) | `two-thirds majority` | **STEERING_COMMITTEE.md** → `[majority/two-thirds majority]` in "approved by a [majority/two-thirds majority] vote" (Election Process) |
| `TSC_TERM_YEARS` | How many years is a TSC member's term? | `2` | **STEERING_COMMITTEE.md** → `[number]` in "term of [number] years" |
| `TSC_QUORUM` | What is the quorum for TSC meetings? (number or percentage) | `majority of TSC members` | **STEERING_COMMITTEE.md** → `[number or percentage]` in quorum definition |
| `TSC_DECISION_THRESHOLD` | What vote threshold is required for general TSC decisions? (`majority` or `two-thirds majority`) | `majority` | **STEERING_COMMITTEE.md** → `[majority/two-thirds majority]` in "Decisions require a [majority/two-thirds majority]" (Decision-Making) |
| `TSC_AGENDA_PROPOSAL_PROCESS` | How can community members propose TSC meeting agenda items? | `opening an issue with the 'tsc-agenda' label` | **STEERING_COMMITTEE.md** → `[process]` in "propose agenda items by [process]" |
| `TSC_MAILING_LIST_EMAIL` | What is the TSC mailing list email address? | `tsc@myproject.org` | **STEERING_COMMITTEE.md** → `[tsc@project_name.org]` |
| `TSC_CHAIR_EMAIL` | What is the TSC Chair's direct contact email? | `chair@myproject.org` | **STEERING_COMMITTEE.md** → `[chair email]` |

---

### Section 9 — TSC Chair (STEERING_COMMITTEE.md)

| ID | Prompt | Example | Files → Placeholder |
|----|--------|---------|---------------------|
| `TSC_CHAIR_NAME` | Who is the current TSC Chair? (full name) | `Jane Smith` | **STEERING_COMMITTEE.md** → `[Name]` in "**Current Chair:** [Name]" |
| `TSC_CHAIR_GITHUB` | What is the TSC Chair's GitHub handle? (without @) | `janesmith` | **STEERING_COMMITTEE.md** → `[github_handle]` in "(@[github_handle])" for the Chair |
| `TSC_CHAIR_TERM_START` | When does the Chair's term start? (YYYY-MM-DD) | `2026-01-01` | **STEERING_COMMITTEE.md** → first `[YYYY-MM-DD]` in Chair Term |
| `TSC_CHAIR_TERM_END` | When does the Chair's term end? (YYYY-MM-DD) | `2027-01-01` | **STEERING_COMMITTEE.md** → second `[YYYY-MM-DD]` in Chair Term |

---

### Section 10 — TSC Members (STEERING_COMMITTEE.md)

Prompt the user: **How many initial TSC members does the project have?** Then collect the following for each member. Populate the table in `STEERING_COMMITTEE.md`, replacing the template rows.

For each TSC member, collect:

| Field | Prompt | Example |
|-------|--------|---------|
| `TSC_MEMBER_NAME` | Full name | `Jane Smith` |
| `TSC_MEMBER_GITHUB` | GitHub handle (without @) | `janesmith` |
| `TSC_MEMBER_ORG` | Organization (or "Independent") | `Acme Corp` |
| `TSC_MEMBER_TERM_START` | Term start date (YYYY-MM-DD) | `2026-01-01` |
| `TSC_MEMBER_TERM_END` | Term end date (YYYY-MM-DD or "Ongoing") | `Ongoing` |

Remove any unfilled template rows from the table. If the user provides zero members, leave the table header with no data rows and add a comment `<!-- Add TSC members here -->`.

---

### Section 11 — Maintainers (MAINTAINERS.md)

Prompt the user: **How many initial maintainers does the project have?** Then collect the following for each. Populate the table in `MAINTAINERS.md`, replacing the template rows.

For each maintainer, collect:

| Field | Prompt | Example |
|-------|--------|---------|
| `MAINTAINER_NAME` | Full name | `John Doe` |
| `MAINTAINER_GITHUB` | GitHub handle (without @) | `johndoe` |
| `MAINTAINER_ORG` | Organization (or "Independent") | `WidgetCo` |
| `MAINTAINER_TZ` | Time zone abbreviation | `PT` |

Remove any unfilled template rows. If the user provides zero maintainers, leave the table header with no data rows and add a comment `<!-- Add maintainers here -->`.

---

### Section 12 — Emeritus Members (MAINTAINERS.md, STEERING_COMMITTEE.md)

Prompt: **Do you have any emeritus maintainers or TSC members to list?** If yes, collect the same fields as above plus a `Tenure` field (e.g., `2024-01-01 - 2025-12-31`). If no, leave the emeritus tables with headers only and a comment `<!-- No emeritus members yet -->`.

---

### Section 13 — Security Policy (SECURITY.md)

| ID | Prompt | Example | Files → Placeholder |
|----|--------|---------|---------------------|
| `SECURITY_EMAIL` | What email address should security vulnerabilities be reported to? | `security@myproject.org` | **SECURITY.md** → `[security@project_name.org]` (both occurrences: reporting section and contact section) |
| `SECURITY_ANNOUNCE_EMAIL` | What is the security announcements mailing list email? | `security-announce@myproject.org` | **SECURITY.md** → `[security-announce@project_name.org]` |
| `SECURITY_ANNOUNCE_LINK` | URL to subscribe to security announcements | `https://lists.example.org/security` | **SECURITY.md** → `[link to mailing list or notification channel]` |
| `SECURITY_ANNOUNCE_CHANNEL` | What communication channel are security announcements posted to? | `#security on Discord` | **SECURITY.md** → `[communication channel]` (in the "Follow our announcements" line) |
| `SECURITY_PGP_INFO` | PGP key link or fingerprint for encrypted communications (optional) | `https://keys.openpgp.org/search?q=security@myproject.org` | **SECURITY.md** → `[link to PGP key or key fingerprint]` |
| `SECURITY_CONFIGURATION_NOTES` | Any security-related configuration guidance for users? (optional) | `See docs/security-hardening.md` | **SECURITY.md** → `[Document any security-related configuration options, hardening guides, or security features of the project]` |

#### Supported Versions Table (SECURITY.md)

Prompt: **How many versions are currently supported with security updates?** Then for each version, collect:

| Field | Prompt | Example |
|-------|--------|---------|
| `VERSION` | Version identifier | `2.1.x` |
| `SUPPORTED` | Is this version supported? (yes/no) | `yes` |

Replace the placeholder rows (`x.x.x`) in the Supported Versions table. Preserve the `< x.x.x | ❌ No` row pattern for unsupported older versions if the user provides a cutoff.

---

### Section 14 — Coding Standards (CONTRIBUTING.md, AGENTS.md)

| ID | Prompt | Example | Files → Placeholder |
|----|--------|---------|---------------------|
| `PRIMARY_LANGUAGES` | What are the primary programming language(s) and versions? | `Python 3.10+, TypeScript 5.x` | **AGENTS.md** → `[e.g., Python 3.10+, TypeScript 5.x]` |
| `STYLE_GUIDE` | What style guide does the project follow? | `PEP 8, Google TypeScript Style Guide` | **AGENTS.md** → `[e.g., PEP 8, Google Style Guide, Airbnb JavaScript Style Guide]` ; **CONTRIBUTING.md** → `[Describe language-specific style guides, e.g., PEP 8 for Python, Google Style Guide for Go, etc.]` |
| `FORMATTING_TOOLS` | What code formatting tools are used? | `black, prettier` | **AGENTS.md** → `[e.g., black, prettier, gofmt]` |
| `LINTING_TOOLS` | What linting tools are used? | `pylint, eslint` | **AGENTS.md** → `[e.g., pylint, eslint, golangci-lint]` |
| `FORMATTING_TOOL_DESCRIPTION` | Describe any code formatting tools or configurations (for CONTRIBUTING.md). | `We use black for Python and prettier for TypeScript` | **CONTRIBUTING.md** → `[Describe any code formatting tools or configurations used, e.g., linters, formatters]` |
| `LINT_COMMAND` | What is the command to run the linter? | `pylint src/` | **CONTRIBUTING.md** → `[linting command]` |
| `FORMAT_COMMAND` | What is the command to format code? | `black .` | **CONTRIBUTING.md** → `[formatting command]` |
| `TEST_COMMAND` | What is the command to run all tests? | `pytest` | **CONTRIBUTING.md** → `[test command]` ; **AGENTS.md** → `[test command]` |
| `SPECIFIC_TEST_COMMAND` | What is the command to run a specific test? | `pytest tests/test_specific.py` | **CONTRIBUTING.md** → `[specific test command]` ; **AGENTS.md** → `[specific test command]` |
| `COVERAGE_COMMAND` | What is the command to check test coverage? | `pytest --cov=src` | **AGENTS.md** → `[coverage command]` |
| `DOCSTRING_FORMAT` | What docstring/comment format is used? | `Google style` | **AGENTS.md** → `[docstring format, e.g., Google style, NumPy style, JSDoc]` |
| `REVIEW_TIMEFRAME` | How quickly can contributors expect a maintainer review? | `one week` | **CONTRIBUTING.md** → `[timeframe, e.g., "one week"]` |

---

### Section 15 — Naming Conventions (AGENTS.md)

| ID | Prompt | Example | Files → Placeholder |
|----|--------|---------|---------------------|
| `NAMING_FILES` | File naming convention | `snake_case.py` | **AGENTS.md** → `[e.g., snake_case.py, kebab-case.ts]` |
| `NAMING_CLASSES` | Class naming convention | `PascalCase` | **AGENTS.md** → `[e.g., PascalCase]` |
| `NAMING_FUNCTIONS` | Function/method naming convention | `snake_case` | **AGENTS.md** → `[e.g., snake_case, camelCase]` (Functions/Methods) |
| `NAMING_VARIABLES` | Variable naming convention | `snake_case` | **AGENTS.md** → `[e.g., snake_case, camelCase]` (Variables) |
| `NAMING_CONSTANTS` | Constants naming convention | `UPPER_SNAKE_CASE` | **AGENTS.md** → `[e.g., UPPER_SNAKE_CASE]` |

---

### Section 16 — Architecture & Domain (AGENTS.md)

These are free-text sections in `AGENTS.md`. Prompt for each.

| ID | Prompt | Example | Files → Placeholder |
|----|--------|---------|---------------------|
| `CORE_COMPONENTS` | List and briefly describe the main components of the project. | `API Gateway: handles routing; Auth Service: manages authentication` | **AGENTS.md** → `[List and briefly describe main components]` |
| `DIRECTORY_STRUCTURE` | Describe the organization of the codebase. | `src/ contains source code, tests/ contains tests, docs/ contains documentation` | **AGENTS.md** → `[Describe the organization of the codebase]` |
| `KEY_DEPENDENCIES` | List critical dependencies and their purposes. | `FastAPI for HTTP serving, SQLAlchemy for ORM, Redis for caching` | **AGENTS.md** → `[List critical dependencies and their purposes]` |
| `KEY_CONCEPTS` | Define 3+ important domain-specific concepts or terms used in the project. Provide as `term: definition` pairs. | `Middleware: a function that runs before/after request handlers` | **AGENTS.md** → The `[Concept 1]`/`[Definition]` pairs (repeat for each concept the user provides) |
| `CODE_PATTERNS` | Describe specific code patterns AI agents should follow. Provide as `pattern: description` pairs. | `Repository pattern: all database access goes through repository classes` | **AGENTS.md** → The `[Pattern 1]`/`[Description and example]` entries |

---

### Section 17 — Acknowledgments (README.md)

| ID | Prompt | Example | Files → Placeholder |
|----|--------|---------|---------------------|
| `ACKNOWLEDGMENT_1` | First organization or person to acknowledge (optional) | `The Linux Foundation` | **README.md** → `[Organization/Person 1]` |
| `ACKNOWLEDGMENT_2` | Second organization or person to acknowledge (optional) | `Our amazing community contributors` | **README.md** → `[Organization/Person 2]` |
| `ACKNOWLEDGMENT_3` | Third organization or person to acknowledge (optional) | `Acme Corp for sponsoring CI infrastructure` | **README.md** → `[Organization/Person 3]` |

---

### Section 18 — Badges (README.md)

| ID | Prompt | Example | Files → Placeholder |
|----|--------|---------|---------------------|
| `OPENSSF_BADGE_ID` | OpenSSF Best Practices badge project ID (optional, or "none") | `12345` | **README.md** → `XXXX` in the OpenSSF badge URL (two occurrences) |

---

## Substitution Procedure

### Step 1 — Collect all values

Prompt the user for every variable in Sections 1–18 above. Group prompts logically and allow batch input where possible. For variables marked `(optional)`, if the user skips them, either remove the line/section from the output file or insert a TODO comment like `<!-- TODO: Add [description] -->`.

### Step 2 — Perform global replacements

In **every** `.md` file listed in [Files to Process](#files-to-process):

1. Replace all occurrences of the literal string `project_name` with the value of `PROJECT_NAME`.
2. Replace all occurrences of the literal string `project_repo` with the value of `PROJECT_REPO`.

**Be careful**: `project_name` appears inside headings, prose, URLs, email addresses (e.g., `security@project_name.org`), and filenames-in-text. All must be replaced. However, do NOT replace occurrences inside this `AGENTSETUP.md` file itself.

### Step 3 — Perform per-file replacements

For each file, find and replace every bracketed placeholder with the corresponding user-supplied value, following the mapping in the Variable Registry.

**Disambiguation rules** for placeholders that use the same bracket text (like `[number]` or `[calendar link]`) in different contexts:

- Match by **file** and **surrounding text context**. The Variable Registry specifies the exact sentence or section where each placeholder lives.
- When a file has multiple `[number]` placeholders, replace them in document order according to the registry mapping.
- When a file has multiple `[calendar link]` or `[meeting link]` placeholders in different sections (e.g., TSC vs. Office Hours in README.md), use the section context to determine which value to substitute.

### Step 4 — Handle dynamic tables

For `MAINTAINERS.md`, `STEERING_COMMITTEE.md`, and the Supported Versions table in `SECURITY.md`:

1. Remove all template rows (rows with `[Full Name]`, `[github_handle]`, `x.x.x`, etc.).
2. Insert one row per entry the user provided.
3. If no entries were provided, leave the table header with a comment row.

### Step 5 — Clean up

- Remove any remaining HTML instructional comments like `<!-- Brief description of what this project does ... -->` and `<!-- Update this section with each release -->` and `<!-- Add relevant badges for your project -->` from README.md.
- Remove the `[Describe the high-level architecture and key components that AI agents should understand.]` instructional lines from AGENTS.md.
- Remove all `[Define important domain-specific concepts, terminology, and patterns used in the project.]` instructional lines.
- Remove all `[Describe specific patterns and practices AI agents should follow.]` instructional lines.
- Ensure no lines remain that begin with `[` and end with `]` that look like unresolved instructions.

---

## Verification

After all substitutions, the agent MUST verify the output:

### Automated checks

Run the following checks across all processed files:

1. **No remaining `project_name` literals**: Search for the exact string `project_name` — there should be zero matches (except inside AGENTSETUP.md itself if it is retained).
2. **No remaining `project_repo` literals**: Search for the exact string `project_repo` — there should be zero matches.
3. **No unresolved bracket placeholders**: Search for patterns matching `\[[A-Za-z].*?\]` that look like template placeholders (e.g., `[Full Name]`, `[number]`, `[description]`). Ignore legitimate Markdown link text like `[GOVERNANCE.md]` or `[SECURITY.md]` which are part of `[text](url)` link syntax.
4. **No remaining example/template values**: Search for `x.x.x`, `XXXX`, `@[github_handle]`, `[YYYY-MM-DD]`, `email@example.com`.
5. **Valid Markdown**: Confirm that all tables still have correct column counts and pipe alignment.
6. **Links are consistent**: Verify that cross-file links (e.g., `[GOVERNANCE.md](GOVERNANCE.md)`) still work and that the `project_repo` URL is well-formed in all constructed URLs (e.g., `project_repo/issues` → `https://github.com/org/repo/issues`).

### Report

Produce a summary listing:
- Total variables substituted
- Any variables that were skipped (optional ones)
- Any verification warnings or issues found
- List of output files produced

---

## Notes for the User

- **This file (`AGENTSETUP.md`) should be removed or archived** after configuration is complete. It is not intended to be part of the published project documentation.
- The `LICENSE` file must be provided separately — this setup process does not generate license text.
- The `DCO` file is a standard document and requires no configuration.
- `CODE_OF_CONDUCT.md`, `ANTITRUST.md`, and `TRADEMARKS.md` are standard LF Projects documents and require no configuration.
- After running this setup, review all files manually to ensure accuracy and completeness.

---

*This AGNETSETUP.md was generated to facilitate automated project bootstrapping. It is compatible with Claude Code, Codex, and other agentic AI frameworks.*
