#!C:\Python27\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'sphinx==1.2.2','console_scripts','sphinx-build'
__requires__ = 'sphinx==1.2.2'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('sphinx==1.2.2', 'console_scripts', 'sphinx-build')()
    )
