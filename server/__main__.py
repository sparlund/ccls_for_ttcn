import logging

from .server import ttcn_server

logging.basicConfig(filename="pygls.log", level=logging.DEBUG, filemode="w")

if __name__ == '__main__':
    ttcn_server.start_io()
