#!/usr/bin/env bash

# Custom environments

# path to cgru root
export CGRU_PATH=/mnt/cgru
# change this line if CGRU have different location on the remote farm
export CGRU_PATH_REMOTE=${CGRU_PATH}
# path to mtoa root
export MTOA_PATH=/mnt/arnold/mtoa/3.0.1
# maya version (need for cgru plugins)
export MAYA_VERSION=2018
# maya location
export MAYA_LOCATION=/opt/Autodesk/Maya2018
# path to maya_starter scripts
export CUSTOM_AF=/mnt/maya/maya_af_custom