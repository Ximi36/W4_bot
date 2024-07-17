import discord
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
SERVER_ID = os.getenv('SERVER_ID')

intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)