import pygame as pg


class ImageLoader:

    def __init__(self):
        pass

    def load_images(self, ImageCount, PathLeavingTrailingNumber, FileExtension, ConvertAlpha=False):
        images = []
        for i in range(0,ImageCount):
            if ConvertAlpha:
                image = pg.image.load(PathLeavingTrailingNumber + str(i) + '.' + FileExtension).convert_alpha()
            else:
                image = pg.image.load(PathLeavingTrailingNumber + str(i) + '.' + FileExtension).convert()
            images.append(image)
        return images

    def down_scale_images(self, Images, Amount):
        scaled_images = []
        for image in Images:
            scaled_image = pg.transform.scale(image, (image.get_width() // Amount, image.get_height() // Amount))
            scaled_images.append(scaled_image)
        return scaled_images
