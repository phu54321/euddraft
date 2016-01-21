import sys
import eudplib
from cx_Freeze import setup, Executable

sys.argv.append('build_exe')

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {
    "packages": ["os", "sys"]
}

# GUI applications require a different base on Windows (the default is for a
# console application).

setup(
    name = "euddraft",
    version = eudplib.eudtrgVersion(),
    description = "euddraft main executable",
    options = {"build_exe": build_exe_options},
    executables = [
        Executable("euddraft.py")
    ]
)

