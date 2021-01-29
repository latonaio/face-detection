# python 3.6 

import os
import time
import json
import cv2

CASC_PATH = "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(CASC_PATH) 

class FaceDetect():
    def __init__(self, video_capture_path):
        self._cap = None
        self._cap_path = video_capture_path
        self._connect_camera()
        self.image = None   # gray scale

    def _connect_camera(self):
        print("camera connection start")
        while (True):
            try:
                self._cap = cv2.VideoCapture(self._cap_path)
                self._cap.set(cv2.CAP_PROP_BUFFERSIZE, 0)
                if self.check_connect_cam():
                    break
                else:
                    print(f"cannot read image: {self._cap_path}")
                    self.finalise()
                    time.sleep(5)
            except:
                print(f"cannot connect camera: {self._cap_path}")
                time.sleep(5)
        print("camera connected")
    
    def _read_image(self):
        _, self.image = self._cap.read()
        if self.image is None:
            print("not read image")
            print("please check camera connection.")
            raise Exception
        self.image = cv2.resize(self.image,(320,180))

    def _cnv_gray_scale(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

    def _detect_multi_scale(self):
        detected_data = {}
        facerects = cascade.detectMultiScale(self.image, minSize=(50,50))
        if len(facerects) == 0:
            return None

        for c, (x, y, w, h) in enumerate(facerects):
            detected_data[c] = {
                "status": True,
                "type": "human",
                "x": int(x),
                "y": int(y),
                "w": int(w),
                "h": int(h),
            }
            # cv2.rectangle(self.image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            # cv2.imwrite(os.path.join(IMAGE_DIR,str(c)+".png"), self.image)
        return json.dumps(detected_data)

    # カメラ接続確認
    def check_connect_cam(self):
        return self._cap.read()[1] is not None

    # 顔検出実行
    def face_detect(self):
        try:
            self._read_image()
            self._cnv_gray_scale()
            self.f_connect_camera = True
            return self._detect_multi_scale()
        except:
            self.f_connect_camera = False
            raise Exception

    def reconnect(self):
        self.finalise()
        print("reconnect camera")
        self._connect_camera()

    def finalise(self):
        if self._cap is not None:
            self._cap.release()
            self._cap = None
        print("camera connection closed")

def test():
    file_path = os.path.join("test","in.png")
    # out_path =  os.path.join("test","out.png")
    
    fd = FaceDetect(0)
    fd.image = cv2.imread(file_path)
    fd._cnv_gray_scale()
    print(fd._detect_multi_scale())

    fd2 = FaceDetect(0)
    while(True):
        print(fd2.face_detect())

if __name__ == "__main__":
    test()
