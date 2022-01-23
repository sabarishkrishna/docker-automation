# Python code to create a file
import argparse
import pyfiglet

class Mongo:


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def mongo_compose_file(self):
        file = open('docker-compose.yml','w')
        compose = """
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
            image: mongo-express
            restart: always
            ports:
                - 8081:8081
            environment:
                ME_CONFIG_MONGODB_ADMINUSERNAME: root
                ME_CONFIG_MONGODB_ADMINPASSWORD: example
                ME_CONFIG_MONGODB_URL: mongodb://root:example@mongo:27017/
        """

        file.write(compose.format(username = self.username, password = self.password))
        file.close()
    
    def dock_file(self, image, app, port):
        file = open('Dockerfile','a+')
        docker = """
        FROM {image}
        RUN apt update && apt upgrade -y
        RUN apt install {app} -y
        RUN bash -c "$(curl -fsSL https://raw.githubusercontent.com/ohmybash/oh-my-bash/master/tools/
        EXPOSE {port}
        """

        file.write(docker.format(image = image, app = app, port = port))
        file.close()




# if __name__== "__main__":


    # compose = Mongo("sabarish", "password")
    # # compose.mongo_compose_file()
    # compose.dock_file("ubuntu", "node", 12)
