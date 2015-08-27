#!/usr/bin/env python
# -*- coding: utf-8 -*-

import falcon

from activestore.api import service 
from activestore.api import buckets 
from activestore.api import objects 

api = application = falcon.API()

api.add_route('/service', service.ServiceAPI())
api.add_route('/bucket', buckets.BucketCollectionAPI())
api.add_route('/bucket/{bucket_name}', buckets.BucketAPI())
api.add_route('/bucket/{bucket_name}/object', objects.ObjectCollectionAPI())
api.add_route('/bucket/{bucket_name}/object/{object_id}', objects.ObjectAPI())


