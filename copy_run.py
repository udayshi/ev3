from os import system,path


def downloadFile():
    cmd='rm -rf {0} && cp {1} {0}'.format('lcl.py','srv.py')
    system(cmd)

downloadFile()
import lcl
print(lcl.hello('Running from local'))