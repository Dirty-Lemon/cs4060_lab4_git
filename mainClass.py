from IntensityTransformsClass import *

class main():
    i = IntensityTransforms()
    i.helloIntTrans()
    
    # Task 1 - Gray Scale Images
    lenaImg = i.myReadImg('lena.tif')
    i.myShowImg(lenaImg)
    i.toNegImg(lenaImg)
    
    # Task 2 - Log Contrast Stretching
    
if __name__ == "__main__":
    main()