import os

from app import Config, Client, Grabber

config = Config()
client = Client(username=config.username,
                api_id=config.api_id, api_hash=config.api_hash)


def grabberStart():
    grabber = Grabber(client, config.grabber_chat_id, config.forwarding_chat_id)
    grabber.start()


if __name__ == '__main__':
    for file in os.listdir(os.getcwd()):
        fileExtension = file.split(".")
        if fileExtension[-1] == "session":
            grabberStart()
        else:
            client.start()
