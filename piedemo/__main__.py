import os
import argparse
from .checkpoint import rclone_host_file
from .auto import function2fields, import_function
from .webdemo import WebDemo


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(help='host command',
                                       description="help with checkpoints saving and loading",
                                       dest='command')
    host_parser = subparsers.add_parser('host')
    host_parser.add_argument('path', type=str)

    web_parser = subparsers.add_parser('web')
    web_parser.add_argument('path', type=str)
    web_parser.add_argument('--port', type=int, default=8008)
    web_parser.add_argument('--host', type=str, default='0.0.0.0')

    args = parser.parse_args()
    return args


def execute(command, path,
            port=8008,
            host='0.0.0.0'):
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
        fn, name = import_function(path)
        input_fields, output_fields = function2fields(fn)
        web = WebDemo(name=name,
                      demo_function=fn,
                      inputs=input_fields,
                      outputs=output_fields)
        web.run(host=host, port=port)


if __name__ == "__main__":
    execute(**vars(parse_args()))
