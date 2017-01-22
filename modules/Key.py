import os


def createKey(username):
    home_dir = os.path.expanduser('~')
    key_dir = home_dir + '/.ssh/keys/' + username
    os.mkdir(key_dir)
    key_filename = key_dir + '/id_rsa'
    os.system('ssh-keygen -q -f ' + key_filename + ' -N \'\'')
    fd = open(key_filename + '.pub')
    pub_key = fd.read()
    fd.close()
    return pub_key


def getPubKey(username):
    home_dir = os.path.expanduser('~')
    key_dir = home_dir + '/.ssh/keys/' + username
    key_filename = key_dir + '/id_rsa'
    try:
        fd = open(key_filename + '.pub')
        pub_key = fd.read()
        fd.close()
        print(pub_key)
        return pub_key
    except:
        return 'ERROR'
