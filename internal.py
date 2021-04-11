
from os import system
from sys import stdout
from platform import system as check_system

from typing import Tuple, Union


# useful constants
__IS_WINDOWS = check_system() == 'Windows'


class Color:
    '''
    Each "pixel" is a Color object
    '''

    ENDCOLOR = '\033[0m'

    def __init__(self, r: int = 0, g: int = 0, b: int = 0):
        self.r = r
        self.g = g
        self.b = b

    def get_color_code(self):
        # the space is what makes the color show up
        return f'\x1b[48;2;{self.r or 0};{self.g or 0};{self.b or 0}m '
        # return f'({self.r};{self.g};{self.b})'

    def __repr__(self) -> str:
        return f'({self.r}, {self.g}, {self.b})'


class Canvas():
    def __init__(self, w: int = 1, h: int = 1) -> None:
        if w < 1 or h < 1:
            raise ValueError('Width and height must be greater than one')

        self.__width = w
        self.__height = h

        self.__grid = [
            [Color(0, 0, 0) for x in range(self.__width)]  # NOSONAR
            for y in range(self.__height)  # NOSONAR
        ]

    def get_pixels(self):
        '''
        Return the all pixels
        '''

        temp = (j for i in self.__grid for j in i)
        return [(i.r, i.g, i.b) for i in temp]

    # def set_pixels(self, pixels: Union[List])

    def background(self, _col: Union[Color, Tuple[int, int, int]]):

        col = Color(_col[0], _col[1], _col[2]) \
            if isinstance(_col, tuple) \
            else _col

        # set every pixel to one color

        for x in range(self.__width):
            for y in range(self.__height):
                self.__grid[y][x].r = col.r
                self.__grid[y][x].g = col.g
                self.__grid[y][x].b = col.b

    def show(self) -> None:
        clear_screen()
        str_to_show = '\n'.join([
            ''.join(self.__grid[y][x].get_color_code()
                    for x in range(self.__width))+Color.ENDCOLOR
            for y in range(self.__height)
        ])
        stdout.write(str_to_show)
        # return arr_to_show


def clear_screen() -> None:
    '''
    Clears colors and screen
    '''

    stdout.write(Color.ENDCOLOR)
    if __IS_WINDOWS:
        system('cls')
    else:
        system('clear')


if __name__ == '__main__':

    # in case the colors are messed up
    clear_screen()
