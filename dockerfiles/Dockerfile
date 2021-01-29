FROM latonaio/l4t-ds-opencv-ffmpeg-7.2:latest
# FROM latonaio/l4t-ds-opencv-7.2:latest

# Definition of a Device & Service
ENV POSITION=FaceDetection \
    SERVICE=face-detection \
    AION_HOME=/var/lib/aion

RUN mkdir ${AION_HOME}
WORKDIR ${AION_HOME}
# Setup Directoties
RUN mkdir -p \
    $POSITION/$SERVICE
WORKDIR ${AION_HOME}/$POSITION/$SERVICE/

# Install UVC Driver Gstreamer
# Add libcanberra-gtk-module libcanberra-gtk3-module
RUN apt-get update && apt-get install -y \
    uvccapture \
    libgstreamer1.0-0 \
    gstreamer1.0-plugins-base \
    gstreamer1.0-plugins-good \
    gstreamer1.0-plugins-bad \
    gstreamer1.0-plugins-ugly \
    gstreamer1.0-libav \
    gstreamer1.0-doc \
    gstreamer1.0-tools \
    python-gst-1.0 \
    python3-gst-1.0 \
    libcanberra-gtk-module \
    libcanberra-gtk3-module \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

COPY . .
# COPY requirements.txt .
RUN pip3 install -r requirements.txt

CMD ["python3", "-u", "main.py"]
