import git
from git_contributions_importer import *
#from dotenv import load_dotenv
#load_dotenv()  # take environment variables from .env.
from  dotenv  import  dotenv_values
config  =  dotenv_values ( ".env" )   # config = {"USUÁRIO": "foo", "EMAIL": "foo@example.org"}

# CONFIGS
# Github email (personal)
github_personal_email = config.GITHUB_EMAIL
# Path to fake repository on Github (personal)
github_fake_repository_path = config.GITHUB_REPO_PATH
# Bithub email (company)
bitbucket_company_email = config.BITBUCKET_REPO_PATH
# Path to project repository on Bitbucket (company)
bitbucket_project_repository_path = Config.BITBUCKET_EMAIL

# SCRIPT
# Your private repo or Bitbucket repo
repo = git.Repo(bitbucket_project_repository_path)
# Your mock/fake repo
mock_repo = git.Repo(github_fake_repository_path)
importer = Importer([repo], mock_repo)
# I use both my personal email and work email here,
# Since the private repo uses work email, and Github profiles uses
# my work email
importer.set_start_from_last('ignore_before_date')
importer.set_author([github_personal_email, bitbucket_company_email])
importer.import_repository()