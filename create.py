import os
import sys

from github import Github
from custom import customise, custom_path

if len(sys.argv) != 3:
    print("Enter the software and project name")
    exit(1)
software = sys.argv[1]
repo_name = sys.argv[2]  # TODO make repo name work with space in the name

print("Creating project...")
softwares = ["py", "python"]

# Github auth and creation of repo
g = Github(login_or_token=os.getenv("GITHUB_REPO_TOKEN"))
user = g.get_user()
login = user.login
repos = [repo.name for repo in user.get_repos()]
created_repo = False

if repo_name not in repos:
    user.create_repo(repo_name)
    created_repo = True

if login and created_repo:
    # Create directory according to the software
    custom_path(software, repo_name)

    # Create README
    with open("README.md", "w") as f:
        f.write(f"# {repo_name}")

    # Git commands
    commands = ['git init',
                f'git remote add origin https://github.com/{login}/{repo_name}.git',
                'git add .',
                'git commit -m "Initial commit"',
                'git push -u origin master']
    for command in commands:
        os.system(command)

    # Add software requirements
    customise(software, repo_name)

else:
    print("\n\nName was taken")
