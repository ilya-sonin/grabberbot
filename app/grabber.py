import sys

from telethon import events


class Handlers:
    def __init__(self, client, grabber_chat_id, forwarding_chat_id):
        self.client = client
        self.grabber_chat_id = grabber_chat_id
        self.forwarding_chat_id = forwarding_chat_id

    @events.register(events.NewMessage())
    async def incoming(self, event):
        try:
            if (event.peer_id.channel_id == int(self.grabber_chat_id)):
                await self.client.send_message(int(self.forwarding_chat_id), event.message)
        except AttributeError:
            pass


class Grabber:
    def __init__(self, client, grabber_chat_id, forwarding_chat_id):
        self.client = client
        self.grabber_chat_id = grabber_chat_id
        self.forwarding_chat_id = forwarding_chat_id

    def start(self):
        if self.client != None:
            handlers = Handlers(client=self.client, grabber_chat_id=self.grabber_chat_id,
                                forwarding_chat_id=self.forwarding_chat_id)
            self.client.add_event_handler(handlers.incoming)
            self.client.run_until_disconnected()
        else:
            sys.exit()
