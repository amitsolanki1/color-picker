from http.server import executable
import cx_Freeze
import sys

from pandas import options

base=None

if sys.platform=="win32":
    base="Win32GUI"
# executables =[cx_Freeze.Executable('color.py',base=base,icon='game.ico')]

# cx_Freeze.setup(
#     name="COLOR-PICKER",
#     options={"build_exe":{"packages":['tkinter'],"include_files":['game.ico","game.png"]}}
# )

executables =[cx_Freeze.Executable('color.py',base=base,)]

cx_Freeze.setup(
    name="COLOR-PICKER",
    options={"build_exe":{"packages":['tkinter']}},
    version="0.0.1",
    description="COLOR PICKER APP Creaated by Amit Solanki!\n Copyright:2021-2022",
    executables=executables
)