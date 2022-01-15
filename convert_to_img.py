from pdf2image import *

pages = convert_from_path('./file.pdf')
a = 1

for page in pages:
    print("Page : " + str(a))
    page.save('images/' + str(a)  + '.png', 'PNG')
    a += 1

