import argparse
import multiprocessing as mp


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--image', metavar='image', type=str,
                        help='Image Filename', required=True)
    parser.add_argument('-m', '--message', metavar='message', type=str,
                        help='Message Filename', required=True)
    return parser.parse_args()

if __name__ == '__main__':
    args = get_args()
