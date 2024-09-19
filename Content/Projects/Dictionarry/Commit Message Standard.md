All commit messages must adhere to the following standard:

```
<type>(<scope>): <subject>

<body>

<footer>
```
## Fields

- `<type>`: Indicates the type of commit. Allowed values:
  - `feat`, `feature`, `new`: A new feature
  - `fix`, `bugfix`, `bug`: A bug fix
  - `docs`, `documentation`, `doc`: Documentation only changes
  - `style`, `formatting`, `format`, `lint`: Changes that do not affect the meaning of the code (white-space, formatting, etc)
  - `refactor`, `refactoring`, `restructure`, `redesign`: A code change that neither fixes a bug nor adds a feature
  - `perf`, `performance`, `optimize`, `optimisation`: A code change that improves performance
  - `test`, `testing`: Adding missing tests or correcting existing tests
  - `chore`, `maintenance`, `maintain`: Other changes that don't modify src or test files

- `<scope>`: Indicates the scope of the commit. Allowed values:
  - `regex`: Changes related to regex patterns
  - `format`: Changes related to custom formats
  - `profile`: Changes related to quality profiles

- `<subject>`: A succinct description of the change
  - Use imperative mood (e.g., "Add" instead of "Added")
  - Capitalize the first letter
  - No period at the end
  - Keep it under 50 characters

- `<body>`: (Optional) A more detailed explanatory text, if necessary
  - Wrap it to about 72 characters
  - Use the body to explain the what and why of the commit, not the how
  - If your explanation spans multiple lines, start each line with a single hyphen (-) followed by a space
  - Hyphens create a bulleted list, making the body easier to read
  - Aim for concise, clear explanations
  - The body should provide additional contextual information about the code changes
  - If the commit addresses a specific issue or pull request, mention it in the body
  - If you need to mention a specific file or directory, wrap it in backticks (`)

- `<footer>`: (Optional) References to issues, pull requests, etc.

## Examples

```
feat(format): Add new custom format for phone numbers

- Implemented a new custom format for validating phone numbers
- Supports various international phone number formats
- Includes options for formatting output for display

Resolves #456
```

```
fix(regex): Correct issue with email validation regex

- The previous regex incorrectly allowed certain invalid email formats
- Updated the regex to be more strict and align with RFC standards
- Added additional test cases to cover the fixed scenarios

Fixes #789
```

```
refactor(profile): Improve readability and efficiency of quality profiles

- Restructured the quality profile module to follow SOLID principles
- Extracted reusable validation logic into separate functions
- Improved naming conventions for variables and functions
- Removed redundant code and simplified complex logic

Relates to #234
```

```
docs(readme): Update README with new installation instructions

- Added detailed steps for installing and configuring the application
- Included prerequisites and system requirements
- Provided examples of common setup scenarios
- Restructured the document to be more user-friendly

See also: #567
```

```
perf(regex): Optimize regex matching for large datasets

- Refactored regex matching logic to improve performance on large datasets
- Implemented lazy matching where possible to reduce unnecessary backtracking
- Added caching mechanism to avoid repeated matching on the same input
- Verified performance improvements through benchmarking tests

Resolves #890
```
