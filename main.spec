# -*- mode: python -*-

def add_path_tree( base_path, path, skip_dirs=[ '.svn', '.git' ]):
    path = os.path.join( base_path, path )
    partial_data_files = []

    for root, dirs, files in os.walk( os.path.join( path )):
        sample_list = []
        for skip_dir in skip_dirs:
          if skip_dir in dirs:
            dirs.remove( skip_dir )
        if files:
            for filename in files:
                sample_list.append( os.path.join( root, filename ))
        if sample_list:
            partial_data_files.append((
                root.replace(
                    base_path + os.sep if base_path else '',
                    '',
                    1
                ),
                sample_list
            ))
    return partial_data_files

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')

block_cipher = None

paths = [
    'C:\\Users\\T4\\Documents\\DjangProjects\\PyBrowse',
    'C:\\Users\\T4\\Envs\\PyBrowseWithPyinstaller\\scripts',
    'C:\\Users\\T4\\Envs\\PyBrowseWithPyinstaller\\Lib\\site-packages\\pywin32_system32',
    'C:\\Users\\T4\\Envs\\PyBrowseWithPyinstaller\\Lib\\site-packages\\pythonwin'
]

binaries = [
    ('WebBrowserInterop.x64.dll', '.'),
    ('WebBrowserInterop.x86.dll', '.'),
]

data_files = [
    ('Resources/static', 'static'),
    ('polls', 'polls'),
    ('db.sqlite3', '.'),
    ('myapp', 'myapp')
    
]
a = Analysis(['start_django_and_cherrypy.py'],
             pathex=paths,
             binaries=binaries,
             datas=data_files,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=False,
          name='PyBrowse on Windows',
          debug=False,
          strip=False,
          upx=True,
          console=True,
          icon='main.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='PyBrowse on Windows')
