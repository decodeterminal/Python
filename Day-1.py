To clone your GitHub repository into Visual Studio Code for the first time:

## 1. Copy the repository URL from GitHub

Open your repo:

[Your GitHub Repository](https://github.com/decodeterminal/Python?utm_source=chatgpt.com)

Click the green Code button → copy the HTTPS URL.

It looks like:


https://github.com/decodeterminal/Python.git


## 2. Open VS Code

Open VS Code.

Then open terminal:


## 3. Go to the folder where you want the project

Example:

cd Desktop



## 4. Clone the repository

Run:
example:
git clone https://github.com/decodeterminal/Python.git


Git will create a new folder named Python.



## 5. Open the project in VS Code


cd Python
code .


Now the GitHub project is connected locally.



## 6. Make changes and push later

After editing files:


after cloning, to push changes:
1)git status
2)git add .
3)git commit -m "updated code"
4)git push



When you do:

git clone https://github.com/username/repo.git

or later:

git push

Git will automatically open a browser window and ask you to log in to GitHub.

👉 You just:

Sign in
Click “Authorize”
Done

No passwords needed.


## Difference between `git init` and `git clone`

* git init → create a brand new Git repository locally
* git clone → download an existing GitHub repository

Since your repo already exists on GitHub, normally you use:


git clone

not git init

Official docs:

* [GitHub Docs – Cloning a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository?utm_source=chatgpt.com)
* [VS Code Git documentation](https://code.visualstudio.com/docs/sourcecontrol/overview?utm_source=chatgpt.com)