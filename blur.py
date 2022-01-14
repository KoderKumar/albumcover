from PIL import Image, ImageFile, ImageDraw, ImageChops, ImageFilter
 
OriImage = Image.open('D:/All/Projects/Albumcover/Cover/clipframe1000.jpg')
OriImage.show()

boxImage = OriImage.filter(ImageFilter.BoxBlur(1.5))
boxImage.show()

boxImage.save('clipframe1000blur.jpg')