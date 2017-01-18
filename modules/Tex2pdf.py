import os

def tex2pdf(repository_dir):
    try:
        os.chdir(repository_dir)
        os.system('make')
    except:
        return False
    return True
