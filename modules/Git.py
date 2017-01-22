import os


def GitClone(repository_url, repo_path, git_ssh_script):
    clone_command = 'GIT_SSH=%s git clone ' % git_ssh_script
    os.system(clone_command + repository_url + ' ' + repo_path)


def GitPull(repository_url, username):
    repository_name = repository_url.split('/')[-1].replace('.git', '')
    script_dir = os.path.abspath(os.path.dirname(__file__))
    user_dir = '/'.join(script_dir.split('/')[:-1]) + '/users/' + username
    repositoory_dir = user_dir + '/repos/' + repository_name
    git_ssh_script = user_dir + '/git-ssh.sh'
    if os.path.exists(repositoory_dir):
        os.chdir(repositoory_dir)
        os.system('GIT_SSH=%s git pull origin master' % git_ssh_script)
    else:
        GitClone(repository_url, repositoory_dir, git_ssh_script)
    return repositoory_dir


def createGitSSH(user_dir):
    home_dir = os.path.expanduser('~')
    username = user_dir.split('/')[-1]
    key_path = home_dir + '/.ssh/keys' + username + 'id_rsa'
    script_path = user_dir + '/git-ssh.sh'
    script = '''
    #!/bin/sh
    exec ssh -o IdentityFile=%s "$@"
    ''' % key_path
    fd = open(script_path, 'a')
    fd.write(script)
    fd.close()
    os.system('chmod 755 %s' % script_path)
    return script_path
