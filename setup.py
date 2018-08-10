# setup.py
from distutils.core import setup
from glob import glob
import py2exe
import sys

# Files to copy because stupid
data_files = [
    ('.', glob(r'C:\Users\T4\Envs\PyBrowseWithPy2exe\Lib\site-packages\Python.Runtime.dll')),
    ('.', glob(r'C:\Users\T4\Documents\DjangProjects\msvcr100.dll')),
    ('.', glob(r'C:\Users\T4\Envs\PyBrowseWithPy2exe\Lib\site-packages\webview\lib\WebBrowserInterop.x86.dll')),
    ('.', glob(r'C:\Users\T4\Envs\PyBrowseWithPy2exe\Lib\site-packages\webview\lib\WebBrowserInterop.x64.dll')),
]

includes = ['clr']

options = {
    'py2exe': {
        'includes': includes
    }
}

# main.exe works without appending this to the path
# sys.path.append('C:\\Users\\T4\\Documents\\DjangProjects\\msvcr100.dll')

# Call setup and set the windows option to convert main.py to an exe with GUI
setup(
    data_files = data_files,
    options = options,
    windows = [
        {
            'script': 'main.py',
            'icon_resources': [(1, 'main.ico')],
        }
    ]
)
