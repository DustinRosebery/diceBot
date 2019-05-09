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
			- []: params -> [ [rolls], modifer, total]
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
		self.params = []
		self.isValid = False
		self.errorMsg = ""

		if "roll" in command[0].lower() or "rolls" in command[0].lower():
			self.action = "roll"
			self.params = [[],0,0]
			self.isValid = self.getRollParameters(command[1:])

		elif "help" in command[0].lower():
			self.action = "help"
			self.isValid = True

	"""
		Sets the object params for the roll command
		params -> [ [rolls], modifier, total]
		Returns True if the command is valid, else returns False
	"""
	def getRollParameters(self, command):
		try:
			print("Command: " + str(command))
			print("Command Length: " + str(len(command)))
			valueCommand = command[0].split("d")

			# parse roll parameters and get rolls
			print("ValueCommand: " + str(valueCommand))
			print("ValueCommand Length: " + str(len(valueCommand)))
			if not valueCommand[0]:
				valueCommand[0] = 1
				self.params[0] = dice.getRolls(int(valueCommand[0]), int(valueCommand[1]))
			elif len(valueCommand) == 2:
				self.params[0] = dice.getRolls(int(valueCommand[0]), int(valueCommand[1]))
			else:
				self.errorMsg = "Invalid Roll Value: " + str(command) + "\nTry !help for more info"
				return False

			# parse modifier
			if len(command) == 1:
				self.params[1] = 0
			elif len(command) == 2:
				rawMod = command[1]
				print("RawMod: " + rawMod)
				self.params[1] = int(rawMod[1:])
				print("Params[1]: " + str(self.params[1])) 
				if "-" in rawMod:
					print("found negative modifier")
					self.params[1] = self.params[1] * -1
				print("Params[1] after negative: " + str(self.params[1]))
			elif len(command) == 3:
				self.params[1] = int(command[2])
				if "-" in command[1]:
					self.params[1] = amount * -1
			else:
				self.errorMsg = "Invalid Roll Modifier: " + str(command) + "\nTry !help for more info"
				return False
			print("Rolls: " + str(self.params[0]))
			print("Modifier3: " + str(self.params[1]))

			# get total
			self.params[2] = (dice.getRollSum(self.params[0], len(self.params[0])) + self.params[1])
			print("Total: " + str(self.params[2]))

		except Exception as ex:
			self.errorMsg = type(ex).__name__ + ": " + str(ex) + "\nTry !help for more info"
			return False
		return True
