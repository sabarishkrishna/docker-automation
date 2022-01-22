# Python code to create a file
import argparse
import pyfiglet


def mongo(username, password):

    file = open('docker-compose.yml','w')

    file1 = """
    version: '3.9'

    services:

    mongo:
        image: mongo
        restart: always
        ports:
            - 27017:27017
        environment:
            MONGO_INITDB_ROOT_USERNAME: {username}
            MONGO_INITDB_ROOT_PASSWORD: {password}

    mongo-express:
    i   mage: mongo-express
        restart: always
        ports:
            - 8081:8081
        environment:
            ME_CONFIG_MONGODB_ADMINUSERNAME: root
            ME_CONFIG_MONGODB_ADMINPASSWORD: example
            ME_CONFIG_MONGODB_URL: mongodb://root:example@mongo:27017/

    """

    file.write(file1.format(username = username, password = password))
    file.close()


def doc_file(image, app, port):
    file = open('Dockerfile','a+')
    file1 = """
FROM {image}
RUN apt update && apt upgrade -y
RUN apt install {app} -y
RUN bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/
EXPOSE {port}

    """

    file.write(file1.format(image = image, app = app, port = port))
    file.close()
    print("[+] compose file is saved...")





if __name__== "__main__":
    result = pyfiglet.figlet_format("DOCKER WEB-AUTOMATE")
    print(result)
    parser = argparse.ArgumentParser()
    parser.add_argument("--service", help="command to to give service")
    parser.add_argument("--username", help="username for your service")
    parser.add_argument("--password", help="password for your service")
    parser.add_argument("--port", help="allote port")
    parser.add_argument("--os", help="seecify os")
    parser.add_argument("--app", nargs='*', type=str, help="seecify app")
    parser.add_argument("--operation", help="command to create to dockerfile/compose-file/both", choices=["doc","com","all"])

    args = parser.parse_args()


    if args.service == "mongo":
        username = args.username
        password = args.password
        if(username) and (password):
            mongo(username, password)
            
            
        else:
            parser = argparse.ArgumentParser()
            parser.add_argument("--username", help="username for your service")
            parser.add_argument("--password", help="password for your service")


            

    if args.operation == "com":
        pass
    elif args.operation == "doc":
        
        if(args.os) and (args.app) and (args.port):

            image = args.os
            app = args.app
            port = args.port
  
            doc_file(image, app, port)
                


        else:
            print("--os", "give the image")
            print("--app", "specify the app")
            print("--port", "specify the port to expose")


        

