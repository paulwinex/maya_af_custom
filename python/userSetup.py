from pymel.all import *
from maya import cmds


# auto load mtoa
def load_mtoa():
    cmds.loadPlugin('mtoa')
    cmds.pluginInfo('mtoa', edit=True, autoload=False)


cmds.evalDeferred(load_mtoa)

# init custom arnold
import custom_af
custom_af.replace_class()
