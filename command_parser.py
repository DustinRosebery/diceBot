import dice_logic as dice

"""
	This class takes a raw command from discord and returns a list of parsed command objects
"""
class Command:

	helpMsg = "I am a dice rolling bot!\nValid commands: !roll, !help\nRoll command: !roll 3d10 +3\nThis would return 3 rolls of a 10 sided dice with +3 as the modifier\nYou can roll up to ~500 dice at a time with any size dice that you like with a positive or negative modifier\nHelp command: print this message"


	"""
		Create a command object
		* Roll Command:
		   	- str: action -> roll, etc
			- int: modifer
			- int: total
			- []: rolls
			- boolean: isValid -> is this a valid roll command
			- []: errorMsg -> [error1, error2, ..., errorN]
			- str: helpMsg

		* Help Command:
			- str: action
			- str: helpMsg

	"""
	def __init__(self, rawCommand):
		command = rawCommand.split(" ")
		self.action = ""
		self.isValid = False
		self.errorMsg = ""

		if "roll" in command[0].lower() or "rolls" in command[0].lower():
			self.action = "roll"
			self.modifer = 0
			self.total = 0
			self.rolls = []
			self.isValid = self.getRollParameters(command)

		elif "help" in command[0].lower():
			self.action = "help"
			self.isValid = True

	"""
		Sets the object params for the roll command
		params -> [ [rolls], modifier, total]
		Returns True if the command is valid, else returns False
	"""
	def getRollParameters(self, rawCommand):
		try:
			print("Raw Command: " + str(rawCommand))
			command = rawCommand[1:]

			# parse modifier
			# if no modifier present
			print("Mod Command: " + str(command))
			lastIndex = len(command) - 1
			if "-" in str(command):
				modAmount = command[lastIndex].split("-")[1]
				command = command[0].split("-")
				print("Neg Temp: " + str(temp))
				modAmount = temp[len(temp) - 1]
				self.modifier = int(modAmount) * -1
			elif "+" in str(command):
				temp = command[lastIndex].split("+")[1]
				command = command[0].split("+")
				print("Pos Temp: " + str(temp))
				modAmount = temp[len(temp) - 1]
				self.modifier = int(modAmount)
			else:
				self.modifier = 0				

			# parse roll parameters and get rolls
			# if numRolls not present -> ex; !roll d20
			command = command[0].split("d")
			print("Roll Command: " + str(command))
			if not command[0]:
				command[0] = 1
				self.rolls = dice.getRolls(int(command[0]), int(command[1]))
			# if numRolls is present -> ex; !roll 3d10
			elif len(command) == 2:
				self.rolls = dice.getRolls(int(command[0]), int(command[1]))
			else:
				self.errorMsg = "Invalid Roll Value: " + str(rawCommand) + "\nTry !help for more info"
				return False

			
			"""
			if len(command) == 1:
				self.params[1] = 0
			# if the modifier portion doesn't have a space -> ex; !roll d20 +2
			elif len(command) == 2:
				rawMod = command[1]
				self.params[1] = int(rawMod[1:]) 
				if "-" in rawMod:
					self.params[1] = self.params[1] * -1
			# if the modifier portion does have a space -> ex; !roll d20 + 2
			elif len(command) == 3:
				self.params[1] = int(command[2])
				if "-" in command[1]:
					self.params[1] = amount * -1
			else:
				self.errorMsg = "Invalid Roll Modifier: " + str(command) + "\nTry !help for more info"
				return False
			"""

			print(command)

			# get total
			self.total = (dice.getRollSum(self.rolls, len(self.rolls)) + self.modifier)

		except Exception as ex:
			self.errorMsg = type(ex).__name__ + ": " + str(ex) + "\nTry !help for more info"
			return False
		return True
