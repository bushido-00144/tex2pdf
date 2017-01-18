import os
import shutil

def tex2pdf(repository_dir):
    try:
        os.chdir(repository_dir)
        os.system('make')
        shutil.move(repository_dir+'/abst.pdf', '../../files/abst.pdf')
    except:
        return 'ERROR'
    file_list = os.listdir(repository_dir)
    if 'abst.pdf' in file_list:
        pdf_file = '/'.join(os.getcwd().split('/')[:-2]) + '/abst.pdf'
        return pdf_file
    return 'ERROR'
