import argparse
import pyfiglet
from subprocess import Popen,STDOUT,PIPE,run




def run_lab():
    run_cmd = run('docker-compose up --build -d',stdout=PIPE,shell=True,stderr=PIPE,text=True)
        # run1 = run('docker run -p 22:22 -d --cap-add=NET_ADMIN -it docker-lab_sabarish bash',stdout=PIPE,shell=True,stderr=PIPE,text=True)
    if(run_cmd):
        wg1 = run('docker exec -d sabarish ip link add wg0 type wireguard',stdout=PIPE,shell=True,stderr=PIPE,text=True)
        wg2 = run('docker exec -d sabarish ip addr add 172.31.0.4/32 dev wg0',stdout=PIPE,shell=True,stderr=PIPE,text=True)
        wg3 = run('docker exec -d sabarish wg set wg0 private-key ./privatekey',stdout=PIPE,shell=True,stderr=PIPE,text=True)
        wg4 = run('docker exec -d sabarish ip link set wg0 up',stdout=PIPE,shell=True,stderr=PIPE,text=True)
        wg4 = run('docker exec -d sabarish wg set wg0 listen-port 51820 peer Dot1GLD/9avuhrtaXZvroRAUYdQDMOmdK7z8uax9FBU= allowed-ips 172.31.0.0/24 endpoint 18.221.124.181:51820',stdout=PIPE,shell=True,stderr=PIPE,text=True)
        wg5 = run('docker exec -d sabarish route add -net 172.31.0.0/24 wg0',stdout=PIPE,shell=True,stderr=PIPE,text=True)
        if(wg1 and wg2 and wg3 and wg4 and wg5):
            print("[+] Lab is built...")
            print("[+] ssh using the ip address")



if __name__ == "__main__":
    result = pyfiglet.figlet_format("docker-labs")
    print(result)
    parser = argparse.ArgumentParser()
    parser.add_argument("build", help="build labs")
    args = parser.parse_args()

    if args.build == "build":
        run_lab()