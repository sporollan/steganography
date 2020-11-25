import argparse
import numpy as np
import cv2 as cv


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', metavar='image', type=str,
                        help='Image Filename', required=True)
    parser.add_argument('-k', '--key', metavar='key', nargs=2, type=int,
                        required=True, help='OFFSET INTERLEAVE in pixels')
    return parser.parse_args()

if __name__ == '__main__':
    
