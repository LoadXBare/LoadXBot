import discord
from discord.ext import commands


class PetTheBunger(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def petthebunger(self, ctx):
        embed = discord.Embed(color=0x1e507d)
        embed.set_image(url='https://i.imgur.com/avHG1hq.gif')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(PetTheBunger(client))