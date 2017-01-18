import os

def tex2pdf(repository_dir):
    try:
        os.chdir(repository_dir)
        os.system('make')
    except:
        return 'ERROR'
    file_list = os.listdir(repository_dir)
    for f in file_list:
        if 'abst.pdf' in f:
            return repository_dir + '/' + 'abst.pdf'
    return 'ERROR'
