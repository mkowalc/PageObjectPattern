import ctypes
import os
from PIL import Image
from subprocess import call


LibName = 'prtscn.so'
AbsLibPath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + LibName
grab = ctypes.CDLL(AbsLibPath)

def grab_screen(x1,y1,x2,y2):
    w, h = x1+x2, y1+y2
    size = w * h
    objlength = size * 3

    grab.getScreen.argtypes = []
    result = (ctypes.c_ubyte*objlength)()

    grab.getScreen(x1,y1, w, h, result)
    return Image.frombuffer('RGB', (w, h), result, 'raw', 'RGB', 0, 1)

def save_screen(image, case_name, name):

    image.save('screens/' + case_name + '/' + name + '.bmp')
