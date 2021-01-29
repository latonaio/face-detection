# README #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

Clone and Build
```
$ git clone git clone git@bitbucket.org:latonaio/face-detection.git
$ cd /path/to/face-detection
$ make docker-build
```

Edit Environment K8s Resource
```
          env:
            - name: PORT
              value: "8888"
            - name: VIDEO_PATH
              value: "rtsp://stream-usb-video-by-rtsp-001-srv:8555/usb"
            - name: DETECT_INTERVAL
              value: 0.1
```

### How to Use ###

* Access `ws://face-detection:8888/websocket` (Only access internal k8s cluster network.)
* Cliant receive　the message like
```json
{
  "0": {"status": true, "type": "human", "x": 92, "y": 136, "w": 276, "h": 276},
  "1": {"status": true, "type": "human", "x": 10, "y": 111, "w": 250, "h": 246}
}
```
paramator
* 0 : detection number.
* status : detected result.
* type : detected object type. (now only human)
* x, y, w, h : detected object postion and size.