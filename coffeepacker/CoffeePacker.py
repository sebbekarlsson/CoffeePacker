import os
import shutil
import json
import subprocess


class CoffeePacker(object):
    def __init__(self):
        print('*===Thank you for using CoffeePacker===*')


    def pack(self, path, execute, export):
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

        find_output = subprocess.Popen(
                '/usr/bin/find {} -name *.java'.format(src_dir),
                shell=True,
                stdout=subprocess.PIPE
                )
        find_array = find_output.communicate()[0].split(b'.java')
        java_files = []
        
        find_array.pop(len(find_array)-1)
        for java in find_array:
            java_files.append('{}.java '.format(java.decode('utf-8')).replace('\n', ''))
        
        java_files[len(java_files) -1] = java_files[len(java_files) -1].replace(':', '')
        source_files = ''.join(java_files)

        libraries = [''.join('{}/{}:'.format(path, lib)) for lib in project['libraries']]
        libraries[len(libraries) -1] = libraries[len(libraries) -1].replace(':', '')
        libraries_path = ''.join(libraries)
        
        darg_line = ''

        if 'D' in project:
            dargs = project['D']

            for obj in dargs:
                key, value = obj.popitem()
                darg_line += '-D{}={} '.format(key, value)


        cmd_compile = '/usr/bin/javac -d {bin_path} -cp {libraries} {source_path}'\
                .format(
                        bin_path=bin_dir,
                        source_path=source_files,
                        libraries=libraries_path
                        )
        compile_p = subprocess.Popen(
                cmd_compile,
                shell=True,
                stdout=subprocess.PIPE
                )

        while compile_p.wait():
            try:
                    print(compile_p.communicate()[0])
            except ValueError:
                return '*===Something went wrong!===*'
        
        cmd_exec = ''
        if execute:
            cmd_exec = '/usr/bin/java -cp {libraries}:{bin_path} {darg_line} {classname}'\
                    .format(
                            bin_path=bin_dir,
                            darg_line=darg_line,
                            source_path=source_files,
                            libraries=libraries_path,
                            classname=project['class']
                            )
            print(cmd_exec)
            subprocess.Popen(
                    cmd_exec,
                    shell=True
                    )

        if export:
            with open('execute.sh', 'w+') as bash_file:
                bash_file.write(
                        '{}{}'.format(cmd_compile, cmd_exec)
                        )

                bash_file.close()

        return '*===Done!===*'
