import sys
sys.path.insert(0, 'C:\\Users\\Dlros\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages')
import discord
import random
import command_parser as cp

TOKEN = 'NTc1MTI4NTY4ODQ2MDkwMjcy.XNEIrg.fgX9oZnNAynl-jG1mBmtM4-A6jc'
 
# BOT client events
client = discord.Client()

@client.event
async def on_ready():
    print("Ready To Roll!!")

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

	# process message
	if message.content[0] == "!":
		print("Message Recieved from " + nickname + ": " + message.content)
		command = cp.Command(message.content)

		if not command.isValid:
			await message.channel.send(command.errorMsg)
			return

		if command.action == "help":
			await message.channel.send(command.helpMsg)
			return

		# ROLL
		if command.action == "roll":
			await message.channel.send(nickname + " rolled: " + str(command.params[0]) + " -> " + str(command.params[2]))
			return

if __name__ == "__main__":
	client.run(TOKEN)