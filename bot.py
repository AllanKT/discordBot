import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
from random import randint
import pandas as pd
import traceback


client = commands.Bot(command_prefix="#")

@client.event
async def on_ready():
	print("Logfed in as")
	print(client.user.name)
	print(client.user.id)
	print("--------------")

@client.command()
async def roll(dice : str):
	try:
		rolls, limit = map(int, dice.split("d"))
	except:
		await client.say('Format has to be in \'NdN\'!')
		return 

	result = ', '.join(str(randint(1, limit)) for _ in range(rolls))
	await client.say(f"🎲 {dice}: {result}")

@client.command(pass_context=True)
async def info(ctx, user : discord.Member):
	try:
		dfFicha = pd.read_excel("ficha.xlsx")
		player = dfFicha.loc[dfFicha['Jogador'] == user.name]
		await client.say(f'FICHA: \n \
			🙂 Jogador: {str(player["Jogador"].values)} \n \
			🎮 Personagem: {str(player["Personagem"].values)}  \n \
			🔱 Progenitor: {str(player["Progenitor"].values)} \n \
			🎂 Idade: {int(player["Idade"].values)} 📏 Altura: {float(player["Altura"].values)} 👦/👧 Sexo: {str(player["Sexo"].values)} \n \
			💪️ Força: {int(player["Força"].values)} 👟 Destreza: {int(player["Destreza"].values)} 💊 Constituição: {int(player["Constituição"].values)} 👀 Sabedoria: {int(player["Sabedoria"].values)} 💬 Carisma: {int(player["Carisma"].values)} \n \
			➕ Divindade: {int(player["Divindade"])}\n \
			💗 LifePoints: {int(player["LifePoints"].values)} \n \
			🛡️ CA: {int(player["CA"].values)} \n \
			📈 Experiência: {int(player["Experiência"].values)} \n \
			📜 Descrição: {str(player["Descrição"].values)}')
	except:
		await client.say("Player not found!")

@client.event
async def on_command_error(error, ctx):
    channel = ctx.message.channel
    if isinstance(error, commands.MissingRequiredArgument):
        await send_cmd_help(ctx)
    elif isinstance(error, commands.BadArgument):
        await send_cmd_help(ctx)
    elif isinstance(error, commands.CommandInvokeError):
        print("Exception in command '{}', {}".format(ctx.command.qualified_name, error.original))
        traceback.print_tb(error.original.__traceback__)

client.run("NDg3OTczNDg1MTM4NjczNjk0.DnVdDg.X19ddHEc4R5e7eThfN4LV-xXtpA")