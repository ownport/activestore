class ObjectCollectionAPI(object):

    def on_get(self, req, resp):

        resp.data = 'ObjectCollection'


class ObjectAPI(object):

    def on_get(self, req, resp, bucket_name, object_id):

        resp.data = 'Object'

        