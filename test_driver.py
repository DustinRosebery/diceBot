import command_parser as cp

def process(message):
	if message[0] == "!":
		command = cp.Command(message)

		if not command.isValid:
			print("Driver Error: " + command.errorMsg)
			return

		if command.action == "help":
			print("Driver Help: " + command.helpMsg)
			return

		# ROLL
		if command.action == "roll":
			print("Driver roll: " + str(command.rolls) + " -> " + str(command.total))
			return

if __name__ == "__main__":
	testInput = "!roll 2d20 + 2"
	process(testInput)