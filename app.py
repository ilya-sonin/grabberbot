import configparser

from telethon.sync import TelegramClient
from telethon import connection

from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

config = configparser.ConfigParser()
config.read("config.ini")

API_ID   = config['Telegram']['api_id']
API_HASH = config['Telegram']['api_hash']
USERNAME = config['Telegram']['username']

