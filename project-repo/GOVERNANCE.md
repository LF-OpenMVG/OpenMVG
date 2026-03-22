# Governance

This document describes the governance model for project_name. This is a consensus-based community project governed by a Technical Steering Committee (TSC).

## Technical Charter

This project operates under the [project_name Technical Charter][charter-link], which establishes the legal framework and foundation-level governance for the project.

[charter-link]: [Link to Technical Charter - do NOT copy the Technical Charter into this repository]

## Community Roles

The project_name community consists of the following roles:

### Contributors

Contributors are individuals who have contributed to the project in any way, including but not limited to:

- Submitting code, documentation, or other content via pull requests
- Reporting bugs or suggesting features via issues
- Participating in discussions and providing feedback
- Helping other community members

Anyone can become a contributor by making a contribution to the project. All contributions must comply with the project's [DCO](DCO) requirements.

### Maintainers

Maintainers are contributors who have demonstrated sustained commitment to the project and have been granted write access to the repository. Maintainers are responsible for:

- Reviewing and merging pull requests
- Triaging issues
- Guiding the technical direction of the project
- Mentoring contributors
- Ensuring the project adheres to its Code of Conduct

The current list of maintainers is maintained in the [MAINTAINERS.md](MAINTAINERS.md) file.

#### Becoming a Maintainer

Contributors may be nominated to become maintainers based on:

- Sustained, high-quality contributions over time
- Demonstrated understanding of the project's codebase and goals
- Active participation in code reviews and community discussions
- Commitment to the project's Code of Conduct

The process for becoming a maintainer is documented in [MAINTAINERS.md](MAINTAINERS.md).

### Technical Steering Committee (TSC) Members

The TSC is responsible for the overall technical direction, governance, and decision-making for the project. TSC members are elected from and by the maintainer community.

TSC responsibilities include:

- Setting the technical vision and roadmap for the project
- Resolving technical disputes that cannot be resolved by maintainers
- Approving changes to governance documents
- Managing project releases
- Representing the project to the Linux Foundation and external parties
- Ensuring the project's long-term health and sustainability

The current list of TSC members is maintained in the [STEERING_COMMITTEE.md](STEERING_COMMITTEE.md) file.

## Current Leadership

### Technical Steering Committee

See [STEERING_COMMITTEE.md](STEERING_COMMITTEE.md) for the current list of TSC members.

### Maintainers

See [MAINTAINERS.md](MAINTAINERS.md) for the current list of maintainers.

## Decision-Making Process

This project uses a consensus-seeking decision-making model. Most decisions are made through informal consensus among contributors and maintainers through discussion in issues, pull requests, and community channels.

### Consensus-Based Decisions

For most decisions:

1. A proposal is made via an issue, pull request, or discussion.
2. Community members discuss the proposal and provide feedback.
3. The proposal is refined based on feedback.
4. If no objections remain, the decision is adopted.

Maintainers are responsible for determining when consensus has been reached.

### Voting

When consensus cannot be reached, or for significant decisions, voting may be used:

#### Types of Votes

| Decision Type | Voters | Approval Threshold |
|---------------|--------|-------------------|
| Code/documentation changes | Maintainers | Approval by at least one maintainer with no objections |
| New maintainer | Maintainers | Two-thirds majority of TSC |
| Remove maintainer | TSC | Two-thirds majority of TSC |
| New TSC member | TSC | Quorum of TSC as defined in Technical Charter |
| Remove TSC member | TSC | Two-thirds majority of TSC |
| Governance changes | TSC | Two-thirds majority of TSC |
| Technical Charter amendments | TSC | Two-thirds majority of TSC |

#### Voting Process

1. A vote is initiated by a maintainer or TSC member opening an issue or pull request with the `vote` label.
2. The voting period is a minimum of [number] business days to allow all eligible voters to participate.
3. Votes are cast by commenting on the issue or pull request with `+1` (approve), `-1` (reject), or `0` (abstain).
4. Votes must be documented in the issue, pull request, or TSC meeting notes.
5. The outcome is determined based on the approval threshold for the decision type.

#### Quorum

Quorum for votes is defined in the project's [Technical Charter][charter-link]. Unless otherwise specified, quorum is a majority of eligible voters.

### Lazy Consensus

For routine decisions, the project uses lazy consensus:

1. A proposal is made with a clear statement that lazy consensus is being used.
2. A waiting period of [number] business days is observed.
3. If no objections are raised, the proposal is adopted.
4. Any objection moves the decision to the standard consensus or voting process.

## Project Policies

### Code of Conduct

All community members must adhere to the project's [Code of Conduct](CODE_OF_CONDUCT.md). Violations may result in removal from the project.

### Contribution Requirements

All contributions must:

- Be submitted under the project's [LICENSE](LICENSE)
- Include a DCO sign-off (see [DCO](DCO) and [CONTRIBUTING.md](CONTRIBUTING.md))
- Follow the project's coding standards and guidelines
- Pass all automated tests and checks

### Security Policy

Security vulnerabilities must be reported according to the [SECURITY.md](SECURITY.md) policy.

### Trademark Policy

Use of project trademarks is governed by the [TRADEMARKS.md](TRADEMARKS.md) policy.

### Antitrust Policy

All participants agree to comply with applicable antitrust and competition laws. See [ANTITRUST.md](ANTITRUST.md).

### Release Process

[Describe the release process or reference a RELEASE.md file]

Releases are approved by the TSC and follow semantic versioning. The release process includes:

1. Release candidate preparation by maintainers
2. Community testing period
3. TSC approval
4. Release publication

## TSC Meetings

The TSC meets regularly to discuss project matters.

**Meeting Schedule:** [frequency, e.g., "Bi-weekly on Wednesdays at 10:00 AM PT"]

**Calendar:** [calendar link]

**Video Conference:** [meeting link]

**Meeting Agendas and Notes:** [link to meeting notes repository or document]

All community members are welcome to attend TSC meetings. Only TSC members may vote on TSC matters.

### Meeting Conduct

- Meetings follow the project's Code of Conduct
- An agenda is published at least [number] hours before each meeting
- Meeting notes are published within [number] business days after each meeting
- Decisions made in meetings must be documented

## Amendments

This governance document may be amended by a two-thirds majority vote of the TSC. Proposed amendments must be submitted as a pull request and discussed for a minimum of [number] business days before voting.

---

*This governance model is designed to be lightweight and to grow with the project. It is subject to change as the project evolves.*

