
import keep_alive
import datetime
from discord.ext import commands, tasks
import discord
from dataclasses import dataclass
import os

client = commands.Bot(command_prefix="247", intents=discord.Intents.all())

my_secret = os.environ['TOKEN']

@client.event
async def on_ready():
  await client.load_extension("cogs.maincog")
  pass

@client.command()
async def r(ctx):
  if ctx.author.id == 877894873842319372:
    await client.unload_extension('cogs.maincog')
    await client.load_extension("cogs.maincog")
    await ctx.send("reloaded")

  else:
    ctx.send("on jah?")

keep_alive.keep_alive()
client.run(my_secret)