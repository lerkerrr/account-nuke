import discord,random,os

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.dm_channel.send('MESSAGE YOU WANT TO BE SENT HERE')
      await user.remove_friend()
      print(f'Removed{user}')
    except:
        (f"Failed To Remove{user}")
  for guild in client.guilds:
    try:
      await guild.leave()
      print(f"Guild left[{guild.name}]") 
    except:
      print(f"Failed To Leave[{guild.name}]") 

client.run('TOKEN HERE', bot=False)
