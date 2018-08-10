import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == 'Win32':
    base = 'Win32GUI'
	
packages = ['os', 'webview', ]

include_files = [
    ('C:\\Users\\T4\Envs\\PyBrowse\\Lib\\site-packages\\Python.Runtime.dll', 'Python.Runtime.dll'),
    ('C:\\Users\\T4\Envs\\PyBrowse\\Lib\\site-packages\\clr.pyd', 'clr.pyd'),
]

includefiles = []

options = {
    'build_exe': {
        'includes': [],
	'packages': packages,
        'excludes': ['tkinter'],
    },
    'include_files': include_files
}

executables = [
    Executable(
        script='main.py',
        base=base,
        icon='main.ico',
        targetName='PyBrowse for Windows.exe',
        shortcutName='PyBrowse for Windows',
    ),
]

setup(
    name='PyBrowse for Windows',
    version='0.1',
    description='PyBrowse for Windows with Django and CherryPy',
    options=options,
    executables=executables,
)
