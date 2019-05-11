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

# Bot owners discord name, set this for kill command
botOwner = "hdbag"
 
# BOT client events
client = discord.Client()

"""
	Bot Startup
"""
@client.event
async def on_ready():
    print("Ready To Roll!")
    game = discord.Game("D&D")
    await client.change_presence(status=discord.Status.online, activity=game)

"""
	Process messages from the discord server
"""
@client.event
async def on_message(message):
	# set nickname
	nickname = str(message.author).split("#")[0] if str(message.author.nick) == "None" else str(message.author.nick)
	# don't let the bot talk to itself
	if message.author == client.user:
		return
	# only act on botChar
	if message.content[0] == botChar:
		
		# process command
		print("\nMessage Recieved from " + nickname + ": " + message.content)
		command = cp.Command()
		command.parseCommand(message.content)

		# send processed command message
		if not command.isValid:
			await message.channel.send(nickname + ": " + command.errorMsg)
			print("Sent Error Message to: " + nickname + " -> " + command.errorMsg)
			return
		elif command.action == "help":
			await message.channel.send(command.helpMsg)
			print("Sent Help Message to: " + nickname)
		# only let bot owner terminate
		elif command.action == "kill" and str(message.author).split("#")[0] == botOwner:
			await message.channel.send("Shutting Down")
			await client.change_presence(status=discord.Status.offline, activity=None)
			await client.close()
			print("Dice Bot Shutdown")
			system.exit(0)
		elif command.action == "roll":
			rollMsg = nickname + " rolled " + str(command.numRolls) + "d" + str(command.diceSize) + str(command.modifierSign) + str(command.modifier) + ": " + str(command.rolls) + " -> " + str(command.total)
			await message.channel.send(rollMsg)
			print(rollMsg)

# Runs the bot using the unique discord generated auth token
if __name__ == "__main__":
	client.run(credentials.TOKEN)