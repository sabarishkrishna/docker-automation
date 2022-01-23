import argparse
import pyfiglet
from mongo import *


result = pyfiglet.figlet_format("DOCKER WEB-AUTOMATE")
print(result)
parser = argparse.ArgumentParser()
parser.add_argument("--stack", help="mean stack setup")
parser.add_argument("--file", help="username for your service", choices = ["all","comp","dock"])
parser.add_argument("--dock", help="username for your service")
parser.add_argument("--all", help="username for your service")
# parser.add_argument("--python-dev", help="password for your service")
parser.add_argument("--port", help="allote port")
parser.add_argument("--os", help="seecify os")
parser.add_argument("--app", type=str, help="seecify app")
parser.add_argument("--username", help="username for your service")
parser.add_argument("--password", help="username for your service")
# parser.add_argument("--operation", help="command to create to dockerfile/compose-file/both", choices=["doc","com","all"])

args = parser.parse_args()

if args.stack == "mean":
    if args.file == "all":
        compose = Mongo(args.username, args.password)
        compose.mongo_compose_file()
        compose.dock_file(args.os, args.app, args.port)
    
    elif args.file == "comp":
        compose = Mongo(args.username, args.password)
        compose.mongo_compose_file()
    
    elif args.file == "dock":
        compose = Mongo(None, None)
        compose.dock_file(args.os, args.app, args.port)
