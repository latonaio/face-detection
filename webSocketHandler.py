from tornado import gen
import tornado.ioloop
import tornado.web
import tornado.websocket
from tornado.log import app_log
import signal
import os

_client_list = []

class WebSocketHandler(tornado.websocket.WebSocketHandler):    
    
    def open(self):
        if self not in _client_list:
            _client_list.append(self)
            # print("WebSocket opend")
            app_log.info("WebSocket opened")
            print("open")

    def check_origin(self, origin):
        return True

    def on_close(self):
        _client_list = []
        app_log.info("WebSocket closed")
        print("WebSocket closed")

def _signal_handler(signum, frame):
    app_log.info("Interrupt caught")
    tornado.ioloop.IOLoop.instance().stop()

def websocket_run():
    tornado.ioloop.IOLoop.instance().start()
    # or you can use a custom handler,
    # in which case recv will fail with EINTR
    app_log.info("registering sigint")
    signal.signal(signal.SIGINT, _signal_handler)

def make_handler():
    app = tornado.web.Application([
        (r"/websocket", WebSocketHandler)
    ])
    app.listen(os.environ.get('PORT'))
    # app.listen(8888)

def get_client():
    return _client_list

def check_client():
    return len(get_client())
