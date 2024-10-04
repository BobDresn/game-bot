import pyautogui as pag
import cv2 as cv
import numpy as np
import time
import mss
import os


def showImage(image):
    cv.imshow('image', image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    
    
def findImage(image, frame,x=0, y=0, w=0, h=0):   
    #Loads image into opencv format
    image = cv.imread(image)
    
    #Converts screenshot to numpy array
    numpyScreenshot = np.array(frame)
    
    #Converts both images into grayscale
    grayFrame = cv.cvtColor(numpyScreenshot.astype(np.uint8), cv.COLOR_BGR2GRAY)
    grayImage = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    #This is where the magic happens
    result = cv.matchTemplate(grayImage, grayFrame, cv.TM_CCOEFF_NORMED)
    
    #How correct the match needs to be IOT consider pressing on entity
    threshold = 0.6
 
    
    loc = np.where(result >= threshold)
    instances = [] 
    for pt in zip(*loc[::-1]):
        instances.append((pt, (pt[0] + image.shape[1], pt[1] + image.shape[0])))
    #Gives our data to play with
    minVal, maxVal, minLoc, maxLoc = cv.minMaxLoc(result)

    #*********************************************************************************
    #This is to draw rectangle to correct size, use later for button pressing with pag
    (startX, startY) = maxLoc
    endX = startX + image.shape[1]
    endY = startY +  image.shape[0]
    centerX = (startX + image.shape[1] / 2)
    centerY = (startY +  image.shape[0] / 2)
    #*********************************************************************************

    #Draws rectangle on image, really only good for testing
    for each in instances:
        cv.rectangle(numpyScreenshot, (each[1], each[0]), (endX ,endY), (0, 255, 0), 2)
    showImage(numpyScreenshot)
    #^^^^^^^^Uncomment  to see rectangle drawn on screenshot^^^^
    

    
    return numpyScreenshot

showImage(findImage('eliteFomorianMage.png', cv.imread('training.png')))





















# with mss.mss() as sct:
#     while True:
#         start_time = time.time()
#         frame = np.array(sct.grab(sct.monitors[0]))
#         frame = cv.cvtColor(frame, cv.COLOR_BGRA2BGR)
#         print(findImage('X.png', frame))
#         end_time = time.time()
#         print(f"Time taken to capture screenshot: {end_time - start_time} seconds")