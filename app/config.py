import configparser
import os


class Config:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(os.getcwd() + "/config.ini")

    @property
    def api_id(self):
        return self.config.get('Telegram', 'api_id')

    @property
    def api_hash(self):
        return self.config.get('Telegram', 'api_hash')

    @property
    def username(self):
        return self.config.get('Telegram', 'username')

    @property
    def grabber_chat_id(self):
        return self.config.get('Telegram', 'grabber_chat_id')

    @property
    def forwarding_chat_id(self):
        return self.config.get('Telegram', 'forwarding_chat_id')
