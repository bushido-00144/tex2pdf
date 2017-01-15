import os

def GitClone(repository_url, repo_path):
    os.system('git clone ' + repository_url + ' ' + repo_path)

def GitPull(repository_url):
    repository_name = repository_url.split('/')[-1].replace('.git', '')
    script_dir = os.path.abspath(os.path.dirname(__file__))
    repositoory_dir = '/'.join(script_dir.split('/')[:-1]) + '/repos/' + repository_name
    if os.path.exists(repositoory_dir):
        os.system('git pull origin master')
    else:
        GitClone(repository_url, repositoory_dir)
