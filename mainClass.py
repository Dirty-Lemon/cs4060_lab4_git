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
    
    # Show all gamma-compressed images at once
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
    ftSpectrumImg = i.myReadImg('FTspectrum.tif')
    i.myShowImg(ftSpectrumImg)      # Show original image for comparison
    
    # Log constrast stretching on FTspectrum.tif
    logFtSpectrumImg = i.logTransform(ftSpectrumImg)
    i.myShowImg(logFtSpectrumImg)
    
    # Log constrast stretching on lena.tif
    i.myShowImg(lenaImg)            # Show original image for comparison
    logLenaImg = i.logTransform(lenaImg)
    i.myShowImg(logLenaImg)
    
if __name__ == "__main__":
    main()