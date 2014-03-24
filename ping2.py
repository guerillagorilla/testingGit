#!/usr/bin/python

import httplib, urllib
import subprocess
import re
import sys
import time

while(True):
  try:

    #headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
    #conn = httplib.HTTPConnection("api.thingspeak.com:80")

    runPing = subprocess.Popen(['fping', '-C1', 'homer3434.dlinkddns.com'],stderr=subprocess.PIPE, stdout=subprocess.PIPE).communicate()[0]
    #print runPing	
		
    re1='.*?'	# Non-greedy match on filler
    re2='([+-]?\\d*\\.\\d+)(?![-+0-9\\.])'	# Float 1

    rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
    m = rg.search(runPing)
    if m:
     	float1=m.group(1)
        print float1
		
    params = urllib.urlencode({'field1': latency, 'key':'HNK995AU6E4X5F8J'})
    headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
    conn = httplib.HTTPConnection("api.thingspeak.com:80")
    conn.request("POST", "/update", params, headers)
    response = conn.getresponse()
    print float1
    print response.status, response.reason
    data = response.read()
    conn.close()    

  except:
    print "Connection Failed"
    #sys.exit()		
  
  # Wait 30 seconds before continuing
  time.sleep(10)
