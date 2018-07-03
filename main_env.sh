#!/usr/bin/env bash

# Custom environments

# path to cgru root
export CGRU_PATH=/render/cgru
# change this line if CGRU have different location on the remote farm
export CGRU_PATH_REMOTE=${CGRU_PATH}
# path to mtoa root
export MTOA_PATH=/render/arnold/2017
# maya version (need for cgru plugins)
export MAYA_VERSION=2017
# maya location
export MAYA_LOCATION=/usr/autodesk/maya2017
# path to maya_starter scripts
export CUSTOM_AF=/render/maya_af_custom
