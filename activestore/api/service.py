import os
import json

"""
Response sample:

{ 
    "buckets": [
        {
            "id": "bucket-1", 
            "description": "Test bucker #1",
            "creation-date": 1440662675
        },
        {
            "id": "bucket-2", 
            "description": "Test bucker #2",
            "creation-date": 1440663675
        }
    ]
}

id              Bucket ID. Type: String
description     Bucket description
creation-date   Date the bucket was created in epoch time

"""

class ServiceAPI(object):
    ''' returns a list of all buckets
    '''

    def on_get(self, req, resp):

        buckets = [
            { "id": "bucket-1", "description": "Test bucker #1", "creation-date": 1440662675 },
            { "id": "bucket-2", "description": "Test bucker #2", "creation-date": 1440663675 },
        ]
        resp.data = json.dumps({u'buckets': buckets})



        