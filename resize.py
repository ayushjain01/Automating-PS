from PIL import Image
path = r"C:\Users\Ayush Jain\Downloads\christopher-campbell-rDEOVtE7vOs-unsplash.jpg"
im1 = Image.open(path)

width, height = im1.size
width = round(width/1.25)
height = round(height/1.25)
newsize = (width,height)
im1 = im1.resize(newsize)
im1.save(path)