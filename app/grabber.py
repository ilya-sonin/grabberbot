import sys

from telethon import events


class Handlers:
    def __init__(self, chat_id):
        self.chat_id = chat_id

    @events.register(events.NewMessage(incoming=True))
    async def incoming(self, event):
        if (str(event.from_id.user_id) == self.chat_id):
            print(event.message.message)


class Grabber:
    def __init__(self, client, chat_id):
        self.client = client
        self.chat_id = chat_id

    def start(self):
        if self.client != None:
            handlers = Handlers(chat_id=self.chat_id)
            self.client.add_event_handler(handlers.incoming)
            self.client.run_until_disconnected()
        else:
            sys.exit()
