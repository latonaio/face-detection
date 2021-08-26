# face-detection #
face-detectionは、カメラの画像から顔を検出するマイクロサービスです。

### デプロイ方法 ###
1. このリポジトリをクローンしてそのディレクトリまで移動してください。

```
$ git clone git clone git@bitbucket.org:latonaio/face-detection.git
$ cd /path/to/face-detection
```
2. 利用したい環境に合わせて環境変数を設定してください。k8s/face-detection.yaml において設定が可能です。
```
          env:
            - name: PORT
              value: "8888"
            - name: VIDEO_PATH
              value: "rtsp://stream-usb-video-by-rtsp-001-srv:8555/usb"
            - name: DETECT_INTERVAL
              value: 0.1
```
3. 以下のコマンドを実行することでdocker-imageを作成してください。
```
$ make docker-build
```
4. 以下のコマンドを実行することでpodを起動してください。
```
$ kubectl apply -f k8s/face-detection.yaml
```

### 使用方法 ###
  - k8s クラスターのネットワークを用いて ws://face-detection:8888/websocket へアクセスしてください。

- クライアントから以下のようなメッセージを受け取ることができます。
```json
{
  "0": {"status": true, "type": "human", "x": 92, "y": 136, "w": 276, "h": 276},
  "1": {"status": true, "type": "human", "x": 10, "y": 111, "w": 250, "h": 246}
}
```
各パラメータは以下を参照してください。

* 0 : 識別子
  
* status : 顔検出の成否
  
* type : 顔検出の結果(現在は"human"のみ)
  
* x, y, w, h : 検出された座標とサイズ

<!-- # README #

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
* x, y, w, h : detected object postion and size. -->