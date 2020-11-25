import argparse
import multiprocessing as mp
import numpy as np
import cv2 as cv


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', metavar='image', type=str,
                        help='Image Filename', required=True)
    parser.add_argument('-m', '--message', metavar='message', type=str,
                        help='Message Filename', required=True)
    parser.add_argument('-k', '--key', metavar='key', nargs=2, type=int,
                        required=True, help='OFFSET INTERLEAVE in pixels')
    return parser.parse_args()


def show(img):
    cv.imshow("display", img)
    cv.waitKey(0)


if __name__ == '__main__':
    args = get_args()
    img = cv.imread(args.image)

    msg = open(args.message, 'rb').read().rstrip()
    msg = "".join([format(x, '#010b')[2:] for x in msg])
    pixel = [0, 0]
    pixel[1] += args.key[0]
    while img.shape[1] <= pixel[1]:
        pixel[1] -= img.shape[1]
        pixel[0] += 1
    msg_idx = 0
    L = len(msg)
    while msg_idx < L:
        for color in range(3):
            byte = format(img.item(pixel[0], pixel[1], color), '#010b')
            byte = list(byte)
            byte[-1] = msg[msg_idx]
            byte = ''.join(byte)
            msg_idx += 1
            byte = int(byte, 2)
            img.itemset((pixel[0], pixel[1], color), byte) 

            if msg_idx == L:
                break
        pixel[1] += args.key[1]
        while img.shape[1] <= pixel[1]:
            pixel[1] -= img.shape[1]
            pixel[0] += 1
    
    if not cv.imwrite('encoded_image.png', img):
        raise Exception("Could not write image")
    else:
        print(f'key is {args.key[0]} {args.key[1]} {int(L/8)}')
