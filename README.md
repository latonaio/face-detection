# face-detection
face-detectionは、主にエッジコンピューティング環境において、カメラの画像から顔を検出するマイクロサービスです。

### デプロイ方法 ###
本リポジトリをクローンし、そのディレクトリまで移動してください。

```
$ git clone git clone git@github.com:latonaio/face-detection.git
$ cd /path/to/face-detection
```
利用したい環境に合わせて環境変数を設定してください。k8s/face-detection.yaml において設定が可能です。
```
          env:
            - name: PORT
              value: "8888"
            - name: VIDEO_PATH
              value: "rtsp://stream-usb-video-by-rtsp-001-srv:8555/usb"
            - name: DETECT_INTERVAL
              value: 0.1
```
以下のコマンドを実行し、デプロイを行ってください。
```
$ make docker-build
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

