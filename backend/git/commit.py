# git_worker.py
import sys
import subprocess

repo_path = "/chemin/vers/votre/repo"
file_path = sys.argv[1]
message = sys.argv[2]

subprocess.run(["git", "add", file_path], cwd=repo_path, check=True)
subprocess.run(["git", "commit", "-m", message], cwd=repo_path, check=True)