# Generate some containers with ssh for test environment

import argparse
import subprocess as cmd

parser = argparse.ArgumentParser()
parser.add_argument("type", help="ubuntu, debian or centos")
parser.add_argument("number", help="number of containers to deploy", type=int)
args = parser.parse_args()

print(args.type)

if args.type == "debian":
    cmd.run("docker pull noxas69/linux_ssh:debian10", shell=True)
    for c in range(args.number):
        cmd.run(f"docker run -d --name debian{c} noxas69/linux_ssh:debian10", shell=True)
        cmd.run(f"docker inspect debian{c} | grep '\"IPAddress\"' | head -n 1", shell=True)
        

elif args.type == "ubuntu":
    cmd.run("docker pull noxas69/linux_ssh:ubuntu20.04", shell=True)
    for c in range(args.number):
        cmd.run(f"docker run -d --name ubuntu{c} noxas69/linux_ssh:ubuntu20.04", shell=True)
        cmd.run(f"docker inspect ubuntu{c} | grep '\"IPAddress\"' | head -n 1", shell=True)


else:
    print("Enter a valid name of linux ditrib (ubuntu, debian)")