import cv2

class IntensityTransforms():
    def __init__(self):
        print("Intensity Transforms")
        
    def helloIntTrans(self):
        print("Hello IT")
        
    # Read image
    def myReadImg(self, imgName):
        imgPath = 'img/' + imgName
        print("Reading " + imgName + "...")
        return cv2.imread(imgPath)
    
    # Display image
    def myShowImg(self, img):
        cv2.imshow("Image", img)
        cv2.waitKey(0)
    
    # Convert image to negative
    def toNegImg(self, img):
        print("Converting to negative image...")