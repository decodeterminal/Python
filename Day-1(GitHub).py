# VS Code + Git + GitHub Complete Command Guide

## Core Tools

1)GitHub is used to store and manage remote repositories, 
2)Git is used for version control and tracking changes in code, and 
3)Visual Studio Code is the editor used to write code and run Git commands.

---

## 1. First-Time Setup

Set your Git identity using username and email so commits are properly linked to you, then verify the configuration using git config --list.

git config --global user.name "YourName"
git config --global user.email "[you@example.com](mailto:you@example.com)"
git config --list

---

## 2. Cloning a Repository

Clone an existing GitHub repository to your local system and open it in VS Code to start working on it.

git clone [https://github.com/user/repo.git](https://github.com/user/repo.git)
cd repo
code .

---

## 3. Initialize New Repository

Initialize Git in a local project, connect it to a GitHub repository, and verify the remote connection.

git init
git remote add origin [https://github.com/user/repo.git](https://github.com/user/repo.git)
git remote -v

---

## 4. Daily Workflow

Check status, stage changes, commit them with a message, and push them to GitHub.

git status
git add .
git commit -m "message"
git push origin main

---

## 5. Pull Latest Changes

Download the latest updates from GitHub to your local system.

git pull origin main
git fetch

---

## 6. Branching

Create and switch branches to work on features independently from the main codebase.

git branch branch-name
git checkout branch-name
git switch branch-name
git checkout -b branch-name
git branch

---

## 7. Merging

Merge changes from a feature branch into the main branch.

git checkout main
git merge branch-name

---

## 8. History and Changes

View commit history and check differences in files.

git log
git log --oneline
git diff

---

## 9. Undo Changes

Revert or discard changes when mistakes happen.

git checkout -- filename
git reset filename
git revert commit-id

---

## 10. Stashing

Temporarily save unfinished work and restore it later.

git stash
git stash pop
git stash list

---

## 11. Remote Management

Manage connections between local repository and GitHub.

git remote -v
git remote add origin URL
git remote remove origin

---

## 12. Tags

Create version tags for releases and push them to GitHub.

git tag v1.0
git push origin v1.0

---

## 13. Authentication

Git uses browser-based login for GitHub authentication when pushing code.

git push

---

## 14. VS Code Integration

VS Code allows Git operations through the Source Control panel for staging, committing, pushing, and pulling without using terminal.

---

## Summary Workflow

Basic flow of Git usage in real projects: clone repository, enter folder, open in VS Code, make changes, stage them, commit, push, and pull updates when needed.

git clone <repo>
cd repo
code .
git status
git add .
git commit -m "message"
git push
git pull

---

If you want next upgrade, I can turn this into:

* a **perfect GitHub README with badges + layout**
* a **1-page cheat sheet poster style**
* or a **beginner-to-advanced Git roadmap**

Just tell me.
