import os


def repo_exists(repo):
    os.chdir(f"D:\\MyProjects\\Python Projects")
    return os.path.isdir(repo)


def check_status(repo):
    os.chdir(f"D:\\MyProjects\\Python Projects\\{repo}")
    os.system("git status")
    os.chdir(f"D:\\MyProjects\\Python Projects")


def delete_local_repo(repo):
    os.chdir("D:\\MyProjects\\Python Projects")
    os.system(f"RD /S /Q {repo}")


def delete_env(repo):
    os.system(f"conda remove --name {repo} --all --yes")
