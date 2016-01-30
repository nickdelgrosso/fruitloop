__author__ = 'nicholas'

from .camera import Camera
from .mixins import Color

class Light(Camera, Color):

    def __init__(self, *args, **kwargs):
        super(Light, self).__init__(*args, **kwargs)