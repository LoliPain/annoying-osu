from cx_Freeze import setup, Executable

base = None

executables = [Executable("workfiles/annoying.py", base=base)]

packages = ["idna", "socket"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Annoying",
    options = options,
    version = "1.0",
    description = '',
    executables = executables
)