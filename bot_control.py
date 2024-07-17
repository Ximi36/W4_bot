import os
import discord
import veryfication_mech
import tickets_mech
import functionality_commands
from client_config import client, intents, TOKEN, SERVER_ID



def run():
    @client.event
    async def on_ready():
        print(f'{client.user} is running')
        global server
        server = client.get_guild(int(SERVER_ID))
        veryfication_mech.start_veryfication_mech(server)
        

    @client.event
    async def on_message(message):
        if not message.author == client.user:
            if isinstance(message.channel, discord.DMChannel):
                await veryfication_mech.second_step(message, server)
            elif not isinstance(message.channel, discord.DMChannel):
                await functionality_commands.beer(message)
        

    client.run(TOKEN)