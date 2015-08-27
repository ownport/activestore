class BucketCollectionAPI(object):

    def on_get(self, req, resp):

        resp.data = 'BucketCollection'


class BucketAPI(object):

    def on_get(self, req, resp, bucket_name):

        resp.data = 'Bucket: %s' % bucket_name


        