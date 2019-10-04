import os
import shutil

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)


create_docker_folder = '{{cookiecutter.docker_container}}' != 'None'

if not create_docker_folder:
     # remove absolute path to file nested inside the generated folder
    remove(os.path.join(os.getcwd(),'docker'))
    print('removed docker folder')