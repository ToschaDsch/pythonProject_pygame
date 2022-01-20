from cx_Freeze import setup, Executable

setup(
    name = "Tiger",
    version = "0.1",
    description = "Tigeer!",
    executables = [Executable("main.py")]
)
