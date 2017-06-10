import discord
import asyncio
from discord.ext import commands

description = 'Hallo fixbeertjes'
bot_prefix = '?'

client = commands.Bot(description=description, command_prefix=bot_prefix)

list_of_string = ['huub is stom', 'huub heeft voelsprieten', 'kafin heeft wel een mooie stem', 'stijn is beter dan huub']
deleted_users = ['']
@client.event
async def on_ready():
    print('Logged in')
    print('Name: {}'.format(client.user.name))
    print('ID: {}'.format(client.user.id))
    print(discord.__version__)
    
@client.command(pass_context=True)
async def ping(ctx):
    if ctx.message.author.id not in deleted_users:
        await client.say('Kaas!')
@client.command(pass_context=True)
async def sas(ctx):
    if ctx.message.author.id not in deleted_users:
        await client.say('PPAP')

@client.event
async def on_message(message):
	if message.author.id in deleted_users:
		await client.delete_message(message)
		await client.send_message(message.channel, 'Jammer pik, jouw mening telt niet')
		#await client.send_message(message.channel, 'Say hello')
	if message.content.lower() in list_of_string:
		await client.add_reaction(message, '👌')
	if message.content.startswith('Hoi'):
		await client.send_message(message.channel, 'Say hello')
		msg = await client.wait_for_message(author=message.author, content='hello')
		await client.send_message(message.channel, 'Hello.')
	await client.process_commands(message)
	

client.run("")
