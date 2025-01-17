__name__ = "scratchconnectplus"
__version__ = "5.1"
__author__ = "jdev082"
__documentation__ = "https://sid72020123.github.io/scratchconnect/"
__doc__ = f"""
ScratchConnect is a Python Library to connect Scratch API and much more.
This library can show/fetch the statistics of Users, Projects, Studios, Forums and also connect and set cloud variables of a project!
Import Statement:
    import scratchconnect
Documentation(Tutorial):
    For documentation, go to {__documentation__}
Required Libraries:
    requests*, re*, json*, time*, traceback*, threading*, urllib*, PIL*, websocket-client
    * -> In-built
Optional Libraries:
    rich - For Terminal feature
Change Log:
    View all the change log at: https://github.com/Sid72020123/scratchconnect#change-log
Credits:
    View all the contributors: https://github.com/Sid72020123/scratchconnect#contributors
"""

print_name = "ScratchConnect"
print(f"[1m[33m{print_name}[32m[3m v{__version__}[37m -[36m {__documentation__}[0m")

from scratchconnect.ScratchConnect import ScratchConnect
from scratchconnect import Exceptions
