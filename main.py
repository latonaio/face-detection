# python 3.6 

import os
import time
from concurrent.futures import ThreadPoolExecutor
import asyncio
from threading import Thread
import webSocketHandler as ws
from faceDetect import FaceDetect
# import time 

VIDEO_PATH = os.environ.get('VIDEO_PATH')
# DETECT_INTERVAL = os.environ.get('DETECT_INTERVAL')

def _send_message(socket, data):
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(socket.write_message(data))
    except:
        print("failed")
    finally:
        loop.close()
        asyncio.set_event_loop(None)

def send_message(data):
    for client in ws.get_client():
        t = Thread(target=_send_message, args=[client, data])
        t.daemon = True
        t.start()
        t.join()


def face_detect_and_send_message_run():
    fd = FaceDetect(VIDEO_PATH)
    f_cam_connect = False
    f_cl_connect = False
    f_face_detect = False

    while(True):
        # time.sleep(float(DETECT_INTERVAL))
        # check client connection
        if ws.check_client():
            # disconnect -> connect
            if not f_cl_connect:
                print("Conect to client")
                f_cl_connect = True
        else:
            if f_cl_connect:
            # connect -> disconnect
                print("Disconnect to client")
                f_cl_connect = False
            continue

        # face detection
        try:
            result = fd.face_detect()
            if not f_cam_connect:
                # camera disconnect -> connect
                print("Connect to camera")
                f_cam_connect = True
        except:
            fd.reconnect()
            if f_cam_connect:
                # camera connect -> disconnect
                print("Disconnect from camera")
                f_cam_connect = False
            continue

        # check detect result
        if result is None:
            if f_face_detect:
                # detect -> lost
                print("Face lost")
                f_face_detect = False
        else:
            if not f_face_detect:
                # lost -> detect
                print("Face detect")
                f_face_detect = True
            send_message(result)


def main():
    print("start")

    ws.make_handler()
    print("maked websocket handler")

    executor = ThreadPoolExecutor(max_workers=1)
    executor.submit(face_detect_and_send_message_run)
    print("thread exec face_detect_and_send_message_run")

    ws.websocket_run()

if __name__ == "__main__":
    main()
