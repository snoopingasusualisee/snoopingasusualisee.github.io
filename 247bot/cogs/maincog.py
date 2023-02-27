import datetime
from discord.ext import commands, tasks
import discord
from dataclasses import dataclass
import os

client = commands.Bot(command_prefix="247", intents=discord.Intents.all())

class MainCog(commands.Cog):
    def __init__(self, client):
        self.bot = client

    @client.command(aliases=["pp"])
    async def p(self, ctx):
      await ctx.send("logan")

    @client.command(aliases=["bb"])
    async def b(self, ctx):
      if ctx.author.id == 877894873842319372:
        await ctx.send("closing")
        await client.close()
      else:
        await ctx.send("on jah?")

async def setup(client):
  await client.add_cog(MainCog(client))