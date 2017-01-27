import os
import shutil

def tex2pdf(repository_dir, username):
    os.chdir(repository_dir)
    os.system('make')
    os.system('make clean')
    shutil.move(repository_dir+'/abst.pdf', '../../../../static/files/' + username + '/abst.pdf')
