#!/usr/bin/env python

import sys
import os.path
import json
import requests

def generate_id():

    url = 'http://api.brooklynintegers.com/rest/'
    params = {'method':'brooklyn.integers.create'}

    try :
        rsp = requests.post(url, params=params)    
        data = rsp.content
    except Exception, e:
        logging.error(e)
        return 0
    
    try:
        data = json.loads(data)
    except Exception, e:
        logging.error(e)
        return 0
    
    return data.get('integer', 0)

if __name__ == '__main__':

    things = sys.argv[1]
    things = os.path.abspath(things)

    fh = open(things, 'r')
    
    buckets = []

    for ln in fh.readlines():

        ln = ln.strip()

        clean = ln
        label = clean.replace("-", " ")

        id = generate_id();

        bucket = {
            'id': id,
            'label': label,
            'label_clean': clean
            }        

        buckets.append(bucket)

    buckets = {'buckets': buckets}

    print json.dumps(buckets, indent=2)
