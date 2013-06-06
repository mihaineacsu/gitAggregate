import tornado.web

class MainHandler(tornado.web.RequestHandler):
    """
        Has reference to mongodb.
        Handles POST requests and saves them in db
    """

    def initialize(self, db):
        self.payloads = db.payloads
    def post(self):
        payload_json = self.get_argument('payload')
        payload_dict = tornado.escape.json_decode(payload_json)
        self.payloads.insert(payload_dict)
