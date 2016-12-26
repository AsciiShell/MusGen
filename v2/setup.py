import sys
from cx_Freeze import setup, Executable

setup(
    name = "AsciiShell",
    version = "1.0",
    description = "AsciiShell brainfuck",
    executables = [Executable("WavGen.py", base = "Win32GUI")])