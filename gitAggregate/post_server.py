import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        payload_json = self.get_argument('payload')
        payload_dict = tornado.escape.json_decode(payload_json)

# Maps root URL to MainHandler
application = tornado.web.Application([
        (r"/", MainHandler),
        ])

if __name__ == "__main__":
    """
        Listens on local port 8888.
        Runs indefinitely.
    """
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
