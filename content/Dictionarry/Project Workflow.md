# Filters

| Qualifier  | Possible values                        | Description                                                                                     | Example/Use Case |
| ---------- | -------------------------------------- | ----------------------------------------------------------------------------------------------- | ---------------- |
| `is`       | open, closed, merged, draft, issue, pr | Filters by item state or type. E.g., `is:open` for open issues/PRs, `is:issue` for only issues. | `is:open is:pr` to find all open pull requests |
| `label`    | "label name"                           | Filters by the presence of a specific label. Use quotes for multi-word labels.                  | `label:"high priority"` to find all high priority items |
| `reason`   | completed, reopened, "not planned"     | Filters by the reason an issue was closed or reopened.                                          | `reason:"not planned"` to find issues marked as not planned |
| `assignee` | GitHub username                        | Filters by the assigned user.                                                                   | `assignee:johndoe` to find all items assigned to user johndoe |
| `no`       | label, assignee, reason                | Filters for items lacking a label, assignee, or close/reopen reason.                            | `no:assignee` to find all unassigned items |

Note: You can combine these filters. For example: `is:open label:bug no:assignee` would find all open, unassigned bug reports.
# Issue Types
| Type            | Description                                           | Example/Use Case                                              |
| --------------- | ----------------------------------------------------- | ------------------------------------------------------------- |
| Bug             | An error, flaw, or fault in the system                | A user reports that the export function crashes unexpectedly  |
| Feature Request | A new capability or functionality suggestion          | A user suggests adding dark mode to the UI                    |
| Improvement     | An enhancement to existing features                   | Proposal to optimize the database query performance           |
| Documentation   | Updates or additions to project documentation         | Request to add installation instructions for Linux users      |
| Refactor        | Code restructuring without changing external behavior | Suggestion to improve code modularity in a specific component |
| Infrastructure  | Changes to project infrastructure or build processes  | Proposal to switch from Travis CI to GitHub Actions           |

# Components
| Type      | Description                        | Url                                          |
| --------- | ---------------------------------- | -------------------------------------------- |
| Profilarr | The main application               | https://github.com/Dictionarry-Hub/profilarr |
| Website   | The project's web presence         | https://github.com/Dictionarry-Hub/website   |
| Database  | Data storage and management        | https://github.com/Dictionarry-Hub/database  |
| Docs      | Project documentation              | https://github.com/Dictionarry-Hub/docs      |
| Discord   | Community chat platform            | https://discord.gg/ZxywYBGRB9                |
| GitHub    | Version control and issue tracking | https://github.com/Dictionarry-Hub/.github   |
