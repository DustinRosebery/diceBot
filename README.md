# DiceBot
Dice Roller Bot for Discord


### Versions

- python: 3.7.3
- discord: 1.0.1

### Commands

Commands start with '!' 
- change this with botChar in dice_bot.py

Roll -> returns individual rolls results and the total adjusted by the modifier
- !roll (rolls 1d20)
- !roll d6
- !roll 2d20
- !roll 2d20 +2
- !roll d100-40
- Roll commands are parsed with regex and can handle *most* inputs of these types


Help -> displays the help message
- !help

Kill -> terminates the bot
- !kill 
- Only the bot owner can run this command, set botOwner in dice_bot.py

**You can use test_driver.py to test input command parsing without blowing up a public discord server :)**

### Installation Help

To run this as your own bot:
- verify you have the proper python version: `python --version` must be 3.7.x
- install the discord module: `python -m pip install discord.py==1.0.1`
- you will need to create a new bot at https://discordapp.com/developers/applications/
- add the generated authorization TOKEN, and the filepath to your discord module (if not default) in a NEW local file named: 

`bot_credentials.py`

```python
class credentials:
	def __init__(self):
		self.TOKEN = 'YOUR_BOTS_AUTH_TOKEN' 
		self.DISCORD_PATH = 'PATH_TO_DISCORD_MODULE'
```

Finally, you need to go to https://discordapp.com/oauth2/authorize?client_id=XXXXXXXXXXXXXXXX&scope=bot (replace XXXXXXXXXXXXXXXXXX with your bots client_id)
and add the bot to a discord server that you have admin priveleges on.

Once you complete the previous steps, you simply build dice_bot.py on your machine, and wait for the "Ready to Roll!"" message to appear in the console.
Enjoy
