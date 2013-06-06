import tornado.web
import tornado.ioloop
from pymongo import MongoClient

import PostServer
import QueryDB

# Connects to the default host and port on mongodb
client = MongoClient()
db = client.db
query_db = QueryDB.QueryHandler(db)

# Maps root URL to MainHandler
# and passes db reference 
app = tornado.web.Application([
        (r"/", PostServer.MainHandler, dict(db=db))
        ])

loop = tornado.ioloop.IOLoop.instance()
