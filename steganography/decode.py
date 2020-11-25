import argparse
import numpy as np
import cv2 as cv


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', metavar='image', type=str,
                        help='Image Filename', required=True)
    parser.add_argument('-k', '--key', metavar='key', nargs=3, type=int,
                        required=True, help='OFFSET INTERLEAVE MESSAGE_LENGTH')
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
    img = cv.imread(args.image)
    pixel = [0, 0]
    msg = [] 
    pixel[1] += args.key[0]
    while img.shape[1] <= pixel[1]:
        pixel[1] -= img.shape[1]
        pixel[0] += 1
    msL = 0
    while msL < args.key[2]*8:
        for color in range(3):
            byte = format(img.item(pixel[0], pixel[1], color), 'b')
            msg.append(byte[-1])
            msL += 1
        pixel[1] += args.key[1]
        while img.shape[1] <= pixel[1]:
            pixel[1] -= img.shape[1]
            pixel[0] += 1
    output = ''
    while len(msg) >= 8:
        b = ''
        for _ in range(8):
            b+=msg.pop(0)
        output += str(chr(int(b, 2)))
    print(f'message: {output}')
        
    
    
