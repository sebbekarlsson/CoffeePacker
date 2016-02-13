import os
import shutil


class CoffeePacker(object):
    def __init__(self):
        print('*===Thank you for using CoffeePacker===*')


    def pack(path):
        json_path = '{}/{}'.format(path, 'project.json')
        src_dir = '{}/{}'.format(path, 'src')
        bin_dir = '{}/{}'.format(path, 'bin')

        if not os.path.isfile(json_path):
            return 'Could not find "project.json".'

        if not os.path.isdir(path):
            return 'Invalid directory.'

        if not os.path.isdir(src_dir):
            return 'Could not find "src" directory.'

        shutil.rmtree(bin_dir)
        os.mkdir(bin_dir)
