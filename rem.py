import os
import subprocess
from datetime import datetime


def stash_changes():
    # Run git stash command to stash any local modifications
    subprocess.run(['git', 'stash'])


def apply_stash():
    # Run git stash apply command to apply the stashed changes back
    subprocess.run(['git', 'stash', 'apply'])


def remove_remote_origin():
    # Run git remote remove origin command to remove the remote origin
    subprocess.run(['git', 'remote', 'remove', 'origin'])


def remove_signature_author():
    # Get the current working directory
    current_dir = os.getcwd()

    # Change directory to the root of the Git repository
    os.chdir(current_dir)

    # Get current date and time
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

    # Run git filter-branch command to remove signatures/authors and set current date and time
    subprocess.run([
        'git',
        'filter-branch',
        '--force',  # Force overwriting existing backups
        '--env-filter',
        f'export GIT_COMMITTER_NAME="Sachin"; '
        f'export GIT_AUTHOR_NAME="Sachin"; '
        f'export GIT_COMMITTER_EMAIL="schnaror@gmail.com"; '
        f'export GIT_AUTHOR_EMAIL="schnaror@gmail.com"; '
        f'export GIT_COMMITTER_DATE="{date_time}"; '
        f'export GIT_AUTHOR_DATE="{date_time}"'
    ])


if __name__ == "__main__":
    # Check if rem.py is modified
    with open('rem.py', 'r') as file:
        file_contents = file.read()
        if 'WIP on master' in file_contents:
            print("Please commit or discard changes in rem.py before running the script.")
            exit(1)

    stash_changes()  # Stash any local modifications
    remove_remote_origin()  # Remove the remote origin
    remove_signature_author()  # Remove signatures/authors and set commit dates
    apply_stash()  # Apply the stashed changes back
