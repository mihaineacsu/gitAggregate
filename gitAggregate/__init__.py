import tornado.web
from pymongo import MongoClient

import PostServer

# Connects to the default host and port on mongodb
client = MongoClient()
db = client.git_payloads

# Maps root URL to MainHandler
# and passes db reference 
app = tornado.web.Application([
        (r"/", PostServer.MainHandler, dict(db=db))
        ])

loop = tornado.ioloop.IOLoop.instance()
