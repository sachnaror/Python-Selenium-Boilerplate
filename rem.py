
import os
import subprocess
from datetime import datetime


def remove_signature_author():
    # Get the current working directory
    current_dir = os.getcwd()

    # Change directory to the root of the Git repository
    os.chdir(current_dir)

    # Get current date and time
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")

  # Run git filter-branch command to remove signatures/authors
    subprocess.run([
        'git',
        'filter-branch',
        '--env-filter',
        'export GIT_COMMITTER_NAME="Sachin"; '
        'export GIT_AUTHOR_NAME="Sachin"; '
        'export GIT_COMMITTER_EMAIL="schnaror@gmail.com"; '
        'export GIT_AUTHOR_EMAIL="schnaror@gmail.com"'
    ])


if __name__ == "__main__":
    remove_signature_author()
