from discord.ext import commands
from Cybernator import Paginator as pag
from tabulate import tabulate
import json, os, sys
import requests, discord


# Настройки
prefix = "!"
client = commands.Bot(command_prefix = prefix)


# Включение
@client.event
async def on_ready():
	print(f'------------------\n{client.user.name} Запущен!\n------------------')

@client.command()
@commands.has_permissions(administrator = True)
async def reload(ctx):
	await ctx.channel.purge(limit = 1)
	os.system("Python main.py")
	sys.exit()

@client.command()
@commands.has_permissions(administrator = True)
async def load(ctx, extension):
	extension = extension.lower()
	client.load_extension(f'cogs.{extension}')
	await ctx.send(f'Ког {extension} успешно выгружен!')

@client.command()
@commands.has_permissions(administrator = True)
async def unload(ctx, extension):
	extension = extension.lower()
	client.unload_extension(f'cogs.{extension}')
	await ctx.send(f'Ког {extension} успешно загружен!')

for filename in os.listdir("./cogs"):
	if filename.endswith(".py") and not filename.startswith("_"):
		client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv("TOKEN"))