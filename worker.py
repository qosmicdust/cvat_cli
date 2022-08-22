from argparse import ArgumentParser
from os import remove, join, listdir
from os.path import isdir
from subprocess import run
import sys


parser = ArgumentParser(description='')
parser.add_argument(
    '-c', '--create', help='create tasks')
parser.add_argument(
    '-r', '--remove', nargs='+', type=int, help='remove tasks')
parser.add_argument(
    '-d', '--dump', nargs='+', type=int, help='dump annotation')
parser.add_argument(
    '-l', '--labels', help='label path')
parser.add_argument(
    '-o', '--output', help='output file name')
args = parser.parse_args()

auth = 'account:password'
host = 'localhost'
port = 8080


def create(src, label):

    global auth
    global host
    global port

    if not isdir(src):
        print(f'{src} is not a directory.')
        sys.exit()
    else:
        for dir in listdir(src):
            images = []
            if '.DS' in dir:
                remove(join(src, dir))
                print('.DS_store has been removed.')
            elif listdir(join(src, dir)) and '@' not in dir:
                for img in listdir(join(src, dir)):
                    images.append(join(src, dir, img))

                cmd = f'python cli.py --auth {auth} --server-host {host} ' +\
                    f'--server-port {port} create "{dir}" --labels {label} ' +\
                    f'local {" ".join(images)}'
                # print(cmd)
                run(cmd, shell=True)
            else:
                print(f'no files in {dir}')


def delete(task_ids):

    global auth
    global host
    global port

    for i in range(task_ids[0], task_ids[-1]+1):
        cmd = f'python cli.py --auth {auth} --server-host {host} ' +\
            f'--server-port {port} delete {i}'
        # print(cmd)
        run(cmd, shell=True)


def dump(task_ids, output_path):

    global auth
    global host
    global port

    for task_id in range(task_ids[0], task_ids[-1]+1):

        output = join(output_path, str(task_id)+'.json')

        cmd = f'python cli.py --auth {auth} --server-host {host} ' +\
            f'--server-port {port} dump --format "COCO 1.0" {task_id} {output}'
        # print(cmd)
        run(cmd, shell=True)


if __name__ == '__main__':

    if args.create and args.labels:
        create(args.create, args.labels)
    elif args.remove:
        delete(args.remove)
    elif args.dump:
        dump(args.dump, args.output)
