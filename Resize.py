import PIL
from PIL import Image
basewidth = 150
img= Image.open('Hasil Thresholding Inverted 1.jpg')
wpercent=(basewidth/float(img.size[0]))
hsize=int((float(img.size[1])*float(wpercent)))
img=img.resize((basewidth,hsize),PIL.Image.ANTIALIAS)
img.save('Hasil Resize.jpg')
