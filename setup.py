from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = ["gi"], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable(script='yobrowser.py', base=base, targetName='yo')
]

setup(name='Yo Browser',
      version = '1.0',
      description = 'Simple Web Browser based on GTK3.0 and WebKit3 in Python3',
      options = dict(build_exe = buildOptions),
      executables = executables)
