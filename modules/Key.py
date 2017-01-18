import os

def createKey(username):
    script_dir = os.path.abspath(os.path.dirname(__file__))
    key_dir = '/'.join(script_dir.split('/')[:-1]) + '/keys/'
    key_filename = key_dir + 'id_rsa_' + username
    os.system('ssh-keygen -q -f ' + key_filename + ' -N \'\'')
    fd = open(key_filename + '.pub')
    pub_key = fd.read()
    fd.close()
    return pub_key

def getPubKey(username):
    script_dir = os.path.abspath(os.path.dirname(__file__))
    key_dir = '/'.join(script_dir.split('/')[:-1]) + '/keys/'
    key_filename = key_dir + 'id_rsa_' + username
    try:
        fd = open(key_filename + '.pub')
        pub_key = fd.read()
        fd.close()
        return pub_key
    except:
        return 'ERROR'

