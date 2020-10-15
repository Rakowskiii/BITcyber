import os
from shutil import copyfile
from glob import glob
from setup import randomFlag
def init():
    if not os.path.exists('/tmp/suspicious_file.txt'):
        with open('/tmp/suspicious_file.txt', 'w+') as f:
            f.write('yeah-there-should-be-our-flag')

    randomFlag()

    if not os.path.exists('./static/__pycache__'):
        os.mkdir('./static/__pycache__')
        
    for f in glob(r'./__pycache__/setup.cpython*.pyc'):
        copyfile(f, './static/__pycache__/{}'.format(os.path.basename(f)))

    if os.path.exists('./static/setup.py'):
        os.remove('./static/setup.py')