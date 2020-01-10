import pystray
from PIL import Image
__import__('os').chdir(r'C:\Users\Emre\Desktop')
image = Image.open('tayyib.jpg')
icon = pystray.Icon('test name',icon=image,title = 'deneme')
# def setup(icon):
icon.visible = True
# image = Image.fromarray(image.astype('uint8'), 'RGB')
icon.run()