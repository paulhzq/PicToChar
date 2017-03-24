# -*- coding: utf-8 -*-
#python 2.7
from PIL import Image
import argparse

#Terminal add_argument processing
parser = argparse.ArgumentParser()

parser.add_argument('file')     #input file
parser.add_argument('-o', '--output')   #output file
parser.add_argument('--width', type = int, default = 80) #output string width
parser.add_argument('--height', type = int, default = 80) #output string height

#get all the argument in the terminal.
args = parser.parse_args()

IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output

#base on the result,the total list number could be changed
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# convert RGB to grayscale and eventually to ascii_char
def get_char(r,g,b,alpha = 1.0):#RGBA color model
    if alpha == 0:
        return ' ' #
    length = len(ascii_char)
    gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)# convert RGB to grayscale.

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(IMG)
    im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

    txt = ""
    for i in range(HEIGHT):
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i))) #append to txt
        txt += '\n'

    print txt

    #output to OUTPUT or output.txt file.
    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)
    else:
        with open("output.txt",'w') as f:
            f.write(txt)
