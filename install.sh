#!/bin/sh

SCRIPT_DIR=$(cd $(dirname $0); pwd)
AOJCLI=`readlink -f ${SCRIPT_DIR}/aojcli.py`

pip install -r ${SCRIPT_DIR}/requirements.txt
echo "alias aojcli='${AOJCLI}'" >> ~/.bashrc

