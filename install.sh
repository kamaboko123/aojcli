#!/bin/sh

SCRIPT_DIR=$(cd $(dirname $0); pwd)
AOJCLI=`readlink -f ${SCRIPT_DIR}/aojcli.py`

echo "export alias aojcli='${AOJCLI}'" >> ~/.bashrc

