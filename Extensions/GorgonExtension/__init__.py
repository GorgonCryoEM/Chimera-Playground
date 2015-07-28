#    The contents of "ToolbarButtonExtension/__init__.py" is
#    identical to the first section of code in "Toolbar Buttons",
#    with the exception that module 'os' is not imported.
#
#    .. "ToolbarButtonExtension/__init__.py" ToolbarButtonExtension/__init__.py
#    .. "Toolbar Buttons" ToolbarButton.html

import re

import chimera
from subprocess import call
import os

def mainGorgon():
    MAINCHAIN = re.compile("^(N|CA|C)$", re.I)
#     for m in chimera.openModels.list(modelTypes=[chimera.Molecule]):
#         for a in m.atoms:
#             a.display = MAINCHAIN.match(a.name) != None    # run external process
#     pathGorgon="/Users/durmaz/Files/eclipse_workspace/workspace_work/gitGorgonBitBucket/Gorgon/src_py/"
    pathGorgon="/Users/durmaz/Files/eclipse_workspace/workspace_work/Gorgon/build-Unix_Makefiles/package/dist/Gorgon.app"
    print "In mainGorgon()"
#     os.chdir(pathGorgon)
#     print "In path: " + pathGorgon
#     check_call("open " + pathGorgon)
    os.system("open " + pathGorgon)
#     print "Tried to run gorgon.pyw"
    print "Tried to run Gorgon.app"
#     call(["python", pathGorgon])
