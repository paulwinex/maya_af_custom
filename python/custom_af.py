from pymel.all import *
import os, getpass, socket, json


if os.getenv('CGRU_LOCATION') and os.getenv('MAYA_CGRU_LOCATION'):
    cgru_setup = os.path.normpath(os.path.join(os.getenv('MAYA_CGRU_LOCATION').strip(os.pathsep), "cgru.mel")).replace(
        '\\', '/')
    mel.source(cgru_setup)


def get_cgru_root():
    return os.getenv('CGRU_PATH_REMOTE')


# '/cg/cgru'

from afanasy import meArnoldRender


class meArnoldRenderVersion(meArnoldRender.meArnoldRender):
    submit_button_text = 'Submit Default'
    remote_button_text = 'Render Remote'

    def fix_arnold_attr(self):
        # fix for arnold 5 (mtoa 2) in default meSubmitter
        opt = PyNode('defaultArnoldRenderOptions')
        if not opt.hasAttr('shader_searchpath'):
            opt.addAttr('shader_searchpath', dt="string")

    def initParameters(self, *args, **kwargs):
        self.fix_arnold_attr()
        super(meArnoldRenderVersion, self).initParameters(*args, **kwargs)

    def setupUI(self):
        super(meArnoldRenderVersion, self).setupUI()
        w = ui.PyUI(self.winMain)
        w.children()[0].children()[-3].setLabel('Submit Default')
        w.children()[0].children()[-2].setLabel('Remote Render')
        w.children()[0].children()[-2].setCommand(self.send_to_remote)

    def generate_ass(self, *args):
        self.fix_arnold_attr()
        super(meArnoldRenderVersion, self).generate_ass()

    def send_to_remote(self, *args):
        tmp = self.ass_param['ass_deferred']
        self.ass_param['ass_deferred'] = False
        self.fix_arnold_attr()
        self.generate_ass()
        self.ass_param['ass_deferred'] = tmp
        self.generate_cmd_script()

    def generate_cmd_script(self):
        inp = self.get_assgen_options('defaultRenderLayer').replace('"', '') + self.job_param[
            'job_separator'] + '@{}@'.format('#' * self.job_param['job_padding']) + '.ass'
        inp = inp.replace('-filename', '').strip()

        job_file = json_template.copy()
        job_file['job']['blocks'][0]['frame_first'] = self.job_param['job_start']
        job_file['job']['blocks'][0]['frame_last'] = self.job_param['job_end']
        job_file['job']['blocks'][0]['frames_inc'] = self.job_param['job_step']
        cmd = 'kick -i "{}" -v 2 -nstdin -dw -dp'.format(inp.replace('\\', '/'))
        job_file['job']['blocks'][0]['command'] = cmd
        job_file['job']['blocks'][0]['working_directory'] = os.path.dirname(inp)
        json.dump(job_file, open(os.path.normpath(os.path.join(os.path.dirname(inp), 'render.sh')), 'w'), indent=2)

        CGRU_ROOT = get_cgru_root()
# {CGRU_ROOT}\python\python.exe "{CGRU_ROOT}\afanasy\python\afjob.py" "{INP}" {START} {END} -by {STEP} -fpt 1 -seq 1 -pwd "{PWD}" -name "{NAME}"  -pause
        cmd_win = r'''
set START_DIR=%~dp0
set PYTHONPATH={CGRU_ROOT}\afanasy\python;{CGRU_ROOT}\lib\python;%PYTHONPATH%
cd {CGRU_ROOT}
call {CGRU_ROOT}\setup.cmd
{CGRU_ROOT}\python\python.exe "{CGRU_ROOT}\afanasy\bin\afcmd.exe" json send "%START_DIR%\job.json"
        '''.format(
            CGRU_ROOT=CGRU_ROOT,
            # INP=inp,
            # START=self.job_param['job_start'],
            # END=self.job_param['job_end'],
            # STEP=self.job_param['job_step'],
            # PWD=os.path.dirname(inp),
            # NAME=os.path.basename(sceneName())
        )
        open(os.path.normpath(os.path.join(os.path.dirname(inp), 'render.cmd')), 'w').write(cmd_win)

        CGRU_ROOT = get_cgru_root()
#         cmd_bash = r'''export PYTHONPATH={CGRU_ROOT}/afanasy/python:{CGRU_ROOT}/lib/python:${{PYTHONPATH}}
# cd {CGRU_ROOT}
# source {CGRU_ROOT}/setup.sh
# python "{CGRU_ROOT}/afanasy/python/afjob.py" "{INP}" {START} {END} -by {STEP} -fpt 1 -seq 1 -pwd "{PWD}" -name "{NAME}"  -pause
#         '''.format(
#             CGRU_ROOT=CGRU_ROOT,
#             INP=inp,
#             START=self.job_param['job_start'],
#             END=self.job_param['job_end'],
#             STEP=self.job_param['job_step'],
#             PWD=os.path.dirname(inp),
#             NAME=os.path.basename(sceneName())
#         ).replace('\\', '/')
        cmd_bash = r'''
export START_DIR="$( cd "$( dirname "${{BASH_SOURCE[0]}}" )" && pwd )"
export PYTHONPATH={CGRU_ROOT}/afanasy/python:{CGRU_ROOT}/lib/python:${{PYTHONPATH}}
cd {CGRU_ROOT}
source {CGRU_ROOT}/setup.sh
python "{CGRU_ROOT}/afanasy/bin/afcmd" json send ${{START_DIR}}/job.json
'''.format(
            CGRU_ROOT=CGRU_ROOT,
            # INP=inp,
            # START=self.job_param['job_start'],
            # END=self.job_param['job_end'],
            # STEP=self.job_param['job_step'],
            # PWD=os.path.dirname(inp),
            # NAME=os.path.basename(sceneName())
        ).replace('\\', '/')

        open(os.path.normpath(os.path.join(os.path.dirname(inp), 'render.sh')), 'w').write(cmd_bash)



def replace_class():
    meArnoldRender.meArnoldRender = meArnoldRenderVersion
    print('CGRU Arnold updated')


json_template = {
    "job":
        {
            "name": "Render Ass",
            "user_name": getpass.getuser(),
            "host_name": socket.gethostname(),
            "blocks": [
                {
                    "name": "Ass Render",
                    "tasks_name": "frames @#@-@#@",
                    "flags": 1,
                    "service": "arnold",
                    "parser": "arnold",
                    "frame_first": 0,
                    "frame_last": 0,
                    "frames_per_task": 0,
                    "frames_inc": 1,
                    "command": r'kick -i "...\untitled_0001.ass" -v 2 -nstdin -dw -dp',
                    "working_directory": "",
                    # "files": ["folder/untitled_@####@.exr"]
                }
            ]
        }
}
