#!/usr/bin/env python

import sys
import textwrap
from gitAggregate import app, loop

usage = textwrap.dedent("""\
        Usage: ./run.py <command> [<args>]
        Commands:
            listen [port no]    Listens by default on 8888
            query [action]      Returns list of commit authors""")

def listen(port):
    """
        Receives list containg local port to listen on.
        Listens on local port and runs indefinitely.
    """

    if not port:
        port = 8888
    else:
        port = port[0]

    app.listen(port)
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
            foo(args[1:])
