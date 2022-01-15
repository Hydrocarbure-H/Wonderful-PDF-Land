from pdf2image import *
from fpdf import FPDF
from PIL import Image
import os

file = open("sav.txt", "r")
lignes = file.readlines()

FILENAME = input("Nom du fichier : ")

MARGE_PAIRE_X = int(lignes[1])
MARGE_PAIRE_Y = int(lignes[2])
MARGE_PAIRE_W = int(lignes[3])
MARGE_PAIRE_H = int(lignes[4])
MARGE_IMPAIRE_X = int(lignes[5])
MARGE_IMPAIRE_Y = int(lignes[6])
MARGE_IMPAIRE_W = int(lignes[7])
MARGE_IMPAIRE_H = int(lignes[8])
file.close()

def pdfToImg():
    # Convert PDF pages into pictures
    # Return the number of pages
    print('\033[1m' + 'Démarrage...' + '\033[0m')
    pages = convert_from_path(FILENAME)
    a = 1
    for page in pages:
        print("Conversion de la page " + str(a) + " en image en cours...")
        page.save('images/' + str(a)  + '.png', 'PNG')
        a += 1
    print('\033[1m' + 'Le document est donc constitué de ' + str(a) + ' pages.' + '\033[0m')
    return a

def countPages():
    # Count PDF pages
    # Return the number of pages
    print('\033[1m' + 'Chargement du nombre de pages...' + '\033[0m')
    pages = convert_from_path(FILENAME)
    a = 1
    for page in pages:
        a += 1
    print('\033[1m' + 'Le document est donc constitué de ' + str(a) + ' pages.' + '\033[0m')
    return a

########################
#1 Extraction pdf ==> img
first = input("Démarrer depuis le début ? [no][yes]")
if first == "yes":
    PAGE_AMOUNT = pdfToImg()
else :
    nb_pages = input("Nombre de pages du document : [no][*int*] ")
    if nb_pages == "no":
        PAGE_AMOUNT = countPages()
    else :
        PAGE_AMOUNT = int(nb_pages)
#######################


def rotateImg():
    # Crop pictures to have the right position
    for i in range (1,PAGE_AMOUNT):
        print("Rotation de la page " + str(i) + " en cours...")
        rotatePicture("images/" + str(i) + ".png", i)

def rotatePicture(picturePath, pictureNumber):
    # Rotate the picture
    file = open("sav.txt", "r")
    lignes = file.readlines()
    ANGLE_PAIRE = int(lignes[10])
    ANGLE_IMPAIRE = int(lignes[11])
    file.close()
    im = Image.open(picturePath)
    if((pictureNumber % 2 )==0):
        im1 = im.rotate(ANGLE_PAIRE)
    else:
        im1 = im.rotate(ANGLE_IMPAIRE)
    im1.save("images_rotate/" + str(pictureNumber) + "_ROTATE.png")

def cropImg():
    # Crop pictures to have the right position
    for i in range (1,PAGE_AMOUNT):
        print("Rognage de la page " + str(i) + " en cours...")
        processingPicture("images/" + str(i) + ".png", i)

def processingPicture(picturePath, pictureNumber):
    # Create the croped picture
    file = open("sav.txt", "r")
    lignes = file.readlines()
    MARGE_PAIRE_X = int(lignes[1])
    MARGE_PAIRE_Y = int(lignes[2])
    MARGE_PAIRE_W = int(lignes[3])
    MARGE_PAIRE_H = int(lignes[4])
    MARGE_IMPAIRE_X = int(lignes[5])
    MARGE_IMPAIRE_Y = int(lignes[6])
    MARGE_IMPAIRE_W = int(lignes[7])
    MARGE_IMPAIRE_H = int(lignes[8])
    file.close()

    im = Image.open(picturePath)
    width, height = im.size
    if((pictureNumber % 2 )==0):
        im1 = im.crop((MARGE_PAIRE_X, MARGE_PAIRE_Y, MARGE_PAIRE_W + MARGE_PAIRE_X, MARGE_PAIRE_H + MARGE_PAIRE_Y))
    else:
        im1 = im.crop((MARGE_IMPAIRE_X, MARGE_IMPAIRE_Y, MARGE_IMPAIRE_W + MARGE_IMPAIRE_X, MARGE_IMPAIRE_H + MARGE_IMPAIRE_Y))
    im1.save("images_croped/" + str(pictureNumber) + "_CROPED.png")

def imgToPDF():
    # Build the PDF t
    pdf = FPDF()
    imageList = []
    for i in range (1,PAGE_AMOUNT):
        imageList.append("images_croped/" + str(i) + "_CROPED.png")

    print('\033[1m' + 'Génération du PDF...' + '\033[0m')
    count = 1
    for image in imageList:
        print("Ajout de la page " + str(count) + " en cours...")
        pdf.add_page()
        pdf.image(image,0,0,210,300)
        count += 1
    print('\033[1m' + 'Finalisation...' + '\033[0m')
    pdf.output(FILENAME + "_out.pdf", "F")
    print("Terminé !")

rotate = input("Faire une rotation sur les pages ? [no][yes]")
while (rotate == "yes"):
    #######################
    #2 rotation / traitement
    rotateImg()
    #######################
    rotate = input('\033[1m' + 'Relancer la rotation ? [no][yes] ' + '\033[0m')

print("Rognage en cours...")

get_out = "re"
while (get_out == "re"):
    #######################
    #2bis remargement / traitement
    cropImg()
    #######################
    get_out = input('\033[1m' + 'Relancer le rognage ? [re][fin] ' + '\033[0m')

#######################
#3 fusion image ==> pdf
imgToPDF()
#######################