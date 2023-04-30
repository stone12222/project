import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import has_permissions
import asyncio

intents = discord.Intents.default()
intents.members = True

class user(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('user cog online')

    # add role to user
    @commands.command()
    @has_permissions(manage_roles=True)
    async def addrole(self,ctx, *, nameRole=''):
        channel = ctx.message.channel
        if nameRole.count('+') == 1:
            name, role = nameRole.split('+')
        else:
            name = ''
            role = ''
        if name == '' or role == '':
            await channel.send(
                '```Plase enter a valid parameter\nnameRole(use + to separate name and role)\n\n\ne.x. john+person```')
        else:
            guild = ctx.guild
            cn = name
            cr = role
            name = get(self.bot.get_all_members(), name=name)
            role = get(guild.roles, name=role)

            print(cr,type(role))

            if not name:
                await channel.send('```NoneObjectException: No such name found! name = ' + cn+'```')
                return
            if not role:
                await channel.send('```NoneObjectException: No such role found! role = ' + cr+'```')
                return

            if role in name.roles:
                await channel.send('```roleOverlapException: Role already exist on user! role = ' + cr+'```')
                return

            await name.add_roles(role)
            await channel.send('```Role named '+cr+' add to user '+cn+'```')

    # remove role to user
    @commands.command()
    @has_permissions(manage_roles=True)
    async def removerole(self,ctx, *, nameRole=''):
        if nameRole.count('+') == 1:
            name, role = nameRole.split('+')
        else:
            name = ''
            role = ''
        if name == '' or role == '':
            await ctx.send(
                '```Plase enter a valid parameter\nnameRole(use + to separate name and role)\n\n\ne.x. john+person```')
        else:
            guild = ctx.guild
            cn = name
            cr = role
            name = get(self.bot.get_all_members(), name=name)
            role = get(guild.roles, name=role)

            if not name:
                await ctx.send('```NoneObjectException: No such name found! name = ' + cn+'```')
                return
            if not role:
                await ctx.send('```NoneObjectException: No such role found! role = ' + cr+'```')
                return

            if not role in name.roles:
                await ctx.send('```NoneObjectException: Role does not exist on user! role = ' + cr+'```')
                return

            await name.remove_roles(role)
            await ctx.send('```Role named '+cr+' removed form user '+ cn+'```')

    # kick member with a reason
    @commands.command()
    @has_permissions(kick_members=True)
    async def kick(self,ctx, *, memberReason=''):
        if memberReason.count('+') == 1:
            member, reason = memberReason.split('+')
        else:
            member = memberReason
            reason = 'none'

        if member == '':
            await ctx.send(
                '```Plase enter a valid parameter\nmemberReason(Reason is optional use + to separate member and reason)'
                '\n\n\ne.x. ray+being a bad boy```')
        else:
            cm = member
            member = get(self.bot.get_all_members(), name=member)

            if not member:
                await ctx.send('```NoneObjectException: No such name found! name = ' + cm+'```')
                return

            await member.send('you have been kick from ' + ctx.message.guild.name + ' for ' + reason)
            await member.kick(reason=reason)
            await ctx.send('```Memeber named '+member+' kicked```')

    # ban member with a reason
    @commands.command()
    @has_permissions(ban_members=True)
    async def ban(self,ctx, *,memberReason=''):
        if memberReason.count('+') == 1:
            member, reason = memberReason.split('+')
        else:
            member = memberReason
            reason = 'none'

        if member == '':
            await ctx.send(
                '```Plase enter a valid parameter\nmemberReason(Reason is optional use + to separate member and reason)'
                '\n\n\ne.x. ray+being a bad boy```')
        else:
            cm = member
            member = get(self.bot.get_all_members(), name=member)

            if not member:
                await ctx.send('```NoneObjectException: No such name found! name = ' + cm+'```')
                return

            await member.send('you have been ban from ' + ctx.message.guild.name + ' for ' + reason)
            await member.ban(reason=reason)
            await ctx.send('```Memeber named '+ cm +' banned```')

    # unban a member
    @commands.command()
    @has_permissions(ban_members=True)
    async def unban(self,ctx,*, member):
        channel = ctx.message.channel
        banned_users=await ctx.guild.bans()

        for banned_entry in banned_users:
            user=banned_entry.user
            if (member==user.name):
                await ctx.guild.unban(user)
                await ctx.send(f'```Unbanned {user.mention}```')
                return

    # mute user for x amount of time
    @commands.command()
    @has_permissions(manage_messages=True)
    async def mute(self,ctx, duration='', *, user=''):
        if duration=='' or user=='':
            await ctx.send('```Plase enter a valid parameter duration and user\n\n\ne.x. 1m MonrayN```')
            return

        if not discord.utils.get(ctx.message.guild.roles, name='muted'):
            await ctx.send("```NoneObjectException: no muted role found!```")
            return

        unit=duration[-1]

        if not unit in ['s','d','m','h']:
            await ctx.send('```interruptionException: invalid value for the unit! unit= '+unit+ '```')
            return

        try:
            duration=int(duration[0:len(duration)-1])
        except:
            await ctx.send('```interruptionException: invalid value for duration! duration= ' + duration[0:len(duration)-1] + '```')
            return

        guild = ctx.guild
        name = get(self.bot.get_all_members(), name=user)
        role = get(guild.roles, name='muted')

        if not name:
            await ctx.send('```interruptionException: No such name found! name = ' + user + '```')
            return

        await ctx.send(f":white_check_mark: Muted {name} for {duration}{unit}")
        await name.add_roles(role)

        wait=0
        if unit == "s":
            wait = 1 * duration
        elif unit == "m":
            wait = 60 * duration
        elif unit == "h":
            wait = 3600 * duration
        elif unit == "d":
            wait = 86400 * duration

        await asyncio.sleep(wait)
        if role in name.roles:
            await name.remove_roles(role)
            await ctx.send(f":white_check_mark: {name} was unmuted")

    # unmute user
    @commands.command()
    @has_permissions(manage_messages=True)
    async def unmute(self,ctx,*,member=''):
        if member=='':
            await ctx.send('```Plase enter a valid parameter member\n\n\ne.x. MonrayN```')
            return

        guild = ctx.guild
        name = get(self.bot.get_all_members(), name=member)
        role = get(guild.roles, name='muted')

        if not name:
            await ctx.send('```interruptionException: No such name found! name = ' + member + '```')
            return

        if not role:
            await ctx.send("```NoneObjectException: no muted role found on server!```")
            return

        if role in name.roles:
            await name.remove_roles(role)
            await ctx.send(f":white_check_mark: {name} was unmuted")
        else:
            await ctx.send('```interruptionException: No mute role found on user!```')



def setup(bot):
    bot.add_cog(user(bot))