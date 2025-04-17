A good workflow is a simple workflow. This document explains how we write and review code, focusing only on what matters.

## Weekly Sprint

Our development cycle follows weekly sprints - short, focused periods of development that emphasize transparency and shared ownership. Every Friday we will:

1. Review Tasks - Review code and research from the previous week's sprint (come prepared to explain your work)
2. Merge Code - Collectively merge pull requests into develop - as a team, we'll evaluate task completion and merge readiness
3. Plan the next Sprint - Discuss and assign next week's tasks, address blockers

## Daily Scrum

Since this isn't a full-time commitment for everyone, we won't require daily scrums. However, if you encounter blockers or need help, communicate this before the next sprint so we can finish those tasks on time. 

## Trunk Based Development

We maintain a single 'develop' branch containing our working code. For simplicity, we skip main, beta, QA, or release branches. When you work on a task, you:

1. Branch off develop into a feature branch
2. Make your changes
3. Submit a pull request to merge back into develop

### Branching Off

- Every ticket you work on constitutes a new branch (no matter how small it is). Even if no code is required, still branch off and maintain documentation for whatever you worked on.
- Use the `<ticket>-<description>` format for branch names
- Always branch from develop

### Making Changes

- Work in whatever way suits you best
- Make as many or as few commits as needed
- You have full autonomy over your code

### Pull Requests

- While branch commits are flexible, pull requests must follow our formatting standards
- PR title format: `<type>(<scope>): <brief description>`
- Include a detailed description of changes
- This approach lets us document changes once comprehensively, rather than through individual commit messages

| Type     | Usage              | Example                            |
| -------- | ------------------ | ---------------------------------- |
| feat     | New features       | `feat(auth): add login component`  |
| tweak    | Minor adjustments  | `tweak(ui): adjust button padding` |
| fix      | Bug fixes          | `fix(api): resolve timeout issue`  |
| refactor | Code restructuring | `refactor(db): optimize queries`   |
| docs     | Documentation      | `docs(readme): update setup guide` |
| style    | Formatting changes | `style(css): normalize spacing`    |
| test     | Testing changes    | `test(unit): add user tests`       |
| chore    | Maintenance        | `chore(deps): update packages`     |

### Merge Strategy

During Friday meetings, we:

- Squash and merge changes (individual commits combine into one clean commit)
- Tag changes using semantic versioning for the sprint's combined work

|Type|When to Use|Example|
|---|---|---|
|Major (x.0.0)|Breaking changes|API changes, major UI overhaul|
|Minor (0.x.0)|New features|New component, additional endpoint|
|Fix (0.0.x)|Bug fixes, minor updates|Typo fix, small bug resolution|



