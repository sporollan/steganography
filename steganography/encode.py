import argparse
import multiprocessing as mp
import cv2 as cv


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', metavar='image', type=str,
                        help='Image Filename', required=True)
    parser.add_argument('-m', '--message', metavar='message', type=str,
                        help='Message Filename', required=True)
    return parser.parse_args()


def show(img):
    cv.imshow("display", img)
    cv.waitKey(0)


if __name__ == '__main__':
    args = get_args()
    img = cv.imread(args.image)
    msg = open(args.message, 'r').read().rstrip()



    if not cv.imwrite('encoded_image.png', img):
        raise Exception("Could not write image")
