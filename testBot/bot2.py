import discord
from discord.ext import commands
import os
from discord.utils import get
from discord.ext.commands import has_permissions
import asyncio
import random

# set up bot
intents = discord.Intents.default()
intents.members = True

class CustomHelpCommand(commands.HelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping):
        a = '```'
        for cog in mapping:
            try:
                a+=cog.qualified_name+':'+'\n'
            except:
                a+='​No Category:'+'\n'

            for command in mapping[cog]:
                a+='  '+command.name+'\n'
        a+='\nType $help command for more info on a command.\n' \
           'You can also type $help category for more info on a category.'
        a +='```'
        await self.get_destination().send(a)

    async def send_cog_help(self, cog):
        if cog.qualified_name=='role':
            a='``` role:\n' \
              '   role category are group of methods based on managing roles. It includes methods on creating/deleting roles' \
              ' and modifying pre-existing roles.\n\nMethods:\n'
            for command in cog.get_commands():
                if command.name=='cR':
                    a +='  '+command.name+'(create role)\n'
                elif command.name=='dR':
                    a += '  ' + command.name + '(delete role)\n'
                elif command.name=='enableDRMSFOM':
                    a += '  ' + command.name + '(enable display role members separately from online \n  members)\n'
                elif command.name=='enableAAMTR':
                    a += '  ' + command.name + '(enable allow anyone to @mention this role)\n'
                else:
                    a+='  '+command.name+'\n'
        else:
            a = '```user:\n' \
              '   user category are group of methods based on managing a user. It includes methods on adding/removing roles from a user' \
              ' and modifying the status of the user on the server.\n\nMethods:\n'
            for command in cog.get_commands():
                a += '  ' + command.name + '\n'

        a += '\nType $help command for more info on a command.\n' \
             'You can also type $help category for more info on a category.'
        a += '```'
        await self.get_destination().send(a)

    async def send_group_help(self, group):
        await self.get_destination().send(f'{group.name}: {[command.name for index,command in enumerate(group.commands)]}')

    async def send_command_help(self, command):
        print()
        a=''
        if command.name=='cR':
            a = '```cR(creat role):\n' \
                '  This method will create a role that you named, with the color you specify and the permissions.' \
                ' This method will need 3 valid parameters, color, permissions and roleName. Having an invalid value' \
                ' for any of the parameters will cause the role to be partially created.\n\ne.x. $cR 0x1fa40c ' \
                '[vc,sm,uee] testing role```'
        elif command.name=='dR':
            a = '```dR(delete role):\n' \
                '  This method will delete the role that you named from your sever. This method will need 1 valid' \
                ' parameter, name. Having an invalid value will cause an error to occur.\n\ne.x. $dR testing role```'
        elif command.name=='changeRoleColor':
            a = '```changeRoleColor:\n' \
                '  This method will change the color of the role that you named from your sever. This method will' \
                ' need 2 valid parameters, color and role. Having an invalid value will cause an error to occur.' \
                '\n\ne.x. $changeRoleColor 0x5bc92e testing role```'
        elif command.name=='changeRolePerm':
            a = '```changeRolePerm:\n' \
                '  This method will invert the permissions you passed trough on the role that you named.' \
                ' This method will need 2 valid parameters, perms and role. Having an invalid value will ' \
                ' cause an error to occur.\n\ne.x. $changeRolePerm [admin,c,s,ms] testing role```'
        elif command.name=='changeRoleName':
            a = '```changeRoleName:\n' \
                '  This method will change the name of the role you named to the name you passed trough.' \
                ' This method will need 1 valid parameter, oldNewRoleName. This parameter includes two values old/new name' \
                ' two value are separated by "+" fail to include "+" or having an invalid old name will cause an error ' \
                'to occur.\n\ne.x. $changeRoleName testing role+testing_role```'
        elif command.name=='enableDRMSFOM':
            a = '```enableDRMSFOM(enable display role members separately from online members):\n' \
                ' This method will enable display role members separately from online members on the role named' \
                ' by you.\n\ne.x. enableDRMSFOM testing role```'
        elif command.name=='enableAAMTR':
            a = '```enableAAMTR(enable allow anyone to @mention this role):\n' \
                ' This method will enable allow anyone to @mention this role on the role named' \
                ' by you.\n\ne.x. enableAAMTR testing role```'
        elif command.name=='addrole':
            a = '```addrole:\n' \
                '  This method will add the role you named to the user you named. This method will need 1 valid' \
                ' parameter, nameRole. This parameter includes two value name and role two values are' \
                ' separated by "+" fail to include "+", or having an invalid name or role will cause an error ' \
                'to occur.\n\ne.x. $addrole role+Stone```'
        elif command.name=='removerole':
            a = '```removerole:\n' \
                '  This method will remove the role you named to the user you named. This method will need 1 valid' \
                ' parameter, nameRole. This parameter includes two value name and role two values are' \
                ' separated by "+", fail to include "+" or having an invalid name or role will cause an error ' \
                'to occur.\n\ne.x. $removerole role+Stone```'
        elif command.name=='kick':
            a = '```kick:\n' \
                '  This method will kick the user you named out of the server. This method will need 1 valid' \
                ' parameter, memberReason. This parameter includes two value member and reason(optional) two' \
                ' values are separated by "+", fail to include "+" or having an invalid member will' \
                ' cause an error to occur.\n\ne.x. $kick Stone+You are too cool!```'
        elif command.name=='ban':
            a = '```ban:\n' \
                '  This method will ban the user you named on the server. This method will need 1 valid' \
                ' parameter, memberReason. This parameter includes two value member and reason(optional) two' \
                ' values are separated by "+", fail to include "+" or having an invalid member will' \
                ' cause an error to occur.\n\ne.x. $ban Stone+You are too cool!```'
        elif command.name=='unban':
            a = '```unban:\n' \
                '  This method will unban the user you named on the server. This method will need 1 valid' \
                ' parameter, member. Having an invalid value member will' \
                ' cause an error to occur.\n\ne.x. $unban Stone```'
        elif command.name=='purge':
            a = '```purge:\n' \
                '  This method will delete x amount of messages you specified on the channle where it\'s called.' \
                ' This method will need 1 valid parameter, amount. Having an invalid value member will not' \
                ' cause an error to occur; the default amount value is 5.\n\ne.x. $purge 10```'
        elif command.name=='warn':
            a = '```warn:\n' \
                '  This method will dm the user you named with the message you typed.' \
                ' This method will need 1 valid parameter, memberText. This parameter includes two value' \
                ' member and Text(optional) two values are separated by "+", fail to include "+" or' \
                ' having an invalid member will cause an error to occur.\n\ne.x. $warn Stone+You are too cool!```'
        elif command.name=='help':
            a = '```help:\n' \
                '  This method is the method you are currently using.```'
        elif command.name=='unload':
            a = '```unload:\n' \
                '  This method will unload the cog extension you named.```'
        elif command.name=='load':
            a = '```load:\n' \
                '  This method will load the cog extension you named.```'
        elif command.name=='mute':
            a = '```mute:\n' \
                '  This method will mute the user you named by x amount of time.' \
                ' This method will need 2 valid parameter, duration and user. Having an invalid value member will' \
                ' cause an error to occur;\n\ne.x. $mute 10h MonrayN```'
        elif command.name=='unmute':
            a = '```unmute:\n' \
                '  This method will unmute the user you named on the server.' \
                ' This method will need 1 valid parameter, member. Having an invalid value member will' \
                ' cause an error to occur;\n\ne.x. $unmute MonrayN```'

        await self.get_destination().send(a)


bot = commands.Bot(intents=intents,command_prefix='$',help_command=CustomHelpCommand())

# even happens on ready
@bot.event
async def on_ready():
    print('bot named {0.user}'.format(bot)+' is ready')

# load cog
@bot.command()
async def load(ctx,extension):
    bot.load_extension(f"cog.{extension}")

# unload cog
@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f"cog.{extension}")

# clear chat log
@bot.command()
@has_permissions(manage_messages=True)
async def purge(ctx,amount=5):
    channel=ctx.message.channel
    await channel.purge(limit=amount+1)
    await ctx.channel.send('Requested amount deleted')

@bot.command()
async def warn(ctx,*,memberText=''):
    channel = ctx.message.channel
    if memberText=='' and memberText.count('+')==0:
        await channel.send('```Plase enter a valid parameter\nmemberText(use + to separate name and text)\n\n\ne.x. ray+being a bad boy```')
    else:
        member,text=memberText.split('+')
        cm = member
        member = get(bot.get_all_members(), name=member)

        if not member:
            await channel.send('```NoneObjectException: No such name found! name = ' + cm+'```')
            return
        await member.send("Warn: "+text)
        await channel.purge(limit=1)
        await channel.send('```Member named '+cm+' warned!```')

poll_list=['MonrayN','YB','Stone','TinaZ']
m_id=''
poll_on=False

def draw():
    if poll_list:
        winner=random.choices(poll_list)
        print(poll_list)
        poll_list.clear()
        return ['@'+winner[0]]
    else:
        return ['None']

@bot.command()
async def draw(ctx,time,*,item):
    global poll_on
    if time == '' or item == '':
        await ctx.send('```Plase enter a valid parameter time and item\n\n\ne.x. 1m MonrayN```')
        return

    if not discord.utils.get(ctx.message.guild.roles, name='muted'):
        await ctx.send("```NoneObjectException: no muted role found!```")
        return

    unit = time[-1]

    if not unit in ['s', 'd', 'm', 'h']:
        await ctx.send('```interruptionException: invalid value for the unit! unit= ' + unit + '```')
        return

    try:
        time = int(time[0:len(time) - 1])
    except:
        await ctx.send(
            '```interruptionException: invalid value for duration! duration= ' + time[0:len(time) - 1] + '```')
        return

    if not poll_on:
        wait = 0
        units=''
        if unit == "s":
            wait = 1 * time
            units='sec(s)'
        elif unit == "m":
            wait = 60 * time
            units='min(s)'
        elif unit == "h":
            wait = 3600 * time
            units='hour(s)'
        elif unit == "d":
            wait = 86400 * time
            units='day(s)'

        poll_on = True
        host = ctx.message.author
        message = await ctx.send('DRAW TIME!\n**'+item+'**\nReact with 👍 to join\n'
                                  +'Hosted by: '+host.mention+'\nEnds in: '+str(time)+' '+units)
        await message.add_reaction('👍')
        await asyncio.sleep(wait)

        if poll_list:
            winner = random.choices(poll_list)
            member = get(bot.get_all_members(), name=winner[0])
            print(poll_list)
            poll_list.clear()
            await message.edit(content='**'+item + '**\nWinner: ' + member.mention +'\nHosted by: '+host.mention
                               +'\nTime: ended')
            await ctx.send('Congratulations '+member.mention+' have won **'+item+'**!:tada::tada::tada:')
        else:
            await message.edit(content=item + '\nWinner: None entered\nHosted by: ' + host.mention
                               +'\nTime: ended')
            await ctx.send('No one entered draw is over!')
        poll_on = False
    else:
        pass
        await ctx.send("A draw is already on currently please with until it is finnish to do a poll again!")

@bot.event
async def on_reaction_add(reaction,user):
    global m_id
    # print(str(reaction.message)[12:30],reaction.message)
    if str(reaction)=='👍' and user!=bot.user and m_id==str(reaction.message)[12:30]:
        print('yes')
        poll_list.append(user.name)
    elif user==bot.user:
        m_id=str(reaction.message)[12:30]
    # print(reaction,user,'add')

@bot.event
async def on_reaction_remove(reaction,user):
    global m_id
    if str(reaction)=='👍' and m_id==str(reaction.message)[12:30]:
        poll_list.remove(user.name)
    elif user==bot.user:
        m_id=str(reaction.message)[12:30]
    # print(reaction,user,'remove')

@bot.event
async def on_command_error(ctx, e):
    await ctx.send('```'+str(e)+'```')

for filename in os.listdir('./pygames/testBot/cog'):
    if filename.endswith('.py') :
        bot.load_extension(f"cog.{filename[:-3]}")

bot.run('ODYxNjY0MjAyNDM0NTQzNjI2.YONFUg.Q34ONxWb4pVDvNPHrvoYZqfRK38')