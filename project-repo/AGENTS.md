# AI Agent Guidelines

This document provides guidance for AI agents, large language models (LLMs), and AI-assisted development tools interacting with the project_name repository. These guidelines ensure that AI-generated contributions meet the project's quality, security, and compliance standards.

## Project Context

### Overview

[Provide a brief description of the project's purpose that helps AI agents understand the context for their contributions.]

project_name is [description of what the project does, its goals, and its importance].

### Architecture

[Describe the high-level architecture and key components that AI agents should understand.]

- **Core components**: [List and briefly describe main components]
- **Directory structure**: [Describe the organization of the codebase]
- **Key dependencies**: [List critical dependencies and their purposes]

### Key Concepts

[Define important domain-specific concepts, terminology, and patterns used in the project.]

- **[Concept 1]**: [Definition]
- **[Concept 2]**: [Definition]
- **[Concept 3]**: [Definition]

## Coding Conventions

AI agents MUST follow these coding conventions when generating code for this project:

### Language and Style

- **Primary language(s)**: [e.g., Python 3.10+, TypeScript 5.x]
- **Style guide**: [e.g., PEP 8, Google Style Guide, Airbnb JavaScript Style Guide]
- **Formatting tools**: [e.g., black, prettier, gofmt]
- **Linting tools**: [e.g., pylint, eslint, golangci-lint]

### Code Patterns

[Describe specific patterns and practices AI agents should follow.]

- [Pattern 1]: [Description and example]
- [Pattern 2]: [Description and example]
- [Pattern 3]: [Description and example]

### Documentation Standards

- All public functions and classes MUST have docstrings/comments
- Use [docstring format, e.g., Google style, NumPy style, JSDoc]
- Include type hints/annotations where applicable
- Update relevant documentation when changing functionality

### Naming Conventions

- **Files**: [e.g., snake_case.py, kebab-case.ts]
- **Classes**: [e.g., PascalCase]
- **Functions/Methods**: [e.g., snake_case, camelCase]
- **Variables**: [e.g., snake_case, camelCase]
- **Constants**: [e.g., UPPER_SNAKE_CASE]

## Contribution Guidelines for AI Agents

### General Requirements

AI-generated contributions are welcome and MUST meet the same standards as human contributions:

1. **DCO Compliance**: All commits MUST include a valid `Signed-off-by` line. The human operator of the AI agent is responsible for the DCO sign-off.

2. **Disclosure**: Pull requests containing AI-generated code SHOULD disclose this in the PR description, including the AI tool used.

3. **Human Review**: All AI-generated contributions MUST be reviewed by a human maintainer before merging.

4. **Testing**: AI-generated code MUST include appropriate tests and pass all existing tests.

5. **License Compliance**: AI agents MUST NOT introduce code that violates the project's license or includes incompatibly licensed dependencies.

### Contribution Workflow

1. **Understand the task**: Review relevant issues, documentation, and existing code before generating changes.

2. **Make focused changes**: Keep contributions small and focused on a single issue or feature.

3. **Follow existing patterns**: Match the style and patterns of the surrounding code.

4. **Include tests**: Write tests for new functionality and ensure existing tests pass.

5. **Update documentation**: Update or create documentation as needed.

6. **Self-review**: Review generated code for errors, security issues, and adherence to guidelines before submission.

### Commit Messages

AI agents SHOULD follow this commit message format:

```
<type>(<scope>): <short summary>

<detailed description if needed>

Signed-off-by: Human Operator Name <email@example.com>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

## Prohibited Actions

AI agents MUST NOT:

- **Modify governance files** without explicit human instruction: GOVERNANCE.md, STEERING_COMMITTEE.md, MAINTAINERS.md, CODE_OF_CONDUCT.md, LICENSE, DCO
- **Bypass security controls**: Do not disable security checks, remove authentication, or weaken access controls
- **Introduce breaking changes** without explicit approval and documentation
- **Remove or weaken tests**: Do not delete tests or reduce test coverage without justification
- **Add dependencies** without security review and license verification
- **Access secrets or credentials**: Do not hardcode, log, or expose sensitive information
- **Ignore CI/CD failures**: Do not submit code that fails automated checks
- **Make changes outside the scope** of the assigned task
- **Generate code from memory** that may be copied from copyrighted sources without proper attribution

## Security Requirements

AI agents MUST follow these security practices:

- **Input validation**: Validate and sanitize all inputs
- **No hardcoded secrets**: Never include API keys, passwords, or tokens in code
- **Secure dependencies**: Only add well-maintained dependencies with no known critical vulnerabilities
- **Follow OWASP guidelines**: Adhere to OWASP best practices for web applications
- **Report vulnerabilities**: If a security issue is discovered, follow the [SECURITY.md](SECURITY.md) reporting process

### Security Review Checklist

Before submitting, AI agents SHOULD verify:

- [ ] No sensitive data is logged or exposed
- [ ] Input validation is implemented
- [ ] Authentication and authorization are properly enforced
- [ ] Dependencies are from trusted sources
- [ ] No SQL injection, XSS, or other common vulnerabilities
- [ ] Error messages do not leak sensitive information

## Testing Requirements

AI-generated code MUST meet these testing standards:

- **Unit tests**: New functions and classes require unit tests
- **Integration tests**: Changes affecting multiple components require integration tests
- **Test coverage**: Maintain or improve existing test coverage
- **Test quality**: Tests should be meaningful, not just coverage padding

### Running Tests

```bash
# Run all tests
[test command]

# Run specific tests
[specific test command]

# Check coverage
[coverage command]
```

## Human Oversight

### Required Human Actions

The following actions REQUIRE human oversight and cannot be performed autonomously by AI agents:

- Merging pull requests
- Approving dependency updates with security implications
- Making releases
- Modifying access controls or permissions
- Responding to security incidents
- Making governance decisions
- Signing off on DCO compliance

### Escalation

AI agents SHOULD escalate to human maintainers when:

- The task is ambiguous or unclear
- The change may have significant impact
- Security concerns are identified
- The change conflicts with existing code or patterns
- Tests fail unexpectedly
- The scope of changes exceeds the original request

## Context Files

AI agents SHOULD review these files before contributing:

- [README.md](README.md) - Project overview and setup
- [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
- [GOVERNANCE.md](GOVERNANCE.md) - Project governance
- [SECURITY.md](SECURITY.md) - Security policies
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - Community standards
- [ARCHITECTURE.md](ARCHITECTURE.md) - System architecture (if available)
- [DEVELOPMENT.md](DEVELOPMENT.md) - Development setup (if available)

## Feedback and Improvements

If you are an AI agent developer or operator and have suggestions for improving these guidelines, please open an issue or submit a pull request to update this document.

---

*This document is maintained by the project_name community and is subject to change. AI agents should check for updates before each contribution session.*
