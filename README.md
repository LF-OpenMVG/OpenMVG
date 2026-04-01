# Open Minimum Viable Governance (OpenMVG)

## What is Open Minimum Viable Governance?

Open Minimum Viable Governance (OpenMVG) is a repository-based framework for establishing lightweight governance in free and open source projects hosted on version control platforms such as GitHub or GitLab. This framework provides per-project governance that aligns with Linux Foundation project standards and best practices.

OpenMVG is designed for individual projects governed by a Technical Steering Committee (TSC). Foundation-level governance is handled separately in the foundation's own repository and is outside the scope of this framework.

OpenMVG allows you to quickly establish collaborations that can grow with your project. It provides simple governance at the outset, including legal terms, licensing and trademark policies, and due process. Having this governance in place early helps avoid disputes among participants down the road.

## Quick Start Guide

Follow these steps to implement OpenMVG governance in your project:

1. **Review the OpenMVG framework** to determine if it meets your project's needs.

2. **Configure the template files** in the `./project-repo` directory using one of the three setup methods described in the [Setting Up Your Templates](#setting-up-your-templates) section below. You can use an AI agent (AGENTSETUP.md), a Python script (SETUP.py), or edit the files manually -- all three approaches are documented with step-by-step instructions. Once complete, the files are ready to be placed at the root of your project repository.

3. **Describe your project's mission** in the GOVERNANCE.md file and define your Technical Charter.  For LF Projects the charter will be the charter established during the formation process.

4. **Establish your TSC** by having each initial TSC member "sign" the STEERING_COMMITTEE.md file by adding their name and organizational affiliation (if applicable).

5. **Establish your maintainers** by having each initial maintainer "sign" the MAINTAINERS.md file by adding their name and organizational affiliation (if applicable).

6. **Choose an appropriate open source license** from [choosealicense.com](https://choosealicense.com/) using the exact text from [SPDX](https://spdx.org/licenses/).  We recommend using MIT or Apache 2.0 for software projects, OpenMDW-1.0 for AI models (openmdw.ai), CDLA-Permissive-2.0 (cdla.dev) for data and CC-BY-4.0 for documentation.

7. **Configure repository permissions** to enforce two-factor authentication and role-based access control.

8. **Set up compliance tooling** for DCO checks and license scanning.

9. **Get to work.**

---

## Setting Up Your Templates

The `project-repo/` directory contains all governance template files pre-populated with placeholder values. Two interactive setup methods are provided to configure them. Both methods prompt you for values section by section and write the results directly to the template files — no manual find-and-replace required.

---

### Method 1 -- AI Agent Setup (AGENTSETUP.md)

`AGENTSETUP.md` is the primary setup method and is part of the **Open Agent Installer** project — a standard for configuring open source project repositories through a conversational AI agent interface.

**Compatible agents:** Claude (Claude Code), OpenAI Codex, OpenClaw, and any other agentic AI framework capable of reading and executing a Markdown instruction file.

**How it works:**

The agent reads `AGENTSETUP.md` in full, then guides you through each of the 18 configuration sections interactively — one section at a time. After collecting your answers, it performs all substitutions across the template files, verifies that no unresolved placeholders remain, and reports a summary of every change made.

**To run:**

In your AI agent session (e.g., Claude Code), navigate to the `OpenMVG/` directory and enter:

```
execute AGENTSETUP.md
```

The agent will prompt you for each value, pause for your input after each section, and complete all file edits automatically.

**What it configures:** All 7 template files — `README.md`, `CONTRIBUTING.md`, `GOVERNANCE.md`, `MAINTAINERS.md`, `STEERING_COMMITTEE.md`, `SECURITY.md`, and `AGENTS.md`.

**When to use this method:**
- You are already working inside an AI agent session (Claude Code, Codex, etc.)
- You want a guided, conversational setup experience
- You prefer the agent to make all file edits on your behalf

---

### Method 2 -- Python Script Setup (SETUP.py)

`SETUP.py` is a standalone Python 3 script that replicates the full `AGENTSETUP.md` workflow without requiring an AI agent. It is ideal for automated pipelines, CI environments, or users who prefer a traditional command-line interface.

**Requirements:** Python 3.6 or later. No external dependencies.

**How it works:**

The script presents the same 18 configuration sections as `AGENTSETUP.md`, prompting you for each value at the terminal. Optional fields can be skipped by pressing Enter. After collecting all inputs, the script performs global and per-file substitutions, builds dynamic tables (TSC members, maintainers, supported versions), removes instructional placeholder text, and writes the updated files. A verification pass then checks for any remaining unresolved placeholders and prints a completion summary.

**To run:**

```bash
cd OpenMVG/
python3 SETUP.py
```

**What it configures:** Same 7 template files as Method 1.

**When to use this method:**
- You do not have access to an AI agent session
- You want a repeatable, scriptable setup process
- You are integrating template configuration into a CI/CD pipeline or automation workflow

---

### Method 3 -- Manual Setup

If you prefer not to use an AI agent or the Python script, you can configure the template files by hand using any text editor.

**Requirements:** Any text editor. No tools or dependencies required.

**How it works:**

Open each file in the `project-repo/` directory and perform the following substitutions:

1. **Global replacements** -- In every template file, replace all occurrences of the literal token `project_name` with your project's name, and all occurrences of `project_repo` with the full URL of your project repository (e.g., `https://github.com/org/repo`). These tokens appear in headings, prose, URLs, email addresses, and code blocks -- all instances must be replaced.

2. **Bracketed placeholders** -- Replace each value enclosed in square brackets `[]` with the appropriate content for your project. For example, replace `[version number]` with your current release version, `[calendar link]` with your TSC meeting calendar URL, and so on. The full list of placeholders and their meanings is documented in `AGENTSETUP.md`.

3. **Dynamic tables** -- In `MAINTAINERS.md`, `STEERING_COMMITTEE.md`, and the Supported Versions table in `SECURITY.md`, replace the placeholder table rows (rows containing `[Full Name]`, `@[github_handle]`, `x.x.x`, etc.) with one row per actual member or version. Remove any unfilled template rows.

4. **Instructional comments** -- Remove HTML comment blocks that contain setup instructions, such as `<!-- Brief description of what this project does -->`. These are authoring aids and should not appear in the published files.

**Files to configure:** `README.md`, `CONTRIBUTING.md`, `GOVERNANCE.md`, `MAINTAINERS.md`, `STEERING_COMMITTEE.md`, `SECURITY.md`, and `AGENTS.md`. The files `CODE_OF_CONDUCT.md`, `ANTITRUST.md`, and `TRADEMARKS.md` are standard LF Projects documents and require no changes.

**When to use this method:**
- You prefer full control over every edit
- You are making selective or partial changes to the templates
- You are updating previously configured files rather than starting from scratch

---

### Comparison

| | Method 1: AGENTSETUP.md | Method 2: SETUP.py | Method 3: Manual |
|---|---|---|---|
| **Interface** | Conversational AI agent | Terminal prompt | Text editor |
| **Requires AI agent** | Yes | No | No |
| **Requires Python** | No | Yes (3.6+) | No |
| **Interactive** | Yes | Yes | No |
| **Edits files automatically** | Yes | Yes | No -- user edits directly |
| **Verifies output** | Yes | Yes | No -- user must verify |
| **Skippable optional fields** | Yes | Yes | Yes |
| **Best for** | Agent sessions | CLI / automation | Selective or partial edits |

> **Note:** `AGENTSETUP.md` and `SETUP.py` should be **removed or archived** from your project repository after setup is complete. They are configuration tools, not project documentation.

---

## Detailed Implementation Guide

This section provides comprehensive requirements and recommendations for setting up your project repository. The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" are defined in accordance with [BCP 14](https://www.rfc-editor.org/info/bcp14).

### Required Repository Files

The following files MUST exist at the root of your repository. These follow standard conventions in open source projects.

If your project has multiple repositories, you MUST either have these files in each repository, or it is RECOMMENDED to maintain the base files in one repository (either the primary code repository or the special `.github`/`.gitlab` repository) and reference them in each of the other repositories.

#### README.md

Each repository MUST have a README.md file containing the following:

- **Project overview**: MUST include an explanation of what the project does.

- **Release information**: MUST include the latest release information (if applicable). Release history, including change logs, can be maintained in a RELEASE file (see [keepachangelog.com](https://keepachangelog.com/) for an example) or by using GitHub/GitLab's Releases functionality.

- **Usage instructions**: MUST explain how a user can use the code in the repository (if applicable). This MAY be split into a separate BUILD or INSTALL file, referenced in the README, if the instructions exceed 30 words.

- **Contribution guidelines**: MUST explain how a user can contribute to the code repository. This SHOULD be split into a separate CONTRIBUTING.md file if it exceeds a paragraph of instructions. Instructions for reporting security vulnerabilities MUST be in a SECURITY.md file, which can be referenced in the README.md but MUST be referenced in the CONTRIBUTING.md file.

- **Support and communication**: MUST include information on how users can get support or discuss the project with others. MUST provide links to mailing lists, communication channels, and where to submit bug reports. MUST include a calendar link for TSC meetings, office hours, or a list of meetings with instructions on how to join.  For private TSC meetings this is NOT requireds.

- **Acknowledgments**: SHOULD acknowledge any initial contributing organizations or persons.

- **Badges**: SHOULD display badges for OpenSSF Best Practices badge status, build status, and license.

#### LICENSE

Each repository MUST have a LICENSE file listing the primary license of the source code. The license text MUST be the exact text from [SPDX](https://spdx.org/licenses/) and must be an approved open source license listed at [SPDX](https://spdx.org/licenses/).

If the repository contains code or assets not under the primary license, they MUST be referenced in a THIRD-PARTY file, which lists the covered files and includes the full license text from SPDX.

Projects SHOULD use SPDX short-form identifiers throughout the codebase.

Recommended licenses are:
  Software - MIT or Apache-2.0
  Specifications or documents - CC-BY-4.0
  Data - CDLA-Permissive-2.0
  AI Models - OpenMDW-1.0

- **Be Advised**: You MUST copy the contents of the license you choose to use and paste them into the LICENSE file manually.

#### GOVERNANCE.md

Each repository MUST have a GOVERNANCE.md file detailing how decisions are made in the project. The following items MUST be included:

- **Technical Charter**: A link to the Technical Charter, DO NOT copy the full contents of the Technical Charter into the document.  For Linux Foundation projects, the Technical Charter is established during the formation process.

- **Community roles**: Definitions of community roles (such as TSC Member, Maintainer/Committer, Contributor) and how one can be promoted to any of those roles.

- **Current leadership**: A list of current leaders in the project. This MAY be maintained in a separate MAINTAINERS.md.

- **Decision-making process**: An explanation of how decisions are made and voting is conducted.

- **Project policies**: Any other project policies or processes. Release instructions MAY be maintained in a RELEASE file.

- **Meeting information**: Schedule and joining instructions for TSC meetings and a link to TSC meeting agendas and notes.

#### CODE_OF_CONDUCT.md

The Code of Conduct MUST be maintained in a CODE_OF_CONDUCT.md file. If using the LF Projects, LLC Code of Conduct, it is RECOMMENDED to include a link to that document in the CODE_OF_CONDUCT.md file instead of copying and pasting the full text.

#### SECURITY.md

The project MUST maintain a SECURITY.md file that outlines the security policy for the project, including procedures for reporting vulnerabilities and policies for responding to them.

For more details, see:

- [OpenSSF Scorecard Security Policy Check](https://github.com/ossf/scorecard/blob/main/docs/checks.md#security-policy)
- [OpenSSF Best Practices Vulnerability Reporting](https://www.bestpractices.dev/en/criteria/0?details=true&rationale=true#0.vulnerability_report_process)

#### CONTRIBUTING.md

Each repository MUST have a CONTRIBUTING.md file that provides guidance for contributors. The following items SHOULD be included:

- **How to contribute**: Clear instructions on the process for submitting contributions, including how to fork the repository, create branches, and submit pull requests or merge requests.

- **Coding standards**: Any coding style guidelines, formatting requirements, or conventions that contributors should follow.

- **Testing requirements**: Expectations for testing contributions before submission.

- **Review process**: An explanation of how contributions are reviewed and what to expect during the review cycle.

- **Security reporting reference**: A reference to the SECURITY.md file for instructions on reporting security vulnerabilities. This reference is REQUIRED.

- **DCO/CLA requirements**: Information about Developer Certificate of Origin sign-off requirements or Contributor License Agreement obligations.

#### ANTITRUST.md

Each repository MUST have an ANTITRUST.md file that contains the project's antitrust policy. This file SHOULD include a statement that all participants agree to comply with applicable antitrust and competition laws. If using the Linux Foundation's standard antitrust policy, it is RECOMMENDED to include a link to that document rather than copying the full text.

#### MAINTAINERS.md

Each repository MUST have a MAINTAINERS.md file that lists the current maintainers of the project. The following items MUST be included:

- **Maintainer list**: Names and organizational affiliations (if applicable) of all current maintainers.

- **Maintainer responsibilities**: A description of the responsibilities and expectations of maintainers.

- **Becoming a maintainer**: The process by which contributors can become maintainers, including any requirements or nomination procedures.

- **Emeritus maintainers**: MAY include a list of former maintainers who have stepped down but made significant contributions to the project.

Each maintainer "signs" this file by adding their name and affiliation, indicating their agreement to the project's governance and policies.

#### STEERING_COMMITTEE.md

Each repository MUST have a STEERING_COMMITTEE.md file that documents the Technical Steering Committee (TSC). The following items MUST be included:

- **TSC member list**: Names and organizational affiliations (if applicable) of all current TSC members.

- **TSC responsibilities**: A description of the TSC's role, authority, and responsibilities within the project.

- **TSC membership**: The process for joining and leaving the TSC, including election or appointment procedures, term lengths (if applicable), and removal processes.

- **Meeting cadence**: Information about how often the TSC meets and how meetings are conducted.

Each TSC member "signs" this file by adding their name and affiliation, indicating their agreement to serve on the TSC and abide by the project's governance.

#### TRADEMARKS.md

Each repository MUST have a TRADEMARKS.md file that provides a link to the LF project's Trademark Policy, which must be consistent with the LF's Trademark Policy. The following items SHOULD be included:

- **Trademark ownership**: A statement identifying who owns the project's trademarks (typically the Linux Foundation or the project itself).

- **Permitted uses**: Guidelines on how the project name, logo, and other trademarks may be used by the community.

- **Restricted uses**: Clear statements about uses that are not permitted without explicit permission.

- **Logo and asset files**: MAY include or reference official logo files and brand guidelines.

If using the Linux Foundation's standard trademark policy, it is RECOMMENDED to include a link to that document rather than copying the full text.

#### DCO

Each repository that implements DCO MUST have a DCO file that contains the Developer Certificate of Origin. The DCO is a lightweight way for contributors to certify that they wrote or otherwise have the right to submit the code they are contributing to the project.

The DCO file MUST contain the full text of the Developer Certificate of Origin version 1.1, available at [developercertificate.org](https://developercertificate.org/).

Contributors sign the DCO by adding a `Signed-off-by` line to their commit messages. This can be done automatically by using the `-s` or `--signoff` flag when committing:

```
git commit -s -m "Your commit message"
```

The CONTRIBUTING.md file MUST reference the DCO file and explain the sign-off requirement to contributors.

#### AGENTS.md

Each repository SHOULD have an AGENTS.md file that provides guidance for AI agents and large language models (LLMs) interacting with the project. As AI-assisted development becomes more prevalent, this file helps ensure AI agents understand and follow project conventions.

The following items SHOULD be included:

- **Project context**: A brief description of the project's purpose, architecture, and key concepts that an AI agent should understand before contributing.

- **Coding conventions**: Specific coding standards, patterns, and practices that AI agents should follow when generating code for the project.

- **Contribution guidelines for agents**: Any special instructions or limitations for AI-generated contributions, including review requirements and disclosure expectations.

- **Prohibited actions**: Clear statements about what AI agents should NOT do, such as modifying certain files, making breaking changes, or bypassing security controls.

- **Testing requirements**: Expectations for AI-generated code, including test coverage and validation requirements.

- **Human oversight**: Requirements for human review of AI-generated contributions.

This file complements CONTRIBUTING.md by providing AI-specific guidance while ensuring that AI contributions meet the same quality and compliance standards as human contributions.

### Repository Permissions

- Write access to the repository MUST be connected to a community role. The project CAN NOT provide write access to a user unless they have a community role that grants them write access.

- All users with write access to the repository MUST have two-factor authentication (2FA) enabled for their accounts.

- Adding or removing users with write access MUST require a vote to approve, and this vote MUST be documented (MAY be documented in a GitHub/GitLab Pull Request or Issue). The voters to approve MUST be a quorum of persons in that community role (for example, a quorum of existing maintainers to approve a new maintainer). Quorum is defined in the project's Technical Charter.

- It is RECOMMENDED to use the Teams functionality in GitHub or Groups in GitLab to manage community roles and write access.

- It is RECOMMENDED to use the CODEOWNERS file to manage users who maintain or have expertise in specific areas of the project. See documentation for [GitHub CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) or [GitLab CODEOWNERS](https://docs.gitlab.com/user/project/codeowners).

### Compliance Requirements

- Projects MUST use tooling to enforce DCO (Developer Certificate of Origin) checks. Recommended tooling includes: [DCO Probot](https://github.com/apps/dco), [GitHub Signoff](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/managing-the-commit-signoff-policy-for-your-repository) and [Gitlab Reject usigned commits](https://docs.gitlab.com/user/project/repository/push_rules/#reject-commits-that-arent-dco-certified)

- If a project uses a CLA (Contributor License Agreement), the project MUST use tooling to enforce CLA checks. LFX EasyCLA MUST be used for CLA checks for Linux Foundation hosted projects.

- Projects SHOULD leverage the Linux Foundation License Scanning Operations Program to ensure license compliance.

- Projects SHOULD use SPDX short-form identifiers in all source files.

---

## Contributing

We welcome contributions to the OpenMVG project. Your help is essential for keeping it great.

Contributions to this project are released to the public under the project's open source license Creative Commons Attribution 4.0 International.

Please note that this project is released with a [Contributor Covnenant 3.0 Code of Conduct](https://www.contributor-covenant.org/version/3/0/code_of_conduct/). By participating in this project you agree to abide by its terms.

### Submitting a Pull Request

1. [Fork](https://github.com/LF-OpenMVG/OpenMVG/fork) and clone the repository.
2. Create a new branch: `git checkout -b my-branch-name`
3. Make your changes.
4. Push to your fork and [submit a pull request](https://github.com/LF-OpenMVG/OpeMVG/compare).
5. Wait for your pull request to be reviewed and merged.

---

## Additional Resources

- [OpenSSF Best Practices Badge Program](https://www.bestpractices.dev/)
- [SPDX License List](https://spdx.org/licenses/)
- [Choose a License](https://choosealicense.com/)
- [Keep a Changelog](https://keepachangelog.com/)
- [LF Projects, LLC Policies](https://lfprojects.org/)