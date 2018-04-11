#!/usr/bin/python

import os
import sys
import argparse
import libaoj

support_oper = ["submit"]

#TODO : get from API
support_lang = ["C", "C++"]

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

parser = argparse.ArgumentParser(description = "AOJ submission tool on CLI")
parser.add_argument(
    "operation",
    const = None,
    choices = support_oper,
    help = 'Operation of AOJ',
)

parser.add_argument(
    "problem_id",
    const = None,
    help = 'Problem ID',
)
parser.add_argument(
    "language",
    const = None,
    choices = support_lang,
    help = 'Laugage of source code'
)
parser.add_argument(
    "file",
    const = None,
    help = 'source code file'
)

args = parser.parse_args()

try:
    with open(args.file, "r") as source_file:
        source_code = source_file.read()
    
    ret = api.submit(args.problem_id, args.language, source_code)
    print "[submit success]"
    print "Access token for checking result : %s" % ret["token"]
    

except IOError as e:
    error_exit(str(e))
except libaoj.AojApiError as e:
    print e.get_detail()
    error_exit(e.get_message())

