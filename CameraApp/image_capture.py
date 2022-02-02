#!/usr/bin/env python3
#This script will capture an image from the camera

import cv2
import depthai as dai

outpath = 'C:\\scripts\\OpenCV_AI_Competetion\\depthai-tutorials-practice\\3-image-capture\\'

# Create pipeline
pipeline = dai.Pipeline()

# Define source and outputs
camRgb = pipeline.create(dai.node.ColorCamera)
xoutVideo = pipeline.create(dai.node.XLinkOut)
xoutPreview = pipeline.create(dai.node.XLinkOut)

xoutVideo.setStreamName("video")
xoutPreview.setStreamName("preview")

# Properties
camRgb.setPreviewSize(300, 300)
camRgb.setBoardSocket(dai.CameraBoardSocket.RGB)
camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
camRgb.setInterleaved(True)
camRgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.BGR)

# Linking
#camRgb.video.link(xoutVideo.input)
camRgb.preview.link(xoutPreview.input)
counter = 0

# Connect to device and start pipeline
with dai.Device(pipeline) as device:

    #video = device.getOutputQueue('video')
    preview = device.getOutputQueue('preview')

    while True:
        
        #videoFrame = video.get()
        previewFrame = preview.get()
        
        # Get BGR frame from NV12 encoded video frame to show with opencv
        #cv2.imshow("video", videoFrame.getCvFrame())
        # Show 'preview' frame as is (already in correct format, no copy is made)
        cv2.imshow("preview", previewFrame.getFrame())
        
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        
        elif key == ord('c'):
            filename = outpath + 'capture_2_1_' + str(counter) +'.jpg'
            cv2.imwrite(filename, previewFrame.getFrame())
            counter = counter + 1
        pass
