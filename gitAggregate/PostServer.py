import tornado.web

class MainHandler(tornado.web.RequestHandler):
    """
        Handles POST requests.
        Has reference to mongodb.
    """

    def initialize(self, db):
        self.db = db
    def post(self):
        payload_json = self.get_argument('payload')
        payload_dict = tornado.escape.json_decode(payload_json)
