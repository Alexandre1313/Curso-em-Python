from cx_Freeze import setup, Executable
import sys
import os

os.environ['TCL LIBRARY'] = 'C:\\Users\\alexa\\AppData\\Local\\Programs\\Python\\Python37\\tcl\\tcl8.6'
os.environ['TCL LIBRARY'] = 'C:\\Users\\alexa\\AppData\\Local\\Programs\\Python\\Python37\\tcl\\tk8.6'

base = None

if sys.platform == 'Win32':
    base = 'Win32GUI'
executables = [Executable('telasuni.py', base=base)]
packages = ['PySimpleGUI',
            'idna', 'sqlite3']

options = {'build_exe': {
                'packages': packages,
                'include_files': [
                    os.path.join('C:\\Users\\alexa\\AppData\\Local\\Programs\\Python\\Python37\\DLLs\\tcl86t.dll'),
                    os.path.join('C:\\Users\\alexa\\AppData\\Local\\Programs\\Python\\Python37\\DLLs\\tk86t.dll')
                ]
          }
}
setup(name='MEDIA_AULAS',
      options=options,
      version='2.0',
      description='Calculo_media_executavel',
      executables=executables)
