# DiceBot
Dice Roller Bot for Discord


### Versions

- python: 3.7.3
- discord: 1.0.1

### Commands

Commands to this bot start with '!' (you can modify this in dice_bot.py by changing the botChar variable)
- !roll 2d20 -> would roll 2 20 sided dice and return the individual results [11, 15] and the total 26

You can include +/- modifiers that will adjust the roll total
- !roll 2d20 +2 -> still returns the individual rolls, as well as the total adjusted by the modifier

For "in-game" help
- !help -> displays the help menu

There is a kill command
- !!! -> kills all diceBots, useful if you have multiple instances running and can't find the process

*OR* use test_driver.py to test input command parsing without blowing up a public discord server :)

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
