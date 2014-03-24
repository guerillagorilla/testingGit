#!/usr/bin/python

import httplib, urllib
import subprocess
import re
import sys
import time

def outsidexConnStatus():

    external = subprocess.Popen(['fping', 'homer3434.dlinkddns.com'],stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0]

    re1='.*?'           # Non-greedy match on filler
    re2='(alive)'       # Grep Alive

    rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
    i = rg.search(external)

    if i:
        reoutside='1'
    else:
        reoutside='0'

    print "outside = ", reoutside

    params = urllib.urlencode({'field2': reoutside, 'key':'HNK995AU6E4X5F8J'})
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()

    print response.status, response.reason

    data = response.read()
    conn.close()

if __name__ == "__main__":
    outsidexConnStatus()
    sys.exit(0)
