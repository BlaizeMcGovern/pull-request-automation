# GitHub Pull Request Automation

This Python program automates the process of opening pull requests on GitHub repositories. 

## Prerequisites

- Python 3.6 or higher
- PyGithub library

### Clone the repository

1. Open a command prompt or terminal.

2. Clone the repository using the following command:

   git clone <repository_url>

### Create a virtual environment

1. Change your current directory to the project folder:

   cd secure-file-transfer-project

2. Create a virtual environment using the `venv` module:

   python -m venv venv

3. Activate the virtual environment:

   venv\Scripts\activate

### Install dependencies

1. Install the required dependencies using `pip`:

   pip install -r requirements.txt

   This will install the necessary dependencies, including `PyGithub`.

### Create .env file

1. Create new file in root directory called .env:
        Add these variables:
        GITHUB_ACCESS_TOKEN=
        Where its equal to your persoanl access token

### Run the project

1.  In pull.py fill in the required information in the repo_file_mappings, where "owner" is your github username, "name" is the repository name and "file_path" is the path the
      file you would like changed. Then add what you want changed to the file_content variable, you do not need an existing commit or branch for this, it serves the purpose of making a change to a file if you all the repos have the same file and you would like them to have the same change. 

2.  Run using: python pull.py
