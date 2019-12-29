class ResponseInfo(object):
    def __init__(self, user=None, **args):
        self.response = {
            "errorCode": args.get('error', 0),
            "message": args.get('message', 'success'),
            "data": args.get('data', [])
        }
