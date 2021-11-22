from telethon.sync import TelegramClient


class Client(TelegramClient):

    def __init__(self, api_id, api_hash, username):
        super().__init__(username, api_id, api_hash)

    def start(self):
        super().start()
