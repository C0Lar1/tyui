from PIL import Image
from PIL import ImageFilter

class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = list()

    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print('Файл не найден!')
        self.original.show()

    def do_left(self):
        rotated = self.original.transpose(Image.FLIP_LEFT_RIGHT)
        self.changed.append(rotated)

MyImage = ImageEditor('original.jpg')
MyImage.open()

MyImage.do_left()
MyImage.do_cropped()

for im in MyImage.changed:
    im.show()
