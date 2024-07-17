import os
import asyncio
import discord
from discord.ext import commands
from client_config import client, intents



@client.event
async def on_guild_channel_create(channel):
    if channel.name.startswith("ticket"):
        for member in channel.members:
            if not any(role.name == "Strażnicy" or role.name == "Administrator Serwera" for role in member.roles) and not member.bot:
                if not any(role.name == "Zweryfikowany" for role in member.roles):
                    
                    await asyncio.sleep(0.5)
                    await channel.send(member.mention)
                    emb=discord.Embed(colour=discord.Colour.from_rgb(153, 0, 0), title="Utworzono zgłoszenie :saluting_face:",description=f"Mój szósty zmysł pozwolił mi wykryć, iż nie jesteś jeszcze zweryfikowany. Jeżeli nie działa Ci link do weryfikacji, który otrzymał*ś w wiadomości powitalnej,to możesz wysłać do mnie **na chat prywatny komendę** ```$link```\nW przypadku innych problemów, **opisz proszę wszystko na tym kanale** :point_down:")

                    await channel.send(embed=emb)
                    
                else:
                    
                    await asyncio.sleep(0.5)
                    await channel.send(member.mention)
                    emb=discord.Embed(colour=discord.Colour.from_rgb(153, 0, 0), title="Utworzono zgłoszenie :saluting_face:",description="Mój szósty zmysł pozwolił mi wykryć, iż jesteś osobą zweryfikowaną.\n**Opisz proszę tutaj problem**, a administratorzy na pewno Ci pomogą :point_down:")
                    
                    await channel.send(embed=emb)