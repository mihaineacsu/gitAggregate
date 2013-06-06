import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        print self.get_argument('payload')

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
