import cv2 as cv
from consts import *
from tools import tools2

cap = cv.VideoCapture(0)
t = tools2()
frame = cv.imread('./Untitled.jpeg')

if not cap.isOpened():
    print('cam nahi khula')


while True:
    ret, frame = cap.read()

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

    largest_contour_green = max(contours_green, key=cv.contourArea)
    largest_contour_brown = max(contours_brown, key=cv.contourArea)
     
    x, y, w, h = cv.boundingRect(largest_contour_green)
    x_b, y_b, w_b, h_b = cv.boundingRect(largest_contour_brown)

    buffer = 20
    cv.rectangle(contour_image, (x-buffer, y-buffer), (x + w+buffer, y + h +buffer), (0, 0, 255), 2)
    cv.rectangle(contour_image, (x_b-buffer, y_b-buffer), (x_b + w_b+buffer, y_b + h_b +buffer), (255, 0 , 0), 2) 

    
    
    cv.imshow("Bounding Box", contour_image)
    

    cv.imshow('cam', frame)
    cv.imshow('cam_hsv', hsv_frame)
    # cv.imshow('contours', contour_image)
    
    if cv.waitKey(1) == ord('q'):
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

