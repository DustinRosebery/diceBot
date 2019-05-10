"""
	dice_bot handles discord interactions with the bot

	TOKEN and DISCORD_PATH not included in public repo
	add bot_credentails.py to your local directory including these.
	for more information, see README.md
"""
import bot_credentials as bc
credentials = bc.credentials()

import sys
sys.path.insert(0, credentials.DISCORD_PATH)

import discord
import random
import command_parser as cp

# Starting character the bot looks for to process a server message
botChar = "!"
 
# BOT client events
client = discord.Client()

"""
	Bot Startup
"""
@client.event
async def on_ready():
    print("Ready To Roll!")

"""
	Process messages from the discord server
"""
@client.event
async def on_message(message):
	# set message parameters
	author = str(message.author)
	nickname = str(message.author.nick)
	if nickname == "None":
		nickname = author.split("#")[0]

	# don't let the bot talk to itself
	if message.author == client.user:
		return
	# kill command
	if message.content == "!!!":
		sys.exit(0)
	# process message
	if message.content[0] == botChar:
		print("Message Recieved from " + nickname + ": " + message.content)
		command = cp.Command(message.content)

		# send processed command message
		if not command.isValid:
			await message.channel.send(command.errorMsg)
			return
		if command.action == "help":
			await message.channel.send(command.helpMsg)
			return
		if command.action == "roll":
			await message.channel.send(nickname + " rolled: " + str(command.rolls) + " -> " + str(command.total))
			return

# Runs the bot using the unique discord generated auth token
if __name__ == "__main__":
	client.run(credentials.TOKEN)