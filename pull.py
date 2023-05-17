from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

# Create a GitHub API instance
g = Github(os.getenv('GITHUB_ACCESS_TOKEN'))

# Define repository and file path mappings
repo_file_mappings = [
    {'owner': ' ', 'name': ' ', 'file_path': ' '},
    {'owner': ' ', 'name': ' ', 'file_path': ' '},
    # Add more repositories and their respective file paths
]

# Define pull request details
pr_title = 'Update Common File'
pr_body = 'Updating common file with new content'
base_branch = 'main'  # Branch you want to merge into
head_branch = 'update-common-file'  # Branch with the changes

# Common file details
file_content = '''
TEST
TEST
TEST
'''

# Loop over repository and file path mappings
for mapping in repo_file_mappings:
    owner = mapping['owner']
    name = mapping['name']
    file_path = mapping['file_path']

    # Retrieve the repository
    try:
        repo = g.get_repo(f"{owner}/{name}")
    except Exception as e:
        print(f"Error retrieving repository {owner}/{name}: {e}")
        continue

    # Get the repository
    repo = g.get_repo(f"{owner}/{name}")

    # Get the current file contents
    try:
        file = repo.get_contents(file_path)
        current_content = file.decoded_content.decode()
    except Exception as e:
        print(file_path)
        print(f"Error retrieving file contents for {owner}/{name} - {file_path}: {e}")
        continue

    # If the content hasn't changed, skip the repository
    if current_content == file_content:
        print(f"No changes for {owner}/{name}. Skipping...")
        continue

    # Create a new branch for the file update
    try:
        branch_name = f"{head_branch}-{name}"
        default_branch = repo.default_branch
        commit_sha = repo.get_branch(default_branch).commit.sha
        repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=commit_sha)
        print(f"Branch '{branch_name}' created successfully.")
    except Exception as e:
        print(f"Error creating branch for {owner}/{name}: {e}")

    # Update the file content
    try:
        repo.update_file(
            path=file_path,
            message='Update common file',
            content=file_content,
            sha=file.sha,
            branch=branch_name
        )
    except Exception as e:
        print(f"Error updating file for {owner}/{name} - {file_path}: {e}")
        continue

    # Create the pull request
    try:
        pr = repo.create_pull(title=pr_title, body=pr_body, base=base_branch, head=branch_name)
        print(f"Pull request created for {owner}/{name}: {pr.html_url}")
    except Exception as e:
        print(f"Error creating pull request for {owner}/{name}: {e}")