import dice_logic as dice

"""
	This class takes a raw command from discord and returns a list of parsed command objects
"""
class Command:

	helpMsg = "I am a dice rolling bot!\nValid commands: !roll, !help\nRoll command: !roll 3d10 +3\nThis would return 3 rolls of a 10 sided dice with +3 as the modifier\nYou can roll up to ~500 dice at a time with any size dice that you like with a positive or negative modifier\nHelp command: print this message"
	tryHelp = "\nTry !help for more info"

	"""
		Create a command object with attributes
		   	- str: action
		   	- boolean: isValid -> is this a valid roll command?
			- str: errorMsg
			- str: helpMsg
			- str: tryHelp

		Unique ROLL attributes
			- int: modifer
			- int: total
			- []: rolls
	"""
	def __init__(self, rawCommand):
		print("Raw Command: " + str(rawCommand))
		action = ""
		isValid = False
		errorMsg = "Unhandled Command Exception\nTry !help for more info"

		command = rawCommand.split(" ")
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
		Sets the params for the roll command
		Params -> modifer, rolls, and total
		Returns -> True if the command is valid, else False
	"""
	def getRollParameters(self, rawCommand):
		try:
			command = rawCommand[1:]

			# parse modifier
			try:
				print("Mod Command: " + str(command))
				lastIndex = len(command) - 1
				# accounts for spaces between rollValue, +/- symbol, and modifier value
				if len(command) == 3:
					command[2] = command[1] + command[2]
				if "-" in str(command):
					modAmount = int(command[lastIndex].split("-")[1]) * -1
					command = command[0].split("-")
					print("Modifer: " + str(modAmount))
					self.modifier = modAmount
				elif "+" in str(command):
					modAmount = int(command[lastIndex].split("+")[1])
					command = command[0].split("+")
					print("Modifier: " + str(modAmount))
					self.modifier = modAmount
				else:
					self.modifier = 0		
			except Exception as modEx:
				self.errorMsg = "Invalid Modifier Value: " + str(command) + self.tryHelp		
				return False

			# parse roll parameters and get roll values
			try:
				command = command[0].split("d")
				print("Roll Command: " + str(command))
				# accounts for numRolls present AND missing, ex; !roll 3d20 AND !roll d20
				if not command[0]:
					command[0] = 1
					self.rolls = dice.getRolls(int(command[0]), int(command[1]))
				elif len(command) == 2:
					self.rolls = dice.getRolls(int(command[0]), int(command[1]))
				else:
					self.errorMsg = "Invalid Roll Value: " + str(command) + self.tryHelp
					return False
			except Exception as valueEx:
				self.errorMsg = "Invalid Roll Value: " + str(command) + self.tryHelp
				return False

			# get total
			self.total = (dice.getRollSum(self.rolls, len(self.rolls)) + self.modifier)

		except Exception as ex:
			self.errorMsg = type(ex).__name__ + ": " + str(ex) + self.tryHelp
			return False

		# returns isValid = True
		return True
