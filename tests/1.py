# import cv2 as cv

# cam = cv.VideoCapture(0)

# while True:
#     ret, frame = cam.read()

#     cv.imshow('frame', frame)

#     if cv.waitKey(1) == ord('q'):
#         break
# cam.release()
# cv.destroyAllWindows()


# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.boxlayout import BoxLayout
# import time
# Builder.load_string('''
# <CameraClick>:
#     orientation: 'vertical'
#     Camera:
#         id: camera
#         resolution: (640, 480)
#         play: False
#     ToggleButton:
#         text: 'Play'
#         on_press: camera.play = not camera.play
#         size_hint_y: None
#         height: '48dp'
#     Button:
#         text: 'Capture'
#         size_hint_y: None
#         height: '48dp'
#         on_press: root.capture()
# ''')


# class CameraClick(BoxLayout):
#     def capture(self):
#         '''
#         Function to capture the images and give them the names
#         according to their captured time and date.
#         '''
#         camera = self.ids['camera']
#         timestr = time.strftime("%Y%m%d_%H%M%S")
#         camera.export_to_png("IMG_{}.png".format(timestr))
#         print("Captured")


# class TestCamera(App):

#     def build(self):
#         return CameraClick()


# TestCamera().run()


# from PyQt5 import QtGui
# from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
# from PyQt5.QtGui import QPixmap
# import sys
# import cv2
# from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
# import numpy as np


# class VideoThread(QThread):
#     change_pixmap_signal = pyqtSignal(np.ndarray)

#     def run(self):
#         # capture from web cam
#         cap = cv2.VideoCapture(0)
#         while True:
#             ret, cv_img = cap.read()
#             if ret:
#                 self.change_pixmap_signal.emit(cv_img)


# class App(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Qt live label demo")
#         self.disply_width = 640
#         self.display_height = 480
#         # create the label that holds the image
#         self.image_label = QLabel(self)
#         self.image_label.resize(self.disply_width, self.display_height)
#         # create a text label
#         self.textLabel = QLabel('Webcam')

#         # create a vertical box layout and add the two labels
#         vbox = QVBoxLayout()
#         vbox.addWidget(self.image_label)
#         vbox.addWidget(self.textLabel)
#         # set the vbox layout as the widgets layout
#         self.setLayout(vbox)

#         # create the video capture thread
#         self.thread = VideoThread()
#         # connect its signal to the update_image slot
#         self.thread.change_pixmap_signal.connect(self.update_image)
#         # start the thread
#         self.thread.start()



#     @pyqtSlot(np.ndarray)
#     def update_image(self, cv_img):
#         """Updates the image_label with a new opencv image"""
#         qt_img = self.convert_cv_qt(cv_img)
#         self.image_label.setPixmap(qt_img)
    
#     def convert_cv_qt(self, cv_img):
#         """Convert from an opencv image to QPixmap"""
#         rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
#         h, w, ch = rgb_image.shape
#         bytes_per_line = ch * w
#         convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
#         p = convert_to_Qt_format.scaled(self.disply_width, self.display_height, Qt.KeepAspectRatio)
#         return QPixmap.fromImage(p)
    
# if __name__=="__main__":
#     app = QApplication(sys.argv)
#     a = App()
#     a.show()
#     sys.exit(app.exec_())






# import cv2 as cv
# import threading
# import os

# def clickPicture(frame):
#     print('thread started')
#     if cv.waitKey(0) == ord('c'):
#         cv.imwrite('file.png', frame)
#         print('called')

# cap = cv.VideoCapture(0)

# if not cap.isOpened():
#     print('camera nahi khula')

# ret, frame = cap.read()
# captureImageThread = threading.Thread(target=clickPicture, args=[frame]).start()


# while True:
#     ret, frame = cap.read()
#     grey = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

#     cv.imshow('greyscale', grey)

#     if cv.waitKey(1) == ord('q'):
#         break
    

# cv.destroyAllWindows()
# cap.release()




# import cv2 as cv

# cap = cv.VideoCapture(0)
# if not cap.isOpened():
#     print('camera nahi khula')

# while True:
#     ret, frame = cap.read()

#     cv.imshow('title', frame)
#     if cv.waitKey(1) == ord('q'):
#         break

# cv.destroyAllWindows()
# cap.release()



# from __future__ import print_function
# import cv2 as cv
# import argparse
 
# parser = argparse.ArgumentParser(description='This program shows how to use background subtraction methods provided by \
#  OpenCV. You can process both videos and images.')
# parser.add_argument('--input', type=str, help='Path to a video or a sequence of image.', default='vtest.avi')
# parser.add_argument('--algo', type=str, help='Background subtraction method (KNN, MOG2).', default='MOG2')
# args = parser.parse_args()
 
 
# if args.algo == 'MOG2':
#     backSub = cv.createBackgroundSubtractorMOG2()
# else:
#     backSub = cv.createBackgroundSubtractorKNN()
 
 
 
# capture = cv.VideoCapture(0)
# if not capture.isOpened():
#     print('Unable to open: ' + args.input)
#     exit(0)
 
 
# while True:
#     ret, frame = capture.read()
#     if frame is None:
#         break
 
 
#     fgMask = backSub.apply(frame)
    
    
    
#     cv.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)
#     cv.putText(frame, str(capture.get(cv.CAP_PROP_POS_FRAMES)), (15, 15),
#     cv.FONT_HERSHEY_SIMPLEX, 0.5 , (0,0,0))
    
    
    
#     cv.imshow('Frame', frame)
#     cv.imshow('FG Mask', fgMask)
    
    
#     keyboard = cv.waitKey(30)
#     if keyboard == 'q' or keyboard == 27:
#         break





 