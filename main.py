import os
from keep_alive import keep_alive
from discord.ext import commands
import asyncio


bot = commands.Bot(
	command_prefix="!",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)
bot2 = commands.Bot(command_prefix='!')
bot3= commands.Bot(command_prefix='!')
bot4= commands.Bot(command_prefix='!')
bot5= commands.Bot(command_prefix='!')


bot.author_id = enter id here  # Change to your discord id!!!


bot.author_id = enter id here  # Change to your discord id!!!

@bot.event
async def on_ready():
  game = discord.Game(f"made by monster")
  await bot.change_presence(status=discord.Status, activity=game)
  print(f'logged in as {bot.user}')

@bot2.event
async def on_ready():
  game = discord.Game(f"made by monster")
  await bot2.change_presence(status=discord.Status, activity=game)
  print(f'logged in as {bot2.user}')

@bot3.event
async def on_ready():
  game = discord.Game(f"made by monster")
  await bot3.change_presence(status=discord.Status, activity=game)
  print(f'logged in as {bot3.user}')

@bot4.event
async def on_ready():
  game = discord.Game(f"made by monster")
  await bot4.change_presence(status=discord.Status, activity=game)
  print(f'logged in as {bot4.user}')

@bot5.event
async def on_ready():
  game = discord.Game(f"made by monster")
  await bot4.change_presence(status=discord.Status, activity=game)
  print(f'logged in as {bot5.user}')







keep_alive()  # Starts a webserver to be pinged.
loop = asyncio.get_event_loop()
loop.create_task(bot.start('enter token here',bot=False))
loop.create_task(bot2.start('enter token here',bot=False))
loop.create_task(bot3.start('enter token here'.bot=False))
loop.create_task(bot4.start('enter token here',bot=False))
loop.create_task(bot5.start('enter token here',bot=False))
# you can add more if you wish you just need to copy loop.create_task(bot5.start('enter token here')) and bot5 = commands.Bot(command_prefix='!'), and change 
# and change the bot5 to bot6 and so forth with how many more bots you want to add
loop.run_forever()
