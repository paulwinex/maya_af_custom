#!/usr/bin/env bash
# Copy this file to CGRU root

source /render/maya_af_custom/main_env.sh 

# mtoa
export PYTHONPATH=${MTOA_PATH}/scripts:${PYTHONPATH}
export MAYA_MODULE_PATH=${MTOA_PATH}
export ARNOLD_PLUGIN_PATH=${MTOA_PATH}/shaders
export PATH=${MTOA_PATH}/bin:${PATH}
export solidangle_LICENSE=5053@pipeline
