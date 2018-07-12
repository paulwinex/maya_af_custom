from pymel.all import *
from maya import cmds


print '='*50, 'INIT CUSTOM'
# auto load mtoa
def load_mtoa():
    cmds.loadPlugin('mtoa')
    cmds.pluginInfo('mtoa', edit=True, autoload=False)


cmds.evalDeferred(load_mtoa)

def init_cgru():
    cgru_setup = os.path.normpath(os.path.join(os.getenv('MAYA_CGRU_LOCATION').strip(os.pathsep), "cgru.mel")).replace('\\', '/')
    print cgru_setup
    print 'REPLACE CLASS', '='*50
    mel.source(cgru_setup)
    import custom_af
    custom_af.replace_class()

cmds.evalDeferred(init_cgru)
