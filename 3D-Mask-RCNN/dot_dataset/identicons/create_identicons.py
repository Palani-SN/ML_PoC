import os
import uuid
import pydenticon
import cv2
import numpy as np
import tifffile as tif

generator = pydenticon.Generator(10, 10)

class Identicon:

    def __init__(self, inp_str:str = None) -> None:
        
        if inp_str == None:
            inp_str = str(uuid.uuid4())
        self.__uuid = inp_str

    def save(self, file_name):

        identicon = generator.generate(self.__uuid, 30, 30, output_format='png')

        f = open(f"{file_name}.png", "wb")
        f.write(identicon)
        f.close()

        __blank = np.zeros((9, 30, 30, 3), dtype=np.uint8)
        inp_img = cv2.imread(f"{file_name}.png")
        __blank[4] = inp_img
        kernel = np.ones((3,3),np.uint8)
        orders = [1,2,3,4]
        for order in orders:
            eroded = cv2.erode(inp_img, kernel, iterations = order)
            __blank[4-order] = eroded
            __blank[4+order] = eroded
            tif.imwrite(f'{file_name}.ome.tif', __blank, photometric='rgb')

if __name__ == '__main__':

    identicon_list = [ Identicon() for i in range(0, 5) ]
    for x in range(0, len(identicon_list)):
        print(f'saving dot_{x}')
        identicon_list[x].save(f'dot_{x}')