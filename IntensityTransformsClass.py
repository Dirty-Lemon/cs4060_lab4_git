import cv2
import numpy as np

class IntensityTransforms():
    def __init__(self):
        print("Intensity Transformations")
        
    # Read image
    def myReadImg(self, imgName):
        imgPath = 'img/' + imgName      # All images will be in the img folder
        print("Reading " + imgName + "...")
        return cv2.imread(imgPath)
    
    # Display image
    def myShowImg(self, img):
        cv2.imshow("Image", img)
        cv2.waitKey(0)
    
    # Takes a 2D array of images to show on one display
    def showMultImg(self, imgsArray):
        print("Loading multiple images...")
        
        imgNum = 1
        for img in imgsArray:
            title = 'Image ' + str(imgNum)
            cv2.imshow(title, img)
            imgNum += 1
            
        cv2.waitKey(0)
    
    # Performs negative transformation function on an image
    # s = L - 1 - r
    def negTransform(self, r):
        print("Applying negative transformation to image...")
        L = r.max()
        s = L - 1 - r
        return s
    
    # Performs the Power Law transformation function on an image
    # s = cr^(gamma)
    def powerLawTransform(self, imgData, gammaVal):
        print("Applying power law transformation to image...")
        r = imgData / 255
        s = r ** gammaVal
        return s
    
    # Performs the Log transformation function on an image
    # s = log(1 + r)
    def logTransform (self, r):
        print("Applying log transformation to image...")
        r = r / 255
        s = np.log(1 + r)
        return s