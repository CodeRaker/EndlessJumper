import pygame as pg

class ImageLoader:
    def __init__(self):
        pass

    def LoadImages(self, imageCount, directoryFolder, nameLeavingTrailingNumber, fileExtension, convertAlpha=False):
        imageList = []
        for i in range(0,imageCount):
            if convertAlpha:
                image = pg.image.load(directoryFolder + nameLeavingTrailingNumber + str(i) + '.' + fileExtension).convert_alpha()
            else:
                image = pg.image.load(directoryFolder + nameLeavingTrailingNumber + str(i) + '.' + fileExtension).convert()
            imageList.append(image)
        return imageList

    def ScaleImages(self, imageList):
        scaledImages = []
        for image in imageList:
            scaledImage = pg.transform.scale(image, (image.get_width() // 2, image.get_height() // 2))
            scaledImages.append(scaledImage)
        return scaledImages
