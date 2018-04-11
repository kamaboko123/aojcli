#!/usr/bin/python

import os
import sys
import libaoj

def error_exit(message, exit_code = -1):
    output = ""
    for line in message:
        output += line
    
    sys.stderr.write(output + "\n")
    exit(exit_code)

try:
    user_id = os.environ["AOJCLI_ID"]
    password = os.environ["AOJCLI_PASSWORD"]
    
except KeyError as e:
    message = [
        "Error.\n\n",
        "Required environment values is not set.\n",
        "Please set following environment values.\n",
        "AOJCLI_ID : Your user id of AOJ\n",
        "AOJCLI_PASSWORD : Your password of AOJ\n",
    ]
    error_exit(message)

try:
    api = libaoj.Api(user_id, password)
except libaoj.AojApiError as e:
    error_exit(e.get_message())

print "Authentication : Success"

