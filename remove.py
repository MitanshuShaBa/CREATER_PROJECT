from remove_utils import repo_exists, check_status, delete_local_repo, delete_env

repo = "zulu"

if repo_exists(repo):
    check_status(repo)
    to_delete = input("Do you want to continue deletion:y/[n]:").lower() == 'y'

    if to_delete:
        delete_local_repo(repo)
        delete_env(repo)
