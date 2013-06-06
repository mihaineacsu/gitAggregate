import tornado.web
from pymongo import MongoClient

import PostServer

# Maps root URL to MainHandler
app = tornado.web.Application([
        (r"/", PostServer.MainHandler),
        ])

loop = tornado.ioloop.IOLoop.instance()

# Connects to the default host and port
client = MongoClient()
db = client.git_payloads
