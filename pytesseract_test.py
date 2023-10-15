from PIL import Image

import pytesseract
#im = Image.open('document/book1/1.jpg')
#im.save('document/book1/1.png')

print(pytesseract.image_to_string(Image.open('document/book1/1.png')))
