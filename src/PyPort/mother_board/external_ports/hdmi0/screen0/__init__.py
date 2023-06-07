from pygame import display, gfxdraw, surface, draw, PixelArray
from pygame import init as init_display
from pygame.locals import *
from pygame.time import Clock
from pygame import image
from ctypes import c_ubyte
from threading import Thread

SIZE: tuple = (1000,500)

INSTRUCTIONS = {
    0x00: lambda *args: 0x00,
    0x01: lambda self, x, y, color: self.draw_pixel(x,y,color),
    0x02: lambda self: self.show(self),
    0x03: lambda self, *args: self.past_pixel_array_1d(*args),
    0x06: lambda self: 0x08,
    0xF: lambda self, *args: self.close()
}


class Screen:
    def __init__(self, size=(800, 600)) -> None:
        return
        init_display()

        self.window = display.set_mode(size, DOUBLEBUF | HWSURFACE)
        self.clock = Clock()
        self.show(self)
        self.started = True

    def draw_pixel(self, x, y, color):
        #self.p_arr[x, y] = color
        self.window.set_at((x, y), color)
        #gfxdraw.pixel(self.temp_surface, x, y, color)
        #self.temp_surface.fill(color, ((x, y), (1, 1)))

    def past_pixel_array_1d(self, x, y, pixel_array_1d, size, alpha):
        pixel_array_1d = (c_ubyte * len(pixel_array_1d))(*pixel_array_1d)
        if (alpha):
            temp = image.frombuffer(pixel_array_1d, size, "RGBA").convert_alpha()
        else:
            temp = image.frombuffer(pixel_array_1d, size, "RGB").convert()

        self.window.blit(temp, (x, y))

    @staticmethod
    def show(self):
        #self.window.blit(self.temp_surface, (0, 0))
        display.flip()
        self.window.fill((0, 0, 0))
        self.clock.tick(60)

    def send_message(self, binary, *args):
        if binary in INSTRUCTIONS:
            return INSTRUCTIONS[binary](self, *args)

    def close(self):
        self.started = False
        display.quit()
        return (0x00)

def loader(hw):
    screen = Screen()

    return screen