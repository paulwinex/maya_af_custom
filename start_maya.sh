#!/usr/bin/env bash
source ./main_env.sh
echo "========== ${CUSTOM_AF}========="
# maya scripts for custom Afanasy submitter
export MAYA_SCRIPT_PATH=${CUSTOM_AF}/python:${MAYA_SCRIPT_PATH}
export PYTHONPATH=${PYTHONPATH}:${CUSTOM_AF}/python

# init cgru for maya
export MAYA_CGRU_LOCATION=${CGRU_PATH}/plugins/maya
export CGRU_LOCATION=${CGRU_PATH}
export AF_ROOT=${CGRU_PATH}/afanasy
export PYTHONPATH=${MAYA_CGRU_LOCATION}:${MAYA_CGRU_LOCATION}/afanasy:${CGRU_PATH}/afanasy/python:${CGRU_PATH}/lib/python:${PYTHONPATH}
export XBMLANGPATH=${MAYA_CGRU_LOCATION}/icons
export MAYA_PLUG_IN_PATH=${MAYA_CGRU_LOCATION}/mll/${MAYA_VERSION}
export MAYA_SCRIPT_PATH=${MAYA_CGRU_LOCATION}/mel/AETemplates
export PATH=${MAYA_CGRU_LOCATION}/afanasy/bin:${PATH}

# init mtoa
#export PYTHONPATH=${MTOA_PATH}/scripts:${PYTHONPATH}
export MAYA_MODULE_PATH=${MTOA_PATH}
export ARNOLD_PLUGIN_PATH=${MTOA_PATH}/shaders
export PATH=${MTOA_PATH}/bin:${PATH}
export solidangle_LICENSE=5053@pipeline

${MAYA_LOCATION}/bin/maya "$@"
