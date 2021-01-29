import websocket
import threading
import time
import logging
 
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(' %(module)s -  %(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)
 
# Callback functions
 
def on_message(ws, message):
	logger.info('Received:{}'.format(message))
 
def on_error(ws, error):
	logger.info('Error:{}'.format(error))
 
def on_close(ws):
	logger.info('Close')
 
def on_open(ws):
	def run(*args):
		logger.info('Open')
		for i in range(3):
			time.sleep(1)
			message = "Hello " + str(i)
			ws.send(message)
			logger.info('Sent:{}'.format(message))
		time.sleep(1)
		ws.close()
		logger.info('Thread terminating...')
	threading.Thread(run, args=())
 
# Main
 
if __name__ == "__main__":
	#websocket.enableTrace(True)
	websocket.enableTrace(False)
	ws = websocket.WebSocketApp("ws://face-detection:8888/websocket",
							on_message = on_message,
							on_error = on_error,
							on_close = on_close)
	ws.on_open = on_open
	ws.run_forever()
