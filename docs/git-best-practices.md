# Git Best Practices Cheatsheet

## Commit Messages
- **Imperative mood**: "Fix login bug" not "Fixed login bug"
- **Short subject line**: <50 characters
- **Blank line after subject**, then detailed body if needed
- **Reference issues**: "Closes #42" or "Related to #7"

## Branching
- **Main branch**: `main` or `master` should always be deployable
- **Feature branches**: `feature/description` or `feat/description`
- **Bugfix branches**: `fix/description`
- **Delete after merge**: `git branch -d branch-name`

## Commits
- **Atomic commits**: One logical change per commit
- **Don't commit**: generated files, binaries, secrets, or dependencies (use .gitignore)
- **Commit often**: small, frequent commits are easier to review and revert

## Pull Requests
- **Keep PRs small**: focused on a single feature/fix
- **Write a clear title and description**: explain what and why
- **Request reviews** from relevant teammates
- **Squash and merge** for feature branches to keep history clean

## Useful Commands
```bash
# Interactive rebase to clean up commits
git rebase -i HEAD~n

# Stash unfinished work
git stash
git stash pop

# Undo last commit but keep changes
git reset --soft HEAD~1

# See log in one line per commit
git log --oneline --graph
```

## Resources
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)