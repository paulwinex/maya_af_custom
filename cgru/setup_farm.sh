#!/usr/bin/env bash
# Copy this file to CGRU root

source ../main_env.sh # todo: change path

# cgru
MAYA_CGRU_LOCATION=${CGRU_PATH}/plugins/maya
excport AF_ROOT=${CGRU_PATH}/afanasy
export PATH=${CGRU_PATH}/afanasy/bin:${CUSTOM_AF}/bin:${PATH}

# mtoa
export PYTHONPATH=${MTOA_PATH}/scripts:${PYTHONPATH}
export MAYA_MODULE_PATH=${MTOA_PATH}
export ARNOLD_PLUGIN_PATH=${MTOA_PATH}/shaders
export PATH=${MTOA_PATH}/bin:${PATH}
#export solidangle_LICENSE=
