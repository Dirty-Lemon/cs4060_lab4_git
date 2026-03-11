from IntensityTransformsClass import *

class main():
    i = IntensityTransforms()
    
    # Read initial image
    lenaImg = i.myReadImg('lena.tif')
    i.myShowImg(lenaImg)
    
    # Task 1 part a) - negative transformation
    negativeImg = i.negTransform(lenaImg)
    i.myShowImg(negativeImg)
    
    # Task 1 part b) - power-law transformation
    powCompressImg1 = i.powerLawTransform(lenaImg, 0.01)   # Perform gamma compression
    powCompressImg2 = i.powerLawTransform(lenaImg, 0.05)   # Perform gamma compression
    powCompressImg3 = i.powerLawTransform(lenaImg, 0.2)    # Perform gamma compression
    powCompressImg4 = i.powerLawTransform(lenaImg, 0.5)    # Perform gamma compression
    
    # Show all gamma-compressed images on one chart
    powCompressImgArray = [powCompressImg1, powCompressImg2, powCompressImg3, powCompressImg4]
    i.showMultImg(powCompressImgArray)
    
    powExpandImg1 = i.powerLawTransform(lenaImg, 1.5)  # Perform gamma expansion
    powExpandImg2 = i.powerLawTransform(lenaImg, 2)    # Perform gamma expansion
    powExpandImg3 = i.powerLawTransform(lenaImg, 3)    # Perform gamma expansion
    powExpandImg4 = i.powerLawTransform(lenaImg, 5)    # Perform gamma expansion
    
    # Show all gamma-expanded images on one chart
    powExpandImgArray = [powExpandImg1, powExpandImg2, powExpandImg3, powExpandImg4]
    i.showMultImg(powExpandImgArray)
    
    # Task 2 - Log Contrast Stretching
    # What is FTspectrum.tif?
    logImg = i.logTransform(lenaImg)
    i.myShowImg(logImg)
    
if __name__ == "__main__":
    main()