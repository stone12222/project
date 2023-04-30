import discord

#
permissions = discord.Permissions()
stort_cut={'vc','mc','mr','me','val','mw','ms','ci','cn','mn','km','bm','sm','el','af','ar',
           'uee','mer','mm','rmh','sttsm','usc','c','s','v','uva','ps','m_m','dm','mov_m','admin'}
dicts={'read_messages':'vc','manage_channels':'mc','manage_roles':'mr','manage_emojis':'me',
       'view_audit_log':'val','manage_webhooks':'mw','manage_guild':'ms','create_instant_invite':'ci',
       'change_nickname':'cn','manage_nicknames':'mn','kick_members':'km','ban_members':'bm',
       'send_messages':'sm','embed_links':'el','attach_files':'af','add_reactions':'ar',
       'external_emojis':'uee','mention_everyone':'mer','manage_messages':'mm','read_message_history':'rmh',
       'send_tts_messages':'sttsm','use_slash_commands':'usc','connect':'c','speak':'s','stream':'v',
       'use_voice_activation':'uva','priority_speaker':'ps','mute_members':'m_m','deafen_members':'dm',
       'move_members':'mov_m','administrator':'admin'}
per_made_permissions={'admins','mod'}

# stort_cut function
def vc(c):
    permissions.update(view_channel=c)
def mc(c):
    permissions.update(manage_channels=c)
def mr(c):
    permissions.update(manage_roles=c)
def me(c):
    permissions.update(manage_emojis=c)
def val(c):
    permissions.update(view_audit_log=c)
def mw(c):
    permissions.update(manage_webhooks=c)
def ms(c):
    permissions.update(manage_guild=c)
def ci(c):
    permissions.update(create_instant_invite=c)
def cn(c):
    permissions.update(change_nickname=c)
def mn(c):
    permissions.update(manage_nicknames=c)
def km(c):
    permissions.update(kick_members=c)
def bm(c):
    permissions.update(ban_members=c)
def sm(c):
    permissions.update(send_messages=c)
def el(c):
    permissions.update(embed_links=c)
def af(c):
    permissions.update(attach_files=c)
def ar(c):
    permissions.update(add_reactions=c)
def uee(c):
    permissions.update(use_external_emojis=c)
def mer(c):
    permissions.update(mention_everyone=c)
def mm(c):
    permissions.update(manage_messages=c)
def rmh(c):
    permissions.update(read_message_history=c)
def sttsm(c):
    permissions.update(send_tts_messages=c)
def usc(c):
    permissions.update(use_slash_commands=c)
def c(c):
    permissions.update(connect=c)
def s(c):
    permissions.update(speak=c)
def v(c):
    permissions.update(stream=c)
def uva(c):
    permissions.update(use_voice_activation=c)
def ps(c):
    permissions.update(priority_speaker=c)
def m_m(c):
    permissions.update(mute_members=c)
def dm(c):
    permissions.update(deafen_members=c)
def mov_m(c):
    permissions.update(move_members=c)
def admin(c):
    permissions.update(administrator=c)

def admins():
    return '[vc,mc,mr,me,val,mw,ms,ci,cn,mn,km,bm,sm,el,af,ar,uee,' \
       'mer,mm,rmh,sttsm,usc,c,s,v,uva,m_m,dm,mov_m,admin]'
def mod():
    return '[vc,mc,mr,val,mw,ci,cn,mn,km,sm,el,af,ar,uee,' \
       'mer,mm,rmh,usc,c,s,v,uva,m_m,mov_m]'