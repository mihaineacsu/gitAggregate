import tornado.web
import PostServer

# Maps root URL to MainHandler
app = tornado.web.Application([
        (r"/", PostServer.MainHandler),
        ])

