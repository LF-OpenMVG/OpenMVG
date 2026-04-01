#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SETUP.py -- Project Repository Configuration Script

Replicates AGENTSETUP.md functionality: prompts the user for configuration
values section by section and performs substitutions across all project
template files in the project-repo/ directory.

Usage:
    python3 SETUP.py
"""

import re
import sys
from pathlib import Path


# -----------------------------------------------------------------------------
# Files to process
# -----------------------------------------------------------------------------

TEMPLATE_FILES = [
    "README.md",
    "CONTRIBUTING.md",
    "GOVERNANCE.md",
    "MAINTAINERS.md",
    "STEERING_COMMITTEE.md",
    "SECURITY.md",
    "AGENTS.md",
]

NO_SUBSTITUTION_FILES = [
    "CODE_OF_CONDUCT.md",
    "ANTITRUST.md",
    "TRADEMARKS.md",
]


# -----------------------------------------------------------------------------
# Input helpers
# -----------------------------------------------------------------------------

def print_section(title):
    """Print a clearly delimited section header."""
    print(f"\n{'=' * 62}")
    print(f"  {title}")
    print(f"{'=' * 62}\n")


def ask(label, optional=False, default=None):
    """
    Prompt the user for a single value.

    Args:
        label:    Display label for the prompt.
        optional: If True, allow empty input (returns None).
        default:  If provided, use this value when input is empty.

    Returns:
        The user-supplied string, the default, or None if optional and skipped.
    """
    hints = []
    if optional:
        hints.append("optional -- press Enter to skip")
    if default is not None:
        hints.append(f"default: {default}")
    hint_str = f"  ({', '.join(hints)})" if hints else ""
    if hint_str:
        print(hint_str)

    while True:
        raw = input(f"  {label}: ").strip()
        if raw:
            return raw
        if default is not None:
            return str(default)
        if optional:
            return None
        print("  [!]  This field is required. Please enter a value.")


def ask_int(label, optional=False, default=None):
    """
    Prompt for a value that should be a number.
    Strips trailing text like ' days' so the user can type '5 days'.
    """
    raw = ask(label, optional=optional, default=str(default) if default is not None else None)
    if raw is None:
        return None
    # Extract the leading numeric part
    m = re.match(r'(\d+)', raw.strip())
    return m.group(1) if m else raw


def confirm(label):
    """Prompt for a yes/no answer."""
    while True:
        val = input(f"  {label} (yes/no): ").strip().lower()
        if val in ("yes", "y"):
            return True
        if val in ("no", "n"):
            return False
        print("  Please answer 'yes' or 'no'.")


def todo(desc):
    """Return an HTML TODO comment."""
    return f"<!-- TODO: Add {desc} -->"


def val_or_todo(value, desc):
    """Return value if set, otherwise a TODO HTML comment."""
    return value if value else todo(desc)


# -----------------------------------------------------------------------------
# Section collectors
# -----------------------------------------------------------------------------

def collect_section_1():
    print_section("Section 1 -- Global Identifiers")
    print("  These two values are substituted everywhere across all files.\n")
    return {
        "PROJECT_NAME": ask("1. Project name (e.g., MyProject)"),
        "PROJECT_REPO": ask("2. Full repository URL (e.g., https://github.com/org/repo)"),
    }


def collect_section_2():
    print_section("Section 2 -- Project Overview  [README.md, AGENTS.md]")
    return {
        "PROJECT_DESCRIPTION": ask("1. Short project description"),
        "CURRENT_VERSION":     ask("2. Current release version (e.g., 1.0.0)"),
        "RELEASE_DATE":        ask("3. Release date (e.g., 2026-03-22)"),
        "LICENSE_NAME":        ask("4. License name (e.g., Apache-2.0, MIT)", optional=True),
    }


def collect_section_3():
    print_section("Section 3 -- Prerequisites, Installation & Usage  [README.md]")
    return {
        "PREREQUISITES":            ask("1. Prerequisites / dependencies",     optional=True),
        "INSTALLATION_INSTRUCTIONS":ask("2. Installation instructions",        optional=True),
        "USAGE_INSTRUCTIONS":       ask("3. Basic usage instructions",         optional=True),
    }


def collect_section_4():
    print_section("Section 4 -- Communication Channels  [README.md, CONTRIBUTING.md]")
    return {
        "MAILING_LIST_LINK":  ask("1. Mailing list URL",                        optional=True),
        "CHAT_CHANNEL_LINK":  ask("2. Chat/Slack/Discord URL",                  optional=True),
        "FORUM_LINK":         ask("3. Discussion forum URL",                    optional=True),
        "CONDUCT_EMAIL":      ask("4. Code of Conduct report email address",    optional=True),
    }


def collect_section_5():
    print_section("Section 5 -- TSC Meetings  [README.md, GOVERNANCE.md, STEERING_COMMITTEE.md]")
    return {
        "TSC_MEETING_FREQUENCY": ask(
            '1. TSC meeting frequency (e.g., Bi-weekly on Wednesdays at 10:00 AM PT)',
            optional=True),
        "TSC_CALENDAR_LINK":     ask("2. TSC calendar URL",                    optional=True),
        "TSC_VIDEO_LINK":        ask("3. TSC video conference URL",             optional=True),
        "TSC_MEETING_NOTES_LINK":ask("4. TSC meeting notes URL",               optional=True),
        "TSC_AGENDA_LINK":       ask("5. TSC agenda URL (if different from notes)", optional=True),
    }


def collect_section_6():
    print_section("Section 6 -- Office Hours  [README.md]")
    return {
        "OFFICE_HOURS_FREQUENCY":    ask(
            "1. Office hours frequency (e.g., Every Thursday at 2:00 PM PT)", optional=True),
        "OFFICE_HOURS_CALENDAR_LINK":ask("2. Office hours calendar URL",       optional=True),
        "OFFICE_HOURS_VIDEO_LINK":   ask("3. Office hours video conference URL",optional=True),
        "OFFICE_HOURS_NOTES_LINK":   ask("4. Office hours notes/recordings URL",optional=True),
    }


def collect_section_7():
    print_section("Section 7 -- Governance Policies  [GOVERNANCE.md, STEERING_COMMITTEE.md]")
    return {
        "CHARTER_LINK":               ask(
            "1. Technical Charter URL (e.g., https://example.org/charter.pdf)", optional=True),
        "VOTING_PERIOD_DAYS":         ask_int(
            "2. Minimum voting period in business days (e.g., 5)",  optional=True, default=5),
        "LAZY_CONSENSUS_DAYS":        ask_int(
            "3. Lazy consensus waiting period in business days (e.g., 3)", optional=True, default=3),
        "AGENDA_LEAD_HOURS":          ask_int(
            "4. Hours agenda must be published before meeting (e.g., 24)", optional=True, default=24),
        "NOTES_PUBLISH_DAYS":         ask_int(
            "5. Business days to publish meeting notes after meeting (e.g., 3)", optional=True, default=3),
        "AMENDMENT_DISCUSSION_DAYS":  ask_int(
            "6. Business days amendments must be discussed before voting (e.g., 7)", optional=True, default=7),
        "RELEASE_PROCESS_DESCRIPTION":ask(
            "7. Release process description or reference (e.g., See RELEASE.md for details.)",
            optional=True),
    }


def collect_section_8():
    print_section("Section 8 -- TSC-Specific Governance  [STEERING_COMMITTEE.md]")
    return {
        "TSC_NOMINATION_PERIOD_DAYS": ask_int(
            "1. TSC nomination period in business days (e.g., 10)", optional=True, default=10),
        "TSC_APPROVAL_THRESHOLD":     ask(
            "2. New TSC member approval threshold (majority / two-thirds majority)",
            optional=True, default="majority"),
        "TSC_TERM_YEARS":             ask_int(
            "3. TSC member term length in years (e.g., 2)",         optional=True, default=2),
        "TSC_QUORUM":                 ask(
            "4. TSC quorum (e.g., majority of TSC members)",
            optional=True, default="majority of TSC members"),
        "TSC_DECISION_THRESHOLD":     ask(
            "5. General TSC decision threshold (majority / two-thirds majority)",
            optional=True, default="majority"),
        "TSC_AGENDA_PROPOSAL_PROCESS":ask(
            "6. How community members propose agenda items "
            "(e.g., opening an issue with the 'tsc-agenda' label)", optional=True),
        "TSC_MAILING_LIST_EMAIL":     ask(
            "7. TSC mailing list email (e.g., tsc@myproject.org)",  optional=True),
        "TSC_CHAIR_EMAIL":            ask(
            "8. TSC Chair direct contact email",                    optional=True),
    }


def collect_section_9():
    print_section("Section 9 -- TSC Chair  [STEERING_COMMITTEE.md]")
    return {
        "TSC_CHAIR_NAME":       ask("1. TSC Chair full name",                  optional=True),
        "TSC_CHAIR_GITHUB":     ask("2. TSC Chair GitHub handle (without @)",  optional=True),
        "TSC_CHAIR_TERM_START": ask("3. Chair term start date (YYYY-MM-DD)",   optional=True),
        "TSC_CHAIR_TERM_END":   ask("4. Chair term end date (YYYY-MM-DD)",     optional=True),
    }


def collect_section_10():
    """Collect TSC members for STEERING_COMMITTEE.md."""
    print_section("Section 10 -- TSC Members  [STEERING_COMMITTEE.md]")
    count_raw = ask("How many initial TSC members does the project have?",
                    optional=True, default="0")
    count = int(re.sub(r'[^0-9]', '', count_raw) or "0")
    members = []
    for i in range(1, count + 1):
        print(f"\n  TSC Member {i}:")
        github = ask("    GitHub handle (without @)").lstrip("@")
        members.append({
            "name":       ask("    Full name"),
            "github":     github,
            "org":        ask("    Organization (or Independent)"),
            "term_start": ask("    Term start (YYYY-MM-DD)"),
            "term_end":   ask("    Term end (YYYY-MM-DD or Ongoing)"),
        })
    return members


def collect_section_11():
    """Collect maintainers for MAINTAINERS.md."""
    print_section("Section 11 -- Maintainers  [MAINTAINERS.md]")
    count_raw = ask("How many initial maintainers does the project have?",
                    optional=True, default="0")
    count = int(re.sub(r'[^0-9]', '', count_raw) or "0")
    maintainers = []
    for i in range(1, count + 1):
        print(f"\n  Maintainer {i}:")
        github = ask("    GitHub handle (without @)").lstrip("@")
        maintainers.append({
            "name":   ask("    Full name"),
            "github": github,
            "org":    ask("    Organization (or Independent)"),
            "tz":     ask("    Time zone (e.g., PT, ET, UTC)"),
        })
    return maintainers


def collect_section_12():
    """Collect emeritus members for MAINTAINERS.md and STEERING_COMMITTEE.md."""
    print_section("Section 12 -- Emeritus Members  [MAINTAINERS.md, STEERING_COMMITTEE.md]")
    has_emeritus = confirm("Do you have any emeritus maintainers or TSC members to list?")
    emeritus = []
    if has_emeritus:
        count_raw = ask("  How many emeritus members?")
        count = int(re.sub(r'[^0-9]', '', count_raw) or "0")
        for i in range(1, count + 1):
            print(f"\n  Emeritus Member {i}:")
            github = ask("    GitHub handle (without @)").lstrip("@")
            emeritus.append({
                "name":    ask("    Full name"),
                "github":  github,
                "org":     ask("    Organization (or Independent)"),
                "tenure":  ask("    Tenure (e.g., 2024-01-01 - 2025-12-31)"),
            })
    return emeritus


def collect_section_13():
    """Collect security policy values for SECURITY.md."""
    print_section("Section 13 -- Security Policy  [SECURITY.md]")
    values = {
        "SECURITY_EMAIL":              ask(
            "1. Security vulnerability report email (e.g., security@myproject.org)",
            optional=True),
        "SECURITY_ANNOUNCE_EMAIL":     ask(
            "2. Security announcements mailing list email",  optional=True),
        "SECURITY_ANNOUNCE_LINK":      ask(
            "3. URL to subscribe to security announcements", optional=True),
        "SECURITY_ANNOUNCE_CHANNEL":   ask(
            "4. Security announcements channel (e.g., #security on Discord)", optional=True),
        "SECURITY_PGP_INFO":           ask(
            "5. PGP key link or fingerprint",                optional=True),
        "SECURITY_CONFIGURATION_NOTES":ask(
            "6. Security configuration guidance for users",  optional=True),
    }

    print("\n  Supported Versions table:")
    count_raw = ask("  How many version entries to list?", optional=True, default="0")
    count = int(re.sub(r'[^0-9]', '', count_raw) or "0")
    versions = []
    for i in range(1, count + 1):
        ver = ask(f"    Version {i} identifier (e.g., 2.1.x)")
        sup_raw = ask(f"    Is {ver} supported? (yes/no)", optional=True, default="yes")
        supported = sup_raw.lower() in ("yes", "y", "true", "1")
        versions.append({"version": ver, "supported": supported})
    values["SUPPORTED_VERSIONS"] = versions
    return values


def collect_section_14():
    """Collect coding standards for CONTRIBUTING.md and AGENTS.md."""
    print_section("Section 14 -- Coding Standards  [CONTRIBUTING.md, AGENTS.md]")
    return {
        "PRIMARY_LANGUAGES":          ask(
            "1.  Primary language(s) and versions (e.g., Python 3.10+, TypeScript 5.x)",
            optional=True),
        "STYLE_GUIDE":                ask(
            "2.  Style guide (e.g., PEP 8, Google Style Guide)",
            optional=True),
        "FORMATTING_TOOLS":           ask(
            "3.  Formatting tools (e.g., black, prettier)",
            optional=True),
        "LINTING_TOOLS":              ask(
            "4.  Linting tools (e.g., pylint, eslint)",
            optional=True),
        "FORMATTING_TOOL_DESCRIPTION":ask(
            "5.  Formatting/linting tools description (for CONTRIBUTING.md)",
            optional=True),
        "LINT_COMMAND":               ask(
            "6.  Lint command (e.g., pylint src/)",
            optional=True),
        "FORMAT_COMMAND":             ask(
            "7.  Format command (e.g., black .)",
            optional=True),
        "TEST_COMMAND":               ask(
            "8.  Run all tests command (e.g., pytest)",
            optional=True),
        "SPECIFIC_TEST_COMMAND":      ask(
            "9.  Run specific test command (e.g., pytest tests/test_foo.py)",
            optional=True),
        "COVERAGE_COMMAND":           ask(
            "10. Coverage command (e.g., pytest --cov=src)",
            optional=True),
        "DOCSTRING_FORMAT":           ask(
            "11. Docstring format (e.g., Google style, NumPy style, JSDoc)",
            optional=True),
        "REVIEW_TIMEFRAME":           ask(
            "12. Expected maintainer review timeframe (e.g., one week)",
            optional=True),
    }


def collect_section_15():
    """Collect naming conventions for AGENTS.md."""
    print_section("Section 15 -- Naming Conventions  [AGENTS.md]")
    return {
        "NAMING_FILES":     ask("1. File naming convention (e.g., snake_case.py)",    optional=True),
        "NAMING_CLASSES":   ask("2. Class naming convention (e.g., PascalCase)",      optional=True),
        "NAMING_FUNCTIONS": ask("3. Function/method naming convention (e.g., snake_case)", optional=True),
        "NAMING_VARIABLES": ask("4. Variable naming convention (e.g., snake_case)",   optional=True),
        "NAMING_CONSTANTS": ask("5. Constants naming convention (e.g., UPPER_SNAKE_CASE)", optional=True),
    }


def collect_section_16():
    """Collect architecture and domain concepts for AGENTS.md."""
    print_section("Section 16 -- Architecture & Domain  [AGENTS.md]")
    values = {
        "CORE_COMPONENTS":   ask("1. Core components (e.g., API Gateway: handles routing; Auth Service: manages authentication)", optional=True),
        "DIRECTORY_STRUCTURE":ask("2. Directory structure (e.g., src/ source code, tests/ tests, docs/ docs)", optional=True),
        "KEY_DEPENDENCIES":  ask("3. Key dependencies (e.g., FastAPI for HTTP, Redis for caching)", optional=True),
    }

    print("\n  Key Concepts -- enter term/definition pairs. Type 'done' to finish.")
    concepts = []
    while True:
        term = ask("    Concept term (or 'done' to finish)", optional=True)
        if not term or term.lower() == "done":
            break
        defn = ask(f"    Definition of '{term}'")
        concepts.append((term, defn))
    values["KEY_CONCEPTS"] = concepts

    print("\n  Code Patterns -- enter pattern/description pairs. Type 'done' to finish.")
    patterns = []
    while True:
        pattern = ask("    Pattern name (or 'done' to finish)", optional=True)
        if not pattern or pattern.lower() == "done":
            break
        desc = ask(f"    Description of '{pattern}'")
        patterns.append((pattern, desc))
    values["CODE_PATTERNS"] = patterns
    return values


def collect_section_17():
    """Collect acknowledgments for README.md."""
    print_section("Section 17 -- Acknowledgments  [README.md]")
    print("  All optional -- press Enter to skip any.\n")
    return {
        "ACKNOWLEDGMENT_1": ask("1. First acknowledgment",  optional=True),
        "ACKNOWLEDGMENT_2": ask("2. Second acknowledgment", optional=True),
        "ACKNOWLEDGMENT_3": ask("3. Third acknowledgment",  optional=True),
    }


def collect_section_18():
    """Collect badge info for README.md."""
    print_section("Section 18 -- Badges  [README.md]")
    return {
        "OPENSSF_BADGE_ID": ask(
            "1. OpenSSF Best Practices badge project ID (or 'none' to skip)",
            optional=True),
    }


# -----------------------------------------------------------------------------
# Substitution utilities
# -----------------------------------------------------------------------------

def sub(content, old, new):
    """Replace all occurrences of old with new."""
    return content.replace(old, new)


def sub_first(content, old, new):
    """Replace only the first occurrence of old with new."""
    return content.replace(old, new, 1)


def apply_global_subs(content, project_name, project_repo):
    """Replace every occurrence of the literal tokens project_name and project_repo."""
    content = content.replace("project_name", project_name)
    content = content.replace("project_repo", project_repo)
    return content


# -----------------------------------------------------------------------------
# Per-file processors
# -----------------------------------------------------------------------------

def process_readme(content, v):
    # Remove HTML instructional comment blocks
    content = re.sub(
        r'<!--\s*Brief description of what this project does.*?-->\s*\n',
        '', content, flags=re.DOTALL)
    content = re.sub(
        r'<!--\s*Update this section with each release\s*-->\s*\n',
        '', content, flags=re.DOTALL)
    content = re.sub(
        r'<!--\s*Add relevant badges for your project\s*-->\s*\n',
        '', content, flags=re.DOTALL)

    # Overview description
    content = sub(content,
        "[Provide a clear explanation of what the project does, its purpose, and the problem it solves.]",
        val_or_todo(v.get("PROJECT_DESCRIPTION"), "project description"))

    # Release info
    content = sub(content, "[version number]",
        val_or_todo(v.get("CURRENT_VERSION"), "version number"))
    # [date] in Latest Release section (replace first occurrence only)
    content = sub_first(content, "[date]",
        val_or_todo(v.get("RELEASE_DATE"), "release date"))

    # License
    license_name = v.get("LICENSE_NAME")
    content = sub(content, "[LICENSE NAME]",
        license_name if license_name else todo("LICENSE NAME"))
    # Badge placeholder [LICENSE] maps to same value
    content = sub(content, "[LICENSE]",
        license_name if license_name else "TODO_LICENSE_NAME")

    # Prerequisites, Installation, Usage
    content = sub(content,
        "[List any prerequisites, dependencies, or system requirements needed to use this project.]",
        val_or_todo(v.get("PREREQUISITES"), "prerequisites"))
    content = sub(content,
        "[Provide step-by-step installation instructions. If instructions exceed 30 words, consider creating a separate INSTALL.md file.]",
        val_or_todo(v.get("INSTALLATION_INSTRUCTIONS"), "installation instructions"))
    content = sub(content,
        "[Explain how to use the code in this repository. Include basic examples.]",
        val_or_todo(v.get("USAGE_INSTRUCTIONS"), "usage instructions"))

    # Communication channels
    content = sub(content, "[mailing list link]",
        val_or_todo(v.get("MAILING_LIST_LINK"), "mailing list link"))
    content = sub(content, "[communication channel link]",
        val_or_todo(v.get("CHAT_CHANNEL_LINK"), "communication channel link"))
    content = sub(content, "[forum link]",
        val_or_todo(v.get("FORUM_LINK"), "forum link"))

    # TSC meetings -- README uses 'Every other Tuesday' variant
    content = sub(content,
        '[frequency, e.g., "Every other Tuesday at 10:00 AM PT"]',
        val_or_todo(v.get("TSC_MEETING_FREQUENCY"), "TSC meeting frequency"))
    # [calendar link] -- TSC first, Office Hours second
    content = sub_first(content, "[calendar link]",
        val_or_todo(v.get("TSC_CALENDAR_LINK"), "TSC calendar link"))
    # [meeting link] -- TSC first, Office Hours second
    content = sub_first(content, "[meeting link]",
        val_or_todo(v.get("TSC_VIDEO_LINK"), "TSC video conference link"))
    content = sub(content, "[link to meeting notes]",
        val_or_todo(v.get("TSC_MEETING_NOTES_LINK"), "TSC meeting notes link"))

    # Office Hours
    content = sub(content,
        '[frequency, e.g., "Every Thursday at 2:00 PM PT"]',
        val_or_todo(v.get("OFFICE_HOURS_FREQUENCY"), "office hours frequency"))
    # Remaining [calendar link] and [meeting link] are office hours
    content = sub(content, "[calendar link]",
        val_or_todo(v.get("OFFICE_HOURS_CALENDAR_LINK"), "office hours calendar link"))
    content = sub(content, "[meeting link]",
        val_or_todo(v.get("OFFICE_HOURS_VIDEO_LINK"), "office hours video conference link"))
    content = sub(content, "[link to notes or recordings, if applicable]",
        val_or_todo(v.get("OFFICE_HOURS_NOTES_LINK"), "office hours notes/recordings link"))

    # Acknowledgments -- build the list, remove skipped entries
    ack_lines = []
    for key in ("ACKNOWLEDGMENT_1", "ACKNOWLEDGMENT_2", "ACKNOWLEDGMENT_3"):
        if v.get(key):
            ack_lines.append(f"- {v[key]}")

    ack_old = (
        "- [Organization/Person 1]\n"
        "- [Organization/Person 2]\n"
        "- [Organization/Person 3]"
    )
    ack_new = "\n".join(ack_lines) if ack_lines else "<!-- TODO: Add acknowledgments -->"
    content = sub(content, ack_old, ack_new)

    # OpenSSF badge ID
    badge_id = v.get("OPENSSF_BADGE_ID")
    if badge_id and badge_id.lower() != "none":
        content = sub(content, "XXXX", badge_id)

    return content


def process_contributing(content, v):
    content = sub(content, "[conduct email address]",
        val_or_todo(v.get("CONDUCT_EMAIL"), "conduct email address"))
    content = sub(content,
        "[Describe language-specific style guides, e.g., PEP 8 for Python, Google Style Guide for Go, etc.]",
        val_or_todo(v.get("STYLE_GUIDE"), "style guide"))
    content = sub(content,
        "[Describe any code formatting tools or configurations used, e.g., linters, formatters]",
        val_or_todo(v.get("FORMATTING_TOOL_DESCRIPTION"), "code formatting tools description"))
    content = sub(content, "[linting command]",
        val_or_todo(v.get("LINT_COMMAND"), "linting command"))
    content = sub(content, "[formatting command]",
        val_or_todo(v.get("FORMAT_COMMAND"), "formatting command"))
    content = sub(content, "[test command]",
        val_or_todo(v.get("TEST_COMMAND"), "test command"))
    content = sub(content, "[specific test command]",
        val_or_todo(v.get("SPECIFIC_TEST_COMMAND"), "specific test command"))
    content = sub(content, '[timeframe, e.g., "one week"]',
        val_or_todo(v.get("REVIEW_TIMEFRAME"), "review timeframe"))
    content = sub(content, "[chat platform and link]",
        val_or_todo(v.get("CHAT_CHANNEL_LINK"), "chat platform and link"))
    content = sub(content, "[mailing list link]",
        val_or_todo(v.get("MAILING_LIST_LINK"), "mailing list link"))
    return content


def process_governance(content, v):
    # Charter
    content = sub(content,
        "[Link to Technical Charter - do NOT copy the Technical Charter into this repository]",
        val_or_todo(v.get("CHARTER_LINK"), "Technical Charter URL"))

    # [number] replacements -- in document order, using sub_first for disambiguation:
    # 1. Voting period: "minimum of [number] business days to allow"
    content = sub_first(content,
        "minimum of [number] business days to allow",
        f"minimum of {val_or_todo(v.get('VOTING_PERIOD_DAYS'), 'voting period days')} business days to allow")
    # 2. Lazy consensus: "waiting period of [number] business days"
    content = sub_first(content,
        "waiting period of [number] business days",
        f"waiting period of {val_or_todo(v.get('LAZY_CONSENSUS_DAYS'), 'lazy consensus days')} business days")

    # TSC meeting details
    content = sub(content,
        '[frequency, e.g., "Bi-weekly on Wednesdays at 10:00 AM PT"]',
        val_or_todo(v.get("TSC_MEETING_FREQUENCY"), "TSC meeting frequency"))
    content = sub(content, "[calendar link]",
        val_or_todo(v.get("TSC_CALENDAR_LINK"), "TSC calendar link"))
    content = sub(content, "[meeting link]",
        val_or_todo(v.get("TSC_VIDEO_LINK"), "TSC video conference link"))
    content = sub(content, "[link to meeting notes repository or document]",
        val_or_todo(v.get("TSC_MEETING_NOTES_LINK"), "TSC meeting notes link"))

    # 3. Agenda lead hours: "at least [number] hours before each meeting"
    content = sub_first(content,
        "at least [number] hours before each meeting",
        f"at least {val_or_todo(v.get('AGENDA_LEAD_HOURS'), 'agenda lead hours')} hours before each meeting")
    # 4. Notes publish days: "within [number] business days after each meeting"
    content = sub_first(content,
        "within [number] business days after each meeting",
        f"within {val_or_todo(v.get('NOTES_PUBLISH_DAYS'), 'notes publish days')} business days after each meeting")
    # 5. Amendment discussion days: "minimum of [number] business days before voting"
    content = sub_first(content,
        "minimum of [number] business days before voting",
        f"minimum of {val_or_todo(v.get('AMENDMENT_DISCUSSION_DAYS'), 'amendment discussion days')} business days before voting")

    # Release process
    content = sub(content,
        "[Describe the release process or reference a RELEASE.md file]",
        val_or_todo(v.get("RELEASE_PROCESS_DESCRIPTION"), "release process description"))

    return content


def process_maintainers(content, maintainers, emeritus):
    # Build maintainer table rows
    if maintainers:
        rows = "\n".join(
            f"| {m['name']} | @{m['github']} | {m['org']} | {m['tz']} |"
            for m in maintainers
        )
    else:
        rows = "<!-- Add maintainers here -->"

    # The template has 3 identical placeholder rows
    template_block = (
        "| [Full Name] | @[github_handle] | [Organization or Independent] | [e.g., PT, ET, UTC] |\n"
        "| [Full Name] | @[github_handle] | [Organization or Independent] | [e.g., PT, ET, UTC] |\n"
        "| [Full Name] | @[github_handle] | [Organization or Independent] | [e.g., PT, ET, UTC] |"
    )
    content = sub(content, template_block, rows)

    # Emeritus table
    if emeritus:
        emeritus_rows = "\n".join(
            f"| {m['name']} | @{m['github']} | {m['org']} | {m['tenure']} |"
            for m in emeritus
        )
    else:
        emeritus_rows = "<!-- No emeritus members yet -->"

    content = sub(content,
        "| [Full Name] | @[github_handle] | [Organization or Independent] | [start date] - [end date] |",
        emeritus_rows)

    return content


def process_steering_committee(content, v, tsc_members, emeritus):
    # TSC members table (template has 3 rows)
    if tsc_members:
        rows = "\n".join(
            f"| {m['name']} | @{m['github']} | {m['org']} | {m['term_start']} | {m['term_end']} |"
            for m in tsc_members
        )
    else:
        rows = "<!-- Add TSC members here -->"

    template_block = (
        '| [Full Name] | @[github_handle] | [Organization or Independent] | [YYYY-MM-DD] | [YYYY-MM-DD or "Ongoing"] |\n'
        '| [Full Name] | @[github_handle] | [Organization or Independent] | [YYYY-MM-DD] | [YYYY-MM-DD or "Ongoing"] |\n'
        '| [Full Name] | @[github_handle] | [Organization or Independent] | [YYYY-MM-DD] | [YYYY-MM-DD or "Ongoing"] |'
    )
    content = sub(content, template_block, rows)

    # TSC Chair
    chair_name   = val_or_todo(v.get("TSC_CHAIR_NAME"),       "TSC Chair name")
    chair_github = val_or_todo(v.get("TSC_CHAIR_GITHUB"),     "TSC Chair GitHub handle")
    chair_start  = val_or_todo(v.get("TSC_CHAIR_TERM_START"), "chair term start date")
    chair_end    = val_or_todo(v.get("TSC_CHAIR_TERM_END"),   "chair term end date")

    content = sub(content,
        "**Current Chair:** [Name] (@[github_handle])",
        f"**Current Chair:** {chair_name} (@{chair_github})")
    content = sub(content,
        "**Chair Term:** [YYYY-MM-DD] to [YYYY-MM-DD]",
        f"**Chair Term:** {chair_start} to {chair_end}")

    # Election process -- nomination period [number] business days (first occurrence)
    content = sub_first(content,
        "[number] business days",
        f"{val_or_todo(v.get('TSC_NOMINATION_PERIOD_DAYS'), 'nomination period days')} business days")
    # Approval threshold (first [majority/two-thirds majority])
    content = sub_first(content,
        "[majority/two-thirds majority]",
        val_or_todo(v.get("TSC_APPROVAL_THRESHOLD"), "TSC approval threshold"))
    # Charter link
    content = sub(content, "[Link to Technical Charter]",
        val_or_todo(v.get("CHARTER_LINK"), "Technical Charter URL"))
    # Term years
    content = sub_first(content,
        "term of [number] years",
        f"term of {val_or_todo(v.get('TSC_TERM_YEARS'), 'TSC term years')} years")

    # Meeting section
    content = sub(content,
        '[frequency, e.g., "Bi-weekly on Wednesdays at 10:00 AM PT"]',
        val_or_todo(v.get("TSC_MEETING_FREQUENCY"), "TSC meeting frequency"))
    content = sub(content, "[calendar link]",
        val_or_todo(v.get("TSC_CALENDAR_LINK"), "TSC calendar link"))
    content = sub(content, "[meeting link]",
        val_or_todo(v.get("TSC_VIDEO_LINK"), "TSC video conference link"))
    content = sub(content, "[link to agenda document or repository]",
        val_or_todo(v.get("TSC_AGENDA_LINK"), "TSC agenda link"))
    content = sub(content, "[link to meeting notes]",
        val_or_todo(v.get("TSC_MEETING_NOTES_LINK"), "TSC meeting notes link"))
    content = sub(content,
        "at least [number] hours before each meeting",
        f"at least {val_or_todo(v.get('AGENDA_LEAD_HOURS'), 'agenda lead hours')} hours before each meeting")
    content = sub(content,
        "propose agenda items by [process]",
        f"propose agenda items by {val_or_todo(v.get('TSC_AGENDA_PROPOSAL_PROCESS'), 'agenda proposal process')}")
    content = sub(content,
        "within [number] business days",
        f"within {val_or_todo(v.get('NOTES_PUBLISH_DAYS'), 'notes publish days')} business days")
    content = sub(content, "[number or percentage]",
        val_or_todo(v.get("TSC_QUORUM"), "TSC quorum"))
    # Decision threshold (second [majority/two-thirds majority])
    content = sub(content,
        "[majority/two-thirds majority]",
        val_or_todo(v.get("TSC_DECISION_THRESHOLD"), "TSC decision threshold"))

    # Emeritus table
    if emeritus:
        emeritus_rows = "\n".join(
            f"| {m['name']} | @{m['github']} | {m['org']} | {m['tenure']} |"
            for m in emeritus
        )
    else:
        emeritus_rows = "<!-- No emeritus members yet -->"

    content = sub(content,
        "| [Full Name] | @[github_handle] | [Organization or Independent] | [start date] - [end date] |",
        emeritus_rows)

    # Contact section.
    # Use a regex for the same reason as the security email above: apply_global_subs()
    # has already replaced project_name inside the bracket, so the literal string
    # "[tsc@project_name.org]" no longer exists in the content at this point.
    content = re.sub(r'\[tsc@[^\]]+\.org\]',
        val_or_todo(v.get("TSC_MAILING_LIST_EMAIL"), "TSC mailing list email"),
        content)
    content = sub(content, "[chair email]",
        val_or_todo(v.get("TSC_CHAIR_EMAIL"), "TSC Chair email"))

    return content


def process_security(content, v):
    # Security email (appears twice: reporting and contact sections).
    # Use a regex rather than a literal string because apply_global_subs() has
    # already run, turning "[security@project_name.org]" into something like
    # "[security@My Project.org]" -- the project_name token is gone.
    security_email = val_or_todo(v.get("SECURITY_EMAIL"), "security email")
    content = re.sub(r'\[security@[^\]]+\.org\]', security_email, content)

    # Supported versions table
    versions = v.get("SUPPORTED_VERSIONS", [])
    if versions:
        ver_rows = "\n".join(
            f"| {ver['version']:<8} | {'[OK] Yes' if ver['supported'] else '[NO] No':<10} |"
            for ver in versions
        )
    else:
        ver_rows = "<!-- TODO: Add supported versions -->"

    old_ver_block = (
        "| x.x.x   | [OK] Yes    |\n"
        "| x.x.x   | [OK] Yes    |\n"
        "| < x.x.x | [NO] No     |"
    )
    content = sub(content, old_ver_block, ver_rows)

    # Announcements
    content = sub(content, "[link to mailing list or notification channel]",
        val_or_todo(v.get("SECURITY_ANNOUNCE_LINK"), "security announcements link"))
    # Same issue for the announcements email placeholder.
    content = re.sub(r'\[security-announce@[^\]]+\.org\]',
        val_or_todo(v.get("SECURITY_ANNOUNCE_EMAIL"), "security announcements email"),
        content)
    content = sub(content, "[communication channel]",
        val_or_todo(v.get("SECURITY_ANNOUNCE_CHANNEL"), "security announcements channel"))

    # Configuration notes
    content = sub(content,
        "[Document any security-related configuration options, hardening guides, or security features of the project]",
        val_or_todo(v.get("SECURITY_CONFIGURATION_NOTES"), "security configuration notes"))

    # PGP key
    content = sub(content, "[link to PGP key or key fingerprint]",
        val_or_todo(v.get("SECURITY_PGP_INFO"), "PGP key info"))

    return content


def process_agents(content, v):
    # Remove instructional text lines
    content = sub(content,
        "[Provide a brief description of the project's purpose that helps AI agents understand the context for their contributions.]",
        "")
    content = re.sub(
        r'\[Describe the high-level architecture and key components that AI agents should understand\.\]\s*\n',
        '', content)
    content = re.sub(
        r'\[Define important domain-specific concepts, terminology, and patterns used in the project\.\]\s*\n',
        '', content)
    content = re.sub(
        r'\[Describe specific patterns and practices AI agents should follow\.\]\s*\n',
        '', content)

    # Project description
    content = sub(content,
        "project_name is [description of what the project does, its goals, and its importance].",
        f"{v.get('PROJECT_NAME', 'This project')} is "
        f"{val_or_todo(v.get('PROJECT_DESCRIPTION'), 'project description')}.")

    # Architecture
    content = sub(content, "[List and briefly describe main components]",
        val_or_todo(v.get("CORE_COMPONENTS"), "core components description"))
    content = sub(content, "[Describe the organization of the codebase]",
        val_or_todo(v.get("DIRECTORY_STRUCTURE"), "directory structure description"))
    content = sub(content, "[List critical dependencies and their purposes]",
        val_or_todo(v.get("KEY_DEPENDENCIES"), "key dependencies"))

    # Key concepts
    concepts = v.get("KEY_CONCEPTS", [])
    if concepts:
        concept_lines = "\n".join(f"- **{term}**: {defn}" for term, defn in concepts)
    else:
        concept_lines = "<!-- TODO: Add key concepts (term: definition pairs) -->"

    old_concepts = (
        "- **[Concept 1]**: [Definition]\n"
        "- **[Concept 2]**: [Definition]\n"
        "- **[Concept 3]**: [Definition]"
    )
    content = sub(content, old_concepts, concept_lines)

    # Language and style
    content = sub(content, "[e.g., Python 3.10+, TypeScript 5.x]",
        val_or_todo(v.get("PRIMARY_LANGUAGES"), "primary languages"))
    content = sub(content, "[e.g., PEP 8, Google Style Guide, Airbnb JavaScript Style Guide]",
        val_or_todo(v.get("STYLE_GUIDE"), "style guide"))
    content = sub(content, "[e.g., black, prettier, gofmt]",
        val_or_todo(v.get("FORMATTING_TOOLS"), "formatting tools"))
    content = sub(content, "[e.g., pylint, eslint, golangci-lint]",
        val_or_todo(v.get("LINTING_TOOLS"), "linting tools"))

    # Code patterns
    patterns = v.get("CODE_PATTERNS", [])
    if patterns:
        pattern_lines = "\n".join(f"- **{p}**: {d}" for p, d in patterns)
    else:
        pattern_lines = "<!-- TODO: Add code patterns (pattern: description pairs) -->"

    old_patterns = (
        "- [Pattern 1]: [Description and example]\n"
        "- [Pattern 2]: [Description and example]\n"
        "- [Pattern 3]: [Description and example]"
    )
    content = sub(content, old_patterns, pattern_lines)

    # Docstring format
    content = sub(content,
        "[docstring format, e.g., Google style, NumPy style, JSDoc]",
        val_or_todo(v.get("DOCSTRING_FORMAT"), "docstring format"))

    # Naming conventions
    content = sub(content, "[e.g., snake_case.py, kebab-case.ts]",
        val_or_todo(v.get("NAMING_FILES"), "file naming convention"))
    content = sub(content, "[e.g., PascalCase]",
        val_or_todo(v.get("NAMING_CLASSES"), "class naming convention"))
    # Functions and Variables share the same example text -- replace first then second
    content = sub_first(content, "[e.g., snake_case, camelCase]",
        val_or_todo(v.get("NAMING_FUNCTIONS"), "function/method naming convention"))
    content = sub(content, "[e.g., snake_case, camelCase]",
        val_or_todo(v.get("NAMING_VARIABLES"), "variable naming convention"))
    content = sub(content, "[e.g., UPPER_SNAKE_CASE]",
        val_or_todo(v.get("NAMING_CONSTANTS"), "constants naming convention"))

    # Test commands
    content = sub(content, "[test command]",
        val_or_todo(v.get("TEST_COMMAND"), "test command"))
    content = sub(content, "[specific test command]",
        val_or_todo(v.get("SPECIFIC_TEST_COMMAND"), "specific test command"))
    content = sub(content, "[coverage command]",
        val_or_todo(v.get("COVERAGE_COMMAND"), "coverage command"))

    # Collapse excessive blank lines introduced by removed instructional lines
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content


# -----------------------------------------------------------------------------
# Verification
# -----------------------------------------------------------------------------

# Bracket placeholder patterns that are intentional (not unresolved template items)
INTENTIONAL_BRACKETS = {
    "Name or handle", "Brief description", "Date",
    "GOVERNANCE.md", "SECURITY.md", "CONTRIBUTING.md", "MAINTAINERS.md",
    "STEERING_COMMITTEE.md", "CODE_OF_CONDUCT.md", "ANTITRUST.md",
    "TRADEMARKS.md", "README.md", "LICENSE", "DCO", "RELEASES",
    "ARCHITECTURE.md", "DEVELOPMENT.md",
}

def verify_files(repo_dir):
    """
    Check all processed files for remaining unresolved placeholders.
    Returns a list of warning strings.
    """
    warnings = []
    for filename in TEMPLATE_FILES:
        path = repo_dir / filename
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8")

        if "project_name" in content:
            warnings.append(f"  [!]  {filename}: still contains literal 'project_name'")
        if "project_repo" in content:
            warnings.append(f"  [!]  {filename}: still contains literal 'project_repo'")
        if "x.x.x" in content:
            warnings.append(f"  [!]  {filename}: still contains 'x.x.x'")
        if "XXXX" in content:
            warnings.append(f"  [!]  {filename}: still contains 'XXXX'")
        if "@[github_handle]" in content:
            warnings.append(f"  [!]  {filename}: still contains '@[github_handle]'")
        if "[YYYY-MM-DD]" in content:
            warnings.append(f"  [!]  {filename}: still contains '[YYYY-MM-DD]'")

        # Look for unresolved bracket placeholders (not Markdown link syntax [text](url))
        candidates = re.findall(r'\[([^\]]+)\](?!\()', content)
        for c in candidates:
            if c not in INTENTIONAL_BRACKETS and not c.startswith("^") and len(c) > 2:
                # Heuristic: likely a placeholder if it looks like an instruction
                if re.search(r'(e\.g\.|Full Name|github_handle|Organization|YYYY|number|description|Definition|Pattern|Concept|list|link|email|command|format|process|frequency|calendar|meeting|version)', c, re.I):
                    warnings.append(f"  [!]  {filename}: possible unresolved placeholder: [{c}]")

    return warnings


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

def main():
    # Ensure stdout and stdin use UTF-8 on all platforms (including Windows,
    # which defaults to cp1252).  reconfigure() is available from Python 3.7+.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    if hasattr(sys.stdin, "reconfigure"):
        sys.stdin.reconfigure(encoding="utf-8")

    print("\n" + "#" * 62)
    print("  SETUP.py -- Project Repository Configuration")
    print("  Based on AGENTSETUP.md  |  LF Projects Template")
    print("#" * 62)

    # Locate the project-repo directory
    script_dir = Path(__file__).parent
    repo_dir = script_dir / "project-repo"
    if not repo_dir.exists():
        print(f"\n[NO]  ERROR: 'project-repo/' directory not found at:\n   {repo_dir}")
        print("   Run this script from the directory that contains project-repo/.")
        sys.exit(1)

    print(f"\n    Repo directory : {repo_dir}")
    print("  You will be prompted for values section by section.")
    print("  Optional fields can be skipped by pressing Enter.\n")

    # -- Collect ----------------------------------------------
    s1          = collect_section_1()
    s2          = collect_section_2()
    s3          = collect_section_3()
    s4          = collect_section_4()
    s5          = collect_section_5()
    s6          = collect_section_6()
    s7          = collect_section_7()
    s8          = collect_section_8()
    s9          = collect_section_9()
    tsc_members = collect_section_10()
    maintainers = collect_section_11()
    emeritus    = collect_section_12()
    s13         = collect_section_13()
    s14         = collect_section_14()
    s15         = collect_section_15()
    s16         = collect_section_16()
    s17         = collect_section_17()
    s18         = collect_section_18()

    # Merge all flat value dicts
    v = {}
    for d in [s1, s2, s3, s4, s5, s6, s7, s8, s9, s13, s14, s15, s16, s17, s18]:
        v.update(d)

    project_name = v["PROJECT_NAME"]
    project_repo = v["PROJECT_REPO"]

    # -- Process files -----------------------------------------
    print("\n" + "-" * 62)
    print("  Performing substitutions...")
    print("-" * 62)

    def process_file(filename, processor=None):
        path = repo_dir / filename
        if not path.exists():
            print(f"  -  {filename}  (file not found -- skipped)")
            return
        original = path.read_text(encoding="utf-8")
        # Step 1: global replacements
        content = apply_global_subs(original, project_name, project_repo)
        # Step 2: per-file replacements
        if processor:
            content = processor(content)
        path.write_text(content, encoding="utf-8")
        changed = content != original
        print(f"  {'[OK]' if changed else '- '}  {filename}")

    process_file("README.md",             lambda c: process_readme(c, v))
    process_file("CONTRIBUTING.md",       lambda c: process_contributing(c, v))
    process_file("GOVERNANCE.md",         lambda c: process_governance(c, v))
    process_file("MAINTAINERS.md",        lambda c: process_maintainers(c, maintainers, emeritus))
    process_file("STEERING_COMMITTEE.md", lambda c: process_steering_committee(c, v, tsc_members, emeritus))
    process_file("SECURITY.md",           lambda c: process_security(c, v))
    process_file("AGENTS.md",             lambda c: process_agents(c, v))

    for filename in NO_SUBSTITUTION_FILES:
        path = repo_dir / filename
        status = "- " if path.exists() else "? "
        print(f"  {status}  {filename}  (no substitutions needed)")

    # -- Verify ------------------------------------------------
    print("\n" + "-" * 62)
    print("  Running verification checks...")
    print("-" * 62)
    warnings = verify_files(repo_dir)
    if warnings:
        for w in warnings:
            print(w)
    else:
        print("  [OK]  All checks passed -- no unresolved placeholders detected.")

    # -- Summary -----------------------------------------------
    skipped_keys = [
        k for k, val in v.items()
        if val is None
        and k not in ("KEY_CONCEPTS", "CODE_PATTERNS", "SUPPORTED_VERSIONS")
    ]
    set_count = sum(1 for val in v.values() if val is not None)

    print("\n" + "=" * 62)
    print("  SETUP COMPLETE")
    print("=" * 62)
    print(f"  Files processed      : {len(TEMPLATE_FILES)}")
    print(f"  Variables set        : {set_count}")
    print(f"  Variables skipped    : {len(skipped_keys)}")
    if skipped_keys:
        for k in skipped_keys:
            print(f"    - {k}")
    if warnings:
        print(f"\n  [!]  {len(warnings)} verification warning(s) -- review output above.")
    print()
    print("    Reminders:")
    print("      * Supply a LICENSE file separately -- it is not templated.")
    print("      * The DCO file requires no configuration.")
    print("      * Delete or archive AGENTSETUP.md and SETUP.py after setup.")
    print("      * Review all files manually before publishing.\n")


if __name__ == "__main__":
    main()
