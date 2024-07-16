from setuptools import setup

APP = ['deskpet.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'packages': ['PyQt6'],
    'includes': ['GlobalShortcutListener', 'Browser'],
     'excludes': ['six.moves','_gdbm', '_io._WindowsConsoleIO', '_overlapped', 'itertools.batched', 'StringIO', '_manylinux', '_typeshed', 'android', 'jnius'],
}


setup(
    app=APP,
    name='小O智能体',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)