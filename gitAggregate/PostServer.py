import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        payload_json = self.get_argument('payload')
        payload_dict = tornado.escape.json_decode(payload_json)
