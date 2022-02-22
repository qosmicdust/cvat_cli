import argparse
import os
import subprocess
import sys


parser = argparse.ArgumentParser(description='')
parser.add_argument('-c','--create', help='create tasks')
parser.add_argument('-r','--remove', nargs='+', type=int, help='remove tasks')
parser.add_argument('-d','--dump', nargs='+', type=int, help='dump annotation')
parser.add_argument('-l','--labels', help='label path')
parser.add_argument('-o','--output', help='output file name')
args = parser.parse_args()

# edit here
auth = 'login_id:login_password'
host = 'server_ip_address_or_localhost'
port = 'port_number_E.g._8080'


def create(src,label):

    global auth
    global host
    global port

    if not os.path.isdir(src):
        print(f'{src} is not a directory.')
        sys.exit()
    else:

        for dir in os.listdir(src):
            images = []
            if '.DS' in dir:
                os.remove(os.path.join(src,dir))
                print('.DS_store has been removed.')
            elif os.listdir(os.path.join(src,dir)):
                for img in os.listdir(os.path.join(src,dir)):
                    images.append(os.path.join(src,dir,img))

                label = 'test_labels.json'
                cmd = f'python cli.py --auth {auth} --server-host {host} --server-port {port} create "{dir}" --labels {label} local {" ".join(images)}'
                # print(cmd)
                subprocess.call(cmd,shell=True)
            else:
                print(f'no files in {dir}')


def delete(task_ids):

    global auth
    global host
    global port

    for i in range(task_ids[0],task_ids[-1]+1):
        cmd = f'python cli.py --auth {auth} --server-host {host} --server-port {port} delete {i}'
        # print(cmd)
        subprocess.call(cmd,shell=True)


def dump(task_ids,output):

    global auth
    global host
    global port

    for task_id in range(task_ids[0],task_ids[-1]+1):

        output = str(task_id)+'.json'
        cmd = f'python cli.py --auth {auth} --server-host {host} --server-port {port} dump --format "COCO 1.0" {task_id} {output}'
        # print(cmd)
        subprocess.call(cmd,shell=True)


if __name__=='__main__':

    if args.create and args.labels:
        create(args.create,args.labels)
    elif args.remove:
        delete(args.remove)
    elif args.dump:
        dump(args.dump,args.output)