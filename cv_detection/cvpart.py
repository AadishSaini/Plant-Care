import cv2 as cv
from cv_detection.consts import *
from cv_detection.tools import tools2
import time, threading 
import models.testingModel1 as testingModel1


class cvmodel:
    def __init__(self):
        self.t = tools2
        self.camera = 0

    def save_img(self, img):
        try:
            cv.imwrite("detected.jpg", img)
            print(testingModel1.predict_top_k("detected.jpg"))
        except:
            pass
    def manual_video(self):
        cap = cv.VideoCapture(self.camera)
        while True:
            ret, frame = cap.read()
            key = cv.waitKey(1)
            if key == ord('q'):  # Press 'q' to quit
                break
            elif key == ord(' '):  # Press space to capture
                self.save_img(frame) # Save the frame
                cv.imshow("frame", frame)
            
            cv.imshow("feed", frame)
    def image_one(self, image):
        hsv_frame = cv.cvtColor(image, cv.COLOR_BGR2HSV)

        # apply green mask
        green_mask, masked_on_frame_green = self.t.create_mask(hsv_frame, image, LOWER_GREEN, UPPER_GREEN)
        brown_mask, masked_on_frame_brown = self.t.create_mask(hsv_frame, image, LOWER_BROWN, UPPER_BROWN)
        
        # find contours
        contours_green, _ = cv.findContours(green_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        contours_brown, _ = cv.findContours(brown_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        

        #create the contoured image
        contour_image = image.copy() 
        try:
            largest_contour_green = max(contours_green, key=cv.contourArea)
            largest_contour_brown = max(contours_brown, key=cv.contourArea)
            x, y, w, h = cv.boundingRect(largest_contour_green)
            x_b, y_b, w_b, h_b = cv.boundingRect(largest_contour_brown)

            buffer = 50
            red_dimensions =  ((x-buffer, y-buffer), (x + w+buffer, y + h +buffer))
            cv.rectangle(contour_image, red_dimensions[0], red_dimensions[1], (0, 0, 255), 2)
            cv.rectangle(contour_image, (x_b-buffer, y_b-buffer), (x_b + w_b+buffer, y_b + h_b +buffer), (255, 0 , 0), 2) 

        except:
            pass
        
        img = image[red_dimensions[0][1]: red_dimensions[1][1], red_dimensions[0][0]:red_dimensions[1][0]]
        self.save_img(img)

    
    def video_one(self):
        cap = cv.VideoCapture(self.camera)
        t = tools2()
        if not cap.isOpened():
            print('cam nahi khula')


        start_time = time.time()
        dt = 0
        while True:
            ret, frame = cap.read()

            if not ret:
                print('cam nahi chala')
            # get frame and cvt to hsv
            frame = cv.flip(frame, 1)
            hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)


            # apply green mask
            green_mask, masked_on_frame_green = t.create_mask(hsv_frame, frame, LOWER_GREEN, UPPER_GREEN)
            brown_mask, masked_on_frame_brown = t.create_mask(hsv_frame, frame, LOWER_BROWN, UPPER_BROWN)
            
            # find contours
            contours_green, _ = cv.findContours(green_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            contours_brown, _ = cv.findContours(brown_mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            

            #create the contoured image
            contour_image = frame.copy() 
            try:
                largest_contour_green = max(contours_green, key=cv.contourArea)
                largest_contour_brown = max(contours_brown, key=cv.contourArea)
                x, y, w, h = cv.boundingRect(largest_contour_green)
                x_b, y_b, w_b, h_b = cv.boundingRect(largest_contour_brown)

                buffer = 50
                red_dimensions =  ((x-buffer, y-buffer), (x + w+buffer, y + h +buffer))
                cv.rectangle(contour_image, red_dimensions[0], red_dimensions[1], (0, 0, 255), 2)
                cv.rectangle(contour_image, (x_b-buffer, y_b-buffer), (x_b + w_b+buffer, y_b + h_b +buffer), (255, 0 , 0), 2) 

            except:
                pass
            
            
            if dt > 2:
                img = frame[red_dimensions[0][1]: red_dimensions[1][1], red_dimensions[0][0]:red_dimensions[1][0]]
                thread = threading.Thread(target=self.save_img, args=(img,))
                thread.start()
                dt = 0

            
            # cv.imshow("Bounding Box", contour_image)
            

            # cv.imshow('cam', frame)
            # cv.imshow('cam_hsv', hsv_frame)
            cv.imshow('contours', contour_image)


            dt += time.time() - start_time
            start_time = time.time()
            
            if cv.waitKey(1) == ord('q'):
                thread.join()
                break

        cap.release()
        cv.destroyAllWindows()




# from tools import *
# import cv2 as cv
# from consts import *

# cap = cv.VideoCapture(0)

# t = tools()

# running = True
# while running:
#     ret, frame = cap.read()

#     hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

#     green_mask = t.create_mask(hsv_frame, LOWER_GREEN, UPPER_GREEN, frame)
#     brown_mask = t.create_mask(hsv_frame, )

#     if cv.waitKey(1) == ord('q'):
#         running = False

#     cv.imshow('image', frame)
#     cv.imshow('hsv', hsv_frame)
#     cv.imshow('green mask', green_mask)

# cap.release()
# cv.destroyAllWindows()

