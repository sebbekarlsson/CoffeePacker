import os
import shutil
import json
import subprocess


class CoffeePacker(object):
    def __init__(self):
        print('*===Thank you for using CoffeePacker===*')


    def pack(self, path, execute):
        json_path = '{}/{}'.format(path, 'project.json')
        
        json_file = open(json_path)
        project = json.loads(json_file.read())
        json_file.close()

        src_dir = '{}/{}'.format(path, 'src')
        bin_dir = '{}/{}'.format(path, 'bin')

        if not os.path.isfile(json_path):
            return 'Could not find "project.json".'

        if not os.path.isdir(path):
            return 'Invalid directory.'

        if not os.path.isdir(src_dir):
            return 'Could not find "src" directory.'

                
        if os.path.isdir(bin_dir):
            shutil.rmtree(bin_dir)
        
        os.mkdir(bin_dir)

        source_files = '{}/**.java'.format(src_dir)

        libraries = [''.join('{}/{}:'.format(path, lib)) for lib in project['libraries']]
        libraries[len(libraries) -1] = libraries[len(libraries) -1].replace(':', '')
        libraries_path = ''.join(libraries)

        compile_p = subprocess.Popen(
                '/usr/bin/javac -d {bin_path} {source_path} -cp {libraries}'\
                        .format(
                            bin_path=bin_dir,
                            source_path=source_files,
                            libraries=libraries_path
                            ),
                shell=True
        )

        while compile_p.wait():
            print('Compiling...')

        if execute:
            subprocess.Popen(
                    '/usr/bin/java -cp {libraries}:{bin_path} {classname}'\
                        .format(
                            bin_path=bin_dir,
                            source_path=source_files,
                            libraries=libraries_path,
                            classname=project['class']
                            ),
                shell=True
        )

        return '*===Done!===*'
