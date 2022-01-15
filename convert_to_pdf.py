from fpdf import FPDF
pdf = FPDF()

imageList = []

print("Création de la liste")
for i in range (1,42):
    imageList.append("images_croped/" + str(i) + "_CROPED.png")

print("Génération du PDF...")
count = 1
for image in imageList:
    print("Ajout de la page " + str(count) + " en cours...")
    pdf.add_page()
    pdf.image(image,0,0,210,300)
    count += 1
print("Finalisation")
pdf.output("output.pdf", "F")   