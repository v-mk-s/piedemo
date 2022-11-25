import os
import argparse
from .checkpoint import rclone_host_file


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='host command',
                                       description="help with checkpoints saving and loading",
                                       dest='command')
    host_parser = subparsers.add_parser('host')
    host_parser.add_argument('path', type=str)

    web_parser = subparsers.add_parser('web')
    web_parser.add_argument('function', type=str)
    web_parser.add_argument('--port', type=int)
    web_parser.add_argument('--host', type=str)

    args = parser.parse_args()
    return args


def execute(command, path):
    if command == 'host':
        print("Host model option")
        gdrive = rclone_host_file(path)
        filename = os.path.basename(path)
        print("Url: ")
        print(f"https://drive.google.com/open?id={gdrive}")
        print("Filename: ")
        print(filename)
        print("Code:")
        print(f"PretrainedCheckpoint(gdrive='{gdrive}',\n"
              f"                     filename='{filename}')")

    elif command == 'web':
        pass


if __name__ == "__main__":
    execute(**vars(parse_args()))
