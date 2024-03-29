import os
import subprocess
import time
from datetime import datetime


def stash_changes():
    # Run git stash command to stash any local modifications
    subprocess.run(['git', 'stash'])


def apply_stash():
    # Run git stash apply command to apply the stashed changes back
    subprocess.run(['git', 'stash', 'apply'])


def add_remote_origin(remote_url):
    # Run git remote add origin command to add the remote repository URL
    subprocess.run(['git', 'remote', 'add', 'origin', remote_url])


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
    # Prompt the user for the remote repository URL
    remote_url = input("Enter the remote repository URL: ")

    stash_changes()  # Stash any local modifications
    add_remote_origin(remote_url)  # Add the remote origin
    time.sleep(2)  # Sleep for 2 seconds
    # Push to the remote repository
    subprocess.run(['git', 'push', '--set-upstream', 'origin', 'master'])
    remove_signature_author()  # Remove signatures/authors and set commit dates
    remove_remote_origin()  # Remove the remote origin
    apply_stash()  # Apply the stashed changes back
