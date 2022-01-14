from PIL import Image

main = Image.open("D:/All/Projects/Albumcover/CC/clipframe3600.jpg")
watermark = Image.open("paec-small.png")

area = (1020, 880) #For images = 1134x966
smallarea = (535, 280) #For Images = 640x360
smallerarea = (345, 292) #For Images = 422x360
main.paste(watermark, smallarea)

main.show()
main.save("output.jpg")