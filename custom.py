import os


def custom_path(software, repo_name):
    if software == "python" or software == "py":
        os.chdir("D:\\MyProjects\\Python Projects")
    else:
        os.chdir("D:\\MyProjects\\General Projects")

    os.mkdir(repo_name)
    os.chdir(os.path.join(os.getcwd(), repo_name))


def customise(software, repo_name):
    if software == "python" or software == "py":
        os.system(f"conda create -n {repo_name} python=3.6")
        os.system("pycharm64.exe .")
    else:
        os.system("code .")


if __name__ == "__main__":
    customise("py", "autotest")
