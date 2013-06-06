#!/usr/bin/env python

import tornado.ioloop
from gitAggregate import app, loop

if __name__ == "__main__":
    """
        Listens on local port 8888.
        Runs indefinitely.
    """
    app.listen(8888)
    loop.start()
