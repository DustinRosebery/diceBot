import dice_logic as dice
import re

debug = False

"""
	This class takes a raw command from discord and processes the input into a command object
	If the command is successfully processed, command.isValid = True, else False
"""
class Command:

	helpMsg = "I am a dice rolling bot!\nValid commands: !roll, !help\nRoll command: !roll 3d10 +3\nThis would return 3 rolls of a 10 sided dice with +3 as the modifier\nYou can roll up to ~500 dice at a time with any size dice that you like with a positive or negative modifier\nHelp command: print this message"
	tryHelp = "\nTry !help for more info"

	"""
		Create default command object
	"""
	def __init__(self):
		self.action = ""
		self.numRolls = 1
		self.diceSize = 20
		self.rolls = []
		self.modifierSign = "+"
		self.modifier = 0
		self.total = 0
		self.isValid = False

	"""
		Parse the command action, and process the commands
		Regex parser groups
		- group 1: modified roll action
		- group 2: numRolls
		- group 3: diceSize
		- group 4: modifier sign
		- group 5: modifier
		- group 6: help kill, or basic roll actions
	"""
	def parseCommand(self, rawCommand):

		#define the regex match
		exp = re.compile("^!(roll|rolls)\\s?(\\d+)?d(\\d+)\\s?([-+])?\\s?(\\d+)?|^!(help|kill|roll)\\s?$")
		regex = exp.match(str(rawCommand))
		print("Regex Type: " + str(type(regex)))
		# catch improper input 
		if not regex:
			self.errorMsg = "Invalid Input: " + str(rawCommand) + self.tryHelp
			return
		if debug:
			print("Group 1: " + str(regex.group(1)))
			print("Group 2: " + str(regex.group(2)))
			print("Group 3: " + str(regex.group(3)))
			print("Group 4: " + str(regex.group(4)))
			print("Group 5: " + str(regex.group(5)))
			print("Group 6: " + str(regex.group(6)))

		# parse the action
		if regex.group(6):
			if regex.group(6) == "help":
				self.setHelpCommand()
			elif regex.group(6) == "kill":
				self.setKillCommand()
			elif regex.group(6) == "roll":
				self.parseRollCommand(regex)
			else:
				self.errorMsg = "Invalid Command" + self.tryHelp
		elif regex.group(1) == "roll":
			self.parseRollCommand(regex)
		else:
			self.errorMsg = "Invalid Command" + self.tryHelp
		
	"""
		Parse the roll command and assign attributes
	"""
	def parseRollCommand(self, regex):
		self.action = "roll"
		try:
			self.numRolls = int(regex.group(2)) if regex.group(2) else 1
			self.diceSize = int(regex.group(3)) if regex.group(3) else 20
			self.rolls = dice.getRolls(self.numRolls, self.diceSize)
			if regex.group(4):
				self.modifierSign = "-" if regex.group(4) == "-" else "+"
				self.modifier = int(regex.group(5)) * -1 if int(regex.group(4) == "-") else int(regex.group(5))
			self.total = int(dice.getRollSum(self.rolls, len(self.rolls))) + self.modifier
			self.isValid = True
		except Exception as ex:
			self.errorMsg = "Invalid Roll" + self.tryHelp
			return

		self.isValid = True

	"""
		Set kill command attributes
	"""
	def setKillCommand(self):
		self.action = "kill"
		self.isValid = True

	"""
		Set help command attributes
	"""
	def setHelpCommand(self):
		self.action = "help"
		self.isValid = True