from cx_Freeze import setup, Executable

setup(
    name="SimpleCalculator",
    version="1.0",
    description="A simple calculator",
    executables=[Executable(
        "calculator.py",
        base="Win32GUI",           # hides console window
        icon="pixel_icon.ico" # path to your icon
    )]
)
