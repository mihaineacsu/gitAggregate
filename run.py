#!/usr/bin/env python

import sys
from gitAggregate import app, loop

usage = 'Usage: '

def listen(port=8888):
    """
        Listens on local port.
        Runs indefinitely.
    """
    app.listen(8888)
    loop.start()

def run_command(command):
    """
        Switch based on given command line argument.
        Returns refernce to function that is to be run.
    """
    return {
        'query' : query,
        'listen': listen,
    }.get(command, None)

def query(p):
    pass

if __name__ == "__main__":
    args = sys.argv[1:]

    if not args:
        print usage
    else:
        foo = run_command(args[0])

        if foo is None:
            print usage
        else:
            foo(sys.argv[1:])
