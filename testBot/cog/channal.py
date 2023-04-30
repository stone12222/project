import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions

intents = discord.Intents.default()
intents.members = True

class role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('channel cog online')

    @commands.command()
    async def makeChannel(self,ctx,*, nameCatename=''):
        if nameCatename.count('+') == 1:
            name, cateName = nameCatename.split('+')
        else:
            name = ''
            cateName = ''
        if name == '' or cateName == '':
            await ctx.send(
                '```Plase enter a valid parameter\nnameCatename(use + to separate name and cateName'
                ')\n\n\ne.x. test+test category```')
        else:
            guild = ctx.message.guild
            category = discord.utils.get(ctx.guild.categories, name=cateName)

            if category==None:
                await ctx.send('```NoneObjectException: No such category found! cateName = ' +cateName + '```')
                return

            await guild.create_text_channel(name,category=category)
            await ctx.send('```Channel name '+cateName+' created!```')

    @commands.command()
    async def deleteChannel(self,ctx, channel_nameCategory):
        if channel_nameCategory.count('+') == 1:
            channel_name, category = channel_nameCategory.split('+')
        else:
            channel_name = ''
            category = ''
        if channel_name == '' or category == '':
            await ctx.send(
                '```Plase enter a valid parameter\nchannel_nameCategory(use + to '
                'separate channel_name and Category)\n\n\ne.x. test+test category```')
        else:
            existing_category = discord.utils.get(ctx.guild.categories, name=category)

            if not existing_category:
                await ctx.send('```NoneObjectException: No such category found! cateName = ' + category + '```')
                return

            existing_channel= discord.utils.get(existing_category.channels, name=channel_name)

            if existing_channel is not None:
                await existing_channel.delete()
            else:
                await ctx.send('```NoneObjectException: No such channel found! channel_name = ' + channel_name + '```')
                return

def setup(bot):
    bot.add_cog(role(bot))