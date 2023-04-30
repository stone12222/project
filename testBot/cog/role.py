import discord
from discord.ext import commands
from perm_shortcut import *
from discord.ext.commands import has_permissions

intents = discord.Intents.default()
intents.members = True


class role(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('role cog online')

    # create role
    @commands.command()
    @has_permissions(manage_roles=True)
    async def cR(self, ctx, colors='', permission='', *, name=''):
        if name == '' or colors == '' or permission == '':
            await ctx.send('```Plase enter a valid parameter\n(roleColor, rolePermissions, roleName)\n\n\n'
                               'e.x. 0xf810cd [c,s,admin, sm] owner\'s pet```')
        else:
            guild = ctx.guild
            if not discord.utils.get(ctx.message.guild.roles, name=name):
                await guild.create_role(name=name)
            else:
                await ctx.send('```roleOverlapException: Role already exist! name = ' + name+'```')
                return

            role = discord.utils.get(ctx.message.guild.roles, name=name)

            try:
                await role.edit(color=discord.Colour(int(colors, 16)))
            except:
                await ctx.send('```interruptionException: Invalid hex value for color! color = ' + colors +
                                   '\ne.x. 0xffffff is a valid value.\nRole created only!```')
                return

            if permission in per_made_permissions:
                permission = eval(permission + '()')
            p = permission[1:len(permission) - 1].split(',')

            for e in p:
                if e in stort_cut:
                    a = e + '(True)'
                    eval(e + '(True)')
                    await role.edit(permissions=permissions)
                elif e != '':
                    await ctx.send('```interruptionException: Invalid element for permission short cut! element = '
                                       + e + '\n\n\nRole created, color changed and partial permission setted only!```')
                    return
            await ctx.send('```Role named ' + name + ' added```')
            for e in stort_cut:
                eval(e + '(False)')

    # delete role
    @commands.command()
    @has_permissions(manage_roles=True)
    async def dR(self, ctx, *, name=''):
        channel = ctx.message.channel
        if name == '':
            await channel.send('```Plase enter a valid parameter\nname\n\n\ne.x.testing role```')
        else:
            role_object = discord.utils.get(ctx.message.guild.roles, name=name)
            if (role_object):
                await role_object.delete()
                await channel.send('```Role named ' + name + ' deleted```')
            else:
                await channel.send('```NoneObjectException: No such role found! role = ' + name+'```')

    # change role color
    @commands.command()
    @has_permissions(manage_roles=True)
    async def changeRoleColor(self, ctx, color='', *, role=''):
        if color == '' or role == '':
            await ctx.send('```Plase enter a valid parameter\ncolor, role\n\n\ne.x. 0x0e4fa9 testing role```')
        else:
            cr = role
            role = discord.utils.get(ctx.message.guild.roles, name=role)

            if not role:
                await ctx.send('```NoneObjectException: No such role found! role = ' + cr+'```')

            try:
                await role.edit(color=discord.Colour(int(color, 16)))
            except:
                await ctx.send('```interruptionException: Invalid hex value for color! color = ' + color +
                               '\ne.x. 0xffffff is a valid value.```')
                return

            await ctx.send('```Color for role named ' + cr + ' changed```')

    # change role permission/s
    @commands.command()
    @has_permissions(manage_roles=True)
    async def changeRolePerm(self, ctx, perms='', *, role=''):
        d = {}
        if perms == '' or role == '':
            await ctx.send('```Plase enter a valid parameter\nperms, role\n\n\ne.x. [vc,admin] testing role```')
        else:
            p = perms[1:len(perms) - 1].split(',')

            cr = role
            role = discord.utils.get(ctx.message.guild.roles, name=role)

            if not role:
                await ctx.send('```NoneObjectException: No such role found! role = ' + cr+'```')
                return

            for e in p:
                if not e in stort_cut and e != '':
                    await ctx.send('```interruptionException: Invalid element for permission short cut! element = '
                                   + e + '\n\n\nNothing Changed!```')
                    return
            for e in role.permissions:
                if e[0] != 'view_guild_insights' and e[0] != 'request_to_speak':
                    a = dicts[e[0]] + '(' + str(e[1]) + ')'
                    eval(a)
                    d[dicts[e[0]]] = e[1]

            for e in p:
                if d[e] == False:
                    a = e + '(True)'
                    eval(a)
                    d[e[0]] = True
                else:
                    a = e + '(False)'
                    eval(a)
                    d[e[0]] = False
            await role.edit(permissions=permissions)

    # change role name
    @commands.command()
    @has_permissions(manage_roles=True)
    async def changeRoleName(self, ctx, *, oldNewRoleName=''):
        if oldNewRoleName.count('+')==0:
            await ctx.send('```Plase enter a valid parameter\noldNewRoleName(use + to separate old and new name)\n\n\ne.x. 0x0e4fa9 testing role```')
        else:
            old,new=oldNewRoleName.split('+')
            role = discord.utils.get(ctx.message.guild.roles, name=old)

            if not role:
                await ctx.send('```NoneObjectException: No such role found! role = ' + old+'```')

            await role.edit(name=new)

            await ctx.send('```Name for role named ' + old + ' changed```')

    # enable display role members separately from online members
    @commands.command()
    @has_permissions(manage_roles=True)
    async def enableDRMSFOM(self,ctx,role=''):
        if role=='':
            await ctx.send('```Plase enter a valid parameter\nrole\n\n\ne.x. testing role```')
        else:
            cr = role
            role = discord.utils.get(ctx.message.guild.roles, name=role)

            if not role:
                await ctx.send('```NoneObjectException: No such role found! role = ' + cr+'```')
                return
            role.hoist = True
            await role.edit(permissions=permissions)
            await ctx.send('```Display role members separately from online members enabled on role name '+cr+'```')

    # enable allow anyone to @mention this role
    @commands.command()
    @has_permissions(manage_roles=True)
    async def enableAAMTR(self,ctx,role=''):
        if role=='':
            await ctx.send('```Plase enter a valid parameter\nrole\n\n\ne.x. testing role```')
        else:
            cr = role
            role = discord.utils.get(ctx.message.guild.roles, name=role)

            if not role:
                await ctx.send('```NoneObjectException: No such role found! role = ' + cr+'```')
                return
            role.mentionable = True
            await role.edit(permissions=permissions)
            await ctx.send('```Allow anyone to @mention this role enabled on role name ' + cr+'```')

def setup(bot):
    bot.add_cog(role(bot))