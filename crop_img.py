# Importing Image class from PIL module
from PIL import Image

# Before chapter 1 impair
MARGE_PAIRE_X = 350
MARGE_PAIRE_Y = 300
MARGE_PAIRE_W = 1250
MARGE_PAIRE_H = 1800


MARGE_IMPAIRE_X = 0
MARGE_IMPAIRE_Y = 270
MARGE_IMPAIRE_W = 1300
MARGE_IMPAIRE_H = 1800

def processingPicture(picturePath, pictureName):
    # Opens a image in RGB mode
    im = Image.open(picturePath)
    width, height = im.size
    # Cropped image of above dimension
    # (It will not change original image)
    if((pictureName % 2 )==0):
        im1 = im.crop((MARGE_PAIRE_X, MARGE_PAIRE_Y, MARGE_PAIRE_W + MARGE_PAIRE_X, MARGE_PAIRE_H + MARGE_PAIRE_Y))
    else:
        im1 = im.crop((MARGE_IMPAIRE_X, MARGE_IMPAIRE_Y, MARGE_IMPAIRE_W + MARGE_IMPAIRE_X, MARGE_IMPAIRE_H + MARGE_IMPAIRE_Y))
    im1.save("images_croped/" + str(pictureName) + "_CROPED.png")



print("Création de la liste")
for i in range (1,42):
    print("Image : " + str(i))
    processingPicture("images/" + str(i) + ".png", i)
